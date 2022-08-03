import random

# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
index = len(names) - 1
random_index = random.randint(0,index)
print (names[random_index] + " is going to buy the meal today!")

# Easier Way
print (random.choice(names) + " is going to buy the meal today!")