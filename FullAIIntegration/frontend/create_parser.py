import os
import openai

def make_parser(prompt, trial):
    print("instruction given\n")
    print(prompt)
    print("\nGenerating Parser...")
    result = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=prompt
    )

    code = result['choices'][0]['message']['content']
    print(code)

    f = open("csvParser{}.py".format(trial), "w+")
    f.write(code)
    f.close
    with open("csvParser{}.py".format(trial), "r") as f:
        lines = f.readlines()

    codeFound = False
    with open("csvParser{}.py".format(trial), "w") as f:
        for line in lines:
            if line.strip("\n").strip("python").strip(" ") == "```" and codeFound == False:
                codeFound = True
                continue
            if line.strip("\n") == "```":
                break
            if codeFound:
                f.write(line)

    with open("csvParser{}.py".format(trial), "r") as f:
        code = f.read()

    return code


def makeRequest(line_begin, line_end, trial):
    openai.api_key = os.getenv("OPENAI_API_KEY")

    begin_line = line_begin
    end_line = line_end

    input_file = "file.csv"
    output_file = "result.json"

    file_type = input_file.split('.')[1]

    schema_lines = ""
    with open("schema.json","r") as f:
        schema_lines = f.read()

    answer_lines = ""
    with open("my_output.json", "r") as f:
        answer_lines = f.read()

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
                                and check if the output matches the json schema requirement. 
                                The code should ignore empty lines. Send me 
                                all of the code when it is executable with the given file, and the 
                                output are the same as the following json object (deliminated by triple asterisks)
                                *{}*
                                """.format(input_file,input_file,begin_line,end_line, output_file,file_lines, schema_lines, answer_lines)}
            ]


    return make_parser(prompt, trial)