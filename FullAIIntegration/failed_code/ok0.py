import csv
import json

def extract_data(file_name):
    with open(file_name, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        data = {}
        
        # read information between line 0 and 81
        for i, row in enumerate(csv_reader):
            if i > 81:
                break
            
            if not row:
                continue
            
            key = row[0]
            value = " ".join(row[1:]).strip()

            if not value:
                continue            

            # determine which section this row belongs to
            if key in device_fields:
                section = "Device"
            elif key in measurement_fields:
                section = "Measurement"
            elif key in subject_fields:
                section = "Subject"
            elif key in study_fields:
                section = "Study Center"
            else:
                section = "Sensor"
                
            # add the data to the appropriate section
            if section not in data:
                data[section] = {}
                
            data[section][key] = value
        
        return data
        
# Schema Fields
device_fields = [
    "Device Type",
    "Device Model",
    "Device Unique Serial Code",
    "Device Firmware Version",
    "Calibration Date",
    "Application name & version"
]

measurement_fields = [
    "Measurement Frequency",
    "Start Time",
    "Last measurement",
    "Device Location Code",
    "Time Zone"
]

subject_fields = [
    "Subject Code",
    "Date of Birth",
    "Sex",
    "Height",
    "Weight",
    "Handedness Code",
    "Subject Notes"
]

study_fields = [
    "Study Centre",
    "Study Code",
    "Investigator ID",
    "Exercise Type",
    "Config Operator ID",
    "Config Time",
    "Config Notes",
    "Extract Operator ID",
    "Extract Time",
    "Extract Notes"
]

if __name__ == '__main__':
    input_file = "file.csv"
    output_file = "result.json"
    result = extract_data(input_file)

    with open(output_file, "w") as f:
        json.dump(result, f, indent=4)