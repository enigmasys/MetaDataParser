import csv
import json

# read csv file and extract data between line 0 and line 81
data = []
with open('file.csv', 'r') as file:
    reader = csv.reader(file, delimiter=',')
    for i, row in enumerate(reader):
        if i > 81:
            break
        elif i == 0:
            headers = row
        else:
            data.append(row)
            
# create dictionary to hold data
output = {"Device": {}, "Measurement": {}, "Subject": {}, "Study Center": {}, "Sensor": []}

# loop through rows and add data to dictionary
for row in data:
    if len(row) == 1 or row == []:
        continue
    elif row[0] in output.keys():
        if row[0] == "Sensor":
            sensor_data = {"Sensor type": row[1], "Range": row[2], "Resolution": row[3], "Units": row[4], "Additional information": row[5]}
            output["Sensor"].append(sensor_data)
        else:
            for i in range(1, len(row)):
                output[row[0]][headers[i-1]] = row[i]
                
# output dictionary as json to result.json file
with open('result.json', 'w') as file:
    json.dump(output, file, indent=4)
