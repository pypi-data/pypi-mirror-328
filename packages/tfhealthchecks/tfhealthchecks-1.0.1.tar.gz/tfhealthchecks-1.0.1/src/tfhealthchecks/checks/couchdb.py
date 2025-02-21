import urllib.parse

from requests.auth import HTTPBasicAuth

from tfhealthchecks.checks.httpcheck import HttpCheckRunner
from tfhealthchecks.healthcheck import CheckResult


class CouchDBCheckRunner(HttpCheckRunner):
    """Check CouchDB status"""

    path = "/_up"

    def __init__(self, url, user, password):
        self._user = user
        self._password = password

        path = urllib.parse.urljoin(url, self.path)
        super().__init__(path)

    def request_parameters(self):
        return {
            'auth': HTTPBasicAuth(self._user, self._password)
        }

    def run_check(self) -> CheckResult:
        return super().run_check()
