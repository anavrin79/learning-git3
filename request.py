import requests
import csv

response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data = response.json()

#from werkzeug.datastructures import MultiDict

# open the file in the write mode
f = open('csv_file.csv', 'w')

# create the csv writer
writer = csv.writer(f)

for value in data[0]['rates']:
    #print(value['currency'], value['code'], value['bid'], value['ask'])
    line = value['currency'], value['code'], value['bid'], value['ask']
    writer.writerow(line)

# close the file
f.close()