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
        with open(argv[1]) as md:
            for line in md:
                if line.startswith("#"):
                    # line.strip()
                    with open(argv[2], "a") as htl:
                        if line.count("#") <= 6:
                            (htl.write(line
                                       .replace("# ", "#")
                                       .strip()
                                       .replace("#"*line.count("#"),
                                                "<h{}>".format(line
                                                               .count(
                                                                      "#"
                                                                     )
                                                               )
                                                ) + "</h{}>\n"
                                                    .format(line
                                                            .count("#")
                                                            )))
        exit(0)
