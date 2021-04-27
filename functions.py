#!/usr/bin/env python3

import os, sys, re

def syntax_error():
    '''TODO'''

def list_filenames(directory):
    filenames = [os.path.join(directory, fn) for fn in next(os.walk(directory))[2]]
    return filenames

def list_directories(directory):
    return [f.path for f in os.scandir(directory) if f.is_dir()]

def print_hello():
    print("Hello World")

def move_biggest(directory):
    '''TODO'''
    print(directory)