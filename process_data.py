import pandas as pd
import glob

# Read all CSV files inside data folder
files = glob.glob("data/*.csv")

df_list = []

for file in files:
    temp = pd.read_csv(file)

    # Extract region from filename  (e.g., data/North.csv → north)
    region = file.split("\\")[-1].split(".")[0].lower()

    temp["region"] = region

    # Convert columns
    temp["price"] = temp["price"].replace('[\$,]', '', regex=True).astype(float)
    temp["quantity"] = temp["quantity"].astype(int)

    # Calculate sales
    temp["sales"] = temp["price"] * temp["quantity"]

    df_list.append(temp)

df = pd.concat(df_list)

# Grouping for final clean output
final = df.groupby(["date", "region"], as_index=False)["sales"].sum()

# Save clean file
final.to_csv("processed_sales_data.csv", index=False)
print("File processed successfully!")
