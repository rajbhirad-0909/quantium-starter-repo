import pandas as pd
import glob
import os

# Path to data folder
data_path = "data/*.csv"

# Read all three CSVs
files = glob.glob(data_path)

all_data = []

for file in files:
    df = pd.read_csv(file)

    # 1. Filter only Pink Morsels
    df = df[df["product"] == "pink morsel"]

    # 2. Create a sales column
    df["sales"] = df["quantity"] * df["price"]

    # 3. Keep only required columns
    df = df[["date", "region", "sales"]]

    all_data.append(df)

# 4. Combine all datasets
final_df = pd.concat(all_data, ignore_index=True)

# 5. Ensure output folder exists
os.makedirs("output", exist_ok=True)

# 6. Save final combined file
final_df.to_csv("output/processed_sales_data.csv", index=False)

print("🎉 Processing complete!")
print("Saved to: output/processed_sales_data.csv")
