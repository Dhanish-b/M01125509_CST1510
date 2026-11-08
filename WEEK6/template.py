"""
RECORD CHECK  -  my version
===========================

Name  :Dhanishta Booneadsy 
Lane  :   Cyber      (delete two)
Date  : 9 Nov 2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

import pandas as pd

# ==================================================================== LOAD
# 1. Read your data file with pd.read_csv(). Make your own CSV, header row
#    plus at least 5 data rows: label,value,limit (or your lane's own field
#    names - same shape, different words).
data= {
    "label": ["R-001","R-002","R-003","R-004","R-005"],
    "value": [87,120,95,45,100],
    "limit":[100,100,100,100,100]
}
df = pd.DataFrame(data)
df.to_csv("file.csv",index=False)
print("File created ")
# ================================================================= PROCESS
# 2. Add a "percent" column: (value / limit) * 100.
#
#    Typical and above: also add a "status" column using .apply() with a
#    lambda - "OVER LIMIT" (100%+), "WARNING" (90%+), otherwise "OK".

# your column(s) go here
df["percent"]=(df["value"]/df["limit"]) * 100
df["status"] = df["percent"].apply(
    lambda x: "OVER LIMIT" if x>=100 else ("WARNING" if x >= 90 else "OK")
)

# ================================================================== OUTPUT
# 3. Print the DataFrame.
#
#    Threshold : print it as-is, with the percent column.
#    Typical   : also filter to show only the rows that are not "OK", using a
#                boolean condition in [] - not a loop.
#    Excellent : also group by "status" and print a count per group, save
#                the full DataFrame to a new CSV with .to_csv(), and save
#                one bar chart of the counts per status.

print(df)
print("\n")
not_ok_df = df[df["status"] != "OK"]
print(not_ok_df)

status_count = df["status"].value_counts()
print(status_count)
df.to_csv("process_data.csv",index=False)

# ==========================================================================
# 4. Before you finish:
#    [ ] Run it and check the percent/status columns by hand for one row
#    [ ] Check you used & (not "and") if you combined more than one condition
#    [ ] Check every column your code refers to actually exists - watch case
