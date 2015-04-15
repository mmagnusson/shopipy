#THIS IS SOOOOOOOOOOOOOOOOO DUMB...THINK ABOUT HOW TO IMPLEMENT SOME EASY ITERATION

import requests

SHOPIFY_API_KEY = ''
SHOPIFY_API_PASSWORD = ''
headers = {'Content-type': 'application/json', 'Accept': 'application/json'}


get_ids1 = requests.get('https://storename.myshopify.com/admin/products.json?fields=id,title&limit=250&page=1',headers=headers, auth=(SHOPIFY_API_KEY,SHOPIFY_API_PASSWORD))
file1 = open('file1.txt','w+')
file1.write(get_ids1.text)
file1.close()
get_ids2 = requests.get('https://storename.myshopify.com/admin/products.json?fields=id,title&limit=250&page=2',headers=headers, auth=(SHOPIFY_API_KEY,SHOPIFY_API_PASSWORD))
file2 = open('file2.txt','w+')
file2.write(get_ids2.text)
file2.close()
get_ids3 = requests.get('https://storename.myshopify.com/admin/products.json?fields=id,title&limit=250&page=3',headers=headers, auth=(SHOPIFY_API_KEY,SHOPIFY_API_PASSWORD))
file3 = open('file3.txt','w+')
file3.write(get_ids3.text)
file3.close()
get_ids4 = requests.get('https://storename.myshopify.com/admin/products.json?fields=id,title&limit=250&page=4',headers=headers, auth=(SHOPIFY_API_KEY,SHOPIFY_API_PASSWORD))
file4 = open('file4.txt','w+')
file4.write(get_ids4.text)
file4.close()
get_ids5 = requests.get('https://storename.myshopify.com/admin/products.json?order=created_at+DESC?fields=id,title&limit=250&page=5',headers=headers, auth=(SHOPIFY_API_KEY,SHOPIFY_API_PASSWORD))
file5 = open('file5.txt','w+')
file5.write(get_ids5.text)
file5.close()
get_ids6 = requests.get('https://storename.myshopify.com/admin/products.json?fields=id,title&limit=250&page=6',headers=headers, auth=(SHOPIFY_API_KEY,SHOPIFY_API_PASSWORD))
file6 = open('file6.txt','w+')
file6.write(get_ids6.text)
file6.close()
get_ids7 = requests.get('https://storename.myshopify.com/admin/products.json?fields=id,title&limit=250&page=7',headers=headers, auth=(SHOPIFY_API_KEY,SHOPIFY_API_PASSWORD))
file7 = open('file7.txt','w+')
file7.write(get_ids7.text)
file7.close()
get_ids8 = requests.get('https://storename.myshopify.com/admin/products.json?fields=id,title&limit=250&page=8',headers=headers, auth=(SHOPIFY_API_KEY,SHOPIFY_API_PASSWORD))
file8 = open('file8.txt','w+')
file8.write(get_ids8.text)
file8.close()
get_ids9 = requests.get('https://storename.myshopify.com/admin/products.json?fields=id,title&limit=250&page=9',headers=headers, auth=(SHOPIFY_API_KEY,SHOPIFY_API_PASSWORD))
file9 = open('file9.txt','w+')
file9.write(get_ids9.text)
file9.close()
get_ids10 = requests.get('https://storename.myshopify.com/admin/products.json?fields=id,title&limit=250&page=10',headers=headers, auth=(SHOPIFY_API_KEY,SHOPIFY_API_PASSWORD))
file10 = open('file10.txt','w+')
file10.write(get_ids10.text)
file10.close()
get_ids11 = requests.get('https://storename.myshopify.com/admin/products.json?fields=id,title&limit=250&page=11',headers=headers, auth=(SHOPIFY_API_KEY,SHOPIFY_API_PASSWORD))
file11 = open('file11.txt','w+')
file11.write(get_ids11.text)
file11.close()
get_ids12 = requests.get('https://storename.myshopify.com/admin/products.json?fields=id,title&limit=250&page=12',headers=headers, auth=(SHOPIFY_API_KEY,SHOPIFY_API_PASSWORD))
file12 = open('file12.txt','w+')
file12.write(get_ids12.text)
file12.close()
get_ids13 = requests.get('https://storename.myshopify.com/admin/products.json?fields=id,title&limit=250&page=13',headers=headers, auth=(SHOPIFY_API_KEY,SHOPIFY_API_PASSWORD))
file13 = open('file13.txt','w+')
file13.write(get_ids13.text)
file13.close()


wait = input('sup bitches, we done')



