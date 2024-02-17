num=int(input("enter the number"))
rev=0
temp=num
while num!=0:
    digit=num%10
    rev=rev*10+digit
    num//=10
print("the number is",rev)

if rev==temp:
    print(f"the number {rev} is palindrome")
else:
    print(f"the number {rev} is not palindrome")


