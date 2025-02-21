import sqlalchemy
import sqlalchemy.exc
import sqlalchemy.orm
import sqlalchemy.orm.dynamic
import sqlalchemy.orm.query
from sqlalchemy.orm import Session, contains_eager

from .. import core, temporary_halolist


class HopStrategy:
    """HopStrategy and its descendants define methods helpful for finding related halos, e.g. progenitors/descendants,
    or corresponding halos in other simulation runs"""

    def __init__(self, halo_from, target=None, order_by=None):
        """Construct a HopStrategy starting from the specified halo"""
        assert isinstance(halo_from, core.halo.SimulationObjectBase)
        self.session = Session.object_session(halo_from)
        self.halo_from = halo_from
        self._initialise_order_by(order_by)
        self._link_orm_class = core.halo_data.HaloLink
        self._target = target
        self._all = None

    def _target_timestep(self, query, ts):
        """Only return those hops which reach the specified timestep"""
        if ts is None:
            query = query.filter(0 == 1)
        else:
            query = query.join(self._link_orm_class.halo_to).filter(core.halo.SimulationObjectBase.timestep_id == ts.id)

        return query

    def _target_simulation(self, query, sim):
        """Only return those hops which reach the specified simulation"""
        query = query.join(self._link_orm_class.halo_to).join(core.SimulationObjectBase.timestep).filter(
            core.timestep.TimeStep.simulation_id == sim.id)

        return query

    def _filter_query_for_target(self, query, db_obj):
        """Only return those hops which reach the specifid simulation or timestep"""
        if db_obj is None:
            return query
        elif isinstance(db_obj, core.timestep.TimeStep):
            return self._target_timestep(query, db_obj)
        elif isinstance(db_obj, core.simulation.Simulation):
            return self._target_simulation(query, db_obj)
        else:
            raise ValueError("Unknown target type")

    def _initialise_order_by(self, names):
        """Specify an ordering for the output hop suggestions.

        Accepted names are:

         - 'weight' - the weight of the link, ascending (default). In the case of MultiHopStrategy, this is the
                      product of the weights along the path found.
         - 'time_asc' - the time of the snapshot, ascending order
         - 'time_desc' - the time of the snapshot, descending order
         - 'halo_number_asc' - the halo number, ascending
         - 'halo_number_desc' - the halo number, descending
         - 'nhops' - the number of hops taken to reach the halo (MultiHopStrategy only)

        Multiple names can be given to order by more than one property.
        """
        if names is None:
            names = ['weight']
        elif isinstance(names, str):
            names = [names]
        self._order_by_names = [x.lower() for x in names]

    def count(self):
        """Return the number of hops matching the conditions"""
        return len(self._get_query_all())

    def _execute_query(self):
        try:
            query = self._filter_query_for_target(self.halo_from.links, self._target)
            results = self._order_query(query).all()
        except sqlalchemy.exc.ResourceClosedError:
            results = []

        results = [x for x in results if x is not None]

        self._all = results

    def _get_query_all(self):
        if self._all is None:
            self._execute_query()
        return self._all

    def temp_table(self):
        # N.B. this could be made more efficient
        ids_list = [x.id if hasattr(x,'id') else None for x in self.all() ]
        return temporary_halolist.temporary_halolist_table(self.session, ids_list)

    def all(self):
        """Return all possible hops matching the conditions"""
        return [x.halo_to for x in self._get_query_all()]

    def weights(self):
        """Return the weights for the possible hops"""
        return [x.weight for x in self._get_query_all()]

    def all_and_weights(self):
        """Return all possible hops matching the conditions, along with
        the weights"""
        all = self._get_query_all()
        weights = [x.weight for x in all]
        halos = [x.halo_to for x in all]
        return halos, weights

    def first(self):
        """Return the suggested hop."""
        link = self._get_query_all()
        if len(link) == 0:
            return None
        else:
            return link[0].halo_to

    def _order_by_clause(self, halo_alias, timestep_alias):
        return [self._generate_order_arg_from_name(name, halo_alias, timestep_alias) for name in self._order_by_names]

    def _generate_order_arg_from_name(self, name, halo_alias, timestep_alias):
        if name == 'weight':
            return self._link_orm_class.weight.desc()
        elif name == 'time_asc':
            return timestep_alias.time_gyr
        elif name == 'time_desc':
            return timestep_alias.time_gyr.desc()
        elif name == 'halo_number_asc':
            return halo_alias.halo_number
        elif name == 'halo_number_desc':
            return halo_alias.halo_number.desc()
        else:
            raise ValueError("Unknown ordering method %r" % name)

    def _ordering_requires_join(self):
        return 'time_asc' in self._order_by_names \
               or 'time_desc' in self._order_by_names \
               or 'halo_number_asc' in self._order_by_names \
               or 'halo_number_desc' in self._order_by_names

    def _order_query(self, query):
        assert isinstance(query, sqlalchemy.orm.query.Query)
        timestep_alias = None
        halo_alias = None
        if self._ordering_requires_join():
            timestep_alias = sqlalchemy.orm.aliased(core.timestep.TimeStep)
            halo_alias = sqlalchemy.orm.aliased(core.halo.SimulationObjectBase)
            query = query.join(halo_alias, self._link_orm_class.halo_to_id == halo_alias.id)\
                .join(timestep_alias)\
                .options(
                  contains_eager(self._link_orm_class.halo_to.of_type(halo_alias))\
                  .contains_eager(halo_alias.timestep.of_type(timestep_alias))
            )
        query = query.order_by(*self._order_by_clause(halo_alias, timestep_alias))
        return query

class HopMajorDescendantStrategy(HopStrategy):
    """A hop strategy that suggests the major descendant for a halo"""

    def __init__(self, halo_from):
        target_ts = halo_from.timestep.next
        if target_ts:
            super().__init__(halo_from, target=target_ts)
        else:
            self._all = []


class HopMajorProgenitorStrategy(HopStrategy):
    """A hop strategy that suggests the major progenitor for a halo"""

    def __init__(self, halo_from):
        target_ts = halo_from.timestep.previous
        if target_ts:
            super().__init__(halo_from, target=target_ts)
        else:
            self._all = []
