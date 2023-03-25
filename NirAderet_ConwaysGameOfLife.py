def update(board):
    """ This method updates the board game by the rules of the game. Do a single iteration.
            Input board - list of lists in the size of 50*50.
            Output None.
            """
    next_board = new_board()  # Set a new board to copy to
    for row in range(50):  # Go over all the rows
        for col in range(50):  # go over all the columns
            next_board[row][col] = board[row][col]  # Copy the board so we can make changes
            alive_n = 0  # Count the number of alive neighbors
            if board[(row - 1) % 50][(col - 1) % 50] == 1:  # Check bottom left
                alive_n += 1
            if board[row % 50][(col - 1) % 50] == 1:  # Check middle left
                alive_n += 1
            if board[(row + 1) % 50][(col - 1) % 50] == 1:  # Check upper left
                alive_n += 1
            if board[(row - 1) % 50][col % 50] == 1:  # Check bottom middle
                alive_n += 1
            if board[(row + 1) % 50][col % 50] == 1:  # Check upper middle
                alive_n += 1
            if board[(row - 1) % 50][(col + 1) % 50] == 1:  # Check bottom right
                alive_n += 1
            if board[row % 50][(col + 1) % 50] == 1:  # Check middle right
                alive_n += 1
            if board[(row + 1) % 50][(col + 1) % 50] == 1:  # Check upper right
                alive_n += 1
            if board[row][col] == 1:  # Check if cell is alive and than check game rules
                if alive_n < 2 or alive_n > 3:
                    next_board[row][col] = 0
            else:
                if alive_n == 3:  # check game rules for dead cell
                    next_board[row][col] = 1
    return next_board


def new_board():
    """ This method creates a 50*50 sized Zero list.
            Input None.
            Output board - list of lists of zeros in the size of 50*50.
            """
    return [[0 for _ in range(50)] for _ in range(50)]  # Create a list with 50 lists and insert 50 cells to each
    # inner list


def add_rle_to_board(board, pattern, pattern_position=(1, 1)):
    """ This method transforms an rle coded pattern to a two dimensional list that holds the pattern, and insert
            the pattern to the game board.
            Dead will be donated with 0 while alive will be donated with 1.
           Input board - list of lists of zeros in the size of 50*50.
                rle coded string.
                pattern_position is a tuple that contains the upper left corner of the pattern. Default ( 1, 1)
           Output None.
           """
    count = ''  # keep track of the amount of commend
    row = pattern_position[0]  # y position
    column = pattern_position[1]  # x position
    list_of_numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for i in range(len(pattern)):  # for loop the length of the rle(pattern)
        if pattern[i] in list_of_numbers:  # Check if there is an amount of specific cells
            count += pattern[i]
        elif pattern[i] == '!':  # End of rle
            break
        elif pattern[i] == 'b':  # Dead cells
            if count != '':  # Check if there is an amount of dead cells to be inserted
                for cell in range(int(count)):
                    board[row % 50][column % 50] = 0
                    column += 1
                count = ''
            else:
                board[row % 50][column % 50] = 0
                column += 1
        elif pattern[i] == 'o':  # Live cells
            if count != '':  # Check if there is an amount of live cells to be inserted
                for cell in range(int(count)):
                    board[row % 50][column % 50] = 1
                    column += 1
                count = ''
            else:
                board[row % 50][column % 50] = 1
                column += 1
        elif pattern[i] == '$':  # Go to next row
            row += 1
            column = pattern_position[1]
    return board


def print_board(board):
    """ This method prints the board game.
                Input board - list of lists of zeros in the size of 50*50.
                Output None.
                """
    for row in range(50):
        print(board[row])


while True:
    num_of_updates = input("Insert number of updates: ")
    if num_of_updates.isdigit() and int(num_of_updates) > 0:
        break
    else:
        print("Invalid input. Please enter a positive integer.")

rle = input("\nInsert a Run Length Encoded (RLE) pattern: ")
check = True
max_reps = check_mark = check_end = 0
while check:  # Check if the input is valid
    while rle == "":
        rle = input("\nPlease insert a correct RLE(for example 3o$o$bo!): ")
    for i in range(len(rle)):
        if rle[i] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'b', 'o', '$', '!']:  # Check if each
            # char is valid
            rle = input("\nPlease insert a correct RLE(for example 3o$o$bo!): ")
            break
        if rle[i] == 'b' or rle[i] == 'o':
            check_mark += 1
        if rle[i] == '!':
            check_end += 1
    if i == len(rle) - 1 and check_mark >= 1 and check_end == 1:  # Check if all of the input was covered
        check = False
    else:
        rle = input("\nPlease insert a correct RLE(for example 3o$o$bo!): ")
        check_end = check_mark = 0
    max_reps += 1
    if max_reps > 100 and len(rle) == 0:  # Check if there was any input
        rle = input("\nPlease insert a correct RLE(for example 3o$o$bo!): ")
        max_reps = 0

print("\nThe program will print the beginning of the board and all of the updates until the given number.")
print("\nThe frame is initialized with modulus so that the pattern can continue from the left side of the board to the "
      "right side "
      "of the board etc.. \nThe rules are:")
print('')
print("1 - A cell is born if he has 3 alive neighbors and survives if he has 2 or 3 alive neighbors.")
print("2 - A cell dies if he has less than 2 neighbors or more than 3 neighbors")
print('')
my_board = new_board()  # Creates the board game
my_board = add_rle_to_board(my_board, rle)  # Insert the rle to the board
print('This is your starting board:')
print_board(my_board)
for x in range(int(num_of_updates)):  # Update and print each step
    my_board = update(my_board)
    print('')
    print('This is update number: ' + str(x + 1))
    print('')
    print_board(my_board)

