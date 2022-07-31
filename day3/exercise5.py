# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
#name1 = input("What is your name? \n")
#name2 = input("What is their name? \n")
name1 = "Brad Pitt"
name2 = "Jennifer Aniston"
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
names = name1.lower() + name2.lower()
count_t = names.count("t")
count_r = names.count("r")
count_u = names.count("u")
count_e = names.count("e")
count_l = names.count("l")
count_o = names.count("o")
count_v = names.count("v")

true_score = count_t + count_r + count_u + count_e
love_score = count_l + count_o + count_v + count_e

true_love = int(f"{true_score}{love_score}")

if (true_love < 10) or (true_love > 90):
  print(f"Your score is {true_love}, you go together like coke and mentos.")
elif (true_love >= 40) and (true_love <=50) :
  print(f"Your score is {true_love}, you are alright together.")
else:
  print(f"Your score is {true_love}.")