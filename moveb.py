#!/usr/bin/env python3

import functions
import os
import pathlib
import sys


def main():
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
            move_biggest(os.path.abspath(max_filename), directory, remove_this_string)


def move_biggest(filename, directory, remove_this_string):
    previous_filepath = pathlib.PurePath(filename)  # full path to file
    previous_filename = os.fspath(pathlib.Path(previous_filepath.parts[-2]))  # convert path object to string
    suffix = pathlib.Path(previous_filepath.parts[-1]).suffix
    dir_to_be_deleted = os.path.join(directory, previous_filename)

    """If second argument is specified, remove specified string from new filename"""
    if len(remove_this_string) > 0:
        if functions.match_all_after(previous_filename, remove_this_string) == 0:
            print("Substring not found.")
            new_filename = os.path.join(directory, previous_filename + suffix)  # create new full path
            print("%s WILL be moved to %s" % (previous_filepath, new_filename + suffix))
        else:
            fixed_string = functions.match_all_after(previous_filename, remove_this_string)
            new_filename = os.path.join(directory, fixed_string + suffix)  # create new full path
            print("%s will be moved to %s" % (previous_filepath, new_filename))
    else:
        new_filename = os.path.join(directory, previous_filename + suffix)  # create new full path
        print("%s will be moved to %s" % (previous_filepath, new_filename))
    if functions.move_file(previous_filepath, new_filename) == 1:
        print("Unable to move %s. File exists." % previous_filepath)
    else:
        if functions.subs_exist(dir_to_be_deleted) < 1:
            if functions.del_dir(dir_to_be_deleted) == 1:
                print("Could not delete %s" % dir_to_be_deleted)


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
