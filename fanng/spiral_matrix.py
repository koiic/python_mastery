def spiral_matrix(m, n, array):
	"""
	Algorithm:
	Create and initialize variables k – starting row index, m – ending row index,
	l – starting column index, n – ending column index
	Run a loop until all the squares of loops are printed.
	In each outer loop traversal print the elements of a square in a clockwise manner.
	Print the top row, i.e. Print the elements of the kth row from column index l to n, and increase the count of k.
	Print the right column, i.e. Print the last column or n-1th column from row index k to m and decrease the count of n.
	Print the bottom row, i.e. if k < m, then print the elements of m-1th row from column n-1 to l and decrease the count of m
	Print the left column, i.e. if l < n, then print the elements of lth column from m-1th row to k and increase the count of l.
	:param array: 2d array of lists
	:param n: ending column index
	:param m: ending row index
	:return:
	"""

	k = 0
	l = 0

	while k < m and l < n:
		# print the first row from the remaining rows
		for i in range(l, n):
			print(array[k][i], end=" ")
		k += 1

		# print the last column from the remaining columns
		for i in range(k, m):
			print(array[i][n - 1], end=" ")
		n -= 1

		# print the last row from the remaining rows
		if k < m:
			for i in range(n - 1, (l - 1), -1):
				print(array[m - 1][i], end=" ")
			m -= 1

		# print the first column from the remaining columns
		if l < n:
			for i in range(m - 1, k - 1, -1):
				print(array[i][l], end=" ")
			l += 1


a = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18]]

R = 3
C = 6

# Function Call
if __name__ == '__main__':
	spiral_matrix(R, C, a)
