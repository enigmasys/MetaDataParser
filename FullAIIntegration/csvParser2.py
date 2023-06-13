import csv
import json

# Define input and output file paths
input_file = 'file.csv'
output_file = 'result.json'

# Load the json schema
with open('json_schema.xml') as f:
    schema = json.loads(f.read())

# Define a function to convert csv rows to json objects
def row_to_json(row):
    data = {}
    for key in schema['properties']:
        if key == 'Sensor':
            # Handle multiple sensor objects in an array
            sensor_arr = []
            for i in range(6):
                sensor = {}
                for prop in schema['properties']['Sensor']['items'][i]['properties']:
                    col_num = schema['properties']['Sensor']['items'][i]['properties'][prop]['column']
                    sensor[prop] = row[col_num].strip()
                sensor_arr.append(sensor)
            data['Sensor'] = sensor_arr
        else:
            col_num = schema['properties'][key]['column']
            data[key] = row[col_num].strip()
    return data

# Open the input file and loop through rows
with open(input_file, 'r') as f:
    csv_reader = csv.reader(f, delimiter=',')
    # Skip header row
    next(csv_reader)
    # Create an array to hold the json objects
    json_data = []
    for row in csv_reader:
        # Ignore empty rows
        if row[0] != '':
            json_obj = row_to_json(row)
            json_data.append(json_obj)

# Write the json objects to the output file
output = {'Device': json_data[0], 'Measurement': json_data[1], 'Subject': json_data[2],
          'Study Center': json_data[3], 'Sensor': json_data[4]['Sensor']}
with open(output_file, 'w') as f:
    f.write(json.dumps(output, indent=4))
