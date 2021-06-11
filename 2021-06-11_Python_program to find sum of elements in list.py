#program to find sum of elements in lisT
"Computer Programming Tutor, Jun11,2021"

total = 0

# Creating A List
List1 = [70,70,70,50,50]

#Iterate each element in List and ADD them in Variable Total

for k in range(0,len(List1)):
    total = total +List1[k]

#Printing Total Value

print("Sum of all Elements in given list:",total)
