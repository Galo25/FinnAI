import os
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from dotenv import load_dotenv
from langchain.agents.agent_types import AgentType
from langchain_experimental.agents import create_csv_agent
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI, OpenAI


def main():
    load_dotenv()

    # Ensure OpenAI API key is set
    openai_api_key = os.getenv("OPENAI_API_KEY")
    if not openai_api_key:
        st.error("⚠️ OPENAI_API_KEY is not set. Please check your .env file.")
        return

    # Streamlit UI
    st.set_page_config(page_title="P&L Analysis Chatbot")
    st.header("📊 P&L Analysis Chatbot - Ask Your CSV")

    # File Upload
    csv_file = st.file_uploader("📁 Upload a CSV file for analysis", type="csv")
    
    if csv_file is not None:
        # Save uploaded CSV to a temporary file
        temp_csv_path = "temp_uploaded_file.csv"
        with open(temp_csv_path, "wb") as f:
            f.write(csv_file.getbuffer())

        # Read the CSV for visualization
        df = pd.read_csv(temp_csv_path)

        # Display the first few rows
        #st.subheader("📋 Preview of Uploaded Data")
        #st.write(df.head())

        # Custom P&L Prompt
        pnl_prompt = PromptTemplate(
            input_variables=["question"],
            template="""
                You are a financial analyst specializing in Profit & Loss (P&L) statements. 
                Your task is to analyze the uploaded CSV file and provide structured, finance-related insights.

                **Guidelines:**
                - Ensure your responses are **based on the CSV data**.
                - Identify whether financial figures are represented in **millions, thousands, or absolute values**:
                - Look for **headers or column descriptions** that indicate scale (e.g., "Revenue (in millions)", "EBITDA (thousands)").
                - If no scale is explicitly mentioned, check if values are **abnormally low or high** to infer the likely scale.
                - Recognize **negative values wrapped in parentheses (`( )`)** as negative numbers.
                - Focus on the following **key financial metrics**:
                - **Total Net Revenue**
                - **Gross Profit**
                - **Expenses (Total Operating Expenses, SG&A, COGS)**
                - **Net Income**
                - **Earnings Before Interest & Taxes (EBIT)**
                - **Earnings Before Interest, Taxes, Depreciation & Amortization (EBITDA)**

                **Financial Calculation Considerations:**
                - **Gross Profit = Total Revenue - Cost of Goods Sold (COGS)**
                - **EBIT = Net Income + Interest + Taxes**
                - **EBITDA = EBIT + Depreciation + Amortization**
                - If any of these values are missing, suggest what data is needed to calculate them.

                **Graph Instructions:**
                - If the question contains keywords like **"plot", "graph", "chart", or "visualize"**, generate Python code to create a Matplotlib chart.
                - The Python code should:
                - Extract the relevant data from the CSV.
                - Create a `fig` object using `plt.subplots()`.
                - Use `st.pyplot(fig)` to display the graph in Streamlit.

                **Now, analyze the CSV and plot if needed to answer the following question:**  
                {question}
                """
        )

        # Initialize OpenAI LLM
        llm = ChatOpenAI(
            model_name="gpt-4-turbo",
            temperature=0
        )

        # Create the CSV Agent
        agent = create_csv_agent(
            llm,
            temp_csv_path,  
            verbose=True,
            agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
            allow_dangerous_code=True
        )

        # User Query Input
        user_question = st.text_input("💬 Ask a financial question about your CSV:")

        if user_question:
            with st.spinner(text="🔎 Analyzing CSV data..."):
                response = agent.invoke({"input": user_question})
                
                # Handle Possible Matplotlib Code Output
                if "plt." in response["output"] or "matplotlib.pyplot" in response["output"]:
                    exec_globals = {}
                    try:
                        print("this is display mode------")
                        exec(response["output"], exec_globals)
                        if "fig" in exec_globals:
                            st.pyplot(exec_globals["fig"])
                    except Exception as e:
                        st.error(f"Error executing graph: {e}")
                else:
                    st.write("📌 **Answer:**", response["output"])

if __name__ == "__main__":
    main()