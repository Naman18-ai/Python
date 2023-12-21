integer=int(input("Enter a number"))
counter=1

for i in range(2,integer):
    if integer%i==0:
        counter+=1
if counter >0:
    print("It is  not a prime")       
else:
    print("It is prime")    
    
    
