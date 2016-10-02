#if not indented the line of codes are sequencial

print "hello world"
print "testing"
x=1
print x+1

#raw_input saves it as a string

name = raw_input("What is your name, Atu? ")
print "Hello", name + "! I am Python Asmare"
age=raw_input("How old are you?")

print "No you are" ,age

#x and y are strings

x = raw_input("Enter a number: ")
y = raw_input("Enter another number: ")
z = x + y
print "The sum of", x, "and", y, "is",  z

#casting string to int

z = int(x) + int(y)
print "The correct sum actually was", z
a = float(raw_input('Enter a number: '))
b = float(raw_input('Enter a number: '))
c = float(raw_input('Enter a number: '))
x = (a + b + c) / 2
y = (x*(x-a)*(x-b)*(x-c))**0.5
print '%.2f' %y
