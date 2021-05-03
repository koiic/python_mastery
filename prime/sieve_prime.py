"""SIEVE In this problem we will develop an even faster method which is known as the Sieve of Eratosthenes (although
it will be more expensive in terms of memory). The Sieve of Eratosthenes is an example of dynamic programming,
where the general idea is to not redo computations we have already done (read more about it here). We will break this
sieve down into several small functions.

Our submission will be a list of all prime numbers less than 2000.

The method works as follows (see here for more details)

Generate a list of all numbers between 0 and N; mark the numbers 0 and 1 to be not prime Starting with  p=2p=2  (the
first prime) mark all numbers of the form  npnp  where  n>1n>1  and  np<=Nnp<=N  to be not prime (they can't be prime
since they are multiples of 2!) Find the smallest number greater than  pp  which is not marked and set that equal to
pp , then go back to step 2. Stop if there is no unmarked number greater than  pp  and less than  N+1N+1 We will
break this up into a few functions, our general strategy will be to use a Python list as our container although we
could use other data structures. The index of this list will represent numbers.

We have implemented a sieve function which will find all the prime numbers up to  nn . You will need to implement the
functions which it calls. They are as follows

list_true Make a list of true values of length  n+1n+1  where the first two values are false (this corresponds with
step 1 of the algorithm above) mark_false takes a list of booleans and a number  pp . Mark all elements  2p,3p,
...n2p,3p,...n  false (this corresponds with step 2 of the algorithm above) find_next Find the smallest True element
in a list which is greater than some  pp  (has index greater than  pp  (this corresponds with step 3 of the algorithm
above) prime_from_list Return indices of True values Remember that python lists are zero indexed. We have provided
assertions below to help you assess whether your functions are functioning properly. """


def list_true(n):
    bool_value = [True for i in range(n + 1)]
    bool_value[0:2] = [False, False]
    return bool_value


def mark_false(bool_list, p):
    for i in range(p * 2, len(bool_list), p):
        bool_list[i] = False
        p += 1
    #     print(mark_false([False, False, True, True, True, True], 2))
    return bool_list


print(mark_false([False, False, True, True, True, True], 2))


def find_next(bool_list, p):
    for index, value in enumerate(bool_list):
        if value and index > p:
            return index
        else:
            index += 1
    return


def prime_from_list(bool_list):
    return [index for index, value in enumerate(bool_list) if value]
