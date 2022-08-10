top_board = ["_", "_", "_"]
mid_board = ["_", "_", "_"]
bot_board = ["_", "_", "_"]

board_dictionary = {1: top_board, 2: mid_board, 3: bot_board}


def draw_board():
	print("---------")
	print(f"| {top_board[0]} {top_board[1]} {top_board[2]} |")
	print(f"| {mid_board[0]} {mid_board[1]} {mid_board[2]} |")
	print(f"| {bot_board[0]} {bot_board[1]} {bot_board[2]} |")
	print("---------")


def get_pos_input():
	while True:
		try:
			board_pos_input, section_pos_input = input().split()
			board_pos_input, section_pos_input = int(board_pos_input), int(section_pos_input)
		except ValueError:
			print("You should enter numbers!")
		except TypeError:
			print("You should enter numbers!")
		except IndexError:
			print("Coordinates should be from 1 to 3!")
		else:
			return board_pos_input, section_pos_input - 1


def win_condition():
	state = 0
	c_met = 0

	def check_horizontal_win():
		nonlocal state
		nonlocal c_met

		if top_board[0] == top_board[1] == top_board[2]:
			match top_board[0]:
				case "X":
					state = 1
					c_met += 1
				case "O":
					state = 2
					c_met += 1

		if mid_board[0] == mid_board[1] == mid_board[2]:
			match mid_board[0]:
				case "X":
					state = 1
					c_met += 1
				case "O":
					state = 2
					c_met += 1

		if bot_board[0] == bot_board[1] == bot_board[2]:
			match bot_board[0]:
				case "X":
					state = 1
					c_met += 1
				case "O":
					state = 2
					c_met += 1

	def check_vertical_win():
		nonlocal state
		nonlocal c_met

		if top_board[0] == mid_board[0] == bot_board[0]:
			match top_board[0]:
				case "X":
					state = 1
					c_met += 1
				case "O":
					state = 2
					c_met += 1

		if top_board[1] == mid_board[1] == bot_board[1]:
			match top_board[1]:
				case "X":
					state = 1
					c_met += 1
				case "O":
					state = 2
					c_met += 1

		if top_board[2] == mid_board[2] == bot_board[2]:
			match top_board[2]:
				case "X":
					state = 1
					c_met += 1
				case "O":
					state = 2
					c_met += 1

	def check_diagonal_win():
		nonlocal state
		nonlocal c_met

		if top_board[0] == mid_board[1] == bot_board[2]:
			match top_board[0]:
				case "X":
					state = 1
					c_met += 1
				case "O":
					state = 2
					c_met += 1

		if top_board[2] == mid_board[1] == bot_board[0]:
			match top_board[2]:
				case "X":
					state = 1
					c_met += 1
				case "O":
					state = 2
					c_met += 1

	check_horizontal_win()
	check_vertical_win()
	check_diagonal_win()
	return state, c_met


def main():
	player_turn = 0
	whole_board = top_board, mid_board, bot_board
	x_count = whole_board.count("X")
	o_count = whole_board.count("O")

	while True:
		game_state, condition_met = win_condition()
		match game_state:
			case 0:
				if "_" not in top_board and "_" not in mid_board and "_" not in bot_board:
					print("Draw")
					break
				else:
					try:
						board_section, section_cell = get_pos_input()
						board_section = board_dictionary.get(board_section)
						if board_section[section_cell] == "_":
							if player_turn == 0:
								board_section[section_cell] = "X"
								player_turn += 1
								draw_board()
							else:
								board_section[section_cell] = "O"
								player_turn -= 1
								draw_board()
						else:
							print("This cell is occupied! Choose another one!")
					except KeyError:
						print("Coordinates should be from 1 to 3!")
					except TypeError:
						print("Coordinates should be from 1 to 3!")
					except IndexError:
						print("Coordinates should be from 1 to 3!")
			case 1:
				if condition_met == 1:
					if x_count - o_count >= 2:
						print("Impossible")
					elif o_count - x_count >= 2:
						print("Impossible")
					else:
						print("X wins")
						break
				elif condition_met > 1:
					print("Impossible")
			case 2:
				if condition_met == 1:
					if x_count - o_count >= 2:
						print("Impossible")
					elif o_count - x_count >= 2:
						print("Impossible")
					else:
						print("O wins")
						break
				elif condition_met > 1:
					print("Impossible")


if __name__ == "__main__":
	main()
