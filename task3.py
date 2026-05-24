'''Integer & Float Mix
Create an integer a and a float b.
Perform addition, subtraction, multiplication, and division on them.
Print the results and observe the type of each result with type().'''

a = 9
b = 4.52
sum = a + b
print("The sum is:",  sum)
print("The type of sum result is:", type(sum))
sub = a - b
print("The difference between a and b is:", sub)
print("The type of difference result is ", type(sub))
mul = a * b
print("The product of a and b is:", mul)
print("The type of product result is:", type(mul))
div = a / b
print("The division of a and b is", a / b)
print("The type of product result is:", type(div))

'''Large Integers & Type
Assign a very large integer to a variable (e.g., in the billions).
Print it and confirm its type is still int in Python or not.'''
no = 9567855678987659087654324567897654324567897654324567898765432456789765449876543567897654324567897654356789765435678765435678976543324567897654345678976543567865987654356897654356789999999765436787654678976546897654567897654567765435687976564542345234567890987650987678976578976587867897
print(f"The type of {no} is:", type(no))

'''Complex Number Basics
Create a complex number z = 3 + 4j.
Print its real part, imaginary part, and confirm its type is complex.
Perform a basic arithmetic operation with another complex number (e.g., (3 + 4j) + (1 + 2j)).'''
z = 3 + 4j
print(f"The real part of {z} is: ", z.real)
print(f"The imaginary part of {z} is:", z.imag)
print(f"The type of {z} is:", type(z))

w = (1 + 2j)
add = z + w
print(f"The sum of {z} and {w} is:", add)

'''Boolean from Comparisons
Create two variables, m = 10 and n = 15.
Define status = (m > n) and print status.
Confirm type(status) is bool.
Assign status = (m != n) and print again'''
m = 10
n = 15
status = (m > n)
print(status)
print(type(status))
status = (m != n)
print(status)

'''String Creation & Indexing
Create a string text = "HelloWorld".
Print the first and last characters using positive and negative indexing.
Comment on the total length of the string.'''

text = "HelloWorld"
print(text[0])
print(text[-10])
print(text[9])
print(text[-1])
print("The length of text is", len(text))

''' String Slicing
With lang = "PythonProgramming", print the substring from index 2 to 8.
Print the substring from the start up to index 5.
Print the entire string in reverse using slicing.'''
lang = "PythonProgramming"
print(lang[2:9])
print(lang[:6])
print(lang[::-1])

'''String Methods
Let phrase = " Hello, Python World! ".
Demonstrate strip(), upper(), and replace() on this string.
Print the results and comment on immutability of strings in Python.'''
phrase = " Hello, Python World!"
p_stip = phrase.strip()
print(p_stip) 
print(phrase.upper())
print(phrase.replace('Hello', 'Hey!!!'))

'''String Formatting
Create two variables: name = "Rajesh" and score = 95.
Print: "Alice scored 95 points." using two methods (concatenation and an f-string or str.format()).'''

name = "Alice"
score = 95
print(f"{name} scored {score} points")

'''Boolean Operations in Expressions
Write a small expression using and, or, and not with boolean values.
Example: result = not(True and False) or (5 > 3).
Print result and explain how Python evaluated the expression.'''
a = 5
b = 9
print("Here the value of a and b are not equal to declared value, which results:", a == 9 and b == 5)
print( a < 5 or b == 9)
print(not( a != b))

'''List Creation & Access
Create a list of 5 different integers.
Print the first item, middle item, and last item using indexing.'''
list = [23, 67, 76, 89, 68]
print("The first interger is:", list[0])
print("The middle interger is:", list[2])
print("The last interger is:", list[-1])

'''List Insertion & Deletion
Start with a list nums = [10, 20, 30, 40].
Insert 25 at index 2.
Remove the last element.
Print the updated list.'''
nums = [10, 20, 30, 40]
print("the original list is:", nums)
nums.insert(2, 25)

