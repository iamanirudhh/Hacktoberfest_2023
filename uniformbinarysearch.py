# Python3 implementation of above approach

MAX_SIZE = 1000

# lookup table
lookup_table = [0] * MAX_SIZE

# create the lookup table
# for an array of length n
def create_table(n):
	
	# power and count variable
	pow = 1
	co = 0
	while True:
		
		# multiply by 2
		pow <<= 1

		# initialize the lookup table
		lookup_table[co] = (n + (pow >> 1)) // pow
		if lookup_table[co] == 0:
			break
		co += 1

# binary search
def binary(arr, v):
	
	# mid point of the array
	index = lookup_table[0] - 1

	# count
	co = 0

	while lookup_table[co] != 0:

		# if the value is found
		if v == arr[index]:
			return index

		# if value is less than the mid value
		elif v < arr[index]:
			co += 1
			index -= lookup_table[co]

		# if value is greater than the mid value
		else:
			co += 1
			index += lookup_table[co]

# main function
arr = [1, 3, 5, 6, 7, 8, 9]
n = len(arr)

# create the lookup table
create_table(n)

# print the position of the array
print("Position of 3 in array = ", binary(arr, 3))
