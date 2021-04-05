 # -*- coding: utf-8 -*-
import csv,json
from flask import Flask
app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/home/<string:value>', methods = ['GET'])
def disp(value):
    print("-------",value)
    check = {}
    with open('Coding Assignment Investor Sample Data.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
    
        for i in csv_reader:
            print("0000000000000000000",i)
    
            if value.replace("-", " ") == i['\ufeffFull Name']:
                check = i
            
    if check:
        return json.dumps({"Location" : check["Location"]})
    else:
        return json.dumps({"data" : "Investor Does not Exit"})

app.run()