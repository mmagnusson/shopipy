#python3

import pypyodbc
import os
import json
import requests
import sys
import easygui

##########################################
# data retrieval and processing
###########################################

# file needs to be titled "fba_needs.csv" and saved at the right location on the GNAS drive
# prompt user to find and select file?  add the input to variable instead of hardcoding filepath and name


# check for fba_needs.csv file on the gnas drive
# the backslashes need to be escaped, that's why they are doubled up here and below
fba_file_exists = None
#filepath = easygui.fileopenbox()
fba_needs_path = "\\\\ims-server1\\GNAS\\_Automation\\_shopify_fba_needs\\fba_needs.csv"

# check for fba_needs.csv file
if os.path.exists(fba_needs_path) is True:
    fba_file_exists = True
    print("File to upload found, running data retrieval program")
else:
    fba_file_exists = False
    print("fba_needs file not found, exiting program")
    sys.exit(1)
    
        
# If the FBA file exists, open connection and continue program
if fba_file_exists is True:
    try:
        conn = pypyodbc.connect("DRIVER={SQL Server};SERVER=;UID=;PWD=;DATABASE=")
        #take note of the Trusted_Connection=yes when logging in w/out 'sa'
        cur = conn.cursor()
        print("Connection to database established")
    except:
        print("Failure connecting to database")


# SQL STATEMENTS:
print("Retrieving data from database...")
# delete any old data from the ShopifyFBANeeds table before inserting new data from file
cur.execute("delete from divadb.dbo.shopifyFBANeeds")
cur.commit()
# bulk insert new data from the fba_needs csv file
cur.execute("BULK INSERT shopifyFBANeeds FROM '\\\\ims-server1\\GNAS\\_Automation\\_shopify_fba_needs\\fba_needs.csv' WITH(FIRSTROW = 2,FIELDTERMINATOR = ',',ROWTERMINATOR = '\n')")
#cur.execute("BULK INSERT shopifyFBANeeds FROM " + filepath + "WITH(FIRSTROW = 2,FIELDTERMINATOR = ',',ROWTERMINATOR = '\n')")
cur.commit()
# Selecting data from ShopifyFBANeeds table
cur.execute("SELECT * FROM ShopifyFBAVariantAndQuantity_view")
# sets fba_needs_query_results to a list of pairs ex: [(None, 6), (1037377993, 5), (1037378305, 15)] (THIS IS WHERE NULLS APPEAR)
fba_needs_query_results = cur.fetchall()
# close the connection -> when?  at the end?  or after the calls are complete?
cur.close()
conn.close()
print("Data retrieved, closing database connection.")


# constructs a list from the sql_results list, adding the necessary JSON keys in this format -> {'variant_id': 1035374081,'quantity': 1}
fba_needs_list = []
for element in fba_needs_query_results:
    if not element[0]:
        print("Null value found for" + str(element))
    else:
        opening = '{'
        closing = '}'
        fba_needs_list.append(opening + '"variant_id"' + ':' + str(element[0]) + ', ' + '"quantity"' + ':' + str(element[1]) + closing)


# dumping to JSON
fba_json_data = json.dumps(fba_needs_list)


# remove when the user input section is working correctly
create_new_order = True


##########################################
# generating create_order calls
###########################################
SHOPIFY_API_KEY = ''
SHOPIFY_API_PASSWORD = ''
headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
url = 'https://ims-fba-inventory.myshopify.com/admin/orders.json'


if create_new_order is True:
    data_string = '{"order": {"line_items": ' + str(fba_needs_list) + '}}' # string
    data_string_noquotes = data_string.replace("'", "")
    new_order = requests.post(url=url, data=data_string_noquotes, headers=headers, auth=(SHOPIFY_API_KEY, SHOPIFY_API_PASSWORD))
    new_order_info = new_order.json()
    new_order_status = new_order.status_code
    if new_order_status is "200" or "201":
        print("Order created successfully!")
    else:
        print("API call returned error " + str(new_order.status_code) + str(new_order.json()) + " please contact IT")


wait_for_end = input("Press a Enter to exit program.")




# create order option, or save the data to file _was previously
# create_order_yes = "yes"
# create_order_no = "no"
# user_input = input("Create a Shopify order from this data? yes/no").lower()
# if user_input is create_order_yes:
#     create_order = True
#     print("you gonna create an order, brah!")
#     wait = input("WAITING")
# else:
#     create_order = False
#     # check for fba_results file
#     # to-do later: create a open and write function for the if-else cond down there
#     if os.path.exists(fba_results_path) is True:
#         fba_results_exists = True
#         print("fba_results file found, saving")
#         file = open(fba_results_path, 'w')
#         file.write(str(fba_needs_list))
#         file.close()
#         if os.path.exists(fba_results_path) is True:
#             fba_results_exists = True
#             print("File saved successfully!")
#         else:
#             fba_results_exists = False
#             print("Error saving file, please contact IT.  Press Enter to continue")
#     else:
#         fba_results_exists = False
#         print("fba_needs file not found, creating new and saving")
#         file = open(fba_results_path, 'w')
#         file.write(str(fba_needs_list))
#         file.close()
#         if os.path.exists(fba_results_path) is True:
#             fba_results_exists = True
#             print("File saved successfully!")
#         else:
#             fba_results_exists = False
#             print("Error saving file, please contact IT.  Press Enter to continue")

    #open new file
    #write fba_needs_list to file
    #close file
    #return message "file saved successfully"







