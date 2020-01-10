from logicmonitor import LM
from pprint import pprint

"""
This script will create a new API keypair set for a given user
"""

# Authentication Information
account_name='acme-firework-co',
access_id='Fahpho7Pahghahwo1aeY',
access_key='=oS-iiKuhei5Ahth{e(oph[ei8Ow8pheekai9iGh'

# Initialize your API connections
lm = LM(account_name, access_id, access_key)

# We want to create an enabled key with a descriptive note
data = {
    'status': 2,
    'note': 'Created from the api'
}

# Create an api token for user 19
response = lm.post('/setting/admins/19/apitokens', data)

# PrettyPrint the result
pprint(response)

"""
# Example Output:
--------------------
{'data': {'accessId': 'fWLD69edrz839S62rZ3W',
          'accessKey': 's=E7w9_NjH3)t+NP2{7]rmr63L=J6-N}xCB_w)^N',
          'adminId': 19,
          'adminName': 'adminuser@example.com',
          'createdBy': 'adminuser@example.com',
          'createdOn': 1578620080,
          'id': 33,
          'lastUsedOn': 0,
          'note': 'Created from the api',
          'roles': ['LM-Admin'],
          'status': 2},
 'errmsg': 'OK',
 'status': 200}
"""
