"""
RECORD CHECK  -  my version
===========================

Name  : Dhanishta Booneady
Lane  :   Cyber      (delete two)
Date  : 02 oct 2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ==================================================================== INPUT
# 1. Ask for your three values.
#
#    - the first is TEXT      (a name, a hostname, an IP)  -> no conversion needed
#    - the second is a NUMBER (use float(), not int())
#    - the third  is a NUMBER (use float(), not int())


label = (input("Enter a name: "))
value = (float(input("Enter a number: ")))
limit = (float(input("Enter a second number: ")))
# ================================================================== PROCESS
# 2. Work out the difference and the percentage.       [Typical and above]

if value > limit:
 difference= value-limit 
else:
 difference= limit-value
percent = difference /limit * 100 


# 3. Decide a status and store it in a variable called status.
#
#    Threshold : if / else        -> "OVER LIMIT" or "OK"
#    Typical   : if / elif / else -> "OVER LIMIT" (100% or more),
#                                     "WARNING" (90% or more), otherwise "OK"
overcount = 0 
if percent >= 100:
 status = "OVER LIMIT"
 overcount+=1
elif percent <100 and percent >90 :
 status = "WARNING"
else:
 status = "OK"
 

# =================================================================== OUTPUT
# 4. Print the report.
#
#    Threshold : the three values you were given, plus status, inside a border
#    Typical   : add difference and percent, 2 decimal places, right-aligned
#    Excellent : wrap sections 1-4 in a loop so you can check as many records
#                as you like in one run - type "quit" as the label to stop.
#                Keep count of how many came back OVER LIMIT and print that
#                once, after the loop ends.

while label != "quit":
  print("=" * 40)
  print(f"  RECORD CHECK  -  {label}")
  print(f" VALUE - {value}")
  print(f" LIMIT - {limit}")
  print(f"The difference is: {difference:>10.2f}")
  print(f"The percentage is: {percent:>10.2f}")
  print("=" * 40)
  print("=" * 40)
  print(f"Status is: {status}")
  print (f"Number of OVER LIMIT: {overcount}")
  print("=" * 40)
  label= (input("Re-enter Name: "))
  if label == "quit":
   break
  value=(float(input("Enter a new value: ")))
  limit=(float(input("Enter a new limit value: ")))
  if value > limit:
   difference= value-limit 
  else:
   difference= limit-value
  percent = difference /limit * 100 
  overcount = 0 
  if percent >= 100:
   status = "OVER LIMIT"
   overcount+=1
  elif percent <100 and percent >90 :
   status = "WARNING"
  status = "OK"
 

# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every variable name says what it holds
