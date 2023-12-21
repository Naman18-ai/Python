num=int(input("Enter a binary number"))
decimal,counter=0,0
while num!=0:
    lsd = num%10
    decimal = decimal +  lsd* pow(2,counter)
    num =num//10
    counter+=1
print(decimal)    