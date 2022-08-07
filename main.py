
player_input = input()

top_board = [symbol for symbol in player_input[0: 3]]
mid_board = [symbol for symbol in player_input[3: 6]]
bot_board = [symbol for symbol in player_input[6: 9]]


def print_board():
	print("---------")
	print(f"| {top_board[0]} {top_board[1]} {top_board[2]} |")
	print(f"| {mid_board[0]} {mid_board[1]} {mid_board[2]} |")
	print(f"| {bot_board[0]} {bot_board[1]} {bot_board[2]} |")
	print("---------")


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

	x_count = player_input.count("X")
	o_count = player_input.count("O")
	game_state, condition_met = win_condition()
	print_board()

	match game_state:
		case 0:
			if condition_met == 0 and game_state == 0:
				if x_count - o_count >= 2:
					print("Impossible")
				elif o_count - x_count >= 2:
					print("Impossible")
				else:
					if "_" not in top_board and "_" not in mid_board and "_" not in bot_board:
						print("Draw")
					else:
						print("Game not finished")
		case 1:
			if condition_met == 1:
				if x_count - o_count >= 2:
					print("Impossible")
				elif o_count - x_count >= 2:
					print("Impossible")
				else:
					print("X wins")
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
			elif condition_met > 1:
				print("Impossible")


if __name__ == "__main__":
	main()
