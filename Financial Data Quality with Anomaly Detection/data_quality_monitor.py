import pandas as pd

# Load the transaction data from CSV file
# (Update the path if your file is in a different location)
df = pd.read_csv("C:\\Users\\Owner\\Project\\Financial data quality project\\data\\transaction.csv")

# Display the first 5 rows to check the data
print(df.head())

# Show data types and basic info about the DataFrame
print(df.info())

# Print column names
print(df.columns)

# Show summary statistics for numerical columns
print(df.describe())

# Print the count of missing values per column
print(df.isnull().sum())

# Count missing values in each column
missing_report = df.isnull().sum()
print("Missing Values per Column:\n", missing_report)

# Check for duplicate rows in the data
duplicates = df[df.duplicated()]
print(f"Number of duplicate rows: {duplicates.shape[0]}")

# Check for duplicate transaction IDs (if the column exists)
if 'transaction_id' in df.columns:
    duplicate_ids = df[df.duplicated(subset=['transaction_id'])]
    print(f"Number of duplicate transaction IDs: {duplicate_ids.shape[0]}")

# Check for negative transaction amounts (if the column exists)
if 'amount' in df.columns:
    negative_amounts = df[df['amount'] < 0]
    print(f"Number of negative amounts: {negative_amounts.shape[0]}")

# Check for transactions with future dates (if the column exists)
import datetime
if 'date' in df.columns:
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    future_dates = df[df['date'] > datetime.datetime.now()]
    print(f"Number of transactions with future dates: {future_dates.shape[0]}")

# Use Isolation Forest to detect anomalies in 'amount' column (if it exists)
from sklearn.ensemble import IsolationForest
if 'amount' in df.columns:
    # Isolation Forest expects 2D input
    amounts = df[['amount']].dropna()
    clf = IsolationForest(contamination=0.01, random_state=42)
    df.loc[amounts.index, 'anomaly'] = clf.fit_predict(amounts)
    anomalies = df[df['anomaly'] == -1]
    print(f"Number of anomalies detected: {anomalies.shape[0]}")
else:
    anomalies = pd.DataFrame()

# Summarize the results in a dictionary
summary = {
    'Missing Values': missing_report.sum(),
    'Duplicate Rows': duplicates.shape[0],
    'Negative Amounts': negative_amounts.shape[0] if 'amount' in df.columns else 0,
    'Future Dates': future_dates.shape[0] if 'date' in df.columns else 0,
    'Anomalies': anomalies.shape[0] if 'amount' in df.columns else 0
}

# Convert the summary dictionary to a DataFrame for easy export
summary_df = pd.DataFrame(list(summary.items()), columns=['Issue', 'Count'])
print(summary_df)

# Save the summary to a CSV file
summary_df.to_csv("C:\\Users\\Owner\\Project\\Financial data quality project\\report\\data_quality_summary.csv", index=False)

print("Data quality check complete! Summary saved to ..report\\data_quality_summary.csv")

# Pause so you can see the output before the terminal closes
input("Press Enter to exit...")
