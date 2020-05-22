# -*- coding: utf-8 -*-

import requests

url = "http://localhost:80/api/product.template/2"

headers = {
'access-token': "access_token_7a43b56a63fd9130e680011b974d69cc8c9e0d6c",
'content-type': "application/json"
}

response = requests.delete(url, headers=headers)

print(response.text)