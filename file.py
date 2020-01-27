
def read_file():
    
    try:
        file_read = open("output1.txt", "r")
        file_read.read()
    except FileNotFoundError :
        print("an error occurred while reading this file")

        

def write_file():
    try:
        r_file = open("/etc/conf", "w")
        r_file.write("I am in love with shiv")
    except PermissionError:
        print("you are not permitted to write into this file")
        
def read_dir():
    try: 
        r_dir = open('/Users/ismailibrahim/Documents/documents/python-mastery')
        r_dir.read()
    except IsADirectoryError:
        print('the path is pointing to a directory, not a file')
        

info_object = {
    'workplace': 'google',
    'stack': 'python', 
    'framework': 'flask',
    'years of experience': 3,
    'gender': 'male',
    'name': 'Ismail Calory'}

def invert_dict(d):
    inverse = dict()
    for key in d:
        print('====>>>', key)
        val = d[key]
        print('====>>>', val, inverse.keys())
        if val not in inverse.keys():
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse    

def invert_dictionary_in_file():
        import pickle
        import json
        
        with open('dict.txt', 'wb') as write_file:
            pickle.dump(info_object, write_file)
        
        with open('dict.txt', 'rb') as read_file:
            value = invert_dict(pickle.loads(read_file.read()))
            with open('invert_dict.txt', 'w') as f_write:
                f_write.write(json.dumps(value))
            
        



if __name__ == '__main__':
    # read_file()
    # write_file()
    # read_dir()
    invert_dictionary_in_file()

