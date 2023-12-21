import math
list=eval(input("Enter tehe list you want!!"))
sum = 0
mean = 0
lnth=len(list)
for i in range(lnth):
    sum+=list[i]
mean=int(sum/lnth)
print("The mean is",mean)
    