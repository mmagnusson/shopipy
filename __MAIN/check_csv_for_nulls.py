#python3.4
import csv
import pypyodbc
import os
import easygui

print("This script will check the needs.csv for any itemnumbers that have no corresponding Shopify variant_id in the DB lookup table")
print("If there is no corresponding variant_id, the item cannot be included in the create_order call to Shopify")
print("Output = nulls.txt in the _Automation\_shopify_needs folder reporting item numbers in fba_needs with no corresponding variant_id in the lookup table")

# check for .csv file on the network drive
# the backslashes need to be escaped, that's why they are doubled up here and below
import_file_exists = None
import_needs_path = ""
#filepath = easygui.fileopenbox()
null_list_filepath = ""

# check for needs.csv file
if os.path.exists(import_needs_path) is True:
    import_file_exists = True
    print("File to upload found, running data retrieval program")
else:
    import_file_exists = False
    print("needs file not found, exiting program")
    sys.exit(1)

    
# If the FBA file exists, open connection and continue program
if import_file_exists is True:
    try:
        conn = pypyodbc.connect("DRIVER={SQL Server};SERVER=server;UID=uid;PWD=pwd;DATABASE=database") #mod to get from settings.py
        #take note of the Trusted_Connection=yes when logging in w/out 'sa'
        cur = conn.cursor()
        print("Connection to database established")
    except:
        print("Failure connecting to database")


# SQL STATEMENTS:
print("Retrieving data from database...")
# delete any old data from the ShopifyNeeds table before inserting new data from file
cur.execute("delete from dbo.ShopifyNeeds")
cur.commit()
# bulk insert new data from the needs csv file
cur.execute("BULK INSERT ShopifyNeeds FROM 'needs.csv' WITH(FIRSTROW = 2,FIELDTERMINATOR = ',',ROWTERMINATOR = '\n')")
#mod_filepath = filepath.replace("\\", "\\\\")
#cur.execute("BULK INSERT ShopifyNeeds FROM " + "'" + filepath + "'" + " WITH(FIRSTROW = 2,FIELDTERMINATOR = ',',ROWTERMINATOR = '\n')")
cur.commit()
# Selecting data from table join that will display item
cur.execute("SELECT variant_id, ItemNumber FROM shopifyFBANeeds LEFT JOIN ShopifyVariantIDLookup ON shopifyFBANeeds.ItemNumber=ShopifyVariantIDLookup.title where variant_id is Null")
# sets fba_needs_query_results to a list of pairs ex: [(None, 6), (1037377993, 5), (1037378305, 15)] (THIS IS WHERE NULLS APPEAR)
fba_needs_query_results = cur.fetchall()
# close the connection -> when?  at the end?  or after the calls are complete?
cur.close()
conn.close()
print("Data retrieved, closing database connection.")


# finding the nulls!
nulls_list = []
for element in fneeds_query_results:
    if not element[0]:
        nulls_list.append("Null value found for " + element[1])                              
        print(element[1])
f = open(null_list_filepath, 'w+')
for i in nulls_list:
    f.write(str(i) + '\n')
f.close()


# ending
print("needs.csv has been checked for nulls.")
