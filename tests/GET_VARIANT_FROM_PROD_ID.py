import requests

SHOPIFY_API_KEY = ''
SHOPIFY_API_PASSWORD = ''

#API boilerplate
https = 'https://'
base_url = 'storename.myshopify.com/admin/'
shopify_call_category = {1:'Products', 2:'Orders', 3:'Variants'} #will be set based on what category is selected
headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
json = '.json'
fields = '?fields=id'
auth1 = 'SHOPIFY_API_KEY, SHOPIFY_API_PASSWORD'

prod_id = [397067645,397067657]
 #test, will be a list of prod_ids for the final script, iterate with for x in list

variant_ids = []

for id in prod_id:
    response = requests.get(url=(full_url), headers=headers, auth=(auth1))
    variant_id = response.text
    variant_ids.append(variant_id)


print(variant_ids)
s = input('neeeeeeeeeeeeeeeed input!')



#response = requests.get('https://ims-fba-inventory.myshopify.com/admin/
#products
#/
#397067665
#/
#variants
#.json?fields=id
#',headers=headers, auth=(SHOPIFY_API_KEY,SHOPIFY_API_PASSWORD))
