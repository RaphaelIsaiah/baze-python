# ----------------- RAPHAEL SAVIOUR ISAIAH ----------------------

# ----------------- IDEAS/24/50355 ----------------------

# ----------------- PYTHON EXERCISES FROM W3SCHOOLS (95 QUESTIONS IN TOTAL) -----------------


# --------- PYTHON SYNTAX  EXERCISES --------

# Question 1: Insert the missing part of the code below to output "Hello World".
print("Hello World")

# Question 2: Complete the code block, print "YES" if 5 is larger than 2.
if 5 > 2:
    print("YES")


# --------- PYTHON COMMENTS EXERCISES --------

# Question 1: Comments in Python are written with a special character, which one?
# This is a comment

# Question 2: Use a multiline string to make the a multiline comment:
"""
This is a comment
written in
more than just one line
"""


# --------- PYTHON VARIABLES EXERCISES --------

# Question 1: Create a variable named carname and assign the value Volvo to itCreate a variable named carname and assign the value Volvo to it.
carname = "Volvo"

# Question 2: Create a variable named x and assign the value 50 to it.
x = 50

# Question 3: Display the sum of 5 + 10, using two variables: x and y.
x = 5
y = 10
print(x + y)

# Question 4: Create a variable called z, assign x + y to it, and display the result.
x = 5
y = 10
z = x + y
print(z)

# Question 5: Insert the correct syntax to assign values to multiple variables in one line:
x, y, z = "Orange", "Banana", "Cherry"

# Question 6: Insert the correct syntax to assign the same value to all three variables in one code line.
x = y = z = "Orange"


# Question 7: Insert the correct keyword to make the variable x belong to the global scope.
def myfunc():
    global x
    x = "fantastic"


# ---------- PYTHON DATA TYPES EXERCISES -----------

# Question 1: The following code example would print the data type of x, what data type would that be?
x = 5
print(type(x))
# Answer: int

# Question 2: The following code example would print the data type of x, what data type would that be?
x = "Hello World"
print(type(x))
# Answer: str

# Question 3: The following code example would print the data type of x, what data type would that be?
x = 20.5
print(type(x))
# Answer: float

# Question 4: The following code example would print the data type of x, what data type would that be?
x = ["apple", "banana", "cherry"]
print(type(x))
# Answer: list

# Question 5: The following code example would print the data type of x, what data type would that be?
x = ("apple", "banana", "cherry")
print(type(x))
# Answer: tuple

# Question 6: The following code example would print the data type of x, what data type would that be?
x = {"name": "John", "age": 36}
print(type(x))
# Answer: dict

# Question 7: The following code example would print the data type of x, what data type would that be?
x = True
print(type(x))
# Answer: bool


# ------------- PYTHON NUMBERS EXERCISES ------------

# Question 1: Insert the correct syntax to convert x into a floating point number.
x = 5
x = float(x)

# Question 2: Insert the correct syntax to convert x into a integer.
x = 5.5
x = int(x)

# Question 3: Insert the correct syntax to convert x into a complex number.
x = 5
x = complex(x)


# ------------- PYTHON STRINGS EXERCISES -------------

# Question 1: Use the len function to print the length of the string.
x = "Hello World"
print(len(x))

# Question 2: Get the first character of the string txt.
txt = "Hello World"
x = txt[0]

# Question 3: Get the characters from index 2 to index 4 (llo).
txt = "Hello World"
x = txt[2:5]

# Question 4: Return the string without any whitespace at the beginning or the end.
txt = " Hello World "
x = txt.strip()

# Question 5: Convert the value of txt to upper case.
txt = "Hello World"
txt = txt.upper()

# Question 6: Convert the value of txt to lower case.
txt = "Hello World"
txt = txt.lower()

# Question 7: Replace the character H with a J.
txt = "Hello World"
txt = txt.replace("H", "J")

# Question 8: Insert the correct syntax to add a placeholder for the age parameter.
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))


# ------------ PYTHON BOOLEANS EXERCISES --------------

# Question 1: The statement below would print a Boolean value, which one?
print(10 > 9)
# Answer: True

# Question 2: The statement below would print a Boolean value, which one?
print(10 == 9)
# Answer: False

# Question 3: The statement below would print a Boolean value, which one?
print(10 < 9)
# Answer: False

