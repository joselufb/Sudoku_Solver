'''
Python array Sudoku solver
References: 
https://towardsdatascience.com/solve-sudokus-automatically-4032b2203b64
'''

# Example of sudoky board
# Gaps are represented with number 0
board_test = [
[0, 0, 9, 8, 0, 0, 7, 6, 0],
[5, 0, 3, 6, 0, 7, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 3, 0, 5],
[2, 5, 0, 0, 8, 0, 6, 0, 0],
[0, 9, 7, 0, 6, 5, 0, 0, 4],
[8, 0, 0, 0, 4, 2, 0, 0, 3],
[0, 3, 8, 0, 2, 6, 0, 0, 7],
[0, 7, 0, 0, 0, 8, 5, 0, 0],
[6, 0, 0, 0, 7, 0, 0, 0, 0],
]


def print_board(board):
	# Print the soduku in a visual way with its grid
	for i in range(len(board)):
		line = " "	

		if i == 3 or i == 6:
			print("-----------------------")	

		for j in range(len(board[i])):
			if j == 3 or j == 6:
				line += "| "
			line += str(board[i][j]) + " "
				
		print(line)		


def find_empty(board):
	# Find the next empty position (indicated by 0)
	# and return a tupple 
	for x in range(9):
		for y in range(9):
			if board[x][y] == 0:
				return x, y

	return -1,-1


def valid(board, i, j, num):
	# Check if num is contained in the row
	check_row = True
	for x in range(9):
		if num == board[i][x]:
			check_row = False
		
	# Check if num is contained in the column
	check_column = True
	if check_row:
		for x in range(9):
			if num == board[x][j]:
				check_column = False
			
	# Check if num is contained in the box 3x3
		if check_column:
			box_x = 3*(i // 3)
			box_y = 3*(j // 3)

			for x in range(box_x, box_x + 3):
				for y in range(box_y, box_y + 3):
					if board[x][y] == num:
						return False

			return True
	return False


def solve(board, i=0, j=0):
	i, j = find_empty(board)
	
	if i == -1:
		return True

	for num in range(1, 10):
		if valid(board, i, j, num):
			board[i][j] = num

			if solve(board, i, j):
				return True
			board[i][j] = 0

	return False


print_board(board_test)
solve(board_test)
print("\nThe solution is:\n")
print_board(board_test)
