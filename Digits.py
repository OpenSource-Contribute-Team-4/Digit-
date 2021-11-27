def printIntro():
    print("                                DIGITS")
    print("              CREATIVE COMPUTING  MORRISTOWN, NEW JERSEY")
    print("\n\n")
    print("THIS IS A GAME OF GUESSING.")


def readInstructionChoice():
    print("FOR INSTRUCTIONS, TYPE '1', ELSE TYPE '0' ? ")
    try:
        choice = int(input())
        return choice == 1
    except (ValueError, TypeError) as m:
        return False


def printInstructions():
    print("\n")
    print("PLEASE TAKE A PIECE OF PAPER AND WRITE DOWN")
    print("THE DIGITS '0', '1', OR '2' THIRTY TIMES AT RANDOM.")
    print("ARRANGE THEM IN THREE LINES OF TEN DIGITS EACH.")
    print("I WILL ASK FOR THEN TEN AT A TIME.")
    print("I WILL ALWAYS GUESS THEM FIRST AND THEN LOOK AT YOUR")
    print("NEXT NUMBER TO SEE IF I WAS RIGHT. BY PURE LUCK,")
    print("I OUGHT TO BE RIGHT TEN TIMES. BUT I HOPE TO DO BETTER")
    print("THAN THAT *****")
    print()


def read10Numbers():
    print("TEN NUMBERS, PLEASE ? ")
    numbers = []

    for i in range(10):
        validInput = False
        while not validInput:
            try:
                n = int(next())
                validInput = True
                numbers.append(n)
            except (TypeError, ValueError) as e:
                print("!NUMBER EXPECTED - RETRY INPUT LINE")

    return numbers


if __name__ == '__main__':
    printIntro()
    if readInstructionChoice():
        printInstructions()

    a = 0
    b = 1
    c = []

    m = [[1]*3 for i in range(27)]
    k = [[9]*3 for i in range(3)]
    l = [[3]*3 for i in range(9)]

    continueGame = True
    while continueGame:
        l[0][0] = 2
        l[4][1] = 2
        l[8][2] = 2
        z = 26
        z1 = 8
        z2 = 2
        runningCorrect = 0

        for i in range(1, 4):
            validNumbers = False
            numbers = []
            while not validNumbers:
                print()
                numbers = read10Numbers()
                validNumbers = True
                for number in numbers:
                    if number < 0 or number > 2:
                        print("ONLY USE THE DIGITS '0', '1', OR '2'.")
                        print("LET'S TRY AGAIN.")
                        validNumbers = False
                        break

            print("\n%-14s%-14s%-14s%-14s" %("MY GUESS", "YOUR NO.", "RESULT", "NO. RIGHT"))


