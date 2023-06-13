import csv
import json

# Open the file.csv
with open('file.csv', newline='') as csvfile:
    # Read the rows and store them in a list
    rows = list(csv.reader(csvfile))
    
    # Initialize empty dictionary for json object
    json_object = {}
    
    # Initialize variables for tracking sections
    current_section = ""
    current_sensor = -1
    
    # Loop through rows
    for row in rows:
        # Ignore empty rows
        if not row:
            continue
            
        # Check if row is a section header
        if row[0].endswith(":"):
            # Set current section
            current_section = row[0].replace(":", "")
            # Add section to json object if does not exist
            if current_section not in json_object:
                json_object[current_section] = {}
                # Check if current section is a sensor
                if current_section == "Sensor":
                    # Increment current sensor counter
                    current_sensor += 1
                    
        # Add key-value pair to current section
        else:
            # Get key and value from row
            key = row[0]
            value = row[1]
            # Add key-value pair to current section
            json_object[current_section][key] = value
            # Check if current section is a sensor
            if current_section == "Sensor":
                # Add current sensor to list in json object
                if "Sensor" not in json_object:
                    json_object["Sensor"] = []
                # Add new sensor object to list
                if current_sensor == len(json_object["Sensor"]):
                    json_object["Sensor"].append({})
                # Add key-value pair to current sensor
                json_object["Sensor"][current_sensor][key] = value

# Open the file result.json for writing
with open('result.json', 'w') as jsonfile:
    # Write the json object to file
    json.dump(json_object, jsonfile, indent=4)
