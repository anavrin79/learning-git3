from flask import Flask, render_template, request
from collections import defaultdict
import requests
import csv

app = Flask(__name__)

#import pandas as pd

response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data = response.json()

f = open('csv_file.csv', 'w')

# create the csv writer
writer = csv.writer(f)
currency = list()
bids = list()

for value in data[0]['rates']:
    line = value['currency'], value['code'], value['bid'], value['ask']
    writer.writerow(line)
    currency.append(value['code'])
    #bids.append(value['bid']) # not necessery as we read it from file

f.close()

temp = list()

@app.route("/requestweb/", methods=["GET", "POST"])
def requestweb():
    if request.method == "POST":
        data = request.form
        with open('csv_file.csv') as f:
            d = defaultdict(list)
            for line in f:
                line_from_file = line.split(",")
                for codefromfile in line_from_file[1]:
                    if (line_from_file[1] == data.get('currency')):
                        amount_to_exchange = int(data.get('amount'))
                        bid_to_exchange = float(line_from_file[2])
                        f.close()
                        amount2get = str(bid_to_exchange*amount_to_exchange) 
                        return render_template("requestwebform.html", currency = currency, bids = bids, amount2get = amount2get, amount = amount_to_exchange, codefromfile = data.get('currency'))

    amount2get="___"
    empty = "___"
    amount_to_exchange = "___"
    return render_template("requestwebform.html", currency = currency, bids = bids, amount2get = empty, amount_to_exchange = amount_to_exchange)

if __name__ == "__main__":
    app.run(debug=True)