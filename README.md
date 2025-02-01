📊 FinnAI - P&L Analysis Chatbot

FinnAI is an AI-powered chatbot that allows users to analyze Profit & Loss (P&L) statements directly from CSV files.
It utilizes LangChain, OpenAI's GPT-4, and Streamlit to provide financial insights and data visualizations.

🚀 Features

📁 Upload CSV files and extract key financial insights.

🔍 Ask questions about revenue, profits, expenses, EBITDA, and more.

📊 Generate graphs dynamically when asked to visualize financial trends.

🤖 Uses LangChain Agents for enhanced understanding of financial data.

🔧 Setup & Installation

1️⃣ Clone the Repository

# Using SSH
git clone git@github.com:Galo25/FinnAI.git
cd FinnAI/vdragent

2️⃣ Create a Virtual Environment

# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate

3️⃣ Install Dependencies

pip install -r requirements.txt

4️⃣ Set Up Environment Variables

Create a .env file in the project root and add your OpenAI API key:

OPENAI_API_KEY=your_openai_api_key_here

▶️ Run the Application

Start the chatbot using Streamlit:

streamlit run main.py

The app will run on http://localhost:8501

📌 How to Use FinnAI

1️⃣ Upload a CSV file containing financial data (Profit & Loss statement).
2️⃣ Ask questions like:

"What is the total revenue for 2021?"

"Plot the EBITDA trends over the last 3 years."

"What are the total expenses for Q3 2020?"
3️⃣ FinnAI analyzes the data and provides accurate financial insights.
4️⃣ If a graph is requested, it will be generated and displayed inside Streamlit.

🛠 Technologies Used

Python 🐍

LangChain (Agent-based AI execution)

OpenAI GPT-4 (LLM for financial analysis)

Streamlit (User Interface)

Matplotlib (Graphing)

🤝 Contributing

Pull requests are welcome! If you'd like to improve the project, follow these steps:

git checkout -b feature-branch
git commit -m "Added a new feature"
git push origin feature-branch

Then, create a Pull Request on GitHub.

📝 License

This project is licensed under the MIT License.

⭐ Support the Project

If you find FinnAI useful, consider giving this repo a ⭐ on GitHub!

🔗 GitHub Repository: https://github.com/Galo25/FinnAI

