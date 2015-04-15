#using python3

import json
import requests

SHOPIFY_API_KEY = ''
SHOPIFY_API_PASSWORD = ''

url = 'https://storename.myshopify.com/admin/orders.json'
data = {'order': {'line_items': [{'variant_id': ,'quantity': }]}}
headers = {'Content-type': 'application/json', 'Accept': 'application/json'}

new_order = requests.post(url, data=json.dumps(data),headers=headers, auth=(SHOPIFY_API_KEY,SHOPIFY_API_PASSWORD))

new_order_info = new_order.json()
print(new_order_info)


#EXAMPLE: r = requests.post(url, data=json.dumps(data), headers=headers)
#using 10 X PAR-ACDPRPL- as a test product in the new store
#
#requets.json() -> use to retrieve the json from get call
