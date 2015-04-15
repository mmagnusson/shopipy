
#THIS IS SOOOOOOOOOOOOOOOOO DUMB...THINK ABOUT HOW TO IMPLEMENT SOME EASY ITERATION

import requests

SHOPIFY_API_KEY = ''
SHOPIFY_API_PASSWORD = ''
headers = {'Content-type': 'application/json', 'Accept': 'application/json'}


get_ids1 = requests.get('https://storename.myshopify.com/admin/products.json?fields=id,handle&limit=250&page=1&order=created_at+desc',headers=headers, auth=(SHOPIFY_API_KEY,SHOPIFY_API_PASSWORD))
file1 = open('newfile1.txt','w+')
file1.write(get_ids1.text)
file1.close()
get_ids2 = requests.get('https://storename.myshopify.com/admin/products.json?fields=id,handle&limit=250&page=2&order=created_at+desc',headers=headers, auth=(SHOPIFY_API_KEY,SHOPIFY_API_PASSWORD))
file1 = open('newfile2.txt','w+')
file1.write(get_ids2.text)
file1.close()
get_ids3 = requests.get('https://storename.myshopify.com/admin/products.json?fields=id,handle&limit=250&page=3&order=created_at+desc',headers=headers, auth=(SHOPIFY_API_KEY,SHOPIFY_API_PASSWORD))
file1 = open('newfile3.txt','w+')
file1.write(get_ids3.text)
file1.close()


wait = input('sup bitches, we done')



