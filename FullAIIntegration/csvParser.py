import csv
import json

# opening csv file
with open('test.csv', newline='') as csvfile:
    data = csv.reader(csvfile, delimiter=']', quotechar='[') # using custom delimiter

    # initializing empty lists to append the data
    device_data = {}
    measurement_data = {}
    subject_data = {}
    study_center_data = {}
    sensor_data = []

    # iterating over each row in data
    for row in data:
        # ignoring empty rows
        if row[0] != '':

            # parsing device data
            if row[0] == 'Device Type':
                device_data['Device Type'] = row[1].strip()
            elif row[0] == 'Device Model':
                device_data['Device Model'] = row[1].strip()
            elif row[0] == 'Device Unique Serial Code':
                device_data['Device Unique Serial Code'] = row[1].strip()
            elif row[0] == 'Device Firmware Version':
                device_data['Device Firmware Version'] = row[1].strip()
            elif row[0] == 'Calibration Date':
                device_data['Calibration Date'] = row[1].strip()
            elif row[0] == 'Application name & version ':
                device_data['Application name & version'] = row[1].strip()

            # parsing measurement data
            elif row[0] == 'Measurement Frequency':
                measurement_data['Measurement Frequency'] = row[1].strip()
            elif row[0] == 'Start Time':
                measurement_data['Start Time'] = row[1].strip()
            elif row[0] == 'Last measurement':
                measurement_data['Last measurement'] = row[1].strip()
            elif row[0] == 'Device Location Code':
                measurement_data['Device Location Code'] = row[1].strip()
            elif row[0] == 'Time Zone':
                measurement_data['Time Zone'] = row[1].strip()

            # parsing subject data
            elif row[0] == 'Subject Code':
                subject_data['Subject Code'] = row[1].strip()
            elif row[0] == 'Date of Birth':
                subject_data['Date of Birth'] = row[1].strip()
            elif row[0] == 'Sex':
                subject_data['Sex'] = row[1].strip()
            elif row[0] == 'Height':
                subject_data['Height'] = row[1].strip()
            elif row[0] == 'Weight':
                subject_data['Weight'] = row[1].strip()
            elif row[0] == 'Handedness Code':
                subject_data['Handedness Code'] = row[1].strip()
            elif row[0] == 'Subject Notes':
                subject_data['Subject Notes'] = row[1].strip()

            # parsing study center data
            elif row[0] == 'Study Centre':
                study_center_data['Study Centre'] = row[1].strip()
            elif row[0] == 'Study Code':
                study_center_data['Study Code'] = row[1].strip()
            elif row[0] == 'Investigator ID':
                study_center_data['Investigator ID'] = row[1].strip()
            elif row[0] == 'Exercise Type':
                study_center_data['Exercise Type'] = row[1].strip()
            elif row[0] == 'Config Operator ID':
                study_center_data['Config Operator ID'] = row[1].strip()
            elif row[0] == 'Config Time':
                study_center_data['Config Time'] = row[1].strip()
            elif row[0] == 'Config Notes':
                study_center_data['Config Notes'] = row[1].strip()
            elif row[0] == 'Extract Operator ID':
                study_center_data['Extract Operator ID'] = row[1].strip()
            elif row[0] == 'Extract Time':
                study_center_data['Extract Time'] = row[1].strip()
            elif row[0] == 'Extract Notes':
                study_center_data['Extract Notes'] = row[1].strip()

            # parsing sensor data
            elif row[0] == 'Sensor type':
                sensor = {}
                sensor['Sensor type'] = row[1].strip()
            elif row[0] == 'Range':
                sensor['Range'] = row[1].strip()
            elif row[0] == 'Resolution':
                sensor['Resolution'] = row[1].strip()
            elif row[0] == 'Units':
                sensor['Units'] = row[1].strip()
            elif row[0] == 'Additional information':
                sensor['Additional information'] = row[1].strip()
                if 'Sensor type' in sensor:
                    sensor_data.append(sensor)

    # creating the json object
    result = {
        'Device': device_data,
        'Measurement': measurement_data,
        'Subject': subject_data,
        'Study Center': study_center_data,
        'Sensor': sensor_data
    }

    # writing the json object to a file
    with open('result.json', 'w') as outfile:
        json.dump(result, outfile, indent=4)
