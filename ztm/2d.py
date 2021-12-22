'''
Given a  2D Array, :

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
An hourglass in  is a subset of values with indices falling in this pattern in 's graphical representation:

a b c
  d
e f g
There are  hourglasses in . An hourglass sum is the sum of an hourglass' values. Calculate the hourglass sum for every hourglass in , then print the maximum hourglass sum. The array will always be .

Example


-9 -9 -9  1 1 1
 0 -9  0  4 3 2
-9 -9 -9  1 2 3
 0  0  8  6 6 0
 0  0  0 -2 0 0
 0  0  1  2 4 0
The  hourglass sums are:

-63, -34, -9, 12,
-10,   0, 28, 23,
-27, -11, -2, 10,
  9,  17, 25, 18
The highest hourglass sum is  from the hourglass beginning at row , column :

0 4 3
  1
8 6 6
'''


def hourglassSum(arr):
	# Write your code here
	max = -63
	for i in range(4):
		for j in range(4):
			value = (arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j + 1]
			         + arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2])
			if value > max:
				max = value
	return max


if __name__ == '__main__':
	list_ = [
		[1, 1, 1, 0, 0, 0],
		[0, 1, 0, 0, 0, 0],
		[1, 1, 1, 0, 0, 0],
		[0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0],
	]
	print(hourglassSum(list_))
