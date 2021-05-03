import pyspark

if __name__ == '__main__':
	sc = pyspark.SparkContext('local[*]')

	# txt = sc.textFile('/Users/admin/Documents/pythons/justpython/python_mastery/youth_unemployment.txt')
	# print(txt.count())
	#
	# python_lines = txt.filter(lambda line: 'python' in line.lower())
	# print(python_lines.count())

	big_list = range(10000)
	print(big_list)
	rdd = sc.parallelize(big_list, 2)
	print(rdd)
	odds = rdd.filter(lambda x: x%2 != 0)
	print(odds.take(5))