'''write a program that inputs a lists, replicates it twice and then prints the sorted list in 
ascending and descending orders'''

lists=eval(input("Enter a list"))
print("The list is:",lists)
lists=lists*2
lists.sort()
print(lists)
lists.sort(reverse=True)
print(lists)