# LogicMonitor-API

This is a simple python wrapper to simplify using the [LogicMonitor API](https://www.logicmonitor.com/support/rest-api-developers-guide/overview/using-logicmonitors-rest-api/).  Constructing the request to interact with the api is a less than straightforward process, and this aims to abstract all of that away so you can focus on getting work done instead of deciphering API nuances.

Note: Requires Python3.6 or newer and the excellent [Python Requests](https://2.python-requests.org/en/master/) library

```python
>>> from logicmonitor import LM
>>> from pprint import pprint

>>> account_name='acme-firework-co',
>>> access_id='Fahpho7Pahghahwo1aeY',
>>> access_key='=oS-iiKuhei5Ahth{e(oph[ei8Ow8pheekai9iGh'

>>> # Initialize your API connections
>>> lm = LM(account_name, access_id, access_key)

>>> # Get a list of all devices in LogicMonitor
>>> devices = lm.get('/devices/devices')

>>> pprint(devices['data'])
{'isMin': False,
 'items': [{'alertDisableStatus': 'none-none-none',
            'alertStatus': 'none',
            'alertStatusPriority': 100000,
            'alertingDisabledOn': None,
            'ancestorHasDisabledLogicModule': False,
            'autoProperties': [],
            'autoPropsAssignedOn': 0,
            'autoPropsUpdatedOn': 0,
            'awsState': 1,
            'azureState': 1,
            'collectorDescription': 'Cloud Collector',
            'createdOn': 1570027698,
            ...............
'searchId': None,
 'total': 1178}
```

More detailed examples can be found in the `examples/` directory
