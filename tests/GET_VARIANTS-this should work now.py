import requests
from time import sleep

#Insert the results of 'get250most-recent_productID_title_created_at.py' into the prod_id list after removing the unneeded data
#Run this script in Powershell and direct the Print output to a file with today's date

#boilerplate
SHOPIFY_API_KEY = ''
SHOPIFY_API_PASSWORD = ''
headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
auth1 = 'SHOPIFY_API_KEY, SHOPIFY_API_PASSWORD'

#url construction
url_1 = 'https://storename.myshopify.com/admin/products/'
url_2 = '/variants.json?fields=id'

#product_ids needed for middle of URL 
prod_id = []
#empty results list
variant_ids = []

for id in prod_id:
    full_url = url_1 + str(id) + url_2
    response = requests.get(url=(full_url),headers=headers, auth=(SHOPIFY_API_KEY,SHOPIFY_API_PASSWORD))
    variant_ids.append(response.text)
    sleep(1)


print(variant_ids)
















#structure of the call, just for reference
#response = requests.get('https://ims-fba-inventory.myshopify.com/admin/
#products
#/
#397067665
#/
#variants
#.json?fields=id
#',headers=headers, auth=(SHOPIFY_API_KEY,SHOPIFY_API_PASSWORD))

#VARIANT.txt
