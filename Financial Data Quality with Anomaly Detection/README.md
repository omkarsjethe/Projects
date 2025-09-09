# Financial Data Quality Project

Automated data quality monitoring system for financial transactions.  
This project uses Python to detect missing values, duplicates, negative amounts, future dates, and anomalies in transaction data. Includes scripts, sample data, a summary dashboard, and documentation to help organizations ensure reliable, accurate financial records.


## Features

- **Missing Values:** Counts missing entries in each column.
- **Duplicate Rows:** Identifies duplicate records.
- **Duplicate Transaction IDs:** Checks for repeated transaction IDs (if column exists).
- **Negative Amounts:** Finds transactions with negative values (if column exists).
- **Future Dates:** Detects transactions with dates in the future (if column exists).
- **Anomaly Detection:** Uses Isolation Forest to flag unusual transaction amounts (if column exists).


## How to Run

1. **Install requirements** (if not already installed):
    ```bash
    pip install pandas scikit-learn
    ```

2. **Place your data file**  
   Ensure your transaction data CSV file is located at:  
   ```
   C:\Users\Owner\Project\Financial data quality project\data\transaction.csv
   ```
   *(Or update the script path if your file is elsewhere.)*

3. **Run the script**
    - Open a Command Prompt.
    - Navigate to the script folder:
      ```bash
      cd "C:\Users\Owner\Project\Financial data quality project\Scripts"
      ```
    - Run:
      ```bash
      python data_quality_monitor.py
      ```



## How to Schedule (Windows Task Scheduler)

1. Open **Task Scheduler**.
2. Create a new basic task.
3. Set your preferred schedule (e.g., daily at 8 AM).
4. For the action:
    - **Program/script:** Path to your Python executable (e.g., `C:\Python311\python.exe`)
    - **Add arguments:**  
      ```
      "C:\Users\Owner\Project\Financial data quality project\Scripts\data_quality_monitor.py"
      ```
5. Save and test the task.



## Output

- The summary of data quality checks is saved to:
  ```
  C:\Users\Owner\Project\Financial data quality project\data\data_quality_summary.csv
  ```



## Troubleshooting

- **ModuleNotFoundError:**  
  Install missing packages with:
  ```bash
  pip install pandas scikit-learn
  ```
- **FileNotFoundError:**  
  Make sure the CSV file path in the script matches your actual file location.
- **Task Scheduler issues:**  
  Ensure all paths are correct and Python is installed.



## Customization

- If your data file, columns, or output paths are different, update the relevant lines in `data_quality_monitor.py`.
- The script pauses at the end (`input("Press Enter to exit...")`) so you can review results before the window closes.



## Contact

For questions or help, contact: gsundararajan@albany.edu

