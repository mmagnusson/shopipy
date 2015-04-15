# With a 1-column list of SKUs, this program will fetch
# title,product_id and then 

import csv
import easygui
import requests
import json


###################################
#Functions to get and read csv file
def get_file_path(filetype):
    filetype = filetype
    easygui.msgbox("Please select a " + str(filetype) + "file that is not currently open")
    filepath = easygui.fileopenbox() #returns single-slash windows path, TO-DO: deal with this
    easygui.msgbox("Path to file is " + str(filepath))
    #mod_filepath = filepath.replace("Z:", "\\\\server\\shared_drive") #to turn local to a Windows network path
    #easygui.msgbox("Network path to file is " + str(mod_filepath))
    return filepath


def read_csv_to_py_list(filepath):
    with open(filepath, 'r') as sku_csv:
        sku_list = []
        for line in sku_csv:
            sku_list.append(line)
    return sku_list

#####################################
# Functions to clean up the call data
def remove_dict_info(string):
    string_line = string
    no_created = string_line.replace('"created_at":', '')
    no_title = no_created.replace('"title":', '')
    no_id = no_title.replace('"id":', '')
    no_brace = no_id.replace("{", "(")
    no_brace2 = no_brace.replace("}", ")")
    almost_clean = no_brace2.replace("),(", "), (")
    ready_for_split_on_space = almost_clean
    return ready_for_split_on_space

def create_list_from_string(string)
    green_mile_string = string
    awesome_list = green_mile_string.split(", ")
    return awesome_list



##########################################
filepath = get_file_path('CSV')
sku_list = read_csv_to_py_list(filepath)


# now we have the list of skus, does the \\n need to be removed?
##new_sku_list = []
##for line in sku_list:
##    stringLine = str(line)
##    rem_newline = stringLine.replace("\\n", "")
##    new_sku_list.append(rem_newline)
##########################################
# API boilerplate
SHOPIFY_API_KEY = ''
SHOPIFY_API_PASSWORD = ''
headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
auth = 'SHOPIFY_API_KEY, SHOPIFY_API_PASSWORD'


#TO-DO: allow user to enter how many items, and make X amount of calls that return 250 items each
prod_url = 'https://storename.myshopify.com/admin/products/?fields=title,id,created_at&limit=250&page=1&order=created_at+desc'

product_title_prodID = requests.get(url=(prod_url),headers=headers, auth=(SHOPIFY_API_KEY,SHOPIFY_API_PASSWORD))

string_product_title_prodID = product_title_prodID.text
clean  remove_dict_info(string_product_title_prodID)
a
b
c
d
e
f
g



jsondata = product_title_prodID.json() #get json data from call response



list_created_title_prodID = jsondata['products'] # cut out the products key and return list of the subvalues
clean_list_created_title_prodID = clean_list(list_created_title_prodID) # removing dict text from each line, inserting into new list


rem_last_two = clean_list_created_title_prodID[:-2]
rem_first_thirteen = rem_last_two[13:]
rem_first_thirteen = 


###url construction
##url_1 = 'https://storename.myshopify.com/admin/products/'
##url_2 = '/variants.json?fields=id'

##for id in prod_id:
##    full_url = url_1 + str(id) + url_2
##    response = requests.get(url=(full_url),headers=headers, auth=(SHOPIFY_API_KEY,SHOPIFY_API_PASSWORD))
##    variant_ids.append(response.text)
##    sleep(1)
##
##
##
##
##variant_url = 'https://storename.myshopify.com/admin/products/variants.json?fields=product-id,title,id,&limit=250&page=1&order=created_at+desc'
##
##product_title_prodID = requests.get(url=(url_1),headers=headers, auth=(SHOPIFY_API_KEY,SHOPIFY_API_PASSWORD))
##
##title_prodID_varID = requestse.get(url=(url_2),headers=headers, auth=(SHOPIFY_API_KEY,SHOPIFY_API_PASSWORD))
##
##a['products'
##
##
##pprint.pprint(a)
##
##
##from operator import getitem
##
##def getFromDict(dataDict, mapList):
##    return reduce(lambda d, k: d[k], mapList, dataDict)
##
##
##for line in a:
##  print(line)


  
