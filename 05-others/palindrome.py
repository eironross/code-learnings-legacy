""" Checks if the Word passed as the argrument is a palindrome"""

text = "levil"

def ispalindrome(text):
    
    lower = text.lower()
    counter = len(lower) - 1
    num = 0
    
    while ( counter >= 0 ):
        lch = lower[num]
        rch = lower[counter]
        
        if lch == rch:
            print("Equal Letters Matched")
        else:
            print("Not Match")
            return False
        
        num+=1
        counter-=1
        
    return True

print(ispalindrome(text))