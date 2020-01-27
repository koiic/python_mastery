alphabet = "abcdefghijklmnopqrstuvwxyz"   

test_dups = ["zzz","dog","bookkeeper","subdermatoglyphic","subdermatoglyphics"] 

test_miss = ["zzz","subdermatoglyphic","the quick brown fox jumps over the lazy dog"]

def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d 

def has_duplicates(sentence):
    
    dict_count = histogram(sentence)
    for value in dict_count.values():
        if  value > 1:
            return True
        else:
            return False
        

def missing_letters(param):
    unavail_char = ""
    dict_count = histogram(param)
    for char in alphabet :
        if char not in dict_count.keys():
            unavail_char += char
    
    return unavail_char
 
 
def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in ["lagos", "portharcourt", "ibadan", "kano", "sokoto"]:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse    

if __name__ == "__main__":
    # print(missing_letters("aba"))
    # for item in test_dups:
    #     if has_duplicates(item):
    #         print(item + " has duplicates")
    #     else:
    #         print(item + " has no duplicates")
            
    # for item in test_miss:
    #     if missing_letters(item):
    #         print(item + " is missing letters " + missing_letters(item))
    #     else:
    #         print(item + " use all alphabets")
    my_dict = {"food": 'grain', "fruit": 'orange', "others": 'water'}
    print(invert_dict(my_dict))
