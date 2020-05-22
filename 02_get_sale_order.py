# -*- coding: utf-8 -*-

import requests

url = "http://localhost:80/api/sale.order"


# "{"limit": 20, "fields": "['id', 'partner_id', 'name']", "domain":"[('id', '>', '10')]", "offset":3}"
payload = '{"limit": 20}'

headers = {
'access-token': "access_token_7a43b56a63fd9130e680011b974d69cc8c9e0d6c",
'content-type': "application/json"
}

response = requests.request("GET", url, data=payload, headers=headers)

print(response.text)