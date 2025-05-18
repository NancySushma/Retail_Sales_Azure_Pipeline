import os
import pandas as pd
import sys

# Define required columns for schema validation
REQUIRED_COLUMNS = [
    "InvoiceNo", "StockCode", "Description", "Quantity",
    "InvoiceDate", "UnitPrice", "CustomerID", "Country"
]

DATA_PATH = "data/raw/online_retail.csv"

# Check if file exists
if not os.path.exists(DATA_PATH):
    print(f"❌ File not found: {DATA_PATH}")
    sys.exit(1)

# Load CSV and validate schema
df = pd.read_csv(DATA_PATH)

missing = [col for col in REQUIRED_COLUMNS if col not in df.columns]

if missing:
    print(f"❌ Missing columns: {missing}")
    sys.exit(1)

print("✅ CSV schema is valid.")
