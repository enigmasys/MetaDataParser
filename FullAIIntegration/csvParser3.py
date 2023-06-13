import csv
import json

# Open CSV file and read contents
with open('file.csv', 'r') as file:
    data = file.readlines()

# Parse relevant information from the CSV file
device = {}
measurement = {}
subject = {}
study_center = {}
sensors = []

section = None
for line in data:
    # Ignore empty lines
    if line.strip() == '':
        continue

    # Determine section based on the first value of the CSV line
    if line.startswith('Device'):
        section = 'Device'
    elif line.startswith('Measurement'):
        section = 'Measurement'
    elif line.startswith('Subject'):
        section = 'Subject'
    elif line.startswith('Study Centre'):
        section = 'Study Center'
    elif line.startswith('Sensor type'):
        section = 'Sensor'
    
    # Parse values based on the section of the CSV file
    if section == 'Device':
        key, value = line.strip().split(',')
        device[key] = value
    elif section == 'Measurement':
        key, value = line.strip().split(',')
        measurement[key] = value
    elif section == 'Subject':
        key, value = line.strip().split(',')
        subject[key] = value
    elif section == 'Study Center':
        key, value = line.strip().split(',')
        study_center[key] = value
    elif section == 'Sensor':
        sensor = {}
        for key_value in line.strip().split(','):
            key, value = key_value.split(':')
            sensor[key.strip()] = value.strip()
        sensors.append(sensor)

# Construct JSON object based on the extracted data and JSON schema
result = {}
result['Device'] = {
    'Device Type': device['Device Type'],
    'Device Model': device['Device Model'],
    'Device Unique Serial Code': device['Device Unique Serial Code'],
    'Device Firmware Version': device['Device Firmware Version'],
    'Calibration Date': device['Calibration Date'],
    'Application name & version': device['Application name & version']
}

result['Measurement'] = {
    'Measurement Frequency': measurement['Measurement Frequency'],
    'Start Time': measurement['Start Time'],
    'Last measurement': measurement['Last measurement'],
    'Device Location Code': measurement['Device Location Code'],
    'Time Zone': measurement['Time Zone']
}

result['Subject'] = {
    'Subject Code': subject['Subject Code'],
    'Date of Birth': subject['Date of Birth'],
    'Sex': subject['Sex'],
    'Height': subject['Height'],
    'Weight': subject['Weight'],
    'Handedness Code': subject['Handedness Code'],
    'Subject Notes': subject['Subject Notes']
}

result['Study Center'] = {
    'Study Centre': study_center['Study Centre'],
    'Study Code': study_center['Study Code'],
    'Investigator ID': study_center['Investigator ID'],
    'Exercise Type': study_center['Exercise Type'],
    'Config Operator ID': study_center['Config Operator ID'],
    'Config Time': study_center['Config Time'],
    'Config Notes': study_center['Config Notes'],
    'Extract Operator ID': study_center['Extract Operator ID'],
    'Extract Time': study_center['Extract Time'],
    'Extract Notes': study_center['Extract Notes']
}

result['Sensor'] = []
for sensor in sensors:
    result['Sensor'].append({
        'Sensor type': sensor['Sensor type'],
        'Range': sensor['Range'],
        'Resolution': sensor['Resolution'],
        'Units': sensor['Units'],
        'Additional information': sensor['Additional information']
    })

# Write JSON object to file
with open('result.json', 'w') as file:
    json.dump(result, file, indent=4)
