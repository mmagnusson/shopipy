#python3
from csv import DictReader

# with open('numberdata.csv', mode='r') as infile:
#     reader = csv.reader(infile)

#     with open('DICT_new.csv', mode='w') as outfile:
#         writer = csv.writer(outfile)
#         for rows in reader:
#         	mydict = {rows[0]:rows[1]}


# print(mydict)


the_reader = DictReader(open('C:\\Users\\mike.magnusson\\Desktop\\shopify_fba_inventory\\csv_json\\numberdata.csv','r'))

mydict = {}

for line_dict in the_reader:
	print(line_dict)

print(mydict)


data = {
	'order': 
		{'line_items': 
			[{'variant_id': 1035374081,
			'quantity': 1}]
	}
}


