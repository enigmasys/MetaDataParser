import csv
import json

json_array = []

with open('file.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    i = 0
    obj = {}
    for row in reader:
        if i <= 81:
            if len(row) == 0:
                if bool(obj):
                    json_array.append(obj)
                obj = {}
            else:
                key = row[0].strip()
                value = row[1].strip()
                obj[key] = value
            i += 1
        else:
            break

json_array = [x for x in json_array if bool(x)]
    
with open('output.json', 'w') as outfile:
    json.dump(json_array, outfile)
