"""Contains the log handler to catch log"""

from __future__ import annotations

import contextlib
import logging
import re
from functools import partial
from logging import LogRecord
from typing import Callable

from .runbot_env import RunbotExcludeWarning, RunbotStepConfig

_logger = logging.getLogger("odoo_runbot")
# 7-bit C1 ANSI sequences
ansi_escape = re.compile(
    r"""
    \x1B  # ESC
    (?:   # 7-bit C1 Fe (except CSI)
        [@-Z\\-_]
    |     # or [ for CSI, followed by a control sequence
        \[
        [0-?]*  # Parameter bytes
        [ -/]*  # Intermediate bytes
        [@-~]   # Final byte
    )
""",
    re.VERBOSE,
)

__all__ = [
    "ExcludeWarningFilter",
    "RunbotWarningWatcherHandler",
    "get_handler",
    "start_warning_log_watcher",
]


class RunbotWarningWatcherHandler(logging.Handler):
    filters: list[ExcludeWarningFilter]

    def __init__(self) -> None:
        super().__init__(logging.WARNING)
        self.set_name(type(self).__name__)

        self.catch_all_filter = self._get_catch_all_filter()

    def _get_catch_all_filter(self) -> ExcludeWarningFilter:
        return ExcludeWarningFilter(
            RunbotExcludeWarning(
                name="Runbot Warning catch all no filter",
                min_match=0,
                max_match=0,  # No warning is accepted
                regex=r".*",  # Every thing it's a match
            ),
        )

    def emit(self, record: LogRecord) -> None:
        "Do nothing, only here to store logging."

    def add_warnings(self, warnings_to_filter: list[RunbotExcludeWarning]) -> None:
        self.filters.extend([ExcludeWarningFilter(warn_rule) for warn_rule in warnings_to_filter])

    def remove_warnings(
        self,
        warnings_to_filter: list[RunbotExcludeWarning] | None = None,
    ) -> list[ExcludeWarningFilter]:
        result: list[ExcludeWarningFilter] = []
        if not warnings_to_filter:
            result = self.filters[:]
            self.filters = []

        for _filter in self.filters[:]:
            if _filter.exclude in warnings_to_filter:
                result.append(_filter)
                self.filters.remove(_filter)

        if not self.filters:
            result.append(self.catch_all_filter)
            self.catch_all_filter = self._get_catch_all_filter()

        return result

    def filter(self, record: LogRecord) -> bool:
        if self.filters:
            no_match = super().filter(record)
            if not no_match:
                return no_match
        return self.catch_all_filter.filter(record)


def get_handler() -> RunbotWarningWatcherHandler | None:
    for h in logging.root.handlers:
        if isinstance(h, RunbotWarningWatcherHandler):
            return h
    return None


class ExcludeWarningFilter(logging.Filter):
    def __init__(self, exclude: RunbotExcludeWarning) -> None:
        super().__init__(exclude.logger)
        self.log_match: list[logging.LogRecord] = []
        self.regex = re.compile(exclude.regex, re.IGNORECASE)
        self.exclude = exclude
        logging.getLogger("runbot.filter").info(
            "Init filter %s match [%s] for logger %s, between [%s, %s]",
            self.exclude.name,
            str(self.regex),
            self.exclude.logger,
            self.exclude.min_match,
            self.exclude.max_match,
        )

    def filter(self, record: logging.LogRecord) -> bool:
        if not super().filter(record):
            return True

        escaped_msg = ansi_escape.sub("", str(record.msg))
        match = self.regex.match(escaped_msg)
        if not match:
            # Line don't match regex, return False to propagate to other filter
            return True
        logging.getLogger("odoo.runbot.filter").info(
            "%s matched %s for logger %s",
            self.exclude.name,
            bool(match),
            record.name,
        )
        # Store this record to later print it as error
        self.log_match.append(record)
        return False  # False mean no more propagate this log record to other filter, avoid duplicate catch

    @property
    def success(self) -> bool:
        return self.exclude.min_match <= len(self.log_match) <= self.exclude.max_match

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(exclude={self.exclude!r})"

    def reset_counter(self) -> None:
        self.log_match = []


@contextlib.contextmanager
def start_warning_log_watcher(step: RunbotStepConfig) -> Callable[[], list[ExcludeWarningFilter]]:
    _logger.debug("Starting odoo logging interceptor with %s regex", len(step.log_filters))
    runbot_handler = get_handler() or RunbotWarningWatcherHandler()  # Auto registering
    runbot_handler.add_warnings(step.log_filters)
    logging.getLogger().addHandler(runbot_handler)
    yield partial(get_warning_log_watcher, step)


def get_warning_log_watcher(step: RunbotStepConfig = None) -> list[ExcludeWarningFilter]:
    runbot_handler = get_handler()
    if not runbot_handler:
        return []
    if not step:
        return runbot_handler.remove_warnings()
    return runbot_handler.remove_warnings(step.log_filters)
