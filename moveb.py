#!/usr/bin/env python3

import functions
import os
import sys


def main():
    color_start = '\033[91m'
    color_end = '\033[0m'
    try:
        user_input = sys.argv[1]
        if not os.path.isdir(user_input):
            syntax(0)
    except IndexError:
        syntax(0)
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
            filesize = os.path.getsize(r'%s' % x)
            if filesize > max_size:
                max_filename = x
                max_size = filesize

        # If all files are 0 bytes in size, max_filename never gets set
        if max_size == 0:
            print("All files were 0 in size or there were no files in %s" % (p))
        else:
            returned = (functions.move_biggest(os.path.abspath(max_filename), directory, remove_this_string))
            if functions.move_file(max_filename, returned[0]) == 1:
                print("%sUnable to move %s. File exists.%s" % (color_start, returned[0].lower() + returned[2], color_end
                                                               ))
            else:
                if functions.subs_exist(returned[1]) < 1:
                    if functions.del_dir(returned[1]) == 1:
                        print("%sCould not delete %s%s" % (color_start, returned[1], color_end))


def syntax(error):
    if error == 0:
        print("Invalid syntax.")
    print(
        '''
Usage: moveb.py argument1 argument2
argument1 - Directory location
argument2 - Remove from end of filename starting with argument2. (optional)
        ''')
    sys.exit()


if __name__ == "__main__":
    main()
