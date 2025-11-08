
word_one = "SLOT MACHINES"
word_two = "CASH LOST IN ME"

def isanagram(word_one: str, word_two: str):
    
    word_one = "".join(word_one.lower().split())
    word_two = "".join(word_two.lower().split())
    
    print(word_one, word_two)
    
    list_one = sorted([ word_one[i] for i in range(len(word_one))])
    list_two = sorted([ word_two[i] for i in range(len(word_two))])
    
    print(list_one, list_two)
    
    if len(list_one) != len(list_two):
        return None
    
    for ch in range(len(list_one)):
        if list_one[ch] == list_two[ch]:
            print("letter matched")
        else:
            print("letter does not matched")
            return False
    return True


print(isanagram(word_one, word_two))
