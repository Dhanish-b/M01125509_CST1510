"""
RECORD CHECK  -  my version
===========================

Name  : Dhanishta Booneady 
Lane  : Cyber     (delete two)
Date  :22 OCT 2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ====================================================================== CLASS
# 1. Define a class called Record.
#
#    Threshold : __init__(self, label, value, limit) storing all three as
#                attributes. No methods yet.
#    Typical   : add a method status(self) that returns "OVER LIMIT" (100%+),
#                "WARNING" (90%+) or "OK", worked out from self.value and
#                self.limit. Give it a one-line docstring.
#    Excellent : also add over_limit_count as a class-level running total -
#                see the note below.

# your class goes here
class Record:
    over_limit_count = 0 
    def __init__(self,label,value,limit):
        self.label = label
        self.value = value 
        self.limit = limit
    def status(self):
      """Method status calculates the percentage and compares it to output status"""
      percent= self.value/self.limit * 100
      if percent >= 100:
         return("OVER LIMIT")
         self.over_limit_count +=1 
      elif percent >= 90:
        return("WARNING")
      else:
        return("OK")


# ==================================================================== RECORDS
# 2. Create your records.
#
#    Threshold : create at least 2 Record instances directly in the code.
#    Typical   : same, but now print each one's .status() as well.
#    Excellent : instead, write load_records(path) that reads label,value,limit
#                lines from a file and returns a list of Record objects. Make
#                your own data file, one record per line.
def load_records(path):
  records = []  
  with open(path) as f:
    for line in f:
     line= line.strip()
     if not line:
        continue 
     label,value,limit = line.split(",")
     records.append(Record(label.strip(),float(value),float(limit)))
  return records 
 
 

    

# ==================================================================== OUTPUT
# 3. Print a report for each record.
#
#    Threshold : label, value, limit, inside a border.
#    Typical   : add the result of .status().
#    Excellent : also keep a running count of how many came back OVER LIMIT
#                across every record, and print that once, after the loop.
#                (Simplest: a plain variable outside the loop, same pattern
#                as Week 4. If you want it to live ON the object instead,
#                that is a stretch worth trying - but a variable is enough.)

records = (load_records("data.txt"))
over_limit_count=0
for x in records:
    status = x.status()
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {x.label}")    
    print("=" * 34)
    print(f"Value: {x.value}")
    print(f" Limit : {x.limit}")
    print(f" Status: {status}")
    print("=" * 34)
    if status == "OVER LIMIT":
       Record.over_limit_count += 1
print()
print("Over limit: ",Record.over_limit_count)

# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers by hand
#    [ ] Check every method only reads/changes its OWN object (self) -
#        nothing reaches outside itself
#    [ ] Check every method and __init__ has a one-line docstring
