#!/usr/bin/python3
""" Takes 2 string arguments """


from sys import argv, exit, stderr
import os

if __name__ == "__main__":
    if len(argv[1:]) != 2:
        stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        exit(1)
    elif os.path.exists(argv[1]) is False:
        stderr.write("Missing {}\n".format(argv[1]))
        exit(1)
    else:
        # print()
        exit(0)
