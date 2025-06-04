import os
import fitz  # PyMuPDF
import gradio as gr
from groq import Groq # LLM API Intergration
import re
import pandas as pd

# OpenAI or Groq API setup
groq_api_key = "Your_Groq_API_KEY"
client = Groq(api_key=groq_api_key)

def extract_text_from_pdf(file):  
    """Extract full text using pdfplumber."""
    text = ""
    with pdfplumber.open(file.name) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text.strip()

def extract_transactions_from_pdf(file):
    merchant_to_category = {
        "Reliance Retail Ltd": "Retail",
        "Amazon Pay": "E-commerce / Retail",
        "One Ninety Seven": "Payments / Other",
        "Paytm Gold": "Digital Wallet",
        "Flipkart": "E-commerce / Retail",
        "Myntra": "E-commerce / Retail",
        "BigBasket": "E-commerce / Grocery",
        "Swiggy": "Food Delivery",
        "Zomato": "Food Delivery",
        "restaurant": "Food",
        "Sandwich": "Food",
        "Hotel": "Food",
        "Cafe": "Food",
        "HOT COOL": "Food",
        "Uber": "Ridesharing / Transport",
        "Ola": "Ridesharing / Transport",
        "BookMyShow": "Entertainment",
        "Netflix": "Streaming Services",
        "Spotify": "Streaming Services",
        "Jio": "Telecommunications",
        "Airtel": "Telecommunications",
        "Vodafone": "Telecommunications",
        "Disney+ Hotstar": "Streaming Services",
        "Paytm": "Digital Wallet",
        "PhonePe": "Digital Wallet",
        "Google Pay": "Digital Wallet",
        "HDFC Bank": "Banking / Finance",
        "ICICI Bank": "Banking / Finance",
        "SBI": "Banking / Finance",
        "Domino's": "Food Delivery",
        "IRCTC": "Travel",
        "Dream11": "Gaming / Sports",
        "Ajio": "E-commerce / Fashion",
        "Nykaa": "Beauty / E-commerce",
        "Masonary": "Civil ",
        "Ele": "Civil",
        "Store": "Shopping",
        "enterprise": "Shopping",
        "Medical": "Health",
    }

    def categorize_transaction(description):
        for merchant, category in merchant_to_category.items():
            if merchant.lower() in description.lower():
                return category
        if "Money sent to" in description:
            return "P2P - Sent"
        elif "Received from" in description:
            return "P2P - Received"
        else:
            return "Uncategorized"

    transactions = []
    all_times = []
    keywords = {
        "Paid to": "Debit",
        "Money sent to": "Debit",
        "Paytm Merchant": "Debit",
        "Received from": "Credit"
    }

    doc = fitz.open(file.name)
    full_text = "\n".join(page.get_text("text") for page in doc)

    # Extract all matching amounts once
    raw_amounts = re.findall(r'(?:INR|₹)\s*([\d,]+\.?\d*)', full_text, re.IGNORECASE)
    cleaned_amounts = [amt.replace(',', '') for amt in raw_amounts]
    amount_index = 0  # index for tracking used amounts

    current_date = ""
    for page in doc:
        text = page.get_text("text")
        lines = text.split("\n")
        for i, line in enumerate(lines):
            time_match = re.search(r"(?:\b|^)(\d{1,2})[:：](\d{2})\s*(am|pm)?(?:\b|$)", line, re.IGNORECASE)
            if time_match:
                hour = time_match.group(1).zfill(2)
                minute = time_match.group(2)
                meridiem = time_match.group(3).upper() if time_match.group(3) else ""
                time_value = f"{hour}:{minute} {meridiem}".strip()
                all_times.append(time_value)

            date_match = re.search(r"\b(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+\d{1,2},?\s+\d{4}\b", line, re.IGNORECASE)
            if date_match:
                current_date = date_match.group(0).strip()

            matched_keyword = next((kw for kw in keywords if kw in line), None)
            if matched_keyword:
                category = keywords[matched_keyword]

                # Pull next unused amount
                amount = ""
                if amount_index < len(cleaned_amounts):
                    amount = cleaned_amounts[amount_index]
                    amount_index += 1

                desc_match = re.search(rf"{matched_keyword}\s+(.+?)(?:₹|Rs|INR|\d|$)", line)
                entity = ""
                if desc_match:
                    raw_entity = desc_match.group(1).strip()
                    entity = re.sub(r'\b(debited|credited|reference\s*debit|reference|debit|credit)\b', '', raw_entity, flags=re.IGNORECASE).strip()
                    entity = re.sub(r'\s{2,}', ' ', entity)

                transactions.append({
                    "Date": current_date,
                    "Receiver": entity,
                    "Amount (₹)": amount,
                    "Type": category
                })

    df = pd.DataFrame(transactions)

    if len(all_times) < len(df):
        last_time = all_times[-1] if all_times else ""
        all_times += [last_time] * (len(df) - len(all_times))

    df["Time"] = all_times[:len(df)]
    df["Transaction Count"] = df["Receiver"].apply(lambda r: df["Receiver"].value_counts().get(r, 1))
    df["Category"] = df["Receiver"].apply(categorize_transaction)

    df = df[["Date", "Time", "Receiver", "Amount (₹)", "Type", "Transaction Count", "Category"]]
    return df

