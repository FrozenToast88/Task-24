# import math package
# open input text document
# readlines runs through input.txt and displays data captured
# this for loop runs through lines where maniputation of the data took place with string functions such as split
# num[-1] is capturing specific data which was not initally requested


import math
file = open("input.txt","r+")
lines = file.readlines()
print(lines)

for line in lines:
    
    store = line.split(":")
    num = store[1].split(",")
    num[-1] = num[-1][0]
print(num)
print(store)
print(fact)

# declared list 
# this for loop runs through num 
# x appended to total list
total = []
for x in num:
    total.append(int(x))
print(total)

# declared empty variable
# this for loop runs through total and adds y to amount each time y runs through total
amount = 0
for y in total:
    amount += y

# declared variables containing math functions len,min and max to obtain requested input
# open output text document write
# write data into output
count = len(total)
less = min(total)
most = max(total)
average = (amount / count)

outlook = open("output.txt","w")

outlook.write("The min of " + str(total) + " is " + str(less) + "\n")
outlook.write("The max of " + str(total) + " is " + str(most) + "\n")
outlook.write("The average of " + str(total) + " is " + str(average))