print("List after inserting 25:", nums)
nums.remove(40)
print("List after removing last element:", nums)


'''List Slicing
Given letters = ["a", "b", "c", "d", "e"], print the slice that contains only ["b", "c", "d"].
Print the slice that omits the first and the last element.'''
letters = ["a", "b", "c", "d", "e"]
print('the slice that contains only ["b", "c", "d"]:', letters[1:-1])
print("the slice that omits the first and the last element:", letters[1:-1])

'''Sorting & Reversing
Create a list of random integers.
Sort the list in ascending order and print it.
Reverse the sorted list and print again.'''
ran =  [1, 4, 7, 234, 87, 13, 76, 23, 7, 24, 76, 34, 4, 53, 34, 64, 24,]
print("Ascending order: ", sorted(ran))
print("Descending order:", sorted(ran, reverse=True))


'''Combining Lists
Let list1 = [1, 2, 3] and list2 = [4, 5, 6].
Combine them into a single list and print.
Demonstrate two ways: using + and using .extend()'''

list1 = [1, 2, 3]
list2 = [4, 5, 6]
single_list = list1 + list2
print("The combine list is:", single_list)
list1.extend(list2)
print("The extended list is:", list1)

'''Aggregating List Values
Create a list of floats, e.g., [2.5, 3.6, 1.2, 5.0].
Print the sum, minimum, and maximum of that list using built-in functions.'''
list_floats = [2.5, 3.6, 1.2, 5.0]
print("The sum of list is:", sum(list_floats))
print("The minimum of list is:", min(list_floats))
print("The maximum of list is:", max(list_floats))

'''Tuple Creation
Create a tuple t = (10, 20, "Hello", True).
Print the tuple and confirm its type with type(t)'''
t = (10, 20, "Hello", True)
print(t)
print(type(t))

'''Tuple Indexing & Slicing
Print the first two elements of t using slicing.
Print the last element of t using negative indexing.'''

print(t[0:2])
print(t[-1])

'''Tuple Unpacking
Suppose t2 = ("Tom", 25, "Engineer").
Unpack it into three separate variables: name, age, profession.
Print these variables individually.'''
t2 = ("Tom", 25, "Engineer")
name, age, profession = t2
print(name)
print(age)
print(profession)

'''Attempt Tuple Mutation
Try to change an element of t (t[0] = 999) and observe the error.
In comments, explain why the error occurs.'''
# t[0] = 999 #This line will give an error because tuples are immutable, which means once a tuple is created, its elements cannot be changed or modified. Therefore, trying to assign a new value to an existing index in the tuple will result in a TypeError.

'''Set Creation & Membership
Create a set my_set = {1, 3, 5, 7}.
Check if 5 is in my_set.
Check if 2 is not in my_set.'''
my_set = {1, 3, 5, 7}
print(5 in my_set) 

'''Add & Remove Elements
Add 9 to my_set.
Remove 3 from my_set.
Print the updated set.'''
my_set.add(9)
print("Set after adding 9 is:", my_set)
my_set.remove(3)
print("After removing 3 is:", my_set)

'''Set Operations
Create two sets: setA = {1, 2, 3} and setB = {3, 4, 5}.
Print the union, intersection, and difference (setA - setB).'''
setA = {1, 2, 3}
setB = {3, 4, 5}
print(setA.union(setB))
print(setA.intersection(setB))
print(setA - setB)

'''Check Unique Values
Define a list vals = [1, 2, 2, 3, 3, 3, 4].
Convert it to a set.
Print both the list and the set to show how duplicates are removed.'''
vals = [1, 2, 2, 3, 3, 3, 4]
print(set(vals))
print(vals)

'''Frozenset Creation
Create a frozenset from a list [2, 4, 4, 6].
Print it and observe whether duplicates are preserved.'''
frozen = frozenset([2, 4, 4, 6])
print(frozen) #frozenset does not preserve duplicates, it will only contain unique elements

