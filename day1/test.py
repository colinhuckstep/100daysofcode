print(
'''
Day 1 - Python Print Function
The function is declared like this:
print('what to print')
'''
)

print("Day 1 - String Manipulation")
print("String Concatenation is done with the "+" sign.")
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")

name = input("What is your name? ")
print(len(name))

# 🚨 Don't change the code below 👇
a = input("a: ")
b = input("b: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
temp = a
a = b
b = temp

#Write your code above this line 👆
####################################

# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)