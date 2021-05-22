#!/usr/bin/env python3

import os
import shutil


def list_filenames(directory):
    """List filenames in a given directory"""

    filenames = [os.path.join(directory, fn) for fn in next(os.walk(directory))[2]]
    return filenames


def list_directories(directory):
    """List directories in a given directory"""

    return [f.path for f in os.scandir(directory) if f.is_dir()]


def match_all_after(string_to_match, string_to_remove):
    try:
        a = string_to_match[string_to_match.index(string_to_remove):]
        b = string_to_match.replace(a, "")
        return b.lower()
    except ValueError:
        return 0


def subs_exist(directory):
    """Returns number of subdirectories"""

    subs = [dI for dI in os.listdir(directory) if os.path.isdir(os.path.join(directory, dI))]
    a = len(subs)
    file = open('db/exempt.txt', 'r')
    for b in file:
        s = b.rstrip('\n')
        if s in subs:
            a = a - 1
    return a


def del_dir(directory):
    """Delete directory"""

    try:
        shutil.rmtree(directory)
        return 0
    except FileExistsError:
        return 1


def move_file(previous_filepath, new_filename):
    """Move file"""

    try:
        os.rename(previous_filepath, new_filename)
        return 0
    except FileExistsError:
        return 1
