#Ask for name, age, city, and favourite subject'
name = input("what is your name: ")
age = int(input("what is your age: "))
city = input("what city do you live in: ")
subject = input("whats your favourite subject: ")
#Calculate and print how many years until they turn 100
years_until_100 = 100 - age
#Print everything in a clean f-string paragraph
print(f""" ----- your bio----
name: {name}
age: {age}
city: {city}
subject: {subject}
You have {years_until_100} years till you are 100 years old.""")
#No hardcoded values — everything comes from input()