from collections import OrderedDict

from past.builtins import xrange

roman_dict = {
	'M': 1000,
	'D': 500,
	'C': 100,
	'L': 50,
	'X': 10,
	'V': 5,
	'I': 1
}


def convert_roman(roman_numeral):
	if len(roman_numeral) == 1:
		return roman_dict[roman_numeral]
	else:
		_dict = OrderedDict()
		for char in roman_numeral:
			_dict[char] = roman_dict[char]
		list_dict = list(_dict.items())
		print(list_dict)

		if len(list_dict) > 2:
			# for i in xrange(len(list_dict)-1, 0,  -1):
			for i in reversed(list_dict):
				print(i)
		else:
			return conversion(list_dict[0][1], list_dict[-1][1])

		# list_dict = list(_dict.items())
		# print(list_dict[0] > list_dict[-1])
		# if list_dict[0] > list_dict[-1]:
		# 	print(list_dict[0][1] + list_dict[-1][1])
		# else:
		# 	print(list_dict[-1][1] - list_dict[0][1])
		# return list_dict


def conversion(first, second):
	if first > second:
		value = first + second
	else:
		value = second - first
	return value


print(convert_roman('IV'))

'''

Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given a number in Roman numeral format, convert it to decimal.

The values of Roman numerals are as follows:

{
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1
}
In addition, note that the Roman numeral system uses subtractive notation for numbers such as IV and XL.

For the input XIV, for instance, you should return 14.


'''