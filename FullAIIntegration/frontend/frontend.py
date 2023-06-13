import streamlit as st
import streamlit_ext as ste
from io import StringIO
import streamlit_scrollable_textbox as stx
import create_parser as GPTParse
import subprocess

# 6 trials sensor is wrong
# 1 wrong
# 5 trials wrong
# 2 trial good

def makeCall(line_begin="", line_end="", max_iteration=10):
    with st.container():
        with open("result.json", "w") as f:
            f.write("")

        if line_end != "" and line_begin != "":
            output_json = ""
            trial = 1
            while (output_json == ""):
                try:
                    code = GPTParse.makeRequest(int(line_begin), int(line_end),trial)
                except Exception as e:
                    st.title("Currently unable to access OpenAI model, please try again.")
                    st.text(e)
                
                print("Code generation trial {}\n".format(trial))
                exec_result = subprocess.run(["python", "csvParser{}.py".format(trial)],stderr=subprocess.PIPE).stderr.decode('utf-8')

                with open("result.json", "r") as f:
                    output_json = f.read()

                
                col3, col4 = st.columns(2)
                with open("result.json", "r") as f:
                    output_json = f.read()
                with col3:
                    st.title("Synthesized Code {}".format(trial))
                    with open("csvParser{}.py".format(trial), "rb") as file:
                        ste.download_button("Download Parser", file, "csvParser{}.py".format(trial))
                    st.code(code, line_numbers=True)
                with col4:
                    if (output_json != ""):
                        st.title("Parsed Meta Data")
                        st.json(output_json)
                    else:
                        st.title("code is unable to run with the following error")
                        st.code(exec_result)

                trial += 1
                if (trial > max_iteration):
                    break
                


st.set_page_config(layout="wide")

st.title("Metadata Parser Synthesizer")
col1, col2 = st.columns(2)

with col1:
    uploaded_file = st.file_uploader("Choose a schema file", "json")
    if uploaded_file is not None:
        # To convert to a string based IO:
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        # To read file as string:
        string_data = stringio.read()
        stx.scrollableTextbox(string_data, height=300, key=1)

        with open("schema.json","wb") as f:
            f.write(uploaded_file.getbuffer())

with col2:
    uploaded_input = st.file_uploader("Choose a data file to be parsed")
    if uploaded_input is not None:
        # To convert to a string based IO:
        stringio = StringIO(uploaded_input.getvalue().decode("utf-8"))
        # To read file as string:
        string_data = stringio.read()
        stx.scrollableTextbox(string_data, height=300, key=2)

        with open("file.csv","wb") as f:
            f.write(uploaded_input.getbuffer())

line_begin = st.text_input("Start extract data from line: ")
line_end = st.text_input("End of target data at line: ")

st.title("Hit \" Generate Parser\" to generate parser")
st.text("""The output of your parser on the file you uploaded will also be displayed. Hit \"Generate Parser\" again 
            if the output is incorrect. We will ask the model to continue generate code until something executable 
            is created or 10 parsers have created.""")
st.button("Generate Parser", type="primary", on_click=makeCall(line_begin, line_end))



