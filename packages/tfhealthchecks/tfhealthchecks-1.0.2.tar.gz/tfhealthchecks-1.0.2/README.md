# tfhealthcheck-py

This library provides set of ready to use health check implementations and provides 
basic abstractions for creating health checks with custom logic.

### Pipeline

To get to the azure pipeline go to
https://dev.azure.com/takeofftech/SE/_build?definitionId=264&_a=summary.

### Installation

```
pip install --extra-index-url <url_to_azure_pypi> tfhealthchecks==0.1.4
```

### Usage

```python
# 1. Registering set of checks 

from tfhealthchecks.library import ElasticHealth, CeleryHealth, TomApiProbe, IMSProbe, OMSProbe

checks = [
            ElasticHealth(ELASTICSEARCH_URL),
            CeleryHealth(celery.app),
            TomApiProbe(TOM_API_URL),
            IMSProbe(IMS_URL),
            OMSProbe(CUSTOMER_ORDER_URL)
        ]

# 2. Run checks and obtain result:

from tfhealthchecks.healthcheck import report

status_code, result = report(checks) # status_code (int) - http staus code to return, result - json serializable
                                     # object which contains result of checks execution

# 3. Return http response:
from django.http import JsonResponse

return JsonResponse(result, status=status_code, safe=False, json_dumps_params={"indent": 4})
    
```

### Implementing own health check

Health check consist of two parts - health check runner (all runners should be inherited from `HttpCheckRunner`)
and check description (should be inherited from `BaseHealthCheck`).

Implementation of new check:

```python

from tfhealthchecks.healthcheck import BaseHealthCheck


class MyNewHealthCheck(BaseBaseHealthCheck):
    def __init__(self, url):
        runner = HttpCheckRunner(url)
        super().__init__()
    
    def name(self):
        return "Human readable health check name"

    def description(self):
        return "Long description"
    
    def is_optional(self):
        '''Indicates that service can function when this check returns false'''
        return False

```

Implementation of custom HC logic:

```python

from tfhealthchecks.healthcheck import HealthCheckRunner, CheckResult
import datetime

class MyHealthCheckRunner(HealthCheckRunner):
    
    """Action to execute to get health response"""
    def run_check(self) -> CheckResult:
       # execution logic
       return CheckResult(False, datetime.datetime.now, 0, [NotImplementedError()])

```
