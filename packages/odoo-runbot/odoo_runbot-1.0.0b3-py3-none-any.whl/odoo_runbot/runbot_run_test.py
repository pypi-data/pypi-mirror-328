"""Contains all the code used to assert Logger and warnings a propely catched."""

from __future__ import annotations

import logging
import typing
import unittest

from xmlrunner import XMLTestRunner

if typing.TYPE_CHECKING:
    import pathlib
    from warnings import WarningMessage

    from .runbot_run_logging import ExcludeWarningFilter

_logger = logging.getLogger("odoo_runbot")


def get_test_runner(output_dir: pathlib.Path | None = None) -> unittest.TextTestRunner:
    """Retun a default Runner.

    If an `output_dir` is filed, then `xmlrunner.XMLTestRunner` is returned
    Args:
        output_dir: The path where the test resul;t should be stored

    Returns: The class to run unittest tests

    """
    if output_dir and output_dir.exists():
        return XMLTestRunner(output=str(output_dir.resolve()), failfast=False)
    return unittest.TextTestRunner(failfast=False)


def execute_test_after_odoo(
    log_filters: list[ExcludeWarningFilter] | None = None,
    warning_message: list[WarningMessage] | None = None,
    *,
    test_runner: unittest.TextTestRunner | None = None,
) -> unittest.result.TestResult:
    """Generate 1 [unittest.TestCase][] for each filter.

    If `test_runner` is `None` then [unittest.TextTestRunner][] is used.

    Note:
        If `filter_to_test` is `None` then A default succeed TestResult is returned.

    Args:
        log_filters: All the Log filter to add in the test suite
        warning_message: All the warning message catch, if any then the suite will failed
        test_runner: your custom runner, or [unittest.TextTestRunner][]

    Returns:
        The result of the test runner with your runner if set.

    """
    _logger.info("Execute Logger Filter test suite for %s filters", (log_filters and len(log_filters)) or 0)
    test_runner = test_runner or unittest.TextTestRunner()
    if not log_filters and not warning_message:
        return unittest.result.TestResult()
    suite = unittest.TestSuite()
    for log_filter in log_filters:
        suite.addTest(_RunbotLoggerUnitTest(log_filter))
    if warning_message:
        suite.addTest(_RunbotPyWarningUnitTest(warning_message))
    _logger.debug("Test suite created, run it with %s", type(test_runner).__name__)
    return test_runner.run(suite)


class _RunbotLoggerUnitTest(unittest.TestCase):
    def __init__(self, warning_filter: ExcludeWarningFilter) -> None:
        super().__init__("test_logger_filter")
        self.warning_filter = warning_filter
        self._testMethodDoc = self._make_description()
        if logging.root.handlers:
            self.format_log = logging.root.handlers[0].format
        else:
            self.format_log = logging.Formatter.format

    def test_logger_filter(self) -> None:
        if self.warning_filter.success:
            self.assertTrue(self.warning_filter.success)  # noqa: PT009
            return

        fail_msg = [
            f"{self.warning_filter.exclude.name} Failed for logger '{self.warning_filter.exclude.logger or 'all'}'",
            f"Expected: {self.warning_filter.exclude.min_match} "
            f"<= len(match_log_lines) <= {self.warning_filter.exclude.max_match}",
            f"Found {len(self.warning_filter.log_match)} "
            f"log line who match the regex r'{self.warning_filter.regex.pattern}'",
        ]
        if self.warning_filter.log_match:
            fail_msg.append("Log line content :")
        fail_msg.extend(["\t> " + self.format_log(log_record) for log_record in self.warning_filter.log_match])
        self.fail("\n".join(fail_msg))

    def _make_description(self) -> str:
        return (
            f"{self.warning_filter.exclude.name} Regex Matcher "
            f"for logger '{self.warning_filter.exclude.logger or 'all'}'"
        )


class _RunbotPyWarningUnitTest(unittest.TestCase):
    def __init__(self, warning_msg: list[WarningMessage]) -> None:
        super().__init__("test_warning_filter")
        self.warning_filter = warning_msg
        self._testMethodDoc = ""

    def test_warning_filter(self) -> None:
        fail_msg = ["Some py.warnings found"] + ["\t> " + str(m) for m in self.warning_filter]
        self.fail(msg="\n".join(fail_msg))
