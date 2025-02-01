📊 FinnAI - P&L Analysis Chatbot
A Streamlit-based chatbot that analyzes Profit & Loss (P&L) CSV files using an AI-powered financial agent.

🚀 Overview
FinnAI is a finance-focused chatbot that lets you upload a CSV file containing Profit & Loss (P&L) data and ask questions about financial metrics, trends, and calculations.

It uses:

Mistral-7B (Local LLM) for offline AI responses
LangChain CSV Agents to interact with financial data
Matplotlib & Seaborn for data visualization
🛠️ Setup & Installation
1️⃣ Clone the Repository
sh
Copy
Edit
git clone git@github.com:Galo25/FinnAI.git
cd FinnAI
2️⃣ Create a Virtual Environment
sh
Copy
Edit
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
3️⃣ Install Dependencies
sh
Copy
Edit
pip install -r requirements.txt
4️⃣ Set Up Your Model
Since Mistral-7B is too large for Git, download it manually and place it inside the models/ folder.

sh
Copy
Edit
mkdir -p models && cd models
wget https://huggingface.co/bartowski/Mistral-7B-Instruct-v0.3-GGUF/resolve/main/Mistral-7B-Instruct-v0.3-Q4_K_M.gguf
📂 File Structure
graphql
Copy
Edit
📁 FinnAI/
│── 📂 models/               # Stores the LLM (ignored in .gitignore)
│── 📂 venv/                 # Virtual environment (ignored in .gitignore)
│── 📂 data/                 # Sample CSV files
│── 📄 main.py               # Streamlit app entry point
│── 📄 requirements.txt       # Python dependencies
│── 📄 .gitignore             # Excludes unnecessary files
│── 📄 README.md              # Project documentation
▶️ How to Run
Once everything is set up, launch the Streamlit app:

sh
Copy
Edit
streamlit run main.py
This will start a local server. Open http://localhost:8501 in your browser to interact with the chatbot.

📊 Features
✅ Upload CSV files for P&L analysis
✅ Ask financial questions like revenue trends, EBITDA, etc.
✅ Detect number formats (millions/thousands)
✅ Understand negative values in ( ) brackets
✅ Generate financial plots & charts dynamically

🔍 Example Questions
"What was the total net revenue for 2019?"
"Plot the year-over-year (YOY) growth of total revenue."
"Calculate EBITDA for 2020."
"What were the biggest expenses in 2021?"
🤝 Contributing
Want to improve FinnAI? Fork & contribute!

Create a new branch
sh
Copy
Edit
git checkout -b feature-new-improvement
Commit your changes
sh
Copy
Edit
git add .
git commit -m "Added a new feature"
Push & create a PR
sh
Copy
Edit
git push origin feature-new-improvement
🛑 .gitignore
We've added the following to .gitignore:

markdown
Copy
Edit
models/
*.gguf
venv/
__pycache__/
This prevents tracking large models and temporary files.

⚡ Troubleshooting
Q: Model path error?
➡ Ensure the model is inside models/ and referenced correctly in main.py.

Q: Slow performance?
➡ Try lowering the context window (n_ctx=1024) in main.py:

python
Copy
Edit
llm = LlamaCpp(
    model_path="./models/Mistral-7B-Instruct-v0.3-Q4_K_M.gguf",
    n_ctx=1024,
    temperature=0.2
)
Q: Can I use OpenAI instead?
➡ Yes! Replace LlamaCpp with:

python
Copy
Edit
llm = ChatOpenAI(model_name="gpt-4-turbo", temperature=0)
🌍 License
This project is open-source under the MIT License. Feel free to use & modify!

📬 Contact
For any issues or questions, open a GitHub Issue or reach out to Galo25. 🚀

✅ Now, you're ready to run FinnAI! 🎯