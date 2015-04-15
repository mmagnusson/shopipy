#py3

##########################################
# CSV and JSON related code
############################################
# CSV_TO_DICT
with open('testcsv.csv', mode='r') as infile:
    reader = csv.reader(infile)

    with open('DICT_new.csv', mode='w') as outfile:
        writer = csv.writer(outfile)
        for rows in reader:
        	mydict = {rows[0]:rows[1]}


print(mydict)
############################################
# CSV_TO_JSON (needs json and csv imported)
def dump_to_json():
    csv_result = []
    filepath = #whatever the filepath is
    with open('filepath', 'r') as csvfile:
        for row in csv.DictReader(csvfile, delimiter=',', quotechar='"'):
            csv_result.append({'variant_id': row['variant_id'], 'quantity': row['quantity']})

    json_feed = [{c['variant_id']: c['quantity']} for c in csv_result]

    with open('C:\\Users\\mike.magnusson\\Desktop\\shopify_fba_inventory\\tests\\test_data\\sample.json', 'w') as outfile:
        json.dump(json_feed, outfile)

# func call
dump_to_json()

print("DONE!")
############################################

############################################
#more variables and options for creating a dynamic call string
############################################

SHOPIFY_API_KEY = ''
SHOPIFY_API_PASSWORD = ''

#API boilerplate
https = 'https://'
base_url = 'storename.myshopify.com/admin/'
shopify_call_category = {1:'Products', 2:'Orders', 3:'Variants'} #will be set based on what category is selected
headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
json = '.json'
auth1 = 'SHOPIFY_API_KEY, SHOPIFY_API_PASSWORD'

#modify for what to pull
fields = '?limit=250, page=11, id, title'

response = requests.get(url=(https + base_url + shopify_call_category[1] + '/' + shopify_call_category[3] + json + fields), headers=headers, auth=(auth1),)
#r = https + base_url + shopify_call_category[1] + json

print(r)
s = input('neeeeeeeeeeeeeeeed input!')



new_order = requests.post(url, data=json.dumps(data),headers=headers, auth=(SHOPIFY_API_KEY,SHOPIFY_API_PASSWORD))
