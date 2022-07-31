#Data Types

#String
string_var = "Hello"
print(string_var[4]) #Subscripting using the array position

#Integer
int_var = 123
print(123 + 345)
print(123_456_789) #Underscores for , breaks.
# Float
print(3.14159)

#Boolean
True
False

#Getting Type
a = 1234
print(type(a))

# Maths
print(3 + 5)
print(7 - 4)
print(3 * 2)
print(6 / 3) # divide always results in a float
print(5 ** 3) #Exponents

#PEMDAS
# ()
# **
# * /
# + -
print(3 * 3 + 3 / 3 - 3) # 7.0
print((3 * 3) + (3 / 3) - 3) # 7.0 easier to read

#Rounding
print( round(8 / 5, 2) ) #round to 2 decimals
print ( 8//5 ) # This makes the Divide an int. Not a round, just a convert

# Shorthand Math
result = 4 / 2
result /= 2
print(result)

score = 0
score += 1
print(score)
score *= 2
print(score)
score -= 1
print(score)

# Easy Type conversions or F strings
score = 0
height = 1.8
isWinning = True

print(f"your score is {score}, your height is {height}, you are winning {isWinning}")
