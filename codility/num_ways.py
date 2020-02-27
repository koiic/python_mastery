''' print out the  number of ways to decode a particular digit into the corresponding mapping 
for example num_ways('1') -> A == 1 ways
            num_ways('12') -> AB || l == 2 ways
            num_ways('') -> '' == ''
            num_ways('01') -> undefined == 0 ways '''

        

#Using recursion

def helper(data, k):
    """
        data: string
        k: string length
    """
    if k == 0: #num_ways("") = 1
        return 1
    
    s = len(data) - k 
    if data[s] == '0': #num_ways("011") = 0
        return 0
    
    result = helper(data, k-1)
    
    if k >= 2 and int(data[:2]) <= 26:
        result = result + helper(data, k-2)
    
    return result
    
    
    
def num_ways(data):
    return helper(data, len(data))

#Using dynamic programming memoization
def helper_num_ways_memo(data, k, memo):
    if k == 0:
        return 1
    
    s = len(data) - k
    if data[s] == '0':
        return 0
    if memo[k] != None:
        return memo[k]
    result = helper_num_ways_memo(data, k-1, memo)
    print(result)
    if k>= 2 and int(data[:2] <= 26):
        result = result + helper_num_ways_memo(data, k-2, memo)
    memo[k] = result
    print(memo)
    return result
    

def num_ways_memo(data):
    memo = [None] * int(len(data) + 1)
    return helper_num_ways_memo(data, len(data), memo)


# print(num_ways('12'))

# print(num_ways('123'))
# print(num_ways('011'))
# print(num_ways(''))
print(num_ways('1235'))
# print(num_ways('27345'))
# print(num_ways('111111'))

print(num_ways_memo('1245'))
# print(num_ways_memo('012'))
# print(num_ways_memo('12345'))
# print(num_ways_memo('111111'))