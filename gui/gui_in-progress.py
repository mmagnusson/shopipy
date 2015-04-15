import easygui
import sys
import csv
import pypyodbc
import os


#SPACE FOR DEFINING FUNCTIONS



while 1:
    # Main button screen
    msg ="Each button represents a step in the ShopiPy process"
    title = "ShopiPy inventory"
    choices = ["Select File", "Null ID check", "Create Order", "Cancel"]
    choice = easygui.buttonbox(msg, title, choices)

    #########################
    # Button selection logic#
    #########################
    # File selection process
    filepath = None
    if choice is "Select File":
        easygui.msgbox("Please select a file from the GNAS drive and make sure it is not currently open")
        filepath = easygui.fileopenbox() #returns single-slash windows path, TO-DO: deal with this
        easygui.msgbox("Path to file is " + str(filepath))
        mod_filepath = filepath.replace("Z:", "\\\\ims-server1\\GNAS")
        easygui.msgbox("Network path to file is " + str(mod_filepath))

    # Null ID Check process
    elif choice is "Null ID check":
        easygui.msgbox('''This script will check the fba_needs.csv for any itemnumbers that have no corresponding Shopify variant_id in the Diva lookup table \n
        If there is no corresponding variant_id, the item cannot be included in the create_order call to Shopify \n
        Output = nulls.txt in the GNAS\_Automation\_shopify_fba_needs folder reporting item numbers in fba_needs with no corresponding variant_id in the lookup table''')
        # check for fba_needs.csv file on the gnas drive
        # the backslashes need to be escaped, that's why they are doubled up here and below
        import_file_exists = None
        fba_needs_path = str(mod_filepath)
        null_list_filepath = ""
        # check for fba_needs.csv file
        if os.path.exists(fba_needs_path) is True:
            import_file_exists = True
            easygui.msgbox("File to upload found, running data retrieval program")
        else:
            import_file_exists = False
            easygui.msgbox("fba_needs file not found, exiting program")
            sys.exit(0)
        # If the FBA file exists, open connection and continue program
        if import_file_exists is True:
            try:
                conn = pypyodbc.connect("DRIVER={SQL Server};SERVER=;UID=;PWD=;DATABASE=") #store in a settings file
                #take note of the Trusted_Connection=yes when logging in w/out 'sa'
                cur = conn.cursor()
                easygui.msgbox("Connection to database established")
            except:
                easygui.msgbox("Failure connecting to database")
        # SQL STATEMENTS:
        easygui.msgbox("Retrieving data from database...")
        # delete any old data from the ShopifyFBANeeds table before inserting new data from file
        cur.execute("delete from divadb.dbo.shopifyFBANeeds")
        cur.commit()
        # bulk insert new data from the fba_needs csv file
        #cur.execute("BULK INSERT shopifyFBANeeds FROM '\\\\ims-server1\\GNAS\\_Automation\\_shopify_fba_needs\\fba_needs.csv' WITH(FIRSTROW = 2,FIELDTERMINATOR = ',',ROWTERMINATOR = '\n')")
        cur.execute("BULK INSERT shopifyFBANeeds FROM " + "'" + fba_needs_path + "'" + " WITH(FIRSTROW = 2,FIELDTERMINATOR = ',',ROWTERMINATOR = '\n')")
        cur.commit()
        # Selecting data from table join that will display item
        cur.execute("SELECT variant_id, ItemNumber FROM shopifyFBANeeds LEFT JOIN ShopifyVariantIDLookup ON shopifyFBANeeds.ItemNumber=ShopifyVariantIDLookup.title where variant_id is Null")
        # sets fba_needs_query_results to a list of pairs ex: [(None, 6), (1037377993, 5), (1037378305, 15)] (THIS IS WHERE NULLS APPEAR)
        fba_needs_query_results = cur.fetchall()
        # close the connection -> when?  at the end?  or after the calls are complete?
        cur.close()
        conn.close()
        easygui.msgbox("Data retrieved, closing database connection.")
        # finding the nulls!
        nulls_list = []
        for element in fba_needs_query_results:
            if not element[0]:
                nulls_list.append("Null value found for " + element[1])
                #print(element[1])
        f = open(null_list_filepath, 'w+')
        for i in nulls_list:
            f.write(str(i) + '\n')
        f.close()
        # ending
        easygui.msgbox("File has been checked for nulls.")

    #Create the API call to make new order out of FBA data
    elif choice is "Create Order":
        pass

    else:
        pass


    msg = "Do you want to continue?"
    title = "Please Confirm"
    
    if easygui.ccbox(msg, title):     # show a Continue/Cancel dialog
        pass  # user chose Continue
    else:
        sys.exit(0)           # user chose Cancel
