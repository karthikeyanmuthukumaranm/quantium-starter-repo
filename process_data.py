import pandas as pd
from pathlib import Path

data_dir = Path("data")
csv_files = [
    f for f in data_dir.glob("daily_sales_data_*.csv")
]

frames = []

for csv_file in csv_files:
    df = pd.read_csv(csv_file)

    # Filter only pink morsel (exact match)
    df = df[df["product"] == "pink morsel"]

    # Convert price "$3.00" → 3.00
    df["price"] = df["price"].replace(r"[\$,]", "", regex=True).astype(float)

    # Compute sales
    df["Sales"] = df["price"] * df["quantity"]

    # Select required columns
    df = df[["Sales", "date", "region"]]
    df.columns = ["Sales", "Date", "Region"]

    frames.append(df)

# Combine all days
final_df = pd.concat(frames, ignore_index=True)

# Save output
output_path = data_dir / "processed_sales.csv"
final_df.to_csv(output_path, index=False)

print("✅ Data processing completed successfully")
print(f"📁 Output saved to: {output_path}")
