print("Your are in the magic maze, in order to get out, you have to make the right moves. Which way do you want to go? (N, S, E, W)")

solution = ["S", "S", "W", "N", "E", "S"]
index = 0
moves = 0
lives = 3

flag = True

while flag:

    command = input("Enter your first move: ")

    if command == solution[0]:
        print("Correct!!")
        print("Moves: ", moves)
        print("Lives: ", lives)
        moves += 1
    else:
        print("Incorrect")
        moves += 1
        print("Moves: ", moves)
        print("Lives: ", lives)

    if command == solution[1]:
        print("Correct!!")
        print("Moves: ", moves)
        print("Lives: ", lives)
        moves += 1
    else:
        print("Incorrect")
        moves += 1
        print("Moves: ", moves)
        print("Lives: ", lives)

    if command == solution[2]:
        print("Correct!!")
        print("Moves: ", moves)
        print("Lives: ", lives)
        moves += 1
    else:
        print("Incorrect")
        moves += 1
        print("Moves: ", moves)
        print("Lives: ", lives)

    if command == solution[3]:
        print("Correct!!")
        print("Moves: ", moves)
        print("Lives: ", lives)
        moves += 1
    else:
        print("Incorrect")
        moves += 1
        print("Moves: ", moves)
        print("Lives: ", lives)

    if command == solution[4]:
        print("Correct!!")
        print("Moves: ", moves)
        print("Lives: ", lives)
        moves += 1
    else:
        print("Incorrect")
        moves += 1
        print("Moves: ", moves)
        print("Lives: ", lives)

    if command == solution[5]:
        print("Correct!!")
        print("Moves: ", moves)
        print("Lives: ", lives)
        moves += 1
    else:
        print("Incorrect")
        moves += 1
        print("Moves: ", moves)
        print("Lives: ", lives)

    if command == solution[6]:
        print("Correct!!, you scaped the maze in", moves, "moves")
        flag = False
    else:
        print("Incorrect")
        moves += 1
        print("Moves: ", moves)
        print("Lives: ", lives)

    if moves % 10 == 0:
        lives = lives - 1

    if lives == 0:
        print("You ran out of lives")
        flag = False