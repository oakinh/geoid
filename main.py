import pandas as pd

# Read the Parquet file
df = pd.read_parquet("census_geoids_wCountyZip5.parquet", engine="pyarrow")  # or engine="fastparquet"

# Save as CSV
df.to_csv("output.csv", index=False)
