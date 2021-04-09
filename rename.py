import os, sys

options = ("-d", "--prepend", "--append")
print(options)

if len(sys.argv) < 4:
    sys.exit("Nothing to do.")
elif options[0] not in sys.argv:
    sys.exit("No directory specified.")
final_name = []

directory = (sys.argv[(sys.argv.index(options[0])) + 1])
if not os.path.isdir(directory):
    sys.exit("Specified directory is not a valid directory.")
filenames_dirs = next(os.walk(directory))[2] # list of files, just filenames, no directories 
filenames = [os.path.join(directory, fn) for fn in next(os.walk(directory))[2]] # list files, no directories, full path
for a in filenames:
    filename1 = a
    if options[1] in sys.argv:
        try:
            prepend = (sys.argv[(sys.argv.index(options[1])) + 1])
            if prepend in options:
                sys.exit("Invalid Prepend.")
            filename1 = prepend + filename1
        except IndexError:
            sys.exit("Invalid Prepend.")
    if options[2] in sys.argv:
        try:
            append = (sys.argv[(sys.argv.index(options[2])) + 1])
            if append in options:
                sys.exit("Invalid Prepend.")
            filename1 = filename1 + append
        except IndexError:
            sys.exit("Invalid Append.")
    final_name.append(filename1)
print(final_name)