def export_transactions_to_csv(file):
    import tempfile
    df = extract_transactions_from_pdf(file)
    temp = tempfile.NamedTemporaryFile(delete=False, suffix=".csv")
    df.to_csv(temp.name, index=False)
    return temp.name

def analyze_financial_data(pdf_file):
    """Analyze full text for financial insights using LLaMA3."""
    if not pdf_file:
        return "⚠️ No file uploaded."

    extracted_text = extract_text_from_pdf(pdf_file)
    if not extracted_text:
        return "⚠️ Could not extract text. Ensure the PDF is not a scanned image."

    prompt = f"""
      Analyze the following Paytm transaction history and generate financial insights:

      {extracted_text}

      Provide a detailed breakdown in the following format:

      **Financial Insights for [User Name]**

      **Key Details:**

      - **Overall Monthly Income & Expenses:**
        - Month: [Month]
        - Income: ₹[Amount]
        - Expenses: ₹[Amount]

      - **Unnecessary Expenses Analysis:**
        - Expense Category: [Category Name]
        - Amount: ₹[Amount]
        - Recommendation: [Suggestion]

      - **Savings Percentage Calculation:**
        - Savings Percentage: [Percentage] %

      - **Expense Trend Analysis:**
        - Notable Trends: [Trend Details]

      - **Cost Control Recommendations:**
        - Suggestion: [Detailed Suggestion]

      - **Category-Wise Spending Breakdown:**
        - Category: [Category Name] - ₹[Amount]
        - Percentage: [Percentage] %

      - **Frequent Receiver or Payees:**
        - Merchant: [Name]
        - No. of Transactions: [Count]
        - Total Spent: ₹[Amount]

      - **Monthly Cash Flow Overview:**
        - Opening Balance: ₹[Amount]
        - Total Inflow: ₹[Amount]
        - Total Outflow: ₹[Amount]
        - Closing Balance: ₹[Amount]

      - **Late-Night or Odd-Hour Transactions:**
        - No. of Transactions: [Count]
        - Total Amount: ₹[Amount]
        - Observations: [Behavioral Insights]

      - **Recurring Payments and Subscriptions:**
        - Service: [Service Name]
        - Frequency: [Monthly/Weekly/etc.]
        - Amount: ₹[Amount]
        - Actionable Advice: [Keep/Cancel]

      - **Top 5 Expense Categories (by Spend):**
        - 1. [Category] - ₹[Amount]
        - 2. [Category] - ₹[Amount]
        - 3. [Category] - ₹[Amount]
        - 4. [Category] - ₹[Amount]
        - 5. [Category] - ₹[Amount]

      - **One-Time Large Transactions:**
        - Description: [Details]
        - Amount: ₹[Amount]
        - Justification Check: [Necessary/Optional]

      - **Spending vs. Previous Month Comparison:**
        - Income Change: [+/- ₹Amount]
        - Expense Change: [+/- ₹Amount]
        - Savings Trend: [Up/Down %]

      - **Top Payment Methods Used:**
        - Method: [Wallet/UPI/Card/etc.]
        - Transactions: [Count]
        - Total Value: ₹[Amount]

      - **Potential Fraud or Suspicious Activities:**
        - Transaction(s): [Details]
        - Reason for Flag: [Explanation]
        - Suggested Action: [Monitor/Report/Ignore]

      - **Financial Health Score (Out of 100):**
        - Score: [Score]
        - Rating: [Excellent/Good/Fair/Poor]
        - Brief Justification: [Summary]
      """


    chat_completion = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {"role": "system", "content": "You are a financial data analyst."},
            {"role": "user", "content": prompt}
        ]
    )

    return chat_completion.choices[0].message.content

