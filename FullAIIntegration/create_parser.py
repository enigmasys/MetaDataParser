import os
import openai

def make_parser(prompt):
    print("instruction given\n")
    print(prompt)
    print("\nGenerating Parser...")
    result = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=prompt
    )

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


openai.api_key = os.getenv("OPENAI_API_KEY")

begin_line = int(input("what line does desired data begin at (only enter a number): \n"))
end_line = int(input("what line does desired data end at (only enter a number): \n"))

input_file = "file.csv"
output_file = "result.json"

file_type = input_file.split('.')[1]

schema_lines = ""
with open("schema.json","r") as f:
    schema_lines = f.read()

expected_output = ""
with open("my_output.json") as f:
    expected_output = f.read()

file_lines = ""
with open("file.csv", "r") as f:
    lines = f.readlines()
    i = 0
    for line in lines:
        if i < begin_line:
            i += 1
            continue
        if i > end_line:
            break

        file_lines += line
        i += 1

prompt = [
            {"role":"system", 
             "content":"""When I ask you for help to write code, you will reply with 
                            an expert-level executable code with detailed comments 
                            and no explanations outside the code."""},
            {"role": "user", 
             "content":"""You will be provided with a {} file (deliminated by square brackets)
                            and a json schema (deliminated by XML tags) that describes a json object. 
                            Based on the example file and json schema, you will write a code using
                            python and packages native to python to extract information from the
                            {} file between line {} and line {} into a json object according to the 
                            json schema. The code will output the result to 
                            file {}.\n Here is the example file [{}]. \nHere is the json schema
                            <JsonSchema>{}</JsonSchema> You are free to run the code on your own, 
                            and check if the output matches the json schema requirement. Send me the
                            code when it is executable with the given file.
                            The code should ignore empty lines.
                            """.format(input_file,input_file,begin_line,end_line, output_file,file_lines, schema_lines)}
        ]


make_parser(prompt)

# error example
# Great, I will begin writing the parser. There are various python libraries I can use for parsing CSV and JSON files. Which do you prefer that I use?
# Ask for description of file
# code does not run because there are empty lines
# Thanks for the schema, I will now write a parser function that reads the csv file and creates the json object according to the schema. Please provide me with the file content.Thanks for the schema, I will now write a parser function that reads the csv file and creates the json object according to the schema. Please provide me with the file content.
# Use uninstalled packages
# open does not respond
# ask for a name of the python file
# mix up category content


# front end
# stream lit
# jupyter note book
# validation of the parser on the same web app. 
# send additional prompt for tweaking parser
# add code to the git organization

# datalake open source application
# delta lake, minio, lakeFS
# versioning for files
# criteria
    # secure, authentication needed, specific access for people
    # meta data and various kinds of raw data needs to be stored 
    # versioning and dependency tracking
    # restAPI needed

# prompt 1
# {"role": "system", "content": "You are a helpful coding assistant who only outputs code needed and nothing else"},
# {"role": "user", "content": """Can you write an executable parser for me in python that extract the meta data in a {} file into a json object? 
# I will give you an example input file and a schema. The output json file should meet the requirement of the schema.
# The input csv file name is {}. The output needs to be stored in file {}. The parser should only
# parse information between line {} and {}. Use library available in native python.
# Specifically, the parser should create a json object first based on the schema. Then, the parser should fill in each field with corresponding information from the input file. 
# When indexing into a datasturcture, make sure the index is valid before indexing.
# Parser should ignore empty lines, and not crash on empty field.
# Let me know when you are ready for the file first.""".format('.'+input_file.split('.')[1], input_file, output_file, begin_line, end_line)},
# {"role": "assistant", "content":"Good, I am ready to write a parser in python for the file and take the file"},
# {"role":"user", "content":file_lines},
# {"role": "assistant", "content":"Cool, I have read the file content. Can you send me the schema for the json object you wish to create?"},
# {"role": "user", "content":schema_lines},
# # {"role" : "assistant", "content":"I have the schema now, can I see want do you expect the json object to look at?"},
# # {"role": "user", "content":expected_output},
# {"role" : "assistant", "content":"I have everything now, should I give you the parser now?"},
# {"role":"user", "content":"Yes, for the next response just send the executable code with no explanation"}

# prompt 2
# {"role":"system", 
#  "content":"""When I ask you for help to write code, you will reply with 
#                 an expert-level executable code with detailed comments 
#                 and no explanations outside the code."""}
# {"role": "user", 
#  "content":"""You will be provided with an example {} file (deliminated by square brackets)
#                 and a json schema (deliminated by XML tags) that describes a json object 
#                 that contains the meta data of the previous file you received. 
#                 Based on the example file and json schema, you will write a code using
#                 python and packages native to python to extract information from a
#                 file named {} between line {} and line {} into the format specified by the 
#                 provided json schema, and the code will output the result to 
#                 file {}. Here is the exmaple file [{}]. Here is the json schema
#                 <JsonSchema>{}</JsonSchema>""".format(input_file.split('.')[1],input_file, 
#                 begin_line, end_line, output_file, input_file.split('.')[1], file_lines, schema_lines)}

