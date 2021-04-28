#!/usr/bin/env python3

import os, sys, functions, pathlib

def main():
    try:
        input = sys.argv[1]
        if not os.path.isdir(input):
            sys.exit("Invalid directory.")
    except IndexError:
        sys.exit("No directory specified.")
    try:
        if len(sys.argv[2]) > 0:
            remove_this_string = sys.argv[2]
    except IndexError:
        remove_this_string = ""
    directory = os.path.abspath(r"%s" % sys.argv[1])
    directory_listing = functions.list_directories(directory)
    for p in directory_listing:
        max_size = 0
        max_filename = ""
        a = functions.list_filenames(p)
        for x in a:
            filesize = os.path.getsize(r'%s' % x )
            if filesize > max_size:
                max_filename = x
                max_size = filesize
        
        # If all files are 0 bytes in size, max_filename never gets set
        if max_size == 0:
            print("All files were 0 in size or there were no files in %s" % (p))
        else:
            move_biggest(os.path.abspath(max_filename), directory, remove_this_string)

def move_biggest(filename, directory, remove_this_string):
    previous_fullpath = pathlib.PurePath(filename) # full path to file
    previous_filename = os.fspath(pathlib.Path(previous_fullpath.parts[-1])) # convert path object to string
    suffix = pathlib.Path(previous_fullpath.parts[-1]).suffix

    """If second argument is specified, remove specified string from new filename"""
    if len(remove_this_string) > 0:
        print("here1")
        if functions.match_all_after(previous_filename, remove_this_string) == 0:
            print("Substring not found.")
        else:
            fixed_string = functions.match_all_after(previous_filename, remove_this_string)
            new_filename= os.path.join(directory, fixed_string + suffix) # create new full path
            print("%s will be moved to %s" % (previous_fullpath, new_filename))
            os.rename(previous_fullpath, new_filename)
    else:
        new_filename= os.path.join(directory, previous_filename + suffix) # create new full path
        print("%s will be moved to %s" % (previous_fullpath, new_filename))
        print("here")
        os.rename(previous_fullpath, new_filename)
        

if __name__ == "__main__":
    main()