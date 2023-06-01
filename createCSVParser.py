import os
import openai
import csv 
import json

def make_parser(prompt, schema):
    openai_error = True
    while openai_error:
        try:
            print("instruction given\n")
            print(prompt)
            print("\nGenerating Praser...")
            result = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=prompt
            )
            openai_error = False
        except:
            print("openai error received. Trying again...\n")
    code = result['choices'][0]['message']['content']
    print(code)

    f = open("csvParser.py", "w+")
    f.write(code)
    f.close
    with open("csvParser.py", "r") as f:
        lines = f.readlines()

    codeFound = False
    with open("csvParser.py", "w") as f:
        for line in lines:
            if line.strip("\n").strip("python").strip(" ") == "```" and codeFound == False:
                codeFound = True
                continue
            if line.strip("\n") == "```":
                break
            if codeFound:
                f.write(line)

# code returned maybe pure code no ''' '''


# none unique names -> better mapping generation
def parse(src_file, output_file, begin, end, schema, mapping=None):
    dict = {}
    with open(src_file, newline='') as csvfile:
        reader = csv.reader(csvfile)
        i = begin
        for row in reader:
            if len(row) == 0:
                i += 1
                continue
            if i <= end:
                key = row[0].strip()
                value = row[1].strip()
                dict.update({key: value})
                i += 1
            else:
                break
    print(dict)
    f = open("dict_output.json", "w+")
    json.dump(dict, f)
    f.close

    if mapping == None:
        with open(schema, 'r') as schema:
            template = json.load(schema)
            mapping = template.copy()
            for category in template.keys():
                for field in template[category].keys():
                    mapping[category][field] = input("The field in category [{}] named [{}] should be mapped to what name?\n".format(category, field))

            # save mapping locally
            with open("{}_map.json".format(src_file.split('.')[0]), 'w') as outfile:
                json.dump(mapping, outfile)

        for category in template.keys():
            for field in template[category].keys():
                template[category][field] = dict[mapping[category][field]]
        
    else:
        with open(schema, 'r') as schema:
            template = json.load(schema)
            with open(mapping, 'r') as mapping:
                mapping = json.load(mapping)
                for category in template.keys():
                    for field in template[category].keys():
                        template[category][field] = dict[mapping[category][field]]

    with open(output_file, 'w') as outfile:
        json.dump(template, outfile)

    return template


# instruct user to specify the range of lines that needs to be parsed
begin_line = int(input("what line does desired data begin at (only enter a number): \n"))
end_line = int(input("what line does desired data end at (only enter a number): \n"))

openai.api_key = os.getenv("OPENAI_API_KEY")

prompt = [
            {"role": "system", "content": "You are a helpful coding assistant who only outputs code needed and nothing else"},
            {"role": "user", "content": """write a executable python code that only parse the content between line {} and line {} of
            a csv file into an array of json objects. Treat each line as a key value pair separated by a comma and lines that are
            separated by multiple empty lines as one json object. Ignore any empty line.
            Then, remove any empty json object in the result.
            The input file path is 'file.csv' and the output file is 'output.json' Respond with no explanation.""".format(begin_line, end_line)}
        ]

# make_parser(prompt, None)
# parse("file.csv", "my_output.json", begin_line, end_line, "schema.json", "file_map.json")