from logicmonitor import LM
from pprint import pprint

"""
This script will find a list of device names enrolled in LogicMonitor
that currently have an uptime of over 6 months
"""

# Authentication Information
account_name='acme-firework-co',
access_id='Fahpho7Pahghahwo1aeY',
access_key='=oS-iiKuhei5Ahth{e(oph[ei8Ow8pheekai9iGh'

# Initialize your API connections
lm = LM(account_name, access_id, access_key)

# We only want to get the displayName field, and we're looking
# for servers with over 6 months (15780000 seconds) of uptime
query = {
    'fields': 'displayName',
    'filter': 'upTimeInSeconds>:15780000'
}

# Get a list of all devices matching our query
devices = lm.get('/device/devices', query)

# PrettyPrint the result
pprint(devices)

"""
Example output:
--------------------
{'data': {'isMin': False,
          'items': [{'displayName': 'host1.example.com'},
                    {'displayName': 'host2.example.com'},
                    {'displayName': 'host3.example.com'},
                    {'displayName': 'host4.example.com'},
                    {'displayName': 'host5.example.com'}],
          'searchId': None,
          'total': 5},
  'errmsg': 'OK',
  'status': 200}
"""
