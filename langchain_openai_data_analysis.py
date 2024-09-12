import streamlit as st
import pandas as pd
import io
from langchain.chat_models import ChatOpenAI
from langchain.agents import AgentType, initialize_agent
from langchain.callbacks import StreamlitCallbackHandler
from langchain.tools import Tool

# Set up OpenAI API key
if 'OPENAI_API_KEY' not in st.secrets:
    st.error("OPENAI_API_KEY is not set in the Streamlit secrets. Please set it up as described in the README.")
    st.stop()

# Initialize OpenAI Chat model
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0, openai_api_key=st.secrets["OPENAI_API_KEY"])

st.title("LangChain Data Analysis Assistant")

# File uploader
uploaded_file = st.file_uploader("Choose a CSV or Excel file", type=["csv", "xlsx"])

if uploaded_file is not None:
    # Read the file
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.write("Data Preview:")
    st.dataframe(df.head())

    # Data info
    st.write("Data Info:")
    buffer = io.StringIO()
    df.info(buf=buffer)
    s = buffer.getvalue()
    st.text(s)

    # Create a custom tool for executing Python code
    class PythonREPLTool(Tool):
        def __init__(self, locals):
            self.name = "python_repl"
            self.description = "Executes Python code"
            self.locals = locals

        def _run(self, code):
            exec(code, globals(), self.locals)
            return self.locals.get("result", "No result returned")

    python_repl = PythonREPLTool(locals={"df": df, "pd": pd})

    # Initialize agent
    agent = initialize_agent(
        [python_repl],
        llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )

    # User input for analysis
    user_input = st.text_area("Ask a question about the data:", height=100)

    if st.button("Analyze"):
        if user_input:
            with st.spinner('Analyzing...'):
                st_callback = StreamlitCallbackHandler(st.container())
                # Prepare the DataFrame and the question for the agent
                setup_code = f"""
import pandas as pd
df = pd.DataFrame({df.to_dict()})
result = None
"""
                question = f"{setup_code}\n\n# Now, answer this question about the DataFrame:\n{user_input}\nresult = answer"
                response = agent.run(question, callbacks=[st_callback])
                st.write("Analysis Result:")
                st.write(response)
        else:
            st.warning("Please enter a question about the data.")

# Chat interface
st.sidebar.header("General Chat")
chat_input = st.sidebar.text_input("Ask a general question:")

if st.sidebar.button("Send"):
    if chat_input:
        with st.sidebar.spinner('Thinking...'):
            response = llm.predict(chat_input)
            st.sidebar.write("LLM Response:")
            st.sidebar.write(response)
    else:
        st.sidebar.warning("Please enter a question.")
