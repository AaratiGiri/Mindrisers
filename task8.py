'''.1. Encapsulation
Create a class Person with private attributes __name and __age.
Use getter and setter methods to access and modify these values.'''

class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

        def get_name(self):
            self.name = name

            def set_name(self, name):
                self.name = name    
        def get_age(self):
            self.age = age      
            def set_age(self, age):
                self.age = age
person1 = Person("Rajesh", 25)
print("Name:", person1._name)
print("Age:", person1._age)

'''2. Polymorphism
Create a function show_details(obj) that works with different classes.
Define the same method name (details()) in two or more classes.
Call show_details() with different objects to show polymorphism.'''

class Student:
    def details(self):
        return "I am a student."
class Teacher:
    def details(self):
        return "I am a teacher."    
def show_details(obj):
    print(obj.details())    
student = Student()
teacher = Teacher()
show_details(student)
show_details(teacher)


'''3. Single Inheritance
Create a base class Vehicle with a method start().
Create a derived class Bike that inherits from Vehicle.
Bike should have its own method wheels() that prints "Two wheels".'''

class Vehicle:
    def start(self):
        return "Vehicle is starting."
    
class Bike(Vehicle):
        def wheels(self):
            return "Two wheels"
        
bike = Bike()
print(bike.start())
print(bike.wheels())

'''4. Multiple Inheritance
Create class Singer with method sing() and class Dancer with method dance().
Create a class Performer that inherits from both.
Create a Performer object and call both methods.'''
class Singer:
    def sing(self):
        return "I am singing."
class Dancer:
    def dance(self):
        return "I am dancing."
class Performer(Singer, Dancer):
    def perform(self):
        return "I am performing both dance and sing."

performer = Performer()
print(performer.sing())
print(performer.dance())
print(performer.perform())

'''5. Hierarchical Inheritance
Create a base class Appliance.
Create two child classes: WashingMachine and Microwave.
WashingMachine should have a method wash(), and Microwave should have a method heat().
Create objects of both and call their respective methods.''' 
class Appliance:
    def base(self):
        return "This is an appliance base class."
class WashingMachine(Appliance):
    def wash(self):
        return "Washing machine is washing clothes."
class Microwave(Appliance):
    def heat(self):
        return "Microwave is heating food."
washing_machine = WashingMachine()
microwave = Microwave()
print(washing_machine.wash())
print(microwave.heat())

'''6. Polymorphism Using a Loop
Create classes Pen and Pencil, both with a method write().
Loop through a list of objects (Pen and Pencil) and call write() on each object.'''
class Pen:
    def write(self):
        return "I am writing with a pen."

class Pencil:
    def write(self):
        return "I am writing with a pencil."

objects = [Pen(), Pencil()]
for obj in objects:
    print(obj.write())
'''7. Use Encapsulation to Protect Age
Create a class Person with private attribute __age.
Use set_age() to set the age.
If age is less than 0, print "Invalid age".
Use get_age() to return the age.'''
class Person:
    def __init__(self):
        self.__age = 0

    def set_age(self, age):
        if age < 0:
            print("Invalid age")
        else:
            self.__age = age

    def get_age(self):
        return self.__age
    
person = Person()
person.set_age(25)
print("Age:", person.get_age())
person.set_age(-5)  # This will print "Invalid age"
'''8. Company Structure
Create class Company with method company_name().
Create class Department that inherits Company and adds department_name().
Create class Employee that inherits Department and adds employee_name().
Create an Employee object and call all the methods.'''
class Company:
    def company_name(self):
        return "Tech Solutions Inc."
class Department(Company):
    def department_name(self):
        return "Software Development"
class Employee(Department):
    def employee_name(self):
        return "John Doe"
employee = Employee()
print(employee.company_name())
print(employee.department_name())
print(employee.employee_name())

'''9. Lambda to check if a Number is Positive
Write a lambda function that takes a number and returns True if it is positive, otherwise False.
Test it with different values like 5, -3, and 0'''
is_positive = lambda x: x > 0
print(is_positive(5))   
print(is_positive(-3))  
print(is_positive(0))   
'''10. Lambda to Get First Character of a String
Create a lambda function that takes a string and returns its first character.
Example: "apple" → 'a'''
first_char = lambda s: s[0] if s else None
print(first_char("apple"))




'''11. Add 10 to All List Elements
Given a list [1, 2, 3, 4, 5],
Use map() and lambda to return a new list where 10 is added to each '''
l = [1, 2, 3, 4, 5]
print(list(map(lambda a: a + 10, l)))


'''12. Get Length of Each Word
Given a list ["apple", "banana", "kiwi"],
Use map() and lambda to return a list of lengths of each word.
→ Output: [5, 6, 4]'''
l = ["apple", "banana", "kiwi"]
print(list(map(lambda a : len(a), l)))

'''13. Filter Numbers Greater Than 50
Given a list [10, 55, 60, 23, 90],
Use filter() and lambda to return only the numbers greater than 50.'''

m = [10, 55, 60, 23, 90]
print(list(filter(lambda x: x > 50, m)))

'''14.Create a Word by Joining Letters
Given a list of letters ['P', 'Y', 'T', 'H', 'O', 'N'],
Use reduce() and lambda to join them into a single word: "PYTHON".'''
import functools
from functools import reduce
letters = ['P', 'Y', 'T', 'H', 'O', 'N']
print(reduce(lambda x, y: x + y, letters))


