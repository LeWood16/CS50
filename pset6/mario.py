block = "#"
space = " "
blocks = 2
height = input("How tall is the half-pyramid? ")
h = int(height)
spaces = h

while ((h < 0) or (h > 23)):
    print("Please enter a positive integer less than 24")
    break

for i in reversed(range(h)):
    for k in range(1, spaces):
        print(space, end="")
        
    for j in range(0, blocks):
        print(block, end="")
        
    blocks += 1
    spaces -= 1
    print(" ")