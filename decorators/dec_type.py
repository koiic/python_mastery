 # write a decorator that ensures all of the argument passed to a function will be strings
 
def only_string_args(func):
    def wrapper(*args, **kwargs):
        return func(*[one_word  for one_word in args if isinstance(one_word, str)],
                        **kwargs)
    return wrapper

def check_arg_type(argtype):
    def middle(func):
        def wrapper(*args, **kwargs):
            return func(*[one_word  for one_word in args if isinstance(one_word, argtype)],
                        **kwargs)
        return wrapper
    return middle


@check_arg_type(str)
def hello(name):
    return f'hello, {name}'

@check_arg_type(int)
def goodbye(name):
    return f'hello, {name}'
    
@check_arg_type(str)
def word_lengths(*words):
    return {one_word : len(one_word)
            for one_word in words}

@check_arg_type(int)
def div(a, b):
    return a/b

print(div(1, 'abc', 3))
print(hello("Ismail"))
print(goodbye(12345))
print(word_lengths("ac", "def", "ert", 5))