import json

with open('file.csv', 'r') as f:
    lines = f.readlines()

data = []
current_obj = {}
for line in lines[:81]:
    if line == '\n':
        if current_obj != {}:
            data.append(current_obj)
            current_obj = {}
    else:
        key, value = line.strip().split(',')
        current_obj[key] = value

if current_obj != {}:
    data.append(current_obj)

result = [obj for obj in data if obj != {}]

with open('output.json', 'w') as f:
    json.dump(result, f)
