import os, sys

options = ("-d", "--prepend", "--append")


def main():
    if len(sys.argv) < 4:
        sys.exit("Nothing to do.")
    elif options[0] not in sys.argv:
        sys.exit("No directory specified.")
    directory = (sys.argv[(sys.argv.index(options[0])) + 1])
    if not os.path.isdir(directory):
        sys.exit("Specified directory is not a valid directory.")
    do_dir(r"%s" % directory)


def do_dir(directory):
    """Main function to do file operations. Pass the directory from command line arguments, 
    --append, --prepend. Does not return anything."""
    final_name = []
    filenames_no_dirs = next(os.walk(directory))[2]  # list of files, just filenames, no directories
    for a in filenames_no_dirs:
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
                filename1 = os.path.splitext(filename1)[0] + append + os.path.splitext(filename1)[1]
            except IndexError:
                sys.exit("Invalid Append.")
        print("{} will be renamed to {}".format(directory + a, directory + filename1))
        raw_dir_name = r'%s' % directory + a
        raw_new_dir_name = r'%s' % directory + filename1
        os.rename(raw_dir_name, raw_new_dir_name)
        final_name.append(directory + filename1)


if __name__ == "__main__":
    main()
