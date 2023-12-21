original_string=input("Enter the first string")
new_string=input("Enter the new string")

if new_string in original_string or original_string in new_string:
    print("The strings are anagram of each other")
else:
    print("They are not anagrams of each other")    
