# -*- coding: utf-8 -*-

import requests, json

headers = {
    'charset':'utf-8',
    'content-type': 'application/x-www-form-urlencoded',
}
data = {
    'login': 'admin',
    'password': 'x1234567890',
    'db': 'db12-spain',
}
base_url = 'http://127.0.0.1'

req = requests.get('{}/api/auth/token'.format(base_url),
  data=data, headers=headers)

print(req)

content = json.loads(req.content.decode('utf-8'))

# or add the access token to the headers
headers['access-token'] = content.get('access_token')
print(headers)