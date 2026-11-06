"""
RECORD CHECK  -  my version
===========================

Name  :  Raimi Thomas
Lane  :  AI
Date  :  06-11-2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ================================================================== OUTPUT
import pandas as pd
import matplotlib.pyplot as plt

# ==================================================================== LOAD

# Read the CSV file
df = pd.read_csv("records_sample.csv")


# ================================================================= PROCESS

# Calculate the percentage for each record
df["percent"] = (df["value"] / df["limit"]) * 100

# Add a status based on the percentage
df["status"] = df["percent"].apply(
    lambda p: "OVER LIMIT" if p >= 100 else "WARNING" if p >= 90 else "OK"
)


# ================================================================== OUTPUT

# Print the complete DataFrame
print(df)

# Print only the rows that are not OK
print(df[df["status"] != "OK"])

# Group by status and count the records in each group
print(df.groupby("status").size())

# Save the full DataFrame to a new CSV file
df.to_csv("records_report.csv", index=False)

# Create a bar chart showing the status counts
df["status"].value_counts().plot(kind="bar")

# Add a title to the chart
plt.title("Status Counts")

# Save the chart
plt.savefig("status_counts.png")

# Display the chart
plt.show()
