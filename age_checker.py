# whether the user is old enough to vote
name=input("what is your name? ")
age=int(input("what is your age? "))
if age>=18:
    print(f"hi {name}, you can vote!")
else:
    print(f"hi {name}, you can vote in {18 - age} years.")