import gradio as gr

with gr.Blocks(title="💰 Personal Finance Assistant") as demo:
    gr.HTML("""
    <style>
    h2, p, .gr-markdown {
        text-align: center;
        color: #2e7d32;
        margin-bottom: 10px;
    }
    button {
        border-radius: 8px !important;
        padding: 10px 18px !important;
        font-weight: 600 !important;
        cursor: pointer;
    }
    .gr-textbox textarea {
        height: 150px !important;
        resize: vertical;
    }
    .gr-textbox label {
        width: 100%;
        display: block;
        text-align: center;
        font-weight: bold;
        color: #2e7d32;
    }
    </style>
    """)

    gr.Markdown("## 💰 AI-Powered Financial Advisor")
    gr.Markdown("Upload your PhonePe Transaction history to get financial insights and preview your transactions.")
    # ✅ PDF upload instructions

    with gr.Row():
        file_input = gr.File(label="📂 Please upload your PhonePe PDF file (max size: 200 MB)", file_types=[".pdf"])

    with gr.Row():
        analyze_button = gr.Button("🔍 Analyze with AI")
        preview_button = gr.Button("👁️ Transactions")
        reset_button = gr.Button("🔄 Reset")

    output_box = gr.Textbox(
        label="📈 Analyzed Report",
        lines=10,
        show_copy_button=True,
        visible=False,
        value=""  # start empty
    )

    transactions_table = gr.Dataframe(
        headers=["Date", "Time", "Receiver", "Amount (₹)", "Type", "Transaction Count", "Category"],
        label="🧾 Extracted Transactions",
        wrap=True,
        visible=False,
        value=[]  # start empty
    )

    csv_button = gr.Button("⬇️ Download CSV", visible=False)
    csv_output = gr.File(label="📁 Download Transactions CSV", visible=False)

    # Reset button


    def reset_ui():
        return (
            None,  # file_input (clears file)
            gr.update(visible=False, value=""),        # output_box
            gr.update(visible=False, value=[]),        # transactions_table
            gr.update(visible=False),                  # csv_button
            gr.update(visible=False)                   # csv_output
        )

    # Connect Reset button to UI reset
    reset_button.click(
        fn=reset_ui,
        inputs=[],
        outputs=[file_input, output_box, transactions_table, csv_button, csv_output]
    )


    # Preview handler: returns empty DataFrame visible + shows CSV button
    def handle_preview(file):
        df = extract_transactions_from_pdf(file)
        return gr.update(visible=True, value=df), gr.update(visible=True), gr.update(visible=False)

    # Analyze handler: returns non-empty report box visible
    def handle_analyze(file):
        report = analyze_financial_data(file)
        return gr.update(visible=True, value=report)

    # CSV handler: shows file output after export
    def handle_csv(file):
        csv_path = export_transactions_to_csv(file)
        return gr.update(visible=True, value=csv_path)

    preview_button.click(
        fn=handle_preview,
        inputs=file_input,
        outputs=[transactions_table, csv_button, csv_output]
    )

    analyze_button.click(
        fn=handle_analyze,
        inputs=file_input,
        outputs=output_box
    )

    csv_button.click(
        fn=handle_csv,
        inputs=file_input,
        outputs=csv_output
    )

demo.launch()
