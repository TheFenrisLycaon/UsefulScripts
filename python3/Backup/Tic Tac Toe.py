def showsetup():
    for i in range(len(setup)):
        for j in range(len(setup[i])):
            print(setup[i][j], end="\t")
        print("\n")


def choice(int):
    if temp <= 9 and y % 2 == 0:
        if temp == 1:
            if setup[0][0] == "-":
                setup[0][0] = "x"
            else:
                print("Invalid Choice\nYou lose your chance\nTurn Goes To Opponent")
        elif temp == 2:
            if setup[0][1] == "-":
                setup[0][1] = "x"
            else:
                print("Invalid Choice\nYou lose your chance\nTurn Goes To Opponent")

        elif temp == 3:
            if setup[0][2] == "-":
                setup[0][2] = "x"
            else:
                print("Invalid Choice\nYou lose your chance\nTurn Goes To Opponent")

        elif temp == 4:
            if setup[1][0] == "-":
                setup[1][0] = "x"
            else:
                print("Invalid Choice\nYou lose your chance\nTurn Goes To Opponent")

        elif temp == 5:
            if setup[1][1] == "-":
                setup[1][1] = "x"
            else:
                print("Invalid Choice\nYou lose your chance\nTurn Goes To Opponent")

        elif temp == 6:
            if setup[1][2] == "-":
                setup[1][2] = "x"
            else:
                print("Invalid Choice\nYou lose your chance\nTurn Goes To Opponent")

        elif temp == 7:
            if setup[2][0] == "-":
                setup[2][0] = "x"
            else:
                print("Invalid Choice\nYou lose your chance\nTurn Goes To Opponent")

        elif temp == 8:
            if setup[2][1] == "-":
                setup[2][1] = "x"
            else:
                print("Invalid Choice\nYou lose your chance\nTurn Goes To Opponent")

        elif temp == 9:
            if setup[2][2] == "-":
                setup[2][2] = "x"
            else:
                print("Invalid Choice\nYou lose your chance\nTurn Goes To Opponent")

        else:
            pass
    elif temp <= 9 and y % 2 != 0:
        if temp == 1:
            if setup[0][0] == "-":
                setup[0][0] = "0"
            else:
                print("Invalid Choice\nYou lose your chance\nTurn Goes To Opponent")

        elif temp == 2:
            if setup[0][1] == "-":
                setup[0][1] = "0"
            else:
                print("Invalid Choice\nYou lose your chance\nTurn Goes To Opponent")

        elif temp == 3:
            if setup[0][2] == "-":
                setup[0][2] = "0"
            else:
                print("Invalid Choice\nYou lose your chance\nTurn Goes To Opponent")

        elif temp == 4:
            if setup[1][0] == "-":
                setup[1][0] = "0"
            else:
                print("Invalid Choice\nYou lose your chance\nTurn Goes To Opponent")

        elif temp == 5:
            if setup[1][1] == "-":
                setup[1][1] = "0"
            else:
                print("Invalid Choice\nYou lose your chance\nTurn Goes To Opponent")

        elif temp == 6:
            if setup[1][2] == "-":
                setup[1][2] = "0"
            else:
                print("Invalid Choice\nYou lose your chance\nTurn Goes To Opponent")

        elif temp == 7:
            if setup[2][0] == "-":
                setup[2][0] = "0"
            else:
                print("Invalid Choice\nYou lose your chance\nTurn Goes To Opponent")

        elif temp == 8:
            if setup[2][1] == "-":
                setup[2][1] = "0"
            else:
                print("Invalid Choice\nYou lose your chance\nTurn Goes To Opponent")

        elif temp == 9:
            if setup[2][2] == "-":
                setup[2][2] = "0"
            else:
                print("Invalid Choice\nYou lose your chance\nTurn Goes To Opponent")

        else:
            pass
    else:
        print("Invalid Input... Try Again")


def checkwin():
    if setup[0][0] == setup[1][1] == setup[2][2] != "-":
        win()
    elif setup[0][0] == setup[0][1] == setup[0][2] != "-":
        win()
    elif setup[1][0] == setup[1][1] == setup[1][2] != "-":
        win()
    elif setup[2][0] == setup[2][1] == setup[2][2] != "-":
        win()
    elif setup[0][0] == setup[1][0] == setup[2][0] != "-":
        win()
    elif setup[0][1] == setup[1][1] == setup[2][1] != "-":
        win()
    elif setup[0][2] == setup[1][2] == setup[2][2] != "-":
        win()
    elif setup[0][2] == setup[1][1] == setup[2][0] != "-":
        win()
    else:
        pass


def win():
    if y % 2 != 0:
        print("Player 2 wins")
        label()
    else:
        print("Player 1 wins")
        label()


def label():
    again = str(input("Wanna Play Again: (Press Y of Yes & N for No)"))
    if again == "y" or "Y":
        main()
    elif again == "n" or "N":
        exit()
    else:
        label()


if __name__ == "__main__":
    y, a = 1, 1
    while True:
        setup = (["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"])

        print(
            "Lets Play Tic Tac Toe...\nHow To Play:\n1. Winning And Losing is similar to the normal game\n2. Entering you input is via num pad which goes left to right and then top to bottom\nFor Example:\n\n1\t2\t3\n4\t5\t6\n7\t8\t9"
        )

        print("\nInitial Setup::\n")
        showsetup()
        print("You know the rules...\nUser 1 Begins!!!")

        for a in range(9):
            if a != 9:
                temp = int(input())
                if temp in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                    y = y + 1
                    choice(temp)
                    showsetup()
                    checkwin()
                else:
                    print("Invalido")
            elif a == 9:
                print("Draw")
                label()
            else:
                pass
