"""Number Guessing Game"""
print(__doc__)
# giving attempts to user
Attempts=10
while Attempts>0:
    # importing random library to generate random numbers
    num=int(input("Choose Number (1-10):"))
    import random
    var=random.randint(1,10)
    print(f"random number is {var}")
    # now making game
    if num==var:
        print(f"{num} is a correct guees")
        break
    else:
        Attempts-=1
        print(f"{num} is a wrong guees, you have {Attempts} attempts left")
        continue
if Attempts==0:
    print("You have no attempts left")