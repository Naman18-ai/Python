'''every 3rd from backward and every 2nd from 3rd to 9th'''
tple=eval(input("Enter the tuple"))
t1=tple[::-3]
t2=tple[2:8:2]
print("Tuple one is:",t1)
print("Tuple two is:",t2)
