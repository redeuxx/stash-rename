#!/usr/bin/env python3

import os, sys, functions, pathlib

def main():
    try:
        input = sys.argv[1]
        if not os.path.isdir(input):
            sys.exit("Invalid directory.")
    except IndexError:
        sys.exit("No directory specified.")
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
            move_biggest(os.path.abspath(max_filename), directory)

def move_biggest(filename, directory):
    previous_fullpath = pathlib.PurePath(filename) # full path to file
    a = previous_fullpath.parts[-2] + pathlib.Path(previous_fullpath.parts[-1]).suffix # create new filename
    new_filename= os.path.join(directory, a) # create new full path
    print("%s will be moved to %s" % (previous_fullpath, new_filename))
    os.rename(previous_fullpath, new_filename)

if __name__ == "__main__":
    main()