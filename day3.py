import re
import numpy as np

def find_max_width_and_height(claims):
	max_width = 0
	max_height = 0
	for claim in claims:
		claim_list = re.split('@ |x|,|: |\n', claim)
		x_start = int(claim_list[1])
		y_start = int(claim_list[2])
		width = int(claim_list[3])
		height = int(claim_list[4])
		if ((x_start + width) > max_width):
			max_width = (x_start + width)
		if ((y_start + height) > max_height):
			max_height = (y_start + height)
	return max_width, max_height

def calculate_array_of_all_claims(claims, max_width, max_height):
	array_of_all_claims = np.zeros([max_height, max_width])

	for claim in claims:
		claim_list = re.split('@ |x|,|: |\n', claim)
		x_start = int(claim_list[1])
		y_start = int(claim_list[2])
		width = int(claim_list[3])
		height = int(claim_list[4])
		for y in range(y_start, (y_start + height)):
			for x in range(x_start, (x_start + width)):
				array_of_all_claims[y][x] = array_of_all_claims[y][x] + 1
	return array_of_all_claims

def find_overlaps(array_of_all_claims):
	number_of_overlaps = 0
	for row in range(len(array_of_all_claims)):
		for column in range(len(array_of_all_claims[0])):
			if (array_of_all_claims[row][column] > 1):
				number_of_overlaps += 1
	return number_of_overlaps

def claim_that_does_not_overlap(array_of_all_claims):
	print(array_of_all_claims)


file_object = open("test_input_day_3.txt", "r")
claims = file_object.readlines()
max_width, max_height = find_max_width_and_height(claims)
array_of_all_claims = calculate_array_of_all_claims(claims, max_width, max_height)
print(find_overlaps(array_of_all_claims))
print(claim_that_does_not_overlap(array_of_all_claims))

file_object.close()