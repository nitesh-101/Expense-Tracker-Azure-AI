import os
import re # For fallback text extraction
from dotenv import load_dotenv
from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient

load_dotenv()

endpoint = os.getenv("AZURE_ENDPOINT")
key = os.getenv("AZURE_KEY")

client = DocumentIntelligenceClient(endpoint, AzureKeyCredential(key))

def categorize(merchant):
    if not merchant or merchant == "N/A":
        return "Other"

    merchant = merchant.lower()
    if "domino" in merchant or "pizza" in merchant or "restaurant" in merchant:
        return "Food"
    elif "uber" in merchant or "ola" in merchant or "taxi" in merchant:
        return "Transport"
    elif "amazon" in merchant or "flipkart" in merchant:
        return "Shopping"
    elif "medical" in merchant or "pharmacy" in merchant:
        return "Health"
    else:
        return "Other"

def analyze_receipt(file_path):

    # File not found
    if not os.path.exists(file_path):
        print("File not found!")
        return []
    try:
        with open(file_path, "rb") as f:
            poller = client.begin_analyze_document(
                model_id="prebuilt-receipt",
                body=f
            )
            result = poller.result()
    # Azure/API error
    except Exception as e:
        print("Azure Error:", e)
        return []

    receipts = []

    # No documents returned
    if not result.documents:
        print("No receipt data found!")
        return []

    for doc in result.documents:
        merchant_field = doc.fields.get("MerchantName")
        merchant = merchant_field.content if merchant_field and merchant_field.content else "N/A"

        total_field = doc.fields.get("Total")
        if total_field and total_field.content:
            total_value = total_field.content
        else:
            # Fallback: extract total manually from raw OCR text
            total_value = "N/A"
            match = re.search(r"total\s*₹?\s*([0-9]+\.?[0-9]*)", result.content.lower())
            if match:
                total_value = match.group(1)

        try:
            total_value = float(str(total_value).replace("₹", "").strip())
        except:
            total_value = "N/A"

        date_field = doc.fields.get("TransactionDate")
        date = date_field.content if date_field and date_field.content else "N/A"
        data = {
            "Merchant": merchant,
            "Date": date,
            "Total": total_value,
            "Category": categorize(merchant)
        }
        receipts.append(data)
    return receipts

data = analyze_receipt("receipt.jpg")
for item in data:
    print(item)