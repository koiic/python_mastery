animals = {'a': ['horse'], 'b': ['baboon'], 'c': ['giraffe']}
animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')


def how_many(dic):
    total = 0
    for key, value in animals.items():
        total += len(value)
    return total


def biggest(dic):
    max = 0
    max_key = ''
    for key, value in animals.items():
        if len(value) > max:
            max = len(value)
            max_key = key
    return (max_key, max)


def dstats(dic):
    return (how_many(dic), biggest(dic)[1])


if __name__ == '__main__':
    print(how_many(animals))
    print(biggest(animals)[0])
    print(dstats(animals))
