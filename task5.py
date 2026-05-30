# Iterate Through a Tuple and Print Types
# Task: Create a tuple with at least 5 different types of elements (int, float, string, bool, and complex).
# Use a for loop to iterate over the tuple and print each element along with its data type.

t = (32, 34.23, 'Hello', False, 3 + 4j)
for element in t:
    print(f'Element: {element}, Type: {type(element)}')

#     Print All Items from a List with a Custom Message
# Task: Create a list of 4 different city names.
# Use a for loop to print each city name followed by the phrase "is a great place".

cities = ("Kathmandu", "Pokahara", "Biratnagar", "Lalitpur")
for city in cities:
       print(f"{city} is a greate place:")


       '''Print Each Character of a String with Its Index
Task: Ask the user to enter a word.
Use a for loop and enumeratecl() to print each character of the string along with its index.'''
word = str(input("Enter a word:"))
for w in word:
    print(f"Index: {word.index(w)}, Character: {w}")

    """Sum of Elements in a List
Task: Create a list of integers.
Use a for loop to calculate the sum of all the elements and print the total"""

integers = [3, 42, 52, 2, 54, 65, 234, 65, 5]
sum = 0
for i in integers:
     sum += i
     print(sum)
print("The total sum of list of integers is ", sum)

'''Count Booleans in a Tuple
Task: Create a tuple containing different data types, including multiple True and False values.
Use a for loop to count how many True values are present and print the count.'''
b = ( 2, 43, 54, 2, True, False, True, "True", "False", False, False, True)
countT = 0
countF = 0
for i in b:
    if i == True:
          countT += i
    elif i == False:
          countF += i
print("The total number of True in tuple is", countT)
print("The total number of False in tuple is", countF)


'''Check and Print Data Types from a List
Task: Create a list with at least 6 elements of different types (int, float, str, bool, etc.).
Use a for loop to iterate through the list and print the data type of each element.'''
elements = (12, 12.4, 'Hello', True, 3 + 4j, 89)
for e in elements:
     print(f"The data type if {e} is {type(e)}")

     '''Check for Vowels in a String
Task: Ask the user for a word.
Use a for loop to check each character and print a message if it’s a vowel (a, e, i, o, u).'''
user = str(input("Enter a word:"))
for u in user:
     if u in "aeiouAEIOU":
          print(f"{u} is a vowel")

'''Print Square of Numbers from a Tuple
Task: Create a tuple of numbers from 1 to 5.
Use a for loop to iterate through the tuple and print the square of each number.'''
h = (1, 2, 3, 4, 5)
for i in h:
    print('The square of number is', i*i)


    '''Print Elements of a List in Uppercase
Task: Create a list of 5 small letter containing words.
Use a for loop to iterate over the list and print each word in lowercase.'''
list = ['Human', 'life', 'is', 'absolutely', 'great']
for l in list:
        print(l.upper())

        '''Count Numbers Greater Than 10 in a List
Task: Create a list of integers.
Use a for loop to count how many numbers in the list are greater than 10.
Print the final count.'''

list = [8, 43, 65, 86, 23,5, 3, 5, 76, 3, 5, 67]
count = 0
for i in list:
    if i > 10:
        count += 1
    
    

print("The number of elements greater than 10 is:", count)

    