def remove(str):
    new=""
    for i in range(len(str)-1):
        new+=str[i]
    return new
str="Be-practicals"
result=remove(str)
print(result)