"""
RECORD CHECK  -  my version
===========================

Name  :  Raimi Thomas
Lane  :  AI 
Date  :  23-10-2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ====================================================================== CLASS

#    Excellent : also add over_limit_count as a class-level running total -
#                see the note below.

# your class goes here
class Record:
    def __init__(self,label,value,limit):
        """Stores all three atrributes (label value limit)"""
        self.label=label
        self.value=value
        self.limit=limit

    def status(self):
        """checks and returns whether it is over limit, warning or ok"""
        if self.value > 100:
            return "OVER LIMIT"
        elif self.value > 90:
            return "Warning"
        else:
            return "OK"
        
class Checker:
    """Checks if the record goes over_limit_count and adds it up"""
    def __init__(self):
        """Sets the intial count to 0"""
        self.over_limit_count=0
    def check (self,value,limit):
        """check whether value is greater than limit and returns count"""
        if value > limit:
            self.over_limit_count+=1

c=Checker()
              
    

# ==================================================================== RECORDS
 

def load_records(path):
    """Reads the label , value ,  limit lines from the file and 
        returns a list of record objects"""
    records=[]
    with open(path) as f:
        for line in f:
            label,value,limit=line.strip().split(",")
            #convert value and limit with float()
            records.append(Record(label,float(value),float(limit)))
    return records

with open ("testfile.txt","w") as f:
    f.write("R-001,87,100\n")
    f.write("R-002,88,100\n")
    f.write("R-003,91,100\n")   

records=load_records("testfile.txt")
      
            
# ==================================================================== OUTPUT

for record in records:
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)

    # your report lines go here

    print("=" * 34)
    print()
    print(f" Value : {record.value:>+10.2f}")
    print(f" Limit : {record.limit:>+10.2f}")
    c.check(record.value,record.limit)
    print(f"Status : {record.status()}")
    print()
    print("="*34)
    print()

print("Count of OVERLIMITS:", c.over_limit_count)

# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers by hand
#    [ ] Check every method only reads/changes its OWN object (self) -
#        nothing reaches outside itself
#    [ ] Check every method and __init__ has a one-line docstring
