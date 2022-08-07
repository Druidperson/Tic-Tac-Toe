# This code is an input routine for the Tic-Tac-Toe game I'm building, and I need to free up space in main.


def take_input(message):
	player_input = input(message)
	return player_input

print_board()

# Take input and assign it to the correct portion of the board
top_board = [symbol for symbol in take_input("Enter 3 symbols for the top row: ")[0: 3]]
mid_board = [symbol for symbol in take_input("Enter 3 symbols for the middle row: ")[0: 3]]
bot_board = [symbol for symbol in take_input("Enter 3 symbols for the bottom row: ")[0: 3]]


# # Checks if game is unfinished
# elif abs(player_input.count("_") > 0 or abs(player_input.count(" ") > 0)):
# print("Game not finished")