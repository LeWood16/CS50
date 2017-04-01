change = input("How much change is due? ")
change = int(change)
count = 0

def decrement (tender): # decrement change by tender
    global change
    change = change - tender
    global count 
    count += 1
    return;
    
def printChangeCount():
    global count
    global change
    if (count == 1):
        print("1 coin is given back as change.")
    else:
        print(count, "coins are given back as change.")
    return;
    
# variables and functions defined above; logic below;

while (change < 0):
    print("Please enter a positive amount of change") 
    break
  
while (change > 0):
    if (change % 25 == 0): # if all change can be in quarters, 
        decrement(25)
    elif (change % 10 == 0):
        decrement(10)
    elif (change % 5 == 0):
        decrement(5)
    elif (change % 1 == 0):
        decrement(1)

if (count > 0):
    printChangeCount()