def countChar(str, char):
	count = 0
	if len(str) > 0:
		for value in str:
			if value == char:
				count += 1
		return count
	return -1


def countCharRecursive(str, char):
	if len(str) <= 0:
		return 0
	if str[0] == char:
		return 1 + countCharRecursive(str[1:], char)
	else:
		return countCharRecursive(str[1:], char)


def fib(n):
	if n == 0:
		return 0
	if n == 1 or n == 2:
		return 1
	return (fib(n - 2) + fib(n - 1))


def permutations_recursion(str_):
	if str_ == "":  # base case
		print("i got here")
		return [""]
	permutes = []
	for char in str_:
		print(char)
		subpermutes = permutations_recursion(str_.replace(char, "", 1))  # recursive step
		print(subpermutes, '&&&&&')
		for each in subpermutes:
			print(each, '''----''')
			permutes.append(char + each)

	return permutes


# result = []
#
#
# def permutations(data, i, length):
# 	if i == length:
# 		result.append(''.join(data))
# 	else:
# 		for j in range(i, length):
# 			# swap
# 			data[i], data[j] = data[j], data[i]
# 			permutations(data, i + 1, length)
# 			data[i], data[j] = data[j], data[i]
#
#
# inti_str = "abc"
# permutations(list(inti_str), 0, len(inti_str))
#
# print(result)

print(permutations_recursion('abc'))
print(countChar('hello', 'l'))
print(countChar('educative', 'b'))
print(countChar('abacada', 'a'))
print(countCharRecursive('hello', 'l'))
print(fib(3))
