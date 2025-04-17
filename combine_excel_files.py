import os
import pandas as pd

from openpyxl import Workbook


#folder_path = "excel_files"
folder_path = "/Users/us4ha8/Documents/development/sql-script/excel_files"

dfs = []

for filename in os.listdir(folder_path):
    if filename.endswith(".xlsx"):
        file_path = os.path.join(folder_path, filename)
        try:
            df = pd.read_excel(file_path, engine="openpyxl")

            # Skip if there are no data rows (headers assumed always present)
            if df.shape[0] == 0:
                print(f"❌ Skipping empty data file: {filename}")
                continue

            dfs.append(df)
            print(f"✅ Loaded: {filename} with {df.shape[0]} rows")

        except Exception as e:
            print(f"⚠️ Error reading {filename}: {e}")

# Combine and save
if dfs:
    combined_df = pd.concat(dfs, ignore_index=True)
    combined_df.to_excel("combined.xlsx", index=False)
    print(f"\n✅ Combined file saved as 'combined.xlsx' with {combined_df.shape[0]} total rows.")
else:
    print("\n⚠️ No files with data rows found to combine.")