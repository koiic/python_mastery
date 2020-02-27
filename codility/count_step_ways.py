''' Programme to count number of ways to climb a stairs '''

#SOLVING USING RECURSION... THIS ALGORITHM IS NOT EFFICIENT ENOUGH
def num_ways(n):
    
    if n <= 1:
        return 1
    result = num_ways(n-1) + num_ways(n-2)
    return result

#SOLVING USING DYNAMIC PROGRAMMING KEEPING TRACK OF THE VALUE OF N
def num_ways_with_dp(n):
    if n <= 1:
        return 1
    nums = [0] * (n + 1)
    nums[0] = 1; nums[1] = 1
    for index in range(2, n+1):
        print(index)
        nums[index] = nums[index-1] + nums[index-2]
        print(nums)
    return nums[n]
    
    
#SOLVING USING RECURSION... THIS ALGORITHM IS NOT EFFICIENT ENOUGH
def step_num_ways(n, steps):
    total = 0
    if n == 0:
        return 1
    for i in steps:
        if n - i >= 0: 
         total += num_ways(n-i)
    return total

#SOLVING USING DYNAMIC PROGRAMMING KEEPING TRACK OF THE VALUE OF N
def step_num_ways_dp(n, steps):
    if n==0:
        return 1
    nums = [0] * (n+1)
    nums[0] = 1
    for index in range(1, n+1):
        total = 0
        for value in steps:
            if index - value >= 0:
                total += nums[index-value]
        nums[index] = total
        
    return nums[n]
# print(step_num_ways(3))
# print(num_ways_with_dp(3))
print(step_num_ways(4, [1,3,5]))
print(step_num_ways_dp(4, {1,3,5}))