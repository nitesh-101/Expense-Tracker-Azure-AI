# 💸 Azure AI Expense Tracker (Receipt Analyzer)

## 📌 Overview

This project is an **AI-based Expense Tracker** that extracts important details from receipt images using Azure AI and automatically categorizes expenses.

It helps reduce manual work and makes expense tracking faster and more accurate.

---

## 🚀 Features

* 📷 Upload receipt images
* 🧠 Extracts:

  * Merchant Name
  * Transaction Date
  * Total Amount
* 🏷️ Automatic expense categorization
* 🔐 Secure API key handling using `.env`
* ⚡ Simple and beginner-friendly Python code

---

## 🧠 Technologies Used

* Python
* Azure AI Document Intelligence
* python-dotenv

---

## ⚙️ How It Works

1. User provides a receipt image
2. Image is sent to Azure AI
3. AI extracts structured data
4. Data is categorized based on merchant
5. Output is displayed

---

## 📂 Project Structure

```
project/
│── receipt_tracker.py
│── receipt.jpg
│── .env              # (not uploaded to GitHub)
│── requirements.txt
│── README.md
│── .gitignore
```

---

## 🔐 Setup Instructions

### 1. Clone the repository

```
git clone https://github.com/YOUR_USERNAME/azure-ai-expense-tracker.git
cd azure-ai-expense-tracker
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Add environment variables

Create a `.env` file:

```
AZURE_ENDPOINT=your_endpoint_here
AZURE_KEY=your_key_here
```

---

## ▶️ Run the Project

```
python receipt_tracker.py
```

---

## 📊 Sample Output

```
Merchant: Dominos
Date: 2026-04-26
Total: ₹299
Category: Food
```

---

## ❓ Why This Project?

Manual expense tracking is time-consuming and error-prone.
This project uses AI to automate the process and improve efficiency.

---

## 🚀 Future Improvements

* Database integration (SQLite / MongoDB)
* Dashboard with charts
* Mobile application
* ML-based smart categorization

---

## 🧾 Conclusion

This project shows how AI can convert unstructured data (receipts) into structured information for real-world applications.

---

