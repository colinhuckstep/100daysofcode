# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
days = 365
weeks = 52
months = 12

total_days = days * 90 
total_weeks = weeks * 90
total_months = months * 90

age = int(age)
age_in_days = age * days
age_in_weeks = age * weeks
age_in_months = age * months

remaing_days = total_days - age_in_days
remaing_weeks = total_weeks - age_in_weeks
remaing_months = total_months - age_in_months

print (f"You have {remaing_days} days, {remaing_weeks} weeks, and {remaing_months} months left.")

# Better solution
age = int(age)
years_remaining = 90 - age
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12
print (f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left.")


