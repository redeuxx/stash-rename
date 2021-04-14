#!/usr/bin/env python3

import os, sys, re, csv

def main():
    try:
        directory = sys.argv[1]
        database_file = sys.argv[2]
        if not os.path.isdir(directory):
            sys.exit("Directory does not exist.")
        if not os.path.isfile(database_file):
            sys.exit("No database file specified.")
    except IndexError:
        syntax_error()

    print(f"Processing {directory}")
    filenames_no_dirs = next(os.walk(directory))[2]
    with open(database_file, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        num_count = 0
        for row in csv_reader:
            for x in filenames_no_dirs:
                if re.match(row["abbreviation"], x):
                    w = re.match(row["abbreviation"], x)
                    new_name = x.replace(w.group(), row['full_name'])
                    num_count += 1
                    print(f"{x} will renamed to {new_name}")
    print(f"Renamed {num_count} files.")

def syntax_error():
    sys.exit('''Syntax error.
Usage: replace.py argument1 argument2
argument1 - Directory location of files to process.
argument2 - Location of the file that contains the replacement database.''')

if __name__ == "__main__":
    main()