'''Operator Precedence
Define a = 4, b = 2, c = 5.
Print the result of a + b * c vs. (a + b) * c.
Explain in comments how the result differs.'''
a = 4
b = 2 
c = 5
print(a + b * c)
print((a + b) * c) #In the first expression, multiplication has higher precedence than addition, so b * c is evaluated first, resulting in 10, and then a is added to it, giving 14. In the second expression, the parentheses change the order of operations, so a + b is evaluated first, resulting in 6, and then that result is multiplied by c, giving 30.

'''Modulo & Floor Division
Let x = 17 and y = 4.
Print x % y and x // y.
Explain the difference between these two operators in comments.'''
x = 17
y = 4
print(x%y)
print(x//y) #The modulo operator (%) gives the remainder of the division of x by y, which is 1 in this case. The floor division operator (//) gives the quotient of the division of x by y, rounded down to the nearest whole number, which is 4 in this case.

'''
Power Operator
Print the result of 2 ** 3.
Write a line to calculate 3 ** 4.
Print the addition of both.'''
print(2**3)
print("we are calculating 3 ** 4")
print( 2**3 + 3 **4 )

'''String Comparison
Compare "apple" and "banana" with <, >, and ==.
Print the results'''

print('apple' > "banana")
print('apple' < "banana")
print('apple' == "banana") 

'''Mixed Type Comparison
Compare 5 and 5.0 with ==.
Compare 5 and 5.0 with is.
Discuss the results in comment.'''
print(5 == 5.0) #True
print(5 is 5.0) #

'''Chain Comparisons
Evaluate the expression 2 < 3 < 5.
Print the result and explain how Python handles chained comparisons.'''
print("Example of chain comaprisons:", 2 < 3 < 5)

'''Logical and
Define p = True and q = False.
Print p and q.
Demonstrate a real-world example: (age > 18) and (has_ID == True).''' ###

p =True
q = False
print(p)
print(q)

'''Logical or
Using the same p and q, print p or q'''
print(p or q)

'''Logical not
Let r = (10 > 5).
Print r, then print not r.'''
r = (10 > 5)
print(r)
print("Logical not example:", not r)

'''Using len()
Create a list with 7 elements.
Use len() to get the total count.
Print the result.'''
l = [ 2, 34, 3, 'sd', 'wer', 'cawpo', 'we']
print("Length:", len(l))

'''Using type()
For each of the following: 10, 10.5, "ten", True, 3+2j, print type(...).
Summarize in comments the data types you observed.'''
print("Type of 10 is:", type(10))
print("Type of 10.5 is:", type(10.5))
print("Type of True is:", type(True))
print("Type of 3 + 2j is:", type(3 + 2j))

'''Using abs()
Print abs(10), abs(-10), and abs(-3.5).
Explain what abs() does in comments.'''
print(abs(10))
print(abs(-10))
print(abs(-3.5))  #it  changes negative number into positive

'''Using round()
Demonstrate round(3.14159, 2).
Show how round(2.5) behaves in Python.'''

print(round(3.14159, 2)) # round has 2 position where first position given float or double value then last position estimate how many number should written at end of float or double

'''Using sum(), max(), min()
Create a list of numeric values.
Print sum(), max(), and min() of that list.'''
n1 = [ 3, 34, 52, 34, 34, 43]
print("The sum of list is:", sum(n1))
print("The maximum number  of list is:", max(n1))
print("The minimum number of list is:", min(n1))


'''
Using sorted()
Create a list or tuple vals = (3, 1, 4, 2).
Use sorted(vals) and print the result.
Show that vals itself is unchanged.'''
vals = (3, 1, 4, 2)
print(sorted(vals))
print(vals) #it remains same as original

'''Using any() / all()
Create a list of booleans, for example [True, False, True].
Print any() on the list, then all() on the list.
Show the difference in how they evaluate.'''
b = [True, False, True]
print(any(b))
print(all(b))


'''Storing Booleans from Comparisons
Compare two values in separate expressions, e.g., a = (10 > 3), b = (5 == 5).
Combine these booleans with and or or.
Print the final result.'''
a = (10 > 3)
b = (5 ==5 )
print("Comparing a and b by boolean:", a and b)
print("Comparing a and b by boolean:", a or b)

'''Multiline String & Counting
Create a multiline string describing your favorite hobby.
Use the string method .count(substring) to count how many times the letter "a" appears (case-insensitive).
Print the count and explain any steps taken to handle case sensitivity.'''
hobby = """My favorite hobby is painting. I love to create art and express myself through colors. Painting allows me to relax and unwind after a long day."""
count_a = hobby.lower().count('a')
print("The number of times 'a' appears in the hobby description is:", count_a)


'''Advanced String Slicing
Take the string "ABCDEFGHIJ" and slice every second character, resulting in "ACEGI".
Print the sliced string.
Also slice in reverse step'''
h = "ABCDEFGHIJ"
print(h[0:-1:2])
print(h[::-1])

'''Casefold vs. Lower
Create two strings, "Case" and "case".
Compare them with the regular == operator directly.
Compare them again after applying .casefold().
Print results and comment on how .casefold() differs from .lower() in edge cases.'''
c1 = 'Case'
c2 = 'case'
print(c1 == c2)
print(c1.casefold())
print(c2.casefold())  

'''Formatted Printing
Define name = "Ramesh", product = "Notebook", quantity = 2, and price = 12.50.
Use an f-string (or str.format()) to print:
"Ramesh purchased 2 Notebook for a total of $25.0."'''
name = 'Ramesh'
product = "Notebook"
quantity = 2
price = 12.50
print(f"{name} purchased {quantity} {product} for a total of ${price}.")

'''Type Conversion Chain
Ask a user for a string that represents a number, e.g., "0".
Convert it to a float, then to a bool, and print the intermediate and final results.'''

number = str(input("Enter a string number:"))
print(number)
print(float(number))
print(bool(number))

'''String List Sorting
Given fruits = ["apple", "banana", "cherry"], sort them in descending alphabetical order.
Print the sorted list, then use the .reverse() method to flip it. Compare the two results.'''
fruits = ["apple", "banana", "cherry"]
print("sorted list is:", sorted(fruits))
fruits.sort(reverse=True)
print("Descending order is:", fruits)

'''Insert Using Slicing
Start with a list [2, 5, 7, 1, 9].
Insert the value 4 right after the 2 using slicing (not insert() or append()).
Print the modified list.'''
lst = [2, 5, 7, 1, 9]
lst[1:1] = [4]
print("Modified list is:", lst)

'''Indexing Within a Mixed List
Create a list info = ["John", 28, True, 4500.75].
Print only "John" and 4500.75 using their indices.'''
info = ["John", 28, True, 4500.75]
print(info[0])
print(info[-1])

'''Tuple Concatenation & Replication
Create two tuples (1, 2) and (3, 4).
Concatenate them into (1, 2, 3, 4).
Replicate (1, 2) 3 times to get (1, 2, 1, 2, 1, 2).'''
m1 = (1, 2)
m2 = (3, 4)
m3 = m1 + m2
print(m3)
print(m1 * 3)

'''Single-Element Tuple
Demonstrate that (42,) is a tuple whereas (42) is just an integer.'''
o = (42,)
print(type(o)) #tuple
p = (42)
print(type(p)) #integer

'''Intersection & Union
Let setA = {1, 2, 3, 4} and setB = {1,2,3}.
Print their intersection using setA & setB.
Print their union using setA | setB.'''
setA = {1, 2, 3, 4} 
setB = {1,2,3}
print(setA.intersection(setB))
print(setA & setB)
print(setA | setB)

'''Subset and Superset
Check if setB is a subset of setA using setB.issubset(setA).
Check if setA is a superset of setB using setA.issuperset(setB).
Print the results.'''
print(setB.issubset(setA)) #True
print(setA.issuperset(setB)) #True
















