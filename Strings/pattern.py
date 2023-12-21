str=input("enter a string!")
i=0
length=len(str)
for a in range(-1,(-length-1),-1):
    print(str[i],'\t',str[a])
    i+=1