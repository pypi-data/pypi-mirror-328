import copy
import logging
from io import StringIO

logger = logging.getLogger(__name__)

logger.setLevel(logging.INFO)
handler_stderr = logging.StreamHandler()
handler_stderr.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s : %(message)s")
handler_stderr.setFormatter(formatter)
logger.addHandler(handler_stderr)


class LogCapturer:
    def __init__(self):
        self.buffer = StringIO()
        self.handler_buffer = logging.StreamHandler(self.buffer)
        self.handler_buffer.setLevel(logging.INFO)
        self.handler_buffer.setFormatter(formatter)
        self._suspended_handlers = []

    def __enter__(self):
        self._suspended_handlers = copy.copy(logger.handlers)
        for x_handler in self._suspended_handlers:
            logger.removeHandler(x_handler)
        logger.addHandler(self.handler_buffer)
        return self

    def __exit__(self, *exc_info):
        for x_handler in self._suspended_handlers:
            logger.addHandler(x_handler)
        self._suspended_handlers = []
        logger.removeHandler(self.handler_buffer)

    def get_output(self):
        return self.buffer.getvalue()

    def get_output_without_timestamps(self):
        lines = self.get_output().split("\n")
        result = ""
        for l in lines:
            try:
                result += l.split(" : ", 1)[1]+"\n"
            except IndexError:
                result += l+"\n"
        return result


def set_identity_string(identifier):
    global handler_stderr
    formatter = logging.Formatter(identifier+"%(asctime)s : %(message)s")
    for handler in logger.handlers:
        handler.setFormatter(formatter)
