import numpy as np
import sys
from graphics import *
from puzzlesolver import *
def calculateCost(input_matrix, target_matrix):
	cost = 0
	for i in range(len(input_matrix)):
		for j in range(len(input_matrix[0])):
			if (input_matrix[i][j] != target_matrix[i][j]) and input_matrix[i][j] != 0:
				cost += 1
	return cost

def checkSolved(input_matrix, target_matrix):
	for i in range(len(input_matrix)):
		for j in range(len(input_matrix[0])):
			if input_matrix[i][j] != target_matrix[i][j]:
				return False

	return True

def solve_puzzle(input_matrix, target_matrix, window):
	forbidden_moves = []
	final_cost = 0
	x_blank_pos = np.nan
	y_blank_pos = np.nan
	level = 0
	dim = len(input_matrix)

	direction = ""
	key1 = []

	# up = 0, down = 1, left = 2, right = 3
	for i in range(dim+1):
		key1.insert(i,i)
	
	key1[0] = 1
	key1[1] = 0
	key1[2] = 3
	key1[3] = 2

	key = 6

	ct = 0

	actual_input = []
	for i in range(dim):
		actual_input.append(input_matrix[i])



	while not checkSolved(input_matrix, target_matrix):
		ct += 1
		level += 1
		cost = sys.maxsize #100000
		#Find the blank space
		move = []
		for i in range(dim):
			move_row = []
			for j in range(dim):
				move_row.append(0)
				if input_matrix[i][j] == 0:
					x_blank_pos = i
					y_blank_pos = j
			move.append(move_row)
		#UP
		if key != 0:
			temp = []
			for i in range(dim):
				row = []
				for j in range(dim):
					row.append(input_matrix[i][j])
				temp.append(row)

			if x_blank_pos != 0: #check that it is not in the first row of the matrix
				temp[x_blank_pos][y_blank_pos] = temp[x_blank_pos - 1][y_blank_pos]
				temp[x_blank_pos-1][y_blank_pos] = 0

				temp_cost = calculateCost(temp, target_matrix)
				cost_min = level + temp_cost
				if cost_min < cost:
					direction = "upwards"
					cost = cost_min
					s = 0
					for i in range(dim):
						for j in range(dim):
							move[i][j] = temp[i][j]


		if key != 1:
			temp = []
			for i in range(dim):
				row = []
				for j in range(dim):
					row.append(input_matrix[i][j])
				temp.append(row)

			if x_blank_pos != dim - 1:   #last row of the matrix
				temp[x_blank_pos][y_blank_pos] = temp[x_blank_pos+1][y_blank_pos]
				temp[x_blank_pos+1][y_blank_pos] = 0

				temp_cost = calculateCost(temp, target_matrix)
				cost_min = level + temp_cost

				if cost_min < cost: #c has changed now.It compares with c of upward matrix
					cost = cost_min
					s = 1
					direction = "downwards"
					for i in range(dim):
						for j in range(dim):
							move[i][j] = temp[i][j]

		if key != 3:
			temp = []
			for i in range(dim):
				row = []
				for j in range(dim):
					row.append(input_matrix[i][j])
				temp.append(row)

			if y_blank_pos != dim - 1: #check if its in the last column
				temp[x_blank_pos][y_blank_pos] = temp[x_blank_pos][y_blank_pos + 1]
				temp[x_blank_pos][y_blank_pos + 1] = 0
				temp_cost = calculateCost(temp, target_matrix)
				cost_min = level + temp_cost

				if cost_min < cost:
					direction = "rightwards"
					cost = cost_min
					s = 3
					for i in range(dim):
						for j in range(dim):
							move[i][j] = temp[i][j]

		if key != 2:
			temp = []
			for i in range(dim):
				row = []
				for j in range(dim):
					row.append(input_matrix[i][j])
				temp.append(row)
			if y_blank_pos != 0: #check if it is the first column of the matrix
				temp[x_blank_pos][y_blank_pos] = temp[x_blank_pos][y_blank_pos-1]
				temp[x_blank_pos][y_blank_pos-1] = 0
				temp_cost = calculateCost(temp, target_matrix)
				cost_min = level + temp_cost

				if cost_min < cost:
					direction = "leftwards"
					cost = cost_min
					s = 2
					for i in range(dim):
						for j in range(dim):
							move[i][j] = temp[i][j]

		print("Selected matrix for level %d is :" % level)
		print(move)
		for i in range(dim):
			print(move[i])

		print("Minimum cost for level %d is %d\n" % (level, cost))
		print("Selected direction is : " + direction)
		key = key1[s] #forbidden move
		for i in range(dim):
			for j in range(dim):
				input_matrix[i][j] = move[i][j]
				temp[i][j] = 0

		final_cost = final_cost + cost
		display_numbers(window, move, dim)
		#if ct == 1000:
			#sys.exit(1)

	print(input_matrix)
	display_numbers(window, input_matrix, len(input_matrix))



		








