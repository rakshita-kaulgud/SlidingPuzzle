from graphics import *
import time
import random
from ideal_solution import *

def initialize_board(filename, dimension, input_matrix):
	#infile = open(filename, "r")
	board = []
	for i in range(dimension):
		board.append([]) 
	for row in range(dimension):
		for col in range(dimension):
			columnvalue = input_matrix[row][col]#eval(infile.readline())
			board[row].append(columnvalue)
	return board

def display_numbers(window,board, dimensions):
	for row in range(dimensions):
		#print(str(row))
		for col in range(dimensions):
			square = Rectangle(Point(col*50,row*50),Point((col+1)*50, (row+1)*50))
			square.setFill("white")
			square.draw(window)
			if board[row][col] != 0:
				center = Point(col*50+25,row*50+25)
				number = Text(center, board[row][col])
				number.setSize(24)
				number.setTextColor("purple")
				number.draw(window)


def main(input_matrix, matrix_input_numbers, dimensions):
	print(dimensions)
	print("Input Matrix:\n")
	print(input_matrix)

	window = GraphWin("Sliding Puzzle ", 50*dimensions, 50*dimensions)

	board = initialize_board("", dimensions, input_matrix)
	display_numbers(window, board, dimensions)

	time.sleep(3)
	print("Target Matrix:\n")
	matrix_input_numbers.sort()

	target_matrix = []

	matrix_input_numbers.remove(matrix_input_numbers[0])
	matrix_input_numbers.append(0)

	j = 0 
	for i in range(dimensions):
		print(i)
		row = []
		count = 0
		while(j<len(matrix_input_numbers)):
			if (count<dimensions):
				row.append(matrix_input_numbers[j])
				j = j+1
				count += 1
			else:
				break
		target_matrix.append(row)
	
	print(target_matrix)

	solve_puzzle(input_matrix, target_matrix, window)

	board = initialize_board("", dimensions, target_matrix)
	display_numbers(window, board, dimensions)
	message = Text(Point(100,100),"GAME OVER")
	message.setSize(24)
	message.setTextColor("orange")
	message.draw(window)
	input("Press <ENTER> to quit.")
	window.close()

if __name__ == "__main__":

	dimensions = input("Enter the dimensions of the puzzle:")

	#input_nums = input("Enter the input numbers:")

	dim = int(dimensions)

	total_nums = dim*dim
	matrix_input_numbers = list(range(total_nums))
	random.shuffle(matrix_input_numbers)
	
	#matrix_input_numbers = input_nums.strip().split(' ')
	matrix_input_numbers6 = [1,2,3,4,6,7,8,5,9,10,11,12,13,15,14,0]
	matrix_input_numbers3_4 = [1,2,0,4,5,7,3,8,9,6,11,12,13,10,14,15] #H
	matrix_input_numbers1_4 = [1,2,3,4,5,6,0,7,10,11,12,8,9,13,14,15] #H
	matrix_input_numbers2_4 = [1,2,3,4,5,6,7,8,9,0,11,12,13,10,14,15] #E
	matrix_input_numbers4_4 = [1,2,3,4,5,6,7,8,9,10,11,12,0,13,14,15] #E


	matrix_input_numbers1_3 = [1,8,2,0,4,3,7,6,5] #H
	matrix_input_numbers2_3 = [1,2,3,4,0,6,7,5,8] #E
	#matrix_input_numbers = [1,8,2,0,4,3,7,6,5]
	matrix_input_numbers = []
	if (dim == 3):
		matrix_input_numbers = matrix_input_numbers2_3
	elif (dim == 4):
		matrix_input_numbers = matrix_input_numbers1_4

	print("Input: " + str(matrix_input_numbers))
	input_matrix = []
	j = 0
	for i in range(dim):
		row = []
		count = 0
		while(j<len(matrix_input_numbers)):
			if (count<dim):
				row.append(matrix_input_numbers[j])
				j = j+1
				count += 1
			else:
				break
		input_matrix.append(row)

	main(input_matrix, matrix_input_numbers, dim)