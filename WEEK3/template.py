"""
RECORD CHECK  -  my version
===========================

Name  : Dhanishta Booneady
Lane  :  Cyber     (delete two)
Date  : 10 Oct 2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Write a function called status_of(percent) that returns "OVER LIMIT"
#    (100% or more), "WARNING" (90% or more), or "OK" (anything else).
#
#    Typical and above: also write check(value, limit) that returns the
#    difference and the percentage as two values - do not print anything
#    inside it, only calculate and return.
#
#    Excellent: also write print_report(label, value, limit, difference,
#    percent, status) that does ALL of the printing below - nothing outside
#    it should contain a print() of its own.
#
#    Give each function a one-line docstring saying what it does.

# your function(s) go here
overcount=0
def status_of(percent):
    """Return OVER LIMIT, WARNING,OK for the percentage"""
    if percent >= 100:
        return("OVER LIMIT")
    
    elif percent >=90:
        return ("WARNING")
    else:
        return ("OK")

def check(value,limit):
  """Return the value of the percenatge and difference based on value and limit"""
  difference = value-limit 
  percentage = (value/limit)*100 
  return difference, percentage  

def print_report(label,value,limit,difference,percent,status):
 """Print the value of the calculation"""
 
 print(label)
 print(f"Value{value}")
 print(f"Limit {limit}")
 print (f"Difference {difference}")
 print (f"Percent {percent}")
 print (f"Status {status}")



# ==================================================================== INPUT
# 2. Ask for your three values.
#
#    - the first is TEXT      (a name, a hostname, an IP)  -> no conversion needed
#    - the second is a NUMBER (use float(), not int())
#    - the third  is a NUMBER (use float(), not int())

while True:
 name = (input("Enter your name: "))
 if name == "Quit":
    break 
 value = (float(input("Enter a value: ")))  # replace with an input() call, converted
 limit = (float(input("Enter a value limit: "))) 


 difference, percentage = check(value,limit)
 status = status_of(percentage) # replace with your code


 def print_report(name,label,value,limit,difference,percent,status):
   """Print report inside a border"""
 print("=" * 34)
 print(f"Your Name: {name:>20}")
 print(f"Value:     {value:>20}")
 print(f"Limit:     {limit:>20}")
 print(f"Difference:{difference:>20.2f}")
 print(f"Percent:   {percentage:>20.2f}")
 print(f"Status:    {status:>20}")
 if status == "OVER LIMIT":
   overcount += 1 
print("=" * 34)
print (f"Overcome: {overcount}")

# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every function does one job - if a function both calculates
#        and prints, split it
