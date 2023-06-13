import pandas as pd
import json

# load csv file into pandas dataframe
df = pd.read_csv("file.csv", header=None, nrows=82)

# create dictionary to hold parsed data
result = {}

# parse Device section
result["Device"] = {
    "Device Type": df[1][0],
    "Device Model": df[1][1],
    "Device Unique Serial Code": df[1][2],
    "Device Firmware Version": df[1][3],
    "Calibration Date": df[1][4],
    "Application name & version": df[1][5]
}

# parse Measurement section
result["Measurement"] = {
    "Measurement Frequency": df[1][8],
    "Start Time": df[1][9],
    "Last measurement": df[1][10],
    "Device Location Code": df[1][11],
    "Time Zone": df[1][12]
}

# parse Subject section
result["Subject"] = {
    "Subject Code": df[1][14],
    "Date of Birth": df[1][15],
    "Sex": df[1][16],
    "Height": df[1][17],
    "Weight": df[1][18],
    "Handedness Code": df[1][19],
    "Subject Notes": df[1][20]
}

# parse Study Center section
result["Study Center"] = {
    "Study Centre": df[1][22],
    "Study Code": df[1][23],
    "Investigator ID": df[1][24],
    "Exercise Type": df[1][25],
    "Config Operator ID": df[1][26],
    "Config Time": df[1][27],
    "Config Notes": df[1][28],
    "Extract Operator ID": df[1][29],
    "Extract Time": df[1][30],
    "Extract Notes": df[1][31]
}

# parse Sensor section
result["Sensor"] = []
for i in range(33, 81, 5):
    temp = {
        "Sensor type": df[1][i],
        "Range": df[1][i+1],
        "Resolution": df[1][i+2],
        "Units": df[1][i+3],
        "Additional information": df[1][i+4]
    }
    result["Sensor"].append(temp)

# write the result to a json file
with open('result.json', 'w') as f:
    json.dump(result, f, indent=4)
