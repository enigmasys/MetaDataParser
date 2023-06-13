# import necessary packages
import csv
import json

# open and read csv file
with open("file.csv") as f:
    reader = csv.reader(f)
    data = [row for row in reader if row]  # ignore empty rows

# create dictionary to hold extracted data
result = {}

# extract data for Device section
result["Device"] = {}
for row in data:
    if row[0] == "Device Type":
        result["Device"]["Device Type"] = row[1]
    elif row[0] == "Device Model":
        result["Device"]["Device Model"] = row[1]
    elif row[0] == "Device Unique Serial Code":
        result["Device"]["Device Unique Serial Code"] = row[1]
    elif row[0] == "Device Firmware Version":
        result["Device"]["Device Firmware Version"] = row[1]
    elif row[0] == "Calibration Date":
        result["Device"]["Calibration Date"] = row[1]
    elif row[0] == "Application name & version ":
        result["Device"]["Application name & version"] = row[1]

# extract data for Measurement section
result["Measurement"] = {}
for row in data:
    if row[0] == "Measurement Frequency":
        result["Measurement"]["Measurement Frequency"] = row[1]
    elif row[0] == "Start Time":
        result["Measurement"]["Start Time"] = row[1]
    elif row[0] == "Last measurement":
        result["Measurement"]["Last measurement"] = row[1]
    elif row[0] == "Device Location Code":
        result["Measurement"]["Device Location Code"] = row[1]
    elif row[0] == "Time Zone":
        result["Measurement"]["Time Zone"] = row[1]

# extract data for Subject section
result["Subject"] = {}
for row in data:
    if row[0] == "Subject Code":
        result["Subject"]["Subject Code"] = row[1]
    elif row[0] == "Date of Birth":
        result["Subject"]["Date of Birth"] = row[1]
    elif row[0] == "Sex":
        result["Subject"]["Sex"] = row[1]
    elif row[0] == "Height":
        result["Subject"]["Height"] = row[1]
    elif row[0] == "Weight":
        result["Subject"]["Weight"] = row[1]
    elif row[0] == "Handedness Code":
        result["Subject"]["Handedness Code"] = row[1]
    elif row[0] == "Subject Notes":
        result["Subject"]["Subject Notes"] = row[1]

# extract data for Study Center section
result["Study Center"] = {}
for row in data:
    if row[0] == "Study Centre":
        result["Study Center"]["Study Centre"] = row[1]
    elif row[0] == "Study Code":
        result["Study Center"]["Study Code"] = row[1]
    elif row[0] == "Investigator ID":
        result["Study Center"]["Investigator ID"] = row[1]
    elif row[0] == "Exercise Type":
        result["Study Center"]["Exercise Type"] = row[1]
    elif row[0] == "Config Operator ID":
        result["Study Center"]["Config Operator ID"] = row[1]
    elif row[0] == "Config Time":
        result["Study Center"]["Config Time"] = row[1]
    elif row[0] == "Config Notes":
        result["Study Center"]["Config Notes"] = row[1]
    elif row[0] == "Extract Operator ID":
        result["Study Center"]["Extract Operator ID"] = row[1]
    elif row[0] == "Extract Time":
        result["Study Center"]["Extract Time"] = row[1]
    elif row[0] == "Extract Notes":
        result["Study Center"]["Extract Notes"] = row[1]

# extract data for Sensor section
result["Sensor"] = []
for i in range(len(data)):
    if data[i][0] == "Sensor type":
        sensor_data = {}
        sensor_data["Sensor type"] = data[i][1]
        sensor_data["Range"] = data[i+1][1]
        sensor_data["Resolution"] = data[i+2][1]
        sensor_data["Units"] = data[i+3][1]
        sensor_data["Additional information"] = data[i+4][1]
        result["Sensor"].append(sensor_data)

# write extracted data to json file
with open("result.json", "w") as f:
    json.dump(result, f, indent=4)
