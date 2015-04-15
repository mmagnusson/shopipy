#using python3

import json
import requests

SHOPIFY_API_KEY = ''
SHOPIFY_API_PASSWORD = ''

url = 'https://storename.myshopify.com/admin/orders.json'

############
json_data = open('C:\\Users\\test_data.json.json')
fba_json_data = json.load(json_data)


data_string = "{'order': {'line_items': " + str(fba_json_data) + "}}"

headers = {'Content-type': 'application/json', 'Accept': 'application/json'}

new_order = requests.post(url, data=json.dumps(data_string),headers=headers, auth=(SHOPIFY_API_KEY,SHOPIFY_API_PASSWORD))


###
#upload file to location -> trigger for when file changes?
#update View
#auto-save csv in a location?  on the web server?
#begin call process:
###
