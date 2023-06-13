import csv
import json

# Read the file.csv and store it in a dictionary.
data = {}
with open('file.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        if row:
            data[row[0]] = row[1]

# Create an empty dictionary for the output json object.
output = {}

# Populate the Device properties.
device = {}
device["Device Type"] = data["Device Type"]
device["Device Model"] = data["Device Model"]
device["Device Unique Serial Code"] = data["Device Unique Serial Code"]
device["Device Firmware Version"] = data["Device Firmware Version"]
device["Calibration Date"] = data["Calibration Date"]
device["Application name & version"] = data["Application name & version"]
output["Device"] = device

# Populate the Measurement properties.
measurement = {}
measurement["Measurement Frequency"] = data["Measurement Frequency"]
measurement["Start Time"] = data["Start Time"]
measurement["Last measurement"] = data["Last measurement"]
measurement["Device Location Code"] = data["Device Location Code"]
measurement["Time Zone"] = data["Time Zone"]
output["Measurement"] = measurement

# Populate the Subject properties.
subject = {}
subject["Subject Code"] = data["Subject Code"]
subject["Date of Birth"] = data["Date of Birth"]
subject["Sex"] = data["Sex"]
subject["Height"] = data["Height"]
subject["Weight"] = data["Weight"]
subject["Handedness Code"] = data["Handedness Code"]
subject["Subject Notes"] = data["Subject Notes"]
output["Subject"] = subject

# Populate the Study Center properties.
study_center = {}
study_center["Study Centre"] = data["Study Centre"]
study_center["Study Code"] = data["Study Code"]
study_center["Investigator ID"] = data["Investigator ID"]
study_center["Exercise Type"] = data["Exercise Type"]
study_center["Config Operator ID"] = data["Config Operator ID"]
study_center["Config Time"] = data["Config Time"]
study_center["Config Notes"] = data["Config Notes"]
study_center["Extract Operator ID"] = data["Extract Operator ID"]
study_center["Extract Time"] = data["Extract Time"]
study_center["Extract Notes"] = data["Extract Notes"]
output["Study Center"] = study_center

# Populate the Sensor properties.
sensors = []
for i in range(6):
    sensor = {}
    sensor["Sensor type"] = data["Sensor type,"+str(i+1)]
    sensor["Range"] = data["Range,"+str(i+1)]
    sensor["Resolution"] = data["Resolution,"+str(i+1)]
    sensor["Units"] = data["Units,"+str(i+1)]
    sensor["Additional information"] = data["Additional information,"+str(i+1)]
    sensors.append(sensor)
output["Sensor"] = sensors

# Convert the output dictionary to json and write it to file.
with open('result.json', 'w') as f:
    json.dump(output, f)
