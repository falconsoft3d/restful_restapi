# -*- coding: utf-8 -*-

import requests

url = "http://localhost:80/api/product.template"

headers = {
'access-token': "access_token_7a43b56a63fd9130e680011b974d69cc8c9e0d6c",
'content-type': "application/json"
}

payload = '{"name": "Demmo REST API", "price_unit":4000}'

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)