#!/usr/bin/env python3
#intended to convert a CSV file into a json structure

import csv  
import json  
  
# Open the CSV  
#f = open( '/path/to/filename.csv', 'rU' )

f = open('C:\\Users\\mike.magnusson\\Desktop\\shopify_fba_inventory\\csv_json\\testcsv.csv', 'rU' )

# Change each fieldname to the appropriate field name. I know, so difficult.  
reader = csv.DictReader( f, fieldnames = ( "variant_id","quantity" ))

# Parse the CSV into JSON  
out = json.dumps( [ row for row in reader ] )
print("JSON parsed!")

# Save the JSON  
f = open( 'C:\\Users\\mike.magnusson\\Desktop\\shopify_fba_inventory\\csv_json\\testresultlonger.json', 'w')  
f.write(out)  
print("JSON saved!")  




#but the issue here...

#Open csv

#


