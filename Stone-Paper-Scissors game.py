# Stone paper scissor game

while True:
    print("...Welcome to Stone-Paper-Scissor game...")

    print("Please select any one among the Stone - Paper - Scissor....")

    print('''
    Type;
    1 for Stone, 
    2 for Paper and,
    3 for scissor
    ''')

    import random

    computer = random.randint(1, 3)


    try:

        user_choice = int(input("Please enter you choice between 1 to 3 : "))

        print()

        if user_choice==computer:
            print('User and Computer choosed same\n')
            print("Its a tie...\n\n")

        elif (user_choice == 1) and (computer == 2):
            print('User choosed stone vs Computer choosed paper\n')
            print("Computer Wins...\n\n")  

        elif (user_choice == 1) and (computer == 3):
            print('User choosed stone vs Computer choosed scissor\n')
            print("User Wins...\n\n")

        elif (user_choice == 2) and (computer == 1):
            print('User choosed paper vs Computer choosed stone \n')
            print("User Wins...\n\n") 

        elif (user_choice == 2) and (computer == 3):
            print('User choosed paper vs Computer choosed scissor \n')
            print("Computer Wins...\n\n")

        elif (user_choice == 3) and (computer == 1):
            print('User choosed scissor vs Computer choosed stone \n')
            print("Computer Wins...\n\n")  

        elif (user_choice == 3) and (computer == 2):
            print('User choosed scissor vs Computer choosed paper\n')
            print("User Wins...\n\n") 

    except ValueError as e:
        print("you entered the wrong value")