# Question 4: The statement below would print a Boolean value, which one?
print(bool("abc"))
# Answer: True

# Question 5: The statement below would print a Boolean value, which one?
print(bool(0))


# ---------------- PYTHON OPERATORS EXERCISES ----------------

# Question 1: Multiply 10 with 5, and print the result.
print(10 * 5)

# Question 2: Divide 10 by 2, and print the result.
print(10 / 2)

# Question 3: Use the correct membership operator to check if "apple" is present in the fruits object.
fruits = ["apple", "banana"]
if "apple" in fruits:
    print("Yes, apple is a fruit!")

# Question 4: Use the correct comparison operator to check if 5 is not equal to 10.
if 5 != 10:
    print("5 and 10 is not equal")

# Question 5: Use the correct logical operator to check if at least one of two statements is True.
if 5 == 10 or 4 == 4:
    print("At least one of the statements is true")


# ------------------- PYTHON LISTS EXERCISES -----------------

# Question 1: Print the second item in the fruits list.
fruits = ["apple", "banana", "cherry"]
print(fruits[1])

# Question 2: Change the value from "apple" to "kiwi", in the fruits list.
fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi"

# Question 3: Use the append method to add "orange" to the fruits list.
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")

# Question 4: Use the insert method to add "lemon" as the second item in the fruits list.
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "lemon")

# Question 5: Use the remove method to remove "banana" from the fruits list.
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")

# Question 6: Use negative indexing to print the last item in the list.
fruits = ["apple", "banana", "cherry"]
print(fruits[-1])

# Question 7: Use a range of indexes to print the third, fourth, and fifth item in the list.
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])

# Question 8: Use the correct syntax to print the number of items in the list.
fruits = ["apple", "banana", "cherry"]
print(len(fruits))


# -------------- PYTHON TUPLES EXERCISES -------------

# Question 1: Use the correct syntax to print the first item in the fruits tuple.
fruits = ("apple", "banana", "cherry")
print(fruits[0])

# Question 2: Use the correct syntax to print the number of items in the fruits tuple.
fruits = ("apple", "banana", "cherry")
print(len(fruits))

# Question 3: Use negative indexing to print the last item in the tuple.
fruits = ("apple", "banana", "cherry")
print(fruits[-1])

# Question 4: Use a range of indexes to print the third, fourth, and fifth item in the tuple.
fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:5])


# ------------- PYTHON SETS EXERCISES ---------------

# Question 1: Check if "apple" is present in the fruits set.
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
    print("Yes, apple is a fruit!")

# Question 2: Use the add method to add "orange" to the fruits set.
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")

# Question 3: Use the correct method to add multiple items (more_fruits) to the fruits set.
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)

# Question 4: Use the remove method to remove "banana" from the fruits set.
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")

# Question 5: Use the discard method to remove "banana" from the fruits set.
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")


# --------------- PYTHON DICTIONARIES EXERCISES -------------------

# Question 1: Use the get method to print the value of the "model" key of the car dictionary.
car = {"brand": "Ford", "model": "Mustang", "year": 1964}
print(car.get("model"))

# Question 2: Change the "year" value from 1964 to 2020.
car = {"brand": "Ford", "model": "Mustang", "year": 1964}
car["year"] = 2020

# Question 3: Add the key/value pair "color" : "red" to the car dictionary.
car = {"brand": "Ford", "model": "Mustang", "year": 1964}
car["color"] = "red"

# Question 4: Use the pop method to remove "model" from the car dictionary.
car = {"brand": "Ford", "model": "Mustang", "year": 1964}
car.pop("model")

# Question 5: Use the clear method to empty the car dictionary.
car = {"brand": "Ford", "model": "Mustang", "year": 1964}
car.clear()


# --------------- PYTHON IF...ELSE EXERCISES ----------------

# Question 1: Print "Hello World" if a is greater than b.
a = 50
b = 10
if a > b:
    print("Hello World")

# Question 2: Print "Hello World" if a is not equal to b.
a = 50
b = 10
if a != b:
    print("Hello World")

# Question 3: Print "Yes" if a is equal to b, otherwise print "No".
a = 50
b = 10
if a == b:
    print("Yes")
else:
    print("No")

# Question 4: Print "1" if a is equal to b, print "2" if a is greater than b, otherwise print "3".
a = 50
b = 10
if a == b:
    print("1")
