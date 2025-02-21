import copy
import os

import numpy as np
import numpy.testing as npt

import tangos as db
import tangos.core.simulation
import tangos.core.timestep
import tangos.input_handlers.halo_stat_files as stat
import tangos.tools.add_simulation as add_simulation
import tangos.tools.property_importer as property_importer
from tangos import parallel_tasks, testing
from tangos.input_handlers.halo_stat_files import translations


def setup_module():
    global ts1, ts2, ts3, sim, session
    testing.init_blank_db_for_testing()
    db.config.base = os.path.dirname(os.path.abspath(__file__))+"/"

    session = db.core.get_default_session()

    sim = tangos.core.simulation.Simulation("test_stat_files")
    session.add(sim)

    ts1 = tangos.core.timestep.TimeStep(sim, "pioneer50h128.1536gst1.bwK1.000832")
    ts1.time_gyr = 6  # unimportant
    ts1.redshift = 2.323  # matters for AHF filename

    ts2 = tangos.core.timestep.TimeStep(sim, "h242.cosmo50PLK.1536g1bwK1C52.004096")
    ts2.time_gyr = 10
    ts2.redshift = 0

    ts3 = tangos.core.timestep.TimeStep(sim, "pioneer50h128MPI.1536gst1.bwK1.000832")
    ts3.time_gyr = 6
    ts3.redshift = 2.323

    session.add_all([ts1,ts2, ts3])


    session.commit()

    adder = add_simulation.SimulationAdderUpdater(sim.get_output_handler())
    adder.min_halo_particles = 300000
    adder.add_objects_to_timestep(ts1)

    parallel_tasks.use('null')

def teardown_module():
    tangos.core.close_db()

def test_statfile_identity():
    global ts1,ts2, ts3
    assert isinstance(stat.HaloStatFile(ts1.filename), stat.AHFStatFile)
    assert isinstance(stat.HaloStatFile(ts2.filename), stat.AmigaIDLStatFile)
    assert isinstance(stat.HaloStatFile(ts3.filename), stat.AHFStatFile)

def test_ahf_values():
    cat_index, finder_id, ngas, nstar, ndm, ntot,  rvir = stat.HaloStatFile(ts1.filename).read("n_gas", "n_star", "n_dm", "npart", "Rvir")
    assert all(cat_index==[1,2,3,4])
    assert all(finder_id==[0,1,2,3])
    assert all(ngas==[324272,  47634,  53939,  19920])
    assert all(nstar==[1227695,   55825,   24561,    7531])
    assert all(ntot==[5900575,  506026,  498433,  226976])
    assert all(ndm==[4348608, 402567, 419933,  199525])
    npt.assert_allclose(rvir, [195.87, 88.75, 90.01, 69.41])

def test_idl_values():
    cat_index, finder_id, ntot, mvir = stat.HaloStatFile(ts2.filename).read("npart","Mvir")
    assert all(finder_id==[1,49,52,58,94,121,127,148,163])
    assert all(cat_index==[1,49,52,58,94,121,127,148,163])
    assert all(ntot==[3273314, 27631, 24654, 22366, 12915, 9831, 9498, 8200, 7256])
    npt.assert_almost_equal(mvir,   [  1.12282280e+12 ,  1.19939950e+10 ,  1.19538740e+10  , 3.07825010e+10,
                                       1.76325820e+10 ,  1.33353700e+10  , 1.28836660e+10 ,  1.11229900e+10,
                                       9.84248220e+09], decimal=5)

def test_mpi_ahf_values():
    cat_index, finder_id, ntot, mvir = stat.AHFStatFile(ts3.filename).read("npart","Mvir")
    assert all(cat_index==[1,2,3,4])
    assert all(finder_id==[32425324, 8712365, 3478612, 907234568])
    assert all(ntot==[5900575,506026,498433,226976])
    npt.assert_almost_equal(mvir,   [5.02432e+11,4.67419e+10, 4.87598e+10, 2.23568e+10  ], decimal=5)


def test_insert_halos():

    # insert has already happened in the setup
    for h in ts1.halos:
        db.get_default_session().delete(h) # remove previous objects so that we can add them afresh

    adder = add_simulation.SimulationAdderUpdater(sim.get_output_handler())
    adder.min_halo_particles = 300000
    adder.add_objects_to_timestep(ts1)

    assert ts1.halos.count()==3
    assert ts1.halos[0].NDM==4348608
    assert ts1.halos[1].NDM==402567

def test_insert_properties():
    for h in ts1.halos:
        db.get_default_session().delete(h) # remove previous objects so that we can add them afresh
    adder = add_simulation.SimulationAdderUpdater(sim.get_output_handler())
    adder.add_objects_to_timestep(ts1)
    importer = property_importer.PropertyImporter()
    importer.parse_command_line("Mvir Rvir hostHalo childHalo --for test_stat_files".split())
    importer.run_calculation_loop()
    npt.assert_almost_equal(ts1.halos[0]["Rvir"], 195.87)
    npt.assert_almost_equal(ts1.halos[0]["Mvir"], 5.02432e+11)
    with npt.assert_raises(KeyError):
        ts1.halos[0]['hostHalo']
    with npt.assert_raises(KeyError):
        ts1.halos[1]['childHalo']
    assert ts1.halos[2]['hostHalo']==ts1.halos[0]
    assert ts1.halos[3]['hostHalo']==ts1.halos[0]
    testing.assert_halolists_equal(ts1.halos[0]['childHalo'], [ts1.halos[2], ts1.halos[3]])

def test_default_value():
    class AHFStatFileWithDefaultValues(stat.AHFStatFile):
        _column_translations = {'nonexistent_column': translations.DefaultValue('nonexistent_column', 42),
                                'existent_column': translations.DefaultValue('n_gas', 43)}

    cat_index, finder_id, fortytwo, n_gas = AHFStatFileWithDefaultValues(ts1.filename).read('nonexistent_column', 'existent_column')

    assert (fortytwo==42).all()
    assert all(n_gas == [324272,  47634,  53939,  19920])

def test_import_properties_is_only_numeric_or_array():
    import tangos.core as core

    # Pick a random existing property name and halo for testing the import of properties
    halo = ts1.halos[0]
    db_name = core.dictionary.get_or_create_dictionary_item(session, "Rvir")

    # Numeric types should create a property successfully
    importer = property_importer.PropertyImporter()
    property = importer._create_property(db_name, halo, int(42))
    assert property.data == 42

    property = importer._create_property(db_name, halo, float(42.0))
    assert property.data == 42.0

    # Arrays of numerics should now create a property successfully
    property = importer._create_property(db_name, halo, np.array([42, 42, 42]))
    assert property.data_is_array() == True
    assert np.issubdtype(property.data.dtype, int)
    npt.assert_allclose(property.data, np.array([42, 42, 42]))

    property = importer._create_property(db_name, halo, np.array([42.0, 42.0, 42.0]))
    assert property.data_is_array() == True
    assert np.issubdtype(property.data.dtype, np.floating)
    npt.assert_allclose(property.data, np.array([42.0, 42.0, 42.0]))

    # Importing a string should fail
    property = importer._create_property(db_name, halo, "42.0")
    assert property is None
    # Importing an object should fail
    property = importer._create_property(db_name, halo, halo)
    assert property is None
    # Importing an array of non-numeric types should fail
    property = importer._create_property(db_name, halo, np.array(["42.0", "42.0", "42.0"]))
    assert property is None
