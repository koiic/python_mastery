# MaxCounters
'''Calculate the values of counters after applying all alternating operations: increase counter by 1; set value of all counters to current maximum.'''

def solution(N, A):
    
    # initialize counter with zeros to N
    counters = [0] * N
    
    last_max_counter = 0
    
    max_applied = False
    current_max_counter = 0
    
    for index in range(len(A)-1):
        value = A[index]
        if value >= 1 and value <= N:
            if max_applied and counters[index - 1] < last_max_counter:
                counters[index - 1] = last_max_counter
            counters[index - 1] += 1
            if current_max_counter < counters[index - 1]:
                current_max_counter = counters[index - 1]
            elif value == N+1:
                max_applied = True;
                last_max_counter = current_max_counter
    
    # apply last max counter to all counters
    for k in range(len(counters)):
        counters[k] = last_max_counter if counters[k] < last_max_counter else counters[k]
    return counters
    
    
    
print(solution(5,[3,4,4,6,1,4,4] ))