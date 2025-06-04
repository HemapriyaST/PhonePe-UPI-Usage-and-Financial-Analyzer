# PhonePe-UPI-Usage-and-Financial-Analyzer
**💸 Personal UPI Usage and Financial Analyzer using LLMs**

**📊 Track, Analyze & Optimize Your UPI Transactions with AI**

🔗 Live Demo
🎥 Video Walkthrough: Watch on YouTube
🌐 Try it Live: PhonePe UPI Usage and Financial Analyzer

🔍 Overview
This project is an AI-powered personal finance assistant that extracts and analyzes UPI transaction statements (PDFs) from platforms like Paytm, GPay, and PhonePe. Leveraging Large Language Models (LLMs) and NLP techniques, it provides personalized financial insights, budget recommendations, and savings suggestions—all from your real UPI data.

🚀 Features
✅ Extract transaction data from PDF statements
✅ Categorize spendings automatically using merchant data
✅ Generate intelligent financial summaries using LLaMA3
✅ Export structured CSV data
✅ Responsive UI built with Gradio
✅ Deployed on Hugging Face Spaces

🧠 Powered By
LLMs (LLaMA3 via Groq API)

PyMuPDF for PDF parsing

Pandas for data processing

Gradio for interactive frontend

Groq API for lightning-fast inference

🖼️ Demo UI
<!-- Replace with actual screenshot URL -->

🏗️ Project Architecture
mermaid
Copy
Edit
graph LR
A[User Uploads UPI PDF] --> B[PDF Text Extraction (PyMuPDF)]
B --> C[Transaction Structuring (Regex + Pandas)]
C --> D[Categorization Engine (Merchant Mapping)]
D --> E[LLM Analysis with Prompt Engineering]
E --> F[Gradio UI Output: Insights + CSV]
🧾 Sample Insight Output
markdown
Copy
Edit
**Financial Insights for John Doe**

- **Monthly Income**: ₹25,000
- **Expenses**: ₹18,500
- **Top Spending Category**: Food Delivery (₹5,200)
- **Savings Rate**: 26%
- **Recommendation**: Reduce ordering from Swiggy/Zomato by 30%.
📂 Folder Structure
bash
Copy
Edit
📁 final_project/
├── final_project_code.py      # Main logic + Gradio app
├── README.md                  # You're here!
├── requirements.txt           # Dependencies
💡 How to Run Locally
bash
Copy
Edit
# Step 1: Clone the repo
git clone https://github.com/your-username/upi-finance-analyzer.git
cd upi-finance-analyzer

# Step 2: Install dependencies
pip install -r requirements.txt

# Step 3: Add your Groq API Key
# In final_project_code.py, replace:
groq_api_key = "Your_Groq_API_KEY"

# Step 4: Run the app
python final_project_code.py
🌐 Deployment
✅ Hosted live on Hugging Face Spaces:
👉 PhonePe UPI Usage and Financial Analyzer

📦 Requirements
txt
Copy
Edit
pymupdf
gradio
openai
groq
pandas

🔬 Evaluation Metrics
✅ PDF parsing accuracy

✅ Categorization correctness

✅ LLM recommendation quality

✅ Insight generation speed

✅ User satisfaction

📈 Skills Demonstrated
✅ PDF Data Extraction

✅ LLM Prompt Engineering

✅ Data Structuring with Pandas

✅ Gradio UI Development

✅ FinTech & Budgeting Insight Generation

✅ Hugging Face Spaces Deployment
