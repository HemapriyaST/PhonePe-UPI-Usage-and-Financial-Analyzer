# 💸 PhonePe-UPI-Usage-and-Financial-Analyzer

📊 **Track, Analyze & Optimize Your UPI Transactions with AI**


## 🧠 Problem Statement

> **Goal:** Build an AI-driven application that parses UPI PDF statements and delivers meaningful financial advice.

## 🔍 Overview

Are you struggling to make sense of your UPI transactions on **PhonePe**?

This AI-powered analyzer helps you:
- 🧾 Extract transaction data from messy PDF statements
- 📊 Detect your spending patterns
- 💡 Get personalized financial insights & cost-saving tips
- 🚀 All powered by **Large Language Models (LLMs)**, beautifully deployed with **Gradio** on Hugging Face Spaces.

---

## 🖼️ App Interface Preview

![image](https://github.com/user-attachments/assets/d17925f9-6c4c-4d2f-9f4b-8e4f3f581dbd)

-----

### 🧩 Key Capabilities:
- Combine statements from Paytm, GPay, PhonePe
- Detect frequent merchants & wasteful expenses
- Recommend personalized budgeting & saving strategies
- Provide visual dashboards and detailed financial reports

---

## 🛠️ Features

| Feature | Description |
|--------|-------------|
| 📂 PDF Upload | Upload your UPI PDF statements (PhonePe supported) |
| 📋 Transaction Table | View structured and categorized transactions |
| 📈 AI Insights | Receive personalized reports using LLaMA3 |
| 📤 CSV Export | Download your transaction data |
| ⚡ Fast & Easy | Deployed on Hugging Face, accessible instantly |

---

## ✅ Evaluation Metrics

Metric	Description

📄 PDF Extraction Accuracy	Measures how well the system extracts text from various UPI PhonePe PDF formats (iphone vs android)

📊 Transaction Structuring Completeness	Checks the integrity and completeness of fields like Date, Amount, Receiver, Time, Category

💡 LLM Insight Relevance	Evaluates the usefulness and accuracy of AI-generated financial advice (via human feedback)

⏱️ Response Time	Measures how quickly the system generates insights and previews after uploading

👍 User Satisfaction	Assessed via qualitative feedback and usability of insights provided

🧠 Category Detection Accuracy	Accuracy of categorizing merchants (e.g., Food, Retail, Transport) from transaction descriptions

🔄 Repeatability	Whether similar inputs produce stable and reproducible outputs


----
## 🧪 Technologies Used

- 🐍 Python, Pandas
- 📄 PyMuPDF for PDF parsing
- 🤗 Hugging Face Transformers & Spaces
- 🧠 Groq + LLaMA3 for financial insights
- 🌐 Gradio UI for deployment

---

## 📽️ Demo

📺 **Watch the demo video** here: [Video Demo](PhonePe-UPI-Usage-and-Financial-Analyzer/video_demo.mp4)  
🌐 **Try it live on Hugging Face**: [PhonePe-UPI-Usage-and-Financial-Analyzer](https://huggingface.co/spaces/Hemaperumal/PhonePe-UPI-Usage-and-Financial-Analyzer)

---

## 🚀 How It Works

1. **Upload** your PhonePe PDF statement
2. Click **👁️ Transactions** to view your extracted and categorized spending
3. Click **🔍 Analyze with AI** to receive personalized financial suggestions
4. Export your structured data as a **CSV** for future use

---

## 📊 Sample Output

- Monthly income/expense summary
- Top categories by spending
- Late-night or frequent transactions
- Budget & saving suggestions
- Suspicious or one-time expenses
- Recurring subscriptions breakdown
- Overall Financial Health Score (out of 100)

---

## 📁 Project Structure
bash
Copy
Edit
📦 PhonePe-UPI-Usage-and-Financial-Analyzer
│
├── final_project_code.py        # Main application logic
├── README.md                    # Project overview
├── assets/app_screenshot.png    # Screenshot of the UI
├── demo_video.mp4               # (Optional) Demo walkthrough

---------

## 📈 Project Impact
✅ Improves personal financial awareness
✅ Saves users from overspending
✅ Converts raw UPI data into smart suggestions
✅ Makes financial analysis easy for everyone

------

##  📢 Feedback & Contributions
We welcome your feedback, feature suggestions, and contributions to make this tool even better. Whether it’s improving the categorization logic, enhancing the LLM prompts, or adding new dashboard features—every input counts!

🛠️ Found a bug? Open an issue

🌟 Enjoyed using the app? Please star the repository!

🤝 Want to contribute? Fork the repo and send a pull request

-------

## 🙋‍♂️ About the Creator
Created with passion by Hemaperumal
🔗 View the Live App on Hugging Face

If this project helped you take control of your spending or just inspired your next build—I'd love to hear from you!


