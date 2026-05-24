'''Even or Odd Checker
Task: Write a program that prompts the user for an integer.
oUse if/else to check whether the number is even or odd.
oPrint "Even" or "Odd" accordingly.'''
num = int(input("Enter a number:"))
if num % 2 == 0:
    print("The given number is even!!!.")
else:
    print("The given number is odd!!!")

'''Positive, Negative, or Zero
Task: Write a program that prompts the user for a number.
oUse if/elif/else to determine if the number is positive, negative, or zero.
oPrint a message such as "The number is positive.".'''
n = int(input("Enter a number:"))
if n == 0 :
    print("The nnumber is zero.")
elif n > 0:
    print("The number is positive.")
else:
    print("The number is negative. ")


'''Grade Categorizer
Task: Prompt the user for a number between 0 and 100 (the score).
oUse if/elif/else to categorize the score:
90–100: "Grade A"
80–89: "Grade B"
70–79: "Grade C"
< 70: "Fail"'''

score = int(input("Enter your exact score in exam:"))
if score >= 90 and score <= 100:
    print("Grade A")
elif score >= 80 and score <= 89:
    print("grade B")
elif score >= 70 and score <= 79:
    print("grade C")
elif score < 70:
    print("Fail")

'''Multiples of 3 and 5
Task: Prompt the user for a single integer n.
oUse a for loop to iterate from 1 up to n (inclusive).
oFor each value i, print:
"Multiple of both" if i is divisible by 3 and 5.
"Multiple of 3" if i is divisible by 3 but not 5.
"Multiple of 5" if i is divisible by 5 but not 3.
The number i itself otherwise.'''

n = int(input("Enter a number:"))
for i in range(1, n + 1):
    if i % 3 == 0 and i % 5 == 0:
        print('Multiple of both')
    elif i % 3 == 0 or i % 5 ==0:
        if i % 3 == 0:
            print('Multiple of 3')
        else:
            print('Multiple of 5')
    else:
        print(i)

        '''Simple Password Check
Task: Prompt the user for a password (e.g., "secret").
oUse if to check if the user’s input matches the correct password.
oIf correct, print "Access granted", otherwise print "Access denied".'''

pw = input("Enter the passwprd:")
if pw == "secret":
    print("Acess Granted!!!")
else:
    print("Access Denied!!!")

'''Count Vowels in a String
Task: Ask the user for a string.
oUse a for loop to iterate over each character.
oUse if conditions to check if it’s a vowel ("a", "e", "i", "o", "u").
oCount the total number of vowels and print the result.'''

s = input("Enter a string:")
count = 0
for char in s:
    if char in "aeiouAEIOU":
        count += 1
print("The total number of vowels in the string is:", count)

'''Smallest of Three Numbers
Task: Prompt the user for three different numbers.
oUse if/elif/else to find and print which one is smallest.'''

x = int(input("Enter the first number:"))
y = int(input("Enter the second number:"))
z = int(input("Enter the third number:"))
if x < y and x < z:
    print("The smallest number is x:", x)

elif y < x and z < x:
    print('The smallest number is:', y)
else:
    print('The smallest number is:', z)

'''Simple Menu Selection
Task: Prompt the user to choose an option (e.g., 1 for "Start", 2 for "Settings", 3 for "Exit").
oUse if/elif/else to print a response based on which option is chosen.
oExample:
If user enters 1: print "Game starting..."
If user enters 2: print "Opening settings..."
If user enters 3 or any other: print "Exiting..."'''
print("Here are the choinces:")

print('1 for Start')
print('2 for settings')
print("3 for exiting")
choice = int(input('Enter a option betweeen 1, 2, and 3: '))
if choice == 1:
    print("Game starting---------")
elif choice == 2:
    print("Opening settings....")
elif choice == 3:
    print("Exiting.....")
else:
    print("Invalid number!!!")