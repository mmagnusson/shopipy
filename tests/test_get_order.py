#using python3

import json
import requests

SHOPIFY_API_KEY = ''
SHOPIFY_API_PASSWORD = ''

#API boilerplate
base_url = 'https://storename.myshopify.com/admin/orders/#1035374081.json'
#additons to base
orders/#.json'
headers = {'Content-type': 'application/json', 'Accept': 'application/json'}



#data for call
data = {'order': {'line_items': [{'variant_id': 1035374081,'quantity': 1}]}}

#create new order
new_order = requests.post(url, data=json.dumps(data),headers=headers, auth=(SHOPIFY_API_KEY,SHOPIFY_API_PASSWORD))
#update order
mod_order = requests.put(url + , data=json.dumps(data),headers=headers, auth=(SHOPIFY_API_KEY,SHOPIFY_API_PASSWORD))





GET /admin/products.json?fields=id,title

product_id_and_title.json()

product_id_and_title = requests.get('https://storename.myshopify.com/admin/variants.json?fields=id,title',headers=headers, auth=(SHOPIFY_API_KEY,SHOPIFY_API_PASSWORD))

data = {'order': {'line_items': [{'variant_id': 1035374081,'quantity': 1}]}}
