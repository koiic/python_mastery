import matplotlib.pyplot as plt
import time

def sum_gauss(N):
  return N*(N + 1)// 2


def sum_num(N):
  sum_ = 0
  for num in range(N + 1):
    sum_ += num
  return sum_

# print(sum_gauss(9))
# print(sum_num(9))

# assert sum_gauss(9) == sum_num(9)

def plot_graph(n_avgs, func, N):

  times = []
  for _ in range(n_avgs):
    ts = time.time()
    func(N)
    times.append(time.time() - ts)
  return sum(times)/ float(len(times)) * 1000


n_avgs = 200
time_sum = []
time_gauss = []
N_range = range(10,100000, 5000)
for N in N_range:
    time_sum.append(plot_graph(n_avgs, sum_num, N))
    time_gauss.append(plot_graph(n_avgs, sum_gauss, N))

plt.plot(N_range, time_sum, 'o-', label='Sum Numbers')
plt.plot(N_range, time_gauss, 'o-', label='Gauss')
plt.xlabel('N')
plt.ylabel('Average time (ms)')
plt.legend()

