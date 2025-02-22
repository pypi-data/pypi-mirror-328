import logging

from odoo.tests import common


class TestStep4(common.TransactionCase):
    def test_filter(self):
        # Step3 - Filter2 will capture this line but not Filter1 (no same logger name)
        self.env["runbot.logger"].log_msg("My Warning message - in root", level=logging.WARNING, logger_name=None)
        self.env["runbot.logger"].log_msg(
            "My Warning message - in custom", level=logging.WARNING, logger_name="Custom.logger"
        )
        self.env["runbot.logger"].log_msg(
            "My Warning message - in base", level=logging.WARNING, logger_name="odoo.addons.base"
        )
