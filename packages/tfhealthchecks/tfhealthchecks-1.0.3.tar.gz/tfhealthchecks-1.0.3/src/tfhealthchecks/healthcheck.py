from datetime import datetime, timezone
from enum import Enum
from typing import List

from tfhealthchecks.utils import status, total_status


class HealthStatus(Enum):
    """
    Health status possible responses

    "ok" if service is able to access all components and resources that it depends on.
    "warn" if service is partially operative (could not connect to some non critical downstream components).
    "fail" if service can not operate or could not connect to its downstream components
    """
    OK = "ok"
    WARN = "warn"
    FAIL = "fail"


class CheckResult(object):
    """Result of health check run"""

    _is_ok: bool
    _execution_start_time: datetime
    _execution_duration_ms: int
    _errors = []

    def __init__(self, is_ok, start_time, duration, errors=None):
        self._is_ok = is_ok
        self._execution_start_time = start_time
        self._execution_duration_ms = duration

        if errors is not None:
            self._errors = errors

    def __repr__(self):
        return {
            'is_ok': self.is_ok,
            'execution_start_time': self.execution_start_time.utcnow(),
            'execution_duration_ms': self.execution_duration,
            'errors': self.errors
        }

    @property
    def is_ok(self):
        """Status returned from the health check"""
        return self._is_ok

    @property
    def execution_start_time(self) -> datetime:
        """Datetime when check were ran"""
        return self._execution_start_time

    @property
    def execution_duration(self) -> int:
        """Time took for the run"""
        return self._execution_duration_ms

    @property
    def errors(self):
        return self._errors


class HealthCheckRunner(object):
    """Action to execute to get health response"""
    def run_check(self) -> CheckResult:
        raise NotImplementedError()


class BaseHealthCheck(object):

    def __init__(self, runner: HealthCheckRunner):
        self.runner = runner

    def execute(self):
        check_result = self.check()
        return {
            'name': self.name(),
            'description': self.description(),
            'status': status(check_result.is_ok, self.is_optional()),
            'is_optional': self.is_optional(),
            'timestamp': check_result.execution_start_time.astimezone(timezone.utc).isoformat(),
            'duration': check_result.execution_duration,
            'errors': check_result.errors
        }

    def name(self):
        raise NotImplementedError()

    def description(self):
        raise NotImplementedError()

    def is_optional(self):
        return False

    def check(self):
        return self.runner.run_check()


def report(checks: List[BaseHealthCheck]):

    result = []
    for check in checks:
        result.append(check.execute())

    status_code, status = total_status(result)

    return status_code, {
        "status": status,
        "checks": result
    }
