"""
2. File stats.
Write a function stats() that takes in a filename and returns a tuple consisting of the number of lines, number of words, and number of characters in the file. You should also write a test program that reads a filename command line argument, calls stats(), and prints the file statistics. For example:
> python stats.py example.txt
3 lines, 20 words, 98 characters
"""

def stats(file):
    number_of_line = 0
    number_of_word = 0
    number_of_character = 0
    with open(file, 'r') as f:
        for line in f:
            line = line.strip('/n')
            words = line.split()
            number_of_line += 1
            number_of_word += len(words)
            number_of_character += len(line)

    return f'{number_of_line} lines, {number_of_word} words, {number_of_character} characters'


if __name__ == '__main__':
    print(stats('change.py'))