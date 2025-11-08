""" Reverses the text from an input"""

text = "ASjdklasdjlaskdjadlsjasdjk"

def reverse_text(text):
    array = []
    print("This is the split test: ", text)
    counter = len(text) - 1
    
    while (counter >= 0):
        array.append(text[counter])
        counter-=1        
    
    result = "".join(array)
    
    return result

print(reverse_text(text))