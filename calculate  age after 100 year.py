from datetime import date 

name = input("Enter your name:")
age = int(input("Enter your age:"))

current_year = date.today().year
year_100 = current_year + (100 -age)

print(f"Hello {name}!")
print(f"You will turn 100 years old in the year {year_100}.")