# write a function that prints all of the name of the name of in directory (string provided as an argument) also print all filenames in subdirectoried. you cannot use os.walk
from os.path import join, isdir
import glob
import os

def print_filenames(dirname):
    all_filenames = os.listdir(dirname)
    for one_filename in all_filenames:
        print(one_filename)
        
# print_filenames('/etc/')

#using glob
def another_print_filenames(dirname):
    all_filenames = glob.glob(join(dirname, "*"))
    for one_filename in all_filenames:
        if isdir(one_filename):
            print(f'******************>>> {one_filename}')
            another_print_filenames(one_filename)  
        else:
            print(one_filename)
another_print_filenames('/etc/')