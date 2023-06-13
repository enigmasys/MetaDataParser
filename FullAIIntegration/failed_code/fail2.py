import csv, json

csv_file = "file.csv"
json_file = "result.json"

csv_rows = []
with open(csv_file) as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        csv_rows.append(row)

# Create a dictionary for the sections and extract the values
data = {
    "Device": {
        "Device Type": csv_rows[0][1],
        "Device Model": csv_rows[1][1],
        "Device Unique Serial Code": csv_rows[2][1],
        "Device Firmware Version": csv_rows[3][1],
        "Calibration Date": csv_rows[4][1],
        "Application name & version": csv_rows[5][1]
    },
    "Measurement": {
        "Measurement Frequency": csv_rows[7][1],
        "Start Time": csv_rows[8][1],
        "Last measurement": csv_rows[9][1],
        "Device Location Code": csv_rows[10][1],
        "Time Zone": csv_rows[11][1]
    },
    "Subject": {
        "Subject Code": csv_rows[13][1],
        "Date of Birth": csv_rows[14][1],
        "Sex": csv_rows[15][1],
        "Height": csv_rows[16][1],
        "Weight": csv_rows[17][1],
        "Handedness Code": csv_rows[18][1],
        "Subject Notes": csv_rows[19][1]
    },
    "Study Center": {
        "Study Centre": csv_rows[21][1],
        "Study Code": csv_rows[22][1],
        "Investigator ID": csv_rows[23][1],
        "Exercise Type": csv_rows[24][1],
        "Config Operator ID": csv_rows[25][1],
        "Config Time": csv_rows[26][1],
        "Config Notes": csv_rows[27][1],
        "Extract Operator ID": csv_rows[28][1],
        "Extract Time": csv_rows[29][1],
        "Extract Notes": csv_rows[30][1]
    },
    "Sensor": [
        {
            "Sensor type": csv_rows[32][0],
            "Range": csv_rows[33][0],
            "Resolution": csv_rows[34][0],
            "Units": csv_rows[35][0],
            "Additional information": csv_rows[36][0]
        },
        {
            "Sensor type": csv_rows[38][0],
            "Range": csv_rows[39][0],
            "Resolution": csv_rows[40][0],
            "Units": csv_rows[41][0],
            "Additional information": csv_rows[42][0]
        },
        {
            "Sensor type": csv_rows[44][0],
            "Range": csv_rows[45][0],
            "Resolution": csv_rows[46][0],
            "Units": csv_rows[47][0],
            "Additional information": csv_rows[48][0]
        },
        {
            "Sensor type": csv_rows[50][0],
            "Range": csv_rows[51][0],
            "Resolution": csv_rows[52][0],
            "Units": csv_rows[53][0],
            "Additional information": csv_rows[54][0]
        },
        {
            "Sensor type": csv_rows[56][0],
            "Range": csv_rows[57][0],
            "Resolution": csv_rows[58][0],
            "Units": csv_rows[59][0],
            "Additional information": csv_rows[60][0]
        }
    ]
}

# Dump data into json file
with open(json_file, 'w') as jsonfile:
    json.dump(data, jsonfile, indent=4)
