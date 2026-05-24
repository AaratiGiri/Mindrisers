#Python Data Structures Assignment 
'''Section 1: Lists
1.Create a List:
Create a list containing the numbers 1 through 15. Print the list.'''
print("Creating list")
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print(l)

'''2.List of Strings:
Create a list of your five favorite fruits. Print the list.'''

print("List of fruits")
f = ['Apple', 'Orange', 'Litchi', 'Banana', 'Dragon Fruit']
print(f)

'''3.Accessing Elements:
Given the list [10, 20, 30, 40, 50], print the first and last element using positive and negative indexing.'''
list = [10, 20, 30, 40, 50]
print("First positive index element:", list[0])
print("First negative index element:",list[-5])
print("Last positive index element:",list[4])
print("Last positive index element:",list[-1])

'''4.List Length:
Create a list of any 5 items and print its length using the len() function.'''
 
q = ["Aarati", 19, 9803744141, 'Giri', 'aaratigiri95']
print("The length of 5 items is:",  len(q))


'''5.Appending Elements:
Start with an empty list and append the numbers 1, 2, and 3. Print the list.'''

w = []
w.append(1)
w.append(2)
w.append(3)
print("The list by appending in empty list is:", w)

'''6.Inserting an Element:
Given a list [1, 3, 4], insert the number 2 at the correct position so that the list becomes [1, 2, 3, 4].'''
 
e = [1, 3, 4]
e.insert(1, 2)
print(e)

'''7.Removing an Element:
Remove the number 3 from the list [1, 2, 3, 4, 5] using a list method and print the new list.
'''
r = [1, 2, 3, 4, 5]
print("Original list before removing 3:", r)
r.remove(3)
print("After removing 3", r)

'''8.Popping an Element:
Given the list [10, 20, 30, 40], pop the last element and print the element and the updated list.'''

t = [10, 20, 30, 40]
print("Before poping last element:", t)
t.pop(-1)
print("After poping last element:", t)

'''9.Slicing a List:
Given the list [0, 1, 2, 3, 4, 5], print a slice that contains the elements from index 2 to 4.'''

y = [0, 1, 2, 3, 4, 5]
print(y[2:4])
''''10.List Concatenation:
Concatenate two lists, e.g., [1, 2, 3] and [4, 5, 6], and print the resulting list.'''

u = [1, 2, 3]
i = [4, 5, 6]
print(u + i)

'''11.Repeating a List:
Create a list [1, 2] and print the list repeated three times.'''
o = [1, 2]
print(o * 3)

''' 12.Copying a List:
Create a copy of a given list and print both the original and the copy.'''

p = ['str', 2.33, 90, 'char', 78902]
p_copy = p.copy()
print("Original list:", p)
print("copied list:", p_copy)
'''Clearing a List:
Given any list, use a method to clear all its elements and then print the empty list'''
p.clear()
print("The empty list:", p)

print("---------------------------------------")
# Section 2: Tuples
# 1.Create a Tuple:
# Create a tuple containing the numbers 1, 2, and 3. Print the tuple.

tup = (1, 2, 3)
print(tup)

# 2.Tuple of Strings:
# Create a tuple of three different color names and print it.

color = ('red', 'yellow', 'blue', 'white', 'black')
print(color)

# Accessing Tuple Elements:
# Given the tuple (10, 20, 30, 40), print the second element

tupl = (10, 20, 30, 40)
print(tupl[1])

'''4.Tuple Slicing:
Using the tuple (0, 1, 2, 3, 4), print a slice that contains elements from index 1 to 3.'''

f = (0, 1, 2, 3, 4)
print(f[1:4])

'''Concatenating Tuples:
Concatenate two tuples, e.g., (1, 2) and (3, 4), and print the result'''
t1 = (1, 2)
t2 = (3, 4)
result = t1 + t2
print(result)

'''6.Tuple Unpacking:
Store the tuple ("Alice", 25, "New York") into three variables and print them.'''

p = ('Alice', 25, 'New York')
name, age, city = p 
print(name)
print(age)
print(city)

'''7.Convert List to Tuple:
Convert the list [1, 2, 3, 4] into a tuple and print the tuple.'''
lst = [1, 2, 3, 4]
t = tuple(lst)
print(t)

'''8.Counting Occurrences:
Given the tuple (1, 2, 2, 3, 2), count how many times the number 2 appears.'''

k = (1, 2, 2, 3, 2)
l = k.count(2)
print("The numer of times 2 occurs in tuple is:", l)

'''
9.Finding an Index:
In the tuple (10, 20, 30, 40), find the index of the element 30 and print it.'''

m = (10, 20, 30, 40)
n = m.index(30)
print("The index of 30 in m is:", n)