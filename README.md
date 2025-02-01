📊 FinnAI - P&L Analysis Chatbot
A Streamlit chatbot for analyzing Profit & Loss (P&L) statements from CSV files using Mistral-7B.

🚀 Getting Started
1️⃣ Clone the Repository
sh
Copy
Edit
git clone git@github.com:Galo25/FinnAI.git
cd FinnAI
2️⃣ Create a Virtual Environment & Install Dependencies
sh
Copy
Edit
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
pip install -r requirements.txt
3️⃣ Download & Set Up the Model
Mistral-7B is not included in the repo. Download it manually:

sh
Copy
Edit
mkdir -p models && cd models
wget https://huggingface.co/bartowski/Mistral-7B-Instruct-v0.3-GGUF/resolve/main/Mistral-7B-Instruct-v0.3-Q4_K_M.gguf
Ensure the model file is in the models/ directory.

▶️ Run the App
sh
Copy
Edit
streamlit run main.py
Then, open http://localhost:8501 in your browser.

📂 Project Structure
graphql
Copy
Edit
📁 FinnAI/
│── 📂 models/               # Stores the LLM (ignored in .gitignore)
│── 📂 data/                 # Sample CSV files
│── 📄 main.py               # Streamlit app
│── 📄 requirements.txt       # Dependencies
│── 📄 .gitignore             # Ignores models & venv
│── 📄 README.md              # Setup guide
❓ FAQ
Q: Model path error?
➡ Ensure the model file is inside models/ and named Mistral-7B-Instruct-v0.3-Q4_K_M.gguf.

Q: Can I use OpenAI instead?
➡ Yes! Replace LlamaCpp with:

python
Copy
Edit
llm = ChatOpenAI(model_name="gpt-4-turbo", temperature=0)
Q: Where can I contribute?
➡ Fork the repo, create a branch, make changes, and submit a Pull Request.

📬 Contact
For any issues, open a GitHub Issue or reach out to Galo25.

🚀 You're all set! Upload a CSV and start analyzing!







