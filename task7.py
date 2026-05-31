"""Function with Default Argument
Question:
Create a function greet(name, message="Welcome!") that prints:
"Hello, <name>! <message>"
Call the function with and without the message argument."""
def greet(name, message = "Welcome!"):
    return f"Hello, {name}! {message}"
nam = str(input("Enter your name:"))
print(greet(nam))   

'''Function with args (Variable Number of Arguments)
Question:
Create a function total(*numbers) that takes any number of numeric arguments and returns their sum.
Example call: total(5, 10, 15) should return 30.'''

def total(*numbers):
    return sum(numbers)

result = total(5 ,10, 15)
print("The total sum of number is:", result)

'''Function with kwargs (Keyword Arguments)
Question:
Create a function display_info(**details) that prints key-value pairs like:
name: Rajesh 
age: 25  
city: Kathmandu'''

def display_info(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

display_info(name="Rajesh", age=25, city="Kathmandu")

'''Function Using Both args and a Default Argument
Question:
Create a function repeat_words(*words, times=2) that repeats each word the given number of times.
Example: repeat_words("Hi", "Bye", times=3)
Output: Hi Hi Hi Bye Bye Bye'''

def repeat_words(*words, times = 2):
    for word in words:
        print(word * times)

repeat_words("Hi", "Bye", times=3)

'''Function Using All Types of Parameters Together
Question:
Create a function user_profile(name, age=18, *hobbies, **extra_info) that:
Prints the name and age.
Prints all hobbies (if any).
Prints any additional info passed via **kwargs.'''
