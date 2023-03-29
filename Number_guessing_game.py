import random

r = random.randint(1, 100)

while True:
    print("Press enter to play game : ")
    ent = str(input("Press enter to play or press 'q' to quit game.... : "))
    ent = ent.lower()

    if (ent == ""):
        try:
            print("\nWelcome to the number guessing Game!!!\n")

            print("Guess the number...")

            ip = int(input("Enter a your guess : "))

            if (ip < r):
                print("The vlaue computer generated is ", r)
                print("""The number you guess is Wrong.....
The number is bigger than you guess..
    """)

            elif (ip == r):
                print("The vlaue computer generated is ", r)
                print("""The number you guess is right.......""")

            elif (ip > r):
                print("The vlaue computer generated is ", r)
                print("""The number you guess is Wrong.....
The number is smaller than you guess..
    """)

        except ValueError as e:
                print("Please enter the right value")
    
    elif (ent == "q"):
        break