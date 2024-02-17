def count(sequence):
    char_count={}
    for char in sequence:
        if char in char_count:
            char_count[char]+=1
        else:
            char_count[char]=1
    return char_count
user=input("enter the characters")
result=count(user)
print(result)