import csv
import json

csv_file = 'file.csv'
json_file = 'result.json'

# Read CSV file into list
with open(csv_file, 'r') as f:
    reader = csv.reader(f)
    data = [row for row in reader]

# Create a dictionary to store the metadata
metadata = {
    "Device": {
        "Device Type": "",
        "Device Model": "",
        "Device Unique Serial Code": "",
        "Device Firmware Version": "",
        "Calibration Date": "",
        "Application name & version": ""
    },
    "Measurement": {
        "Measurement Frequency": "",
        "Start Time": "",
        "Last measurement": "",
        "Device Location Code": "",
        "Time Zone": ""
    },
    "Subject": {
        "Subject Code": "",
        "Date of Birth": "",
        "Sex": "",
        "Height": "",
        "Weight": "",
        "Handedness Code": "",
        "Subject Notes": ""
    },
    "Study Center": {
        "Study Centre": "",
        "Study Code": "",
        "Investigator ID": "",
        "Exercise Type": "",
        "Config Operator ID": "",
        "Config Time": "",
        "Config Notes": "",
        "Extract Operator ID": "",
        "Extract Time": "",
        "Extract Notes": ""
    },
    "Sensor": []
}

# Update metadata dictionary with CSV data
for row in data[0:81]:
    print(row[0])
    if row[0] in metadata["Device"]:
        metadata["Device"][row[0]] = row[1]
    elif row[0] in metadata["Measurement"]:
        metadata["Measurement"][row[0]] = row[1]
    elif row[0] in metadata["Subject"]:
        metadata["Subject"][row[0]] = row[1]
    elif row[0] in metadata["Study Center"]:
        metadata["Study Center"][row[0]] = row[1]
    elif row[0] == 'Sensor type':
        metadata["Sensor"].append({
            "Sensor type": row[1],
            "Range": row[2],
            "Resolution": row[3],
            "Units": row[4],
            "Additional information": row[5]
        })

# Write metadata dictionary to JSON file
with open(json_file, 'w') as f:
    json.dump(metadata, f, indent=4)
