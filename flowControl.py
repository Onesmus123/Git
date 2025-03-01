# CONDITIONALS

# Example 1

age = int(input("Enter your age:"))
if age >= 18:
    print("Old enough to vote!")
else:
    print("Too young! NOT allowed to vote!")


# Example 2

bananas = int(input("How many bananas do you have? "))

if bananas >= 5:
    print("I have a bunch of bananas.")
elif bananas >= 1:
    print("I have a small bunch of bananas.")
else :
    print("I have no bananas.")


# WHILE loop.
number  = int(input("Enter a anumber between 1 - 10: "))

while(number <= 10):
    print("I love coding!")
    number += number

# FOR loop!
num = [45,34,25,86,45]

for x in num:
    print(x)

names = ["Onesmus", "John", "Evan", "Reuben"]

for y in names:
    print(y)