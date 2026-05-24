#Basic Arithmetic and Type Identification
#Create three variables: one integer, one float, and one complex number.
#Print each variable and use the type() function to confirm their data types.
a = 10
b = 3.3
c = 4 + 8j
print("The data type of a is:", type(a))
print("The data type of b is:", type(b))
print("The data type of c is:", type(c))
print("-----------------------------------------------------------------------------")
#Arithmetic with Mixed Types
#Create one int variable (a) and one float variable (b).
#Print the sum, difference, product, and quotient of a and b.
#Print the type() of each result (notice how types may change).

a = 3
b = 6.67
print(f"The sum of {a} and {b} is:", a + b)
print(f"The difference between {a} and {b} is:", a - b)
print(f"The product of {a} and {b} is:", a * b)
print(f"The quotient of {a} and {b} is:", a / b)
print("-----------------------------------------------------------------------------")

#Comparison Operators
#Let x = 10 and y = 7.
#Print the results of x > y, x < y, x == y, and x != y.
#After observing the output, explain why each result is True or False in comments.

x = 10
y = 7
print(x > y)  #Here x is greater than y. Therefore, when the condition satisfy with variables then its result is True. It follows Booleon operation
print(x < y)   #As mention before, y is less than x which doesnt satisfy with condition, and result is  False
print( x == y) #Again, == operator shoes equal symbol. here x is 10 and y is 7 which is not equal. Ultimately is gives False result
print( x != y)  #The use of != is to display not equal. As mention, x is greater than y. so x is not equal to y which display result True, satisy the operand
print("-------------------------------------------------------------------------------------------------------------------------------")

#Boolean Variables
#Define a variable status = True.
#Print the value of status and confirm it is a boolean using type(status).
#Reassign status to False and confirm its type again.

status = True
print(status)
print(type(status))
status = False
print(status)
print(type(status))
print("(❁´◡`❁)(❁´◡`❁)(❁´◡`❁)(❁´◡`❁)(❁´◡`❁)(❁´◡`❁)(❁´◡`❁)(❁´◡`❁)(❁´◡`❁)")

'''String Creation and Length
Create a string variable, for example text = "Hello World".
Use len(text) to print its length.
Use type(text) to verify it is a string'''

text = "Hello World"
print(len(text))
print(type(text))
print("-----------------------------------------")

'''String Indexing
With the string s = "Python", print each character. Then print just the first and last characters using negative indexing.'''

s = "Python"
for i in range(len(s)):
    print(s[i])
print(s[0])  #First character
print(s[-1])  #Last character
print("-------------------------------------------")

'''String Slicing
Let lang = "Programming".
Print the substring from index 0 to index 4.
Print the substring from index 3 to the end.
Print the substring that omits the first 2 and last 2 characters'''

lang = "Programming"
print(lang[0:5])
print(lang[3:])
print(lang[2:-2])
print("-------------------------------------------")

'''Exploring len() on Slices
Continue using lang = "Programming".
Slice lang to get "Program" and store it in a variable part1.
Print len(part1) and comment how it differs from len(lang).
'''

lang = "Programming"
part1 = lang[0:7]
print(len(part1))  #The length of part1 is 7 beacuse it has 7 character
print(len(lang)) #Here  the length of lang is 11 because it consists full string whereas part1 is substring of lang  which only contains 7 character.
print('----------------------------------------')

'''String Methods – Case Conversion
Let phrase = "Hello, Python!".
Print phrase.upper() and phrase.lower().
Print the original phrase to show it remains unchanged (strings are immutable).'''
 
phrase = "Hello, Python!"
print(phrase.upper())
print(phrase.lower())
print(phrase) #Eventhough we change string phrase into upper and lower case, it remains in origiaal phase in the end. Hence strings are immubatble
print("---------------------------------------")

"""
Combining Strings
Create two strings, str1 = "Data" and str2 = "Science".
Combine them into a single string with a space in between and print it.
Print the length of the combined string."""
str1 = "Data"
str2 = "Science"
s = str1  + " " +  str2
print(s)
print(len(s))
print("-----------------------------------------------")

'''
In-Place vs. Reassignment with String Methods
Let word = "example".
Call word.upper() but do not store it, then print word.
Now set word = word.upper(), then print word.
Comment on why the second print is different from the first.'''

word = "example"
word.upper()
print(word)
word = word.upper()
print(word)
print("--------------------------------")

'''Arithmetic Operator Precedence
Define a = 5, b = 3, c = 2.
Print the result of the expression a + b * c.
Print the result of (a + b) * c.
In comments, explain how operator precedence affects the outcome'''

a = 5
b = 3
c = 2
print(a + b *c)
print((a + b) * c)
print("----------------------------------------------------")

'''String Index Out of Range
Let text = "Hello".
Attempt to access an index that doesn’t exist, like text[10].
Observe the error message (IndexError) and explain why it happens in comments.'''

text = "Hello"
#print(text[10])
#IndexError it does not print out of index
print("---------------------------------")

'''
Equality vs. Identity Check (Conceptual Explanation)
Create two variables with the same string value, s1 = "test" and s2 = "test".
Use the == operator to compare them, then use the is operator.'''

s1 = "text"
s2 = "text"
print(s1 == s2) # == it comaprison s1 and s2 operator. it cheecks if both varible have  same character or length. then it satisfy the == operator which gives True as result
print(s1 is s2) # is is the condition which executes the  True result when both condition or variables are match otherwise it executes false
print("------------------------------")

'''Creating and Checking a Complex Number
Define z = 3 + 4j.
Print the real part (z.real) and the imaginary part (z.imag).
Confirm that its type is complex using type(z).'''
z = 3 + 4j
print(z.real)
print(z.imag)
print(type(z))
print("-----------------------------------------------------------")

'''Comparisons with Floats
Let f1 = 0.1 + 0.2 and f2 = 0.3.
Print f1 == f2.
Print the actual values of f1 and f2 to explain any difference in the comparison outcome (floating-point precision).'''
f1 = 0.1 + 0.2
f2 = 0.3
print(f1 == f2)
print(f1)
print(f2)