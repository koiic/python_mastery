# Iterttols product, permutations, combinations, accumulate, gropuby, and infinite iterators

from itertools import product, permutations, combinations, combinations_with_replacement, accumulate, groupby, cycle, \
	count, repeat

''':PRODUCT
	Computes Cartesian product of input iterables
'''
a = [1, 2]
b = [3, 4]

prod = product(a, b)
a = [1, 2]
b = [3]
prod2 = product(a, b, repeat=2)  # we can also decide number of repetition
# cartesian product(1*3, 1*4, 2*3, 2*4)
# prod -> iterator( use list(prod) to display the product)
print(list(prod))  # -> [(1,3), (1,4), (2,3), (2,4)]
print(list(prod2))  # -> [(1,3,1,3), (1,3,2,3), (2,3,1,3) (2,3,2,3)]

""": PERMUATION
	List out all possible orderings of an Input
"""
a = [1, 2, 3]
perm = permutations(a)
print(list(perm))  # -> [(1,2,3), (1,3,2), (2,1,3), (2,3,1), (3,1,2), (3,2,1)]

perm2 = permutations(a, 2)  # describe the length of the permutation (2)
print(list(perm2))  # -> [(1,2), (1,3), (2,1), (2,3), (3,1), (3,2)]

""": COMBINATIONS
	return all combinations with specified length
"""
a = [1, 2, 3, 4]
comb = combinations(a, 2)  # length of possible combinations with length 2
print(list(comb))  # -> [(1,2), (1, 3), (1,4), (2,3), (2,4),(3,4)]

comb2 = combinations_with_replacement(a, 2)  # length of possible combinations with length 2
print(list(comb2))  # ->  [(1, 1), (1, 2), (1, 3), (1, 4), (2, 2), (2, 3), (2, 4), (3, 3), (3, 4), (4, 4)]

""":ACCUMULATE
	return accumulated iterables based on binary functions
"""
acc = accumulate([1,2,3,4])
print(list(acc)) #-> default accumulation is sum  [1, 3, 6, 10]

import operator
acc2 = accumulate([1,2,3,4], func=operator.mul)
print(list(acc2)) #-> return  multiplied accumulation  [1, 2, 6, 24]

acc3 = accumulate([1,2,3,4], func=max)
print(list(acc3))  #-> [1, 5, 5, 6, 6, 6]


""": GROUPBY
	return iterators with consecutive keys and groups from the iterable. 
	The key is a function of computing a key value for each element 
"""
def smaller_than_3(x):
	return x < 3

group_obj = groupby([1,2,3,4], key=smaller_than_3)
for key, group in group_obj:
	print(key, list(group))

# Or use a lambda function, e.g words with 'i':
group_obj = groupby(['hi', 'nice', 'hello', 'cool'], key = lambda x : 'i' in x)
for key, group in group_obj:
	print(key, list(group))

persons = [{'name': 'Tim', 'age': 25}, {'name': 'Dan', 'age': 25},
           {'name': 'Lisa', 'age': 27}, {'name': 'Claire', 'age': 28}]
for key, group in groupby(persons, key=lambda x:x['age']):
	print(key, list(group))

'''
True [1, 2]
False [3, 4]
True ['hi', 'nice']
False ['hello', 'cool']
25 [{'name': 'Tim', 'age': 25}, {'name': 'Dan', 'age': 25}]
27 [{'name': 'Lisa', 'age': 27}]
28 [{'name': 'Claire', 'age': 28}]
'''

""":INFINITE ITERATORS
	count(), cycle(), repeat()
"""
# count(x): count from x: x, x+1, x+2, x+3...
for i in count(10):
    print(i)
    if  i >= 13:
        break

# cycle(iterable) : cycle infinitely through an iterable
print("")
sum = 0
for i in cycle([1, 2, 3]):
    print(i)
    sum += i
    if sum >= 12:
        break

# repeat(x): repeat x infinitely or n times
print("")
for i in repeat("A", 3):
    print(i)



