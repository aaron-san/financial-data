import csv
import sqlite3
import os
import pandas as pd


# list of available files:
# All files are in their respective folders
# e.g., CSV/industries/industries.csv

file_name = "industries"
# file_name = "markets"
# file_name = "us-shareprices-daily"
# file_name = "us-balance-quarterly"
# file_name = "us-cashflow-quarterly"
# file_name = "us-income-quarterly"

def csv_to_sql(file_name):
    # --- Base path ---
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    print("Base directory:", BASE_DIR)
    # print(__file__)

    # --- Configuration ---
    csv_path = os.path.join(BASE_DIR, f"../{file_name}/{file_name}.csv")
    db_path = os.path.join(BASE_DIR, "../company_data.db")
    table_name = file_name.replace("-", "_")

    # --- Create DB if doesn't exist ---
    os.makedirs(os.path.dirname(db_path), exist_ok=True)

    # print(f"Detected columns:", list(df.columns))
    # print("Preview:\n", df.head())


    # --- Read CSV and insert rows ---
    with open(csv_path, newline='', encoding='utf-8') as f:
            sample = f.read(2048)
            f.seek(0)
            try: 
                dialect = csv.Sniffer().sniff(sample)
                delimiter = dialect.delimiter
            except csv.Error:
                print("Could not detect delimiter - defaulting to comma")
                dialect = csv.get_dialect("excel")
                delimiter = ","
            
            
    print(f"Detected delimiter:  {repr(dialect.delimiter)}")
    df = pd.read_csv(csv_path, sep=delimiter)

    # --- Connect to SQLite ---
    conn = sqlite3.connect(db_path)

    # --- Insert rows ---
    df.to_sql(table_name, conn, if_exists="replace", index=False)

    conn.close()

    print(f"Imported {len(df)} rows from {csv_path} into table '{table_name}' ({db_path})")

    print("CSV imported successfully")
    
if __name__ == "__main__":
    csv_to_sql(file_name)
        
        
