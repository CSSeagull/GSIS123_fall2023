"""name = input("Enter your name: ")
surname = input("Enter your surname: ")
age = input("Enter your age: ")
print(name,  surname , "I'm" , age) 


import turtle

t = turtle.Turtle()

for _ in range (8):
    t.forward(100)
    t.left(50)
    

turtle. exitonclick() """

def user_name():

    name = input("Enter your name: ")
    surname = input("Enter your surname: ")
    age = input("Enter your birth year: ")
    month = input("Enter your birth month: ")
    day = input("Enter your birth day: ")
    print("My name is" , name,  surname , "I was born in", age, "in" , month, day) 

user_name()
user_name()
user_name()