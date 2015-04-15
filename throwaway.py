import requests
import json

# API boilerplate
SHOPIFY_API_KEY = ''
SHOPIFY_API_PASSWORD = ''
headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
auth1 = 'SHOPIFY_API_KEY, SHOPIFY_API_PASSWORD'

#url construction
prod_url = 'https://storename.myshopify.com/admin/products/?fields=title,id,created_at&limit=250&page=1&order=created_at+desc'

a = requests.get(url=(prod_url),headers=headers, auth=(SHOPIFY_API_KEY,SHOPIFY_API_PASSWORD))



e = product_title_prodID.text
returns a string

kill first 13
last 1?

e = product_title_prodID.text
f = e[:-2]
g = f[13:]
h.replace("{", "(")
h.replace('"created_at":', '')
h.replace('"title":', '')
h.replace('"id":', '')
>>> w6 = w5.replace("),(", "), (")
list1 = w6.split(", ")



for line in list1:
    splitList = line.split(',')
    

