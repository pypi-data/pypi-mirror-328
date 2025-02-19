import logging
import warnings

from odoo import models

_DEFAULT_LOGGER_NAME = __name__


class SimpleLogger(models.AbstractModel):
    _name = "runbot.logger"
    _description = "Logging Tester"

    def log_msg(self, msg, level=logging.INFO, logger_name=_DEFAULT_LOGGER_NAME):
        print(logging.getLogger(logger_name).handlers)
        print(logging.getLogger(logger_name).propagate)
        logging.getLogger(logger_name).log(level, msg)

    def do_pywarnings(self, msg, warning_type):
        warnings.warn(msg, warning_type, stacklevel=2)
