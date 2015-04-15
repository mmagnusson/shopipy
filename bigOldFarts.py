import requests
import easygui

SHOPIFY_API_KEY = ''
SHOPIFY_API_PASSWORD = ''
headers = {'Content-type': 'application/json', 'Accept': 'application/json'}

easygui.msgbox('''This program will retrieve the Product ID, Title and Created_at fields for the 250 most recently created products on Shopify.
Manual processing of the file will be needed to extract only the ProductID to feed into the GET_VARIANTS.py script
               ''') 

get_ids1 = requests.get('https://storename.myshopify.com/admin/products.json?fields=id,title,created_at&limit=250&page=1&order=created_at+desc',headers=headers, auth=(SHOPIFY_API_KEY,SHOPIFY_API_PASSWORD))
file1 = open('250most_recently_created_products.txt','w+')
file1.write(get_ids1.text)
file1.close()

print("Process completed")
