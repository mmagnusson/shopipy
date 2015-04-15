# py3
# library of commonly-used Shopify functions

# NOT USED YET IN PRODUCTION

import pypyodbc
import os
import json
import requests
import sys


# check for fba_needs.csv file
def check_for_fba_csv(fba_needs_path):
    if os.path.exists(fba_needs_path) is True:
        fba_file_exists = True
        print("fba_needs file found, running data retrieval program")
    else:
        fba_file_exists = False
        print("fba_needs file not found, exiting program")
        sys.exit(1)
    return fba_file_exists


# If the FBA file exists, open connection and continue program
def open_diva_connection(fba_file_exists): #add settings authentication string to this, and pass to the connect method
    if fba_file_exists is True:
        try:
            conn = pypyodbc.connect("DRIVER={SQL Server};SERVER=;UID=;PWD=;DATABASE=")
            #take note of the Trusted_Connection=yes when logging in w/out 'sa'
            database_connection = True
            print("Connection to database established")
        except:
            database_connection = False
            print("Failure connecting to database")

    return database_connection # bool


def create_cursor(conn):
    cur = conn.cursor()

    return cur


def execute_and_commit_sql(cur, sql_string):
    if database_connection is True:
        cur.execute(sql_string)
        cur.commit()
    else:
