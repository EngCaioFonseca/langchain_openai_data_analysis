# LangChain Data Analysis Assistant

## Overview

This Streamlit-based web application uses LangChain and OpenAI's GPT-3.5-turbo to analyze CSV and Excel datasets. It provides intelligent data analysis and general question answering capabilities.

## Features

- Upload and preview CSV or Excel files
- Display basic dataset information
- LLM-powered data analysis based on user questions
- General chat interface for broader queries
- Utilizes LangChain's Pandas DataFrame Agent for data analysis

## Requirements

- Python 3.7+
- Streamlit
- Pandas
- Openpyxl
- LangChain
- OpenAI

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/langchain-data-analysis-assistant.git
   cd langchain-data-analysis-assistant
   ```

2. Install the required packages:
   ```
   pip install streamlit pandas openpyxl langchain openai
   ```

3. Set up your OpenAI API key in Streamlit secrets.

## Usage

1. Run the Streamlit app:
   ```
   streamlit run app.py
   ```

2. Open your web browser and go to `http://localhost:8501`

3. Use the file uploader to select a CSV or Excel file for analysis

4. Ask questions about the data in the text area provided

5. Use the sidebar to ask general questions to the LLM

## How it Works

1. The application uses OpenAI's GPT-3.5-turbo model through the LangChain library
2. Users can upload CSV or Excel files, which are then parsed using Pandas
3. Basic information about the dataset is displayed
4. LangChain's Pandas DataFrame Agent is used to analyze the data and answer questions
5. Users can ask questions about the data, which are then processed by the agent
6. A general chat interface is provided in the sidebar for broader queries

## Customization

- You can adjust the OpenAI model parameters in the `OpenAI()` function call
- To use GPT-4, change `llm = OpenAI(temperature=0)` to `llm = OpenAI(model_name="gpt-4", temperature=0)`

## Limitations

- Requires an OpenAI API key and incurs usage costs
- Analysis quality depends on the capabilities of the OpenAI model used
- The Pandas DataFrame Agent may struggle with very large datasets

## Contributing

Contributions to improve the LangChain Data Analysis Assistant are welcome. Please follow these steps:
1. Fork the repository
2. Create a new branch for your feature
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License

This project is open-source and available under the MIT License.

## Acknowledgments

- Streamlit for the web app framework
- LangChain for the integration with OpenAI and the Pandas DataFrame Agent
- OpenAI for the GPT models
