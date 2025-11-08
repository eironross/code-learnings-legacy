"""
Counts the vowels and consotant of a given string
"""


def count_vowels_consonants(string):
    
    num_vowels = 0
    num_consonants = 0
    
    if not string:
        return [-1, -1]
    
    trimmed_string = "".join(string.lower().split())
    
    for ch in trimmed_string:
        if ((ord(ch) in range(ord("a"), ord("z") + 1)) 
            and (ch not in ["a", "e", "i", "o", "u"])):
            
            num_consonants+=1
        else:
            num_vowels+=1
            
    return [num_vowels, num_consonants]

input_string = ""

check = count_vowels_consonants(input_string)

print("Number of vowels are:", check[0] )
print("Number of consonants are:", check[1])