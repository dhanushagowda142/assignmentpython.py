my_list = [10,20,30,40,50,60,70,80,90]
print(my_list[0::2])

my_list = [10,20,30,40,50,60,70,80,90]
add_index=[]
for i in range(len(my_list)):
    if i%2!=0:
        add_index.append(my_list[i])
print(add_index)

