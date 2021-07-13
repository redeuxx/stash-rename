import os
import shutil
import csv
import re
import sys
import pathlib


def list_filenames(directory):
    """List filenames in a given directory"""

    return [os.path.join(directory, fn) for fn in next(os.walk(directory))[2]]


def list_directories(directory):
    """List directories in a given directory"""

    return [f.path for f in os.scandir(directory) if f.is_dir()]


def match_all_after(string_to_match, string_to_remove):
    """Returns a string with an input string removed from the end of the string"""

    try:
        a = string_to_match[string_to_match.index(string_to_remove):]
        b = string_to_match.replace(a, "")
        return b.lower()
    except ValueError:
        return 0


def subs_exist(directory):
    """Returns number of subdirectories minus exempted directories"""

    subs = [dI for dI in os.listdir(directory) if os.path.isdir(os.path.join(directory, dI))]
    a = len(subs)
    file = open(os.path.abspath('db/exempt.txt'), 'r')
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


def replace(max_filename, directory):
    """Replace strings stored in db/replace.csv"""

    database_file = os.path.abspath('db/replace.csv')
    new_name = max_filename
    if not os.path.isfile(database_file):
        sys.exit("%s is invalid." % database_file)
    with open(database_file, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        num_count = 0
        for row in csv_reader:
            if re.match(row["abbreviation"], max_filename):
                w = re.match(row["abbreviation"], max_filename)
                new_name = directory + "/" + max_filename.replace(w.group(), row['full_name'])
                num_count += 1
    return new_name


def move_biggest(filename, directory, remove_this_string):
    """Search for biggest file in directory, return new file location, directory to be deleted"""

    previous_filepath = pathlib.PurePath(filename)  # full path to file
    previous_filename = os.fspath(pathlib.Path(previous_filepath.parts[-2]))  # convert path object to string
    suffix = pathlib.Path(previous_filepath.parts[-1]).suffix
    dir_to_be_deleted = os.path.join(directory, previous_filename)

    # If third argument is specified, remove specified string from new filename
    if len(remove_this_string) > 0:
        if match_all_after(previous_filename, remove_this_string) == 0:
            new_filename = replace(os.path.join(directory, previous_filename.lower() + suffix),
                                   directory)  # create new full path
            print("%s -> %s" % (previous_filepath, new_filename.lower() + suffix))
        else:
            fixed_string = match_all_after(previous_filename, remove_this_string)
            new_filename = replace(os.path.join(directory, fixed_string.lower() + suffix),
                                   directory)  # create new full path
            print("%s -> to %s" % (previous_filepath, new_filename.lower()))
    else:
        new_filename = replace(os.path.join(directory, previous_filename.lower() + suffix),
                               directory)  # create new full path
        print("%s -> to %s" % (previous_filepath, new_filename.lower()))
    return new_filename, dir_to_be_deleted
