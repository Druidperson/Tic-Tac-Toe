
# TODO:
#   Map out all winning scenarios or find a better way to detect a winning scenario without breaking pep8.
#   Figure out how these winning scenarios will work in the logic (Bunch of nested ifs?).
#   Figure out how to map the following scenarios:
#       Game not finished when neither side has three in a row but the grid still has empty cells.
#       Draw when no side has a three in a row and the grid has no empty cells.
#       X wins when the grid has three X's in a row (including diagonals).
#       O wins when the grid has three O's in a row (including diagonals).
#       Impossible when the grid has three of each kind in a row, or there are a lot more X's than O's.
#   To note: I want to die right now.

def main():

	player_input = input("Enter 9 symbols: ")

	# Take input and assign it to the correct part of the board
	top_board = [symbol for symbol in player_input[0: 3]]
	mid_board = [symbol for symbol in player_input[3: 6]]
	bot_board = [symbol for symbol in player_input[6: 9]]

	def print_board():
		print("---------")
		print(f"| {top_board[0]} {top_board[1]} {top_board[2]} |")
		print(f"| {mid_board[0]} {mid_board[1]} {mid_board[2]} |")
		print(f"| {bot_board[0]} {bot_board[1]} {bot_board[2]} |")
		print("---------")

	print_board()


if __name__ == "__main__":
	main()
