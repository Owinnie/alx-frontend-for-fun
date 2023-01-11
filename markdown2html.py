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
            # ls = []
            for line in md:
                ls = []
                with open(argv[2], "a") as htl:

                    # Headings

                    if line.startswith("#"):
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
                    
                    # unordered lists

                    if line.startswith("-"):
                        ls.append(line)

                    for ln in ls:
                        (htl.write(ln
                                   .replace("- ", "-")
                                   .strip()
                                   .replace("-", "<li>") + "</li>\n"))
        with open(argv[2], "r") as h:
            cont = h.readlines()

        cont.insert(1, "<ul>\n")
        cont.append("</ul>\n")

        with open(argv[2], "w") as h:
            cont = "".join(cont)
            h.write(cont)
        exit(0)
