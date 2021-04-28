#!/usr/bin/env python3

import os, sys, re

def list_filenames(directory):
    filenames = [os.path.join(directory, fn) for fn in next(os.walk(directory))[2]]
    return filenames

def list_directories(directory):
    return [f.path for f in os.scandir(directory) if f.is_dir()]

def match_all_after(string_to_match, string_to_remove):
    try:
        a = string_to_match[string_to_match.index(string_to_remove):]
        b = string_to_match.replace(a, "")
        return b.lower()
    except ValueError:
        return 0