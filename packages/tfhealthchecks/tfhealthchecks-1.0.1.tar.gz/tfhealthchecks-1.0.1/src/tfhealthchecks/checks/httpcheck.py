import datetime
import time

import requests

from tfhealthchecks.utils import to_millis
from tfhealthchecks.healthcheck import HealthCheckRunner, CheckResult


class HttpCheckRunner(HealthCheckRunner):
    """Check if HTTP network service is reachable"""

    timeout = 5  # seconds

    def __init__(self, url):
        self.url = url

    def request_parameters(self):
        """template method for additional request parameters"""
        return {}

    def run_check(self) -> CheckResult:
        execution_time = datetime.datetime.utcnow()
        start_time = time.clock()

        try:
            response = requests.get(self.url, timeout=self.timeout, **self.request_parameters())
            status = 200 <= response.status_code < 300

            return CheckResult(status, execution_time, to_millis(response.elapsed.total_seconds()))

        except BaseException as e:
            return CheckResult(False, execution_time, to_millis(time.clock() - start_time), errors=[e.__repr__()])


