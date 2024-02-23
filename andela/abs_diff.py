"""
function absoluteDiff(numbers) {
  let min_difference = Number.MAX_VALUE;
  numbers.sort((a, b) => a - b);
  let minPairs = [];
  for (let i = 0; i < numbers.length - 1; i++) {
      if (Math.abs(numbers[i] - numbers[i+1]) < min_difference) {
        min_difference = Math.abs(numbers[i] - numbers[i+1]);
        minPairs = [[numbers[i], numbers[i+1]]];
      } else if (Math.abs(numbers[i] - numbers[i+1]) == min_difference) {
        minPairs.push([numbers[i], numbers[i+1]]);
      }
  }
  for (let i = 0; i < minPairs.length; i++) {
    console.log(minPairs[i][0], minPairs[i][1]);
  }
}

absoluteDiff([6, 2, 4, 10]);
"""
import cProfile

import sys

MAX_INT = sys.maxsize

def absolute_difference(numbers):
    min_diff = MAX_INT
    sorted_numbers = sorted(numbers)
    min_pairs  = []
    breakpoint()

    for i in range(len(sorted_numbers)-1):
        temp_min = abs(sorted_numbers[i] - sorted_numbers[i+1])
        if temp_min < min_diff:
            min_diff = temp_min
            min_pairs = [[sorted_numbers[i], sorted_numbers[i+1]]]
        elif temp_min == min_diff:
            min_pairs.append([sorted_numbers[i], sorted_numbers[i+1]])

    for i in range(len(min_pairs)):
        print(min_pairs[i][0], min_pairs[i][1])
        

if __name__ == "__main__":
   absolute_difference([4, 2, 1, 3])