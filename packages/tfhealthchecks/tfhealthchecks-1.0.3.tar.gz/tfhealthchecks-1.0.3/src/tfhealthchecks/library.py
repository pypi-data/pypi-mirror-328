"""
Set of checks for components that are used within Takeoff
"""

from tfhealthchecks.checks.couchdb import CouchDBCheckRunner
from tfhealthchecks.checks.httpcheck import HttpCheckRunner
from tfhealthchecks.healthcheck import BaseHealthCheck

class CouchDBHealth(BaseHealthCheck):

    def __init__(self, url, username, password):
        runner = CouchDBCheckRunner(url, username, password)
        super().__init__(runner)

    def description(self):
        return "Check CouchDB health"

    def name(self):
        return "CouchDB Health"

class ServiceProbe(BaseHealthCheck):

    def __init__(self, url):
        super().__init__(HttpCheckRunner(url))


class OMSProbe(ServiceProbe):

    def description(self):
        return "Check OMS availability"

    def name(self):
        return "OMS"


class IMSProbe(ServiceProbe):

    def description(self):
        return "Check IMS availability"

    def name(self):
        return "IMS"


class TomApiProbe(ServiceProbe):

    def description(self):
        return "Check Tom API availability"

    def name(self):
        return "Tom API"


class AuthServiceProbe(ServiceProbe):

    def description(self):
        return "Check Auth Service availability"

    def name(self):
        return "Auth Service"


class TSCServiceProbe(ServiceProbe):

    def description(self):
        return "Check TSC - Takeoff Service Configuration Backend availability"

    def name(self):
        return "TSC"
