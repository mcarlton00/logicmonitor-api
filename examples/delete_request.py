from logicmonitor import LM
from pprint import pprint

"""
This script will delete the dashboard with an id of 41
"""

# Authentication Information
account_name='acme-firework-co'
access_id='Fahpho7Pahghahwo1aeY'
access_key='=oS-iiKuhei5Ahth{e(oph[ei8Ow8pheekai9iGh'

# Initialize your API connections
lm = LM(account_name, access_id, access_key)

# Delete the dashboard at id 41
response = lm.delete('/dashboard/dashboards/41')

# PrettyPrint the result
pprint(response)

"""
# Example Output:
--------------------
{'data': None, 'errmsg': 'OK', 'status': 200}
"""
