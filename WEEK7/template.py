"""
RECORD CHECK  -  my version
===========================

Name  : Dhanishta Booneady 
Lane  :   Cyber       (delete two)
Date  : 7 Nov 2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Write parse_line(raw_line) that cleans and parses one raw, messy line
#    into a dict. Handle inconsistent spacing and case - that is the whole
#    point of this week.
#
#    Typical and above: also write status_of(...), shaped for your lane
#    (e.g. OVER LIMIT / WARNING / OK, or FLAGGED / OK). Give both a
#    one-line docstring.

# your function(s) go here
def parse_line(raw_line):
    """cleans messy key value into a dict with lowercase keys """
    record ={}
    #split the line using commas 
    for i in raw_line.split(","):
        #skipd non key 
        if "=" not in i:
            continue 
        key, value = i.split("=",1)
        key = key.strip().lower()
        value = value.strip()
        if key == "attempts": #converet attempts in a number to compare 
            value = int (value)
        elif key == "result": #normalise result flagged 
            value = value.upper()
        record[key] = value 
    return record 
def status_of(record):
  """return ok """
  if record.get("attempts",0) >= 10:
      return "FLAGGED"
  return "OK"
# ====================================================================== INPUT
# 2. Your raw, messy records - at least 5, deliberately varied in spacing
#    and case. Match the shape to your lane:
#
#    AI / Data Science : "  Survey_2026 , rating=4 , age=23  "
#    Cyber Security     : "SRC=10.0.0.5,ATTEMPTS=12,RESULT=FAILED"
#    IT                  : "  Srv-01 , used=87 , total=100  "
#
#    Excellent: save these lines to a file and load them with open() /
#    a for loop over the file, instead of writing them directly here.
Raw_File = "raw_records.txt"
#input of records 
raw_records = [
    "SRC = 10.0.0.5, ATTEMPTS = 12, RESULT = FAILED ",  
    "src=10.0.0.6 , Attempts = 5 , result = Success",
    "Src = 10.0.0.7, attempts =9 , Result = success",
    "SRC = 10.0.0.5, Attempts = 18 , Result= Failed",
    "Src=10.0.07, ATTEMPTS = 15, Result = FAILED",
    ]
#saves raw records in 1 line in a file 
with open(Raw_File,"w") as f:
    for line in raw_records:
        f.write(line + "\n")
#loas raw records from the file 
records_load = []
with open(Raw_File,"r") as f:
    for line in f:
        if line.strip():
            records_load.append(line.strip())
# =============================================================== PROCESS + OUTPUT
# 3. Parse and report on every record.
#
#    Threshold : parse each record, print the cleaned dict.
#    Typical   : also call status_of(...) for each, print it alongside.
#    Excellent : print a one-line summary at the end - how many records,
#                how many flagged.
total =0  #counter for the summary 
flagged = 0
#parse each record and check its status 
for line in records_load:
    record = parse_line (line)
    status = status_of(record)
    total += 1 
    if status == "FLAGGED":
        flagged += 1
    print(record, status)
    #one line summary of the records processed 
print(f"Summary: {total } records, {flagged} flagged")


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it against at least 5 genuinely messy raw records
#    [ ] Run it with a value that will not convert to a number - write the
#        error down
#    [ ] Check every function does one job, with a docstring