elif a > b:
    print("2")
else:
    print("3")

# Question 5: Print "Hello" if a is equal to b, and c is equal to d.
a = 10
b = 10
c = 30
d = 30
if a == b and c == d:
    print("Hello")

# Question 6: Print "Hello" if a is equal to b, or if c is equal to d.
a = 10
b = 10
c = 30
d = 30
if a == b or c == d:
    print("Hello")

# Question 7: Complete the code block, print "YES" if 5 is larger than 2.
if 5 > 2:
    print("YES")

# Question 8: Use the correct one line short hand syntax to print "YES" if a is equal to b, otherwise print("NO").
a = 2
b = 5
print("YES") if a == b else print("NO")

# Question 9: Use an if statement to print "YES" if either a or b is equal to c.
a = 2
b = 50
c = 2
if a == c or b == c:
    print("YES")


# ---------------- PYTHON WHILE LOOPS -------------

# Question 1: Print i as long as i is less than 6.
i = 1
while i < 6:
    print(i)
    i += 1

# Question 2: Stop the loop if i is 3.
i = 1
while i < 6:
    if i == 3:
        break
    i += 1

# Question 3: In the loop, when i is 3, jump directly to the next iteration.
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

# Question 4: Print a message once the condition is false.
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")


# --------------- PYTHON FOR LOOPS ------------------

# Question 1: Loop through the items in the fruits list.
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

# Question 2: In the loop, when the item value is "banana", jump directly to the next item.
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

# Question 3: Use the range function to loop through a code set 6 times.
for x in range(6):
    print(x)

# Question 4: Exit the loop when x is "banana".
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)


# ------------------PYTHON FUNCTIONS EXERCISES--------------------


# Question 1: Create a function named my_function.
def my_function():
    print("Hello from a function")


# Question 2: Execute a function named my_function.
def my_function():
    print("Hello from a function")


my_function()


# Question 3: Inside a function with two parameters, print the first parameter.
def my_function(fname, lname):
    print(fname)


# Question 4: Let the function return the x parameter + 5.
def my_function(x):
    return x + 5


# Question 5: If you do not know the number of arguments that will be passed into your function, there is a prefix you can add in the function definition, which prefix?
def my_function(*kids):
    print("The youngest child is " + kids[2])


# Question 6: If you do not know the number of keyword arguments that will be passed into your function, there is a prefix you can add in the function definition, which prefix?
def my_function(**kid):
    print("His last name is " + kid["lname"])


# --------------- PYTHON LAMBDA EXERCISE -------------------


# Question 1: Create a lambda function that takes one parameter (a) and returns it.
def x(a):
    return a


# --------------- PYTHON CLASSES EXERCISES -------------------


# Question 1: Create a class named MyClass:
class MyClass:
    x = 5


# Question 2: Create an object of MyClass called p1:
class MyClass:
    x = 5


p1 = MyClass()


# Question 3: Use the p1 object to print the value of x:
class MyClass:
    x = 5


p1 = MyClass()
print(p1.x)


# Question 4: What is the correct syntax to assign a "init" function to a class?
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# -----------------PYTHON INHERITANCE EXERCISES ----------------


# Question 1: What is the correct syntax to create a class named Student that will inherit properties and methods from a class named Person?
class Student(Person):
    pass


# Question 2: We have used the Student class to create an object named x.
# What is the correct syntax to execute the printname method of the object x?


class Person:
    def __init__(self, fname):
        self.firstname = fname

    def printname(self):
        print(self.firstname)


class Student(Person):
    pass


x = Student("Mike")
x.printname()


# -------------- PYTHON MODULES EXERCISES -----------------

# Question 1: What is the correct syntax to import a module named "mymodule"?
# Answer: import mymodule

# Question 2: If you want to refer to a module by using a different name, you can create an alias.
# What is the correct syntax for creating an alias for a module?
# Answer: import mymodule as mx

# Question 3: What is the correct syntax of printing all variables and function names of the "mymodule" module?
# Answer: import mymodule
# print(dir(mymodule))

# Question 4: What is the correct syntax of importing only the person1 dictionary of the "mymodule" module?
# Answer: from mymodule import person1


# ---------------- END OF THE PYTHON EXERCISES (95 QUESTIONS IN TOTAL) -------------------
