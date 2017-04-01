import sys

# ascii values for alphabetic characters
lower_min = 97
lower_max = 122
upper_min = 65
upper_max = 90

def lc(a): # check if lowercase
    global lower_min
    global lower_max
    if (ord(a) > lower_min - 1 and ord(a) < lower_max + 1): # lowercase ascii range (if lowercase),
        return True;
    else:
        return False;
    
def uc(a): # check if uppercase
    global upper_min
    global upper_max
    if (ord(a) > upper_min - 1 and ord(a) < upper_max + 1): # uppercase ascii range (if uppercase),
        return True;
    else:
        return False;

def not_a_letter(a): # check if a letter
    if (ord(a) < 65 or ord(a) > 122): 
        return True;
    else:
        return False;

def overflow(a, key):
    # for each character in plaintext,
    if (lc(a) and (ord(a) + key > 122)): # if lowercase AND it overflows,
        return True;
    elif (uc(a) and (ord(a) + key > 90)): # if uppercase AND if overflows,
        return True;
    else:
        return False;

# otherwise, set key to first argument, prompt user for plaintext, and store plaintext into 'text' string;

       
# variables and functions defined above; logic below;

while True:
    try:
        key = int(input("please enter a number: "))
        break
    except ValueError:
        print("usage: caesar.py [int]")
        
text = input("plain-text:")

for i in range(0, len(text)):
        
    if (not_a_letter(text[i])): 
        # if not a letter, print exactly as it was entered in;
        print(text[i], end="")           
            
    # if lowercase,    
    elif (lc(text[i])): # lowercase ascii range (if lowercase),

        # if key would cause lowercase to overflow, wrap it around instead 97-122
        if (overflow(text[i], key)):
            s = ord(text[i]) + key
            extra = s - lower_max - 1 # set up an overflow integer to add to lower_min, thus wrapping around
            print(chr(lower_min + extra), end="")

        else: # if no overflow, simply add key to ascii value and return enciphered lowercase character
            s = ord(text[i]) + key
            print(chr(s), end=""); 
        # printing to the same as earlier text
        
    # if uppercase,   
    elif (uc(text[i])): # uppercase ascii range (if uppercase),

        # if key would cause uppercase to overflow, wrap it around instead 65-90
        if (overflow(text[i], key)):
            s = ord(text[i]) + key
                
            extra = s - upper_max - 1 # set up an overflow integer to add to upper_min, thus wrapping around
            print(chr(upper_min + extra), end="")
                
        else:
            print(chr(ord(text[i]) + key), end="") # if no overflow, simply add key to ascii value and return enciphered uppercase character

# print new line when finished
print("\n")