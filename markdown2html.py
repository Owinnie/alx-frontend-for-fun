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
            with open(argv[2], "a") as htl:
                type_of_ls = ""
                for line in md:

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
                        type_of_ls = "ul"
                        (htl.write(line
                                   .replace("- ", "-")
                                   .strip()
                                   .replace("-", "<li>") + "</li>\n"))

                    # ordered lists

                    if line.startswith("*"):
                        type_of_ls = "ol"
                        (htl.write(line
                                   .replace("* ", "*")
                                   .strip()
                                   .replace("*", "<li>") + "</li>\n"))

                    # paragraphs

                        # ... Coming soon ...
            if type_of_ls == "ul":
                with open(argv[2], "r") as h:
                    cont = h.readlines()

                # First occurrence of <li>
                str_cont = " ".join(cont)
                index = str_cont.find("<li>")
                nstr_cont = str_cont[:index] + "<ul>\n " + str_cont[index:]
                cont = list(nstr_cont.split(" "))

                # Last occurence of </li>
                str_cont = " ".join(cont)
                index = str_cont.rfind("</li>")
                nstr_cont = (str_cont[:index+len("</li>\n")] +
                             "</ul>\n " + str_cont[index+len("</li>\n"):])
                cont = list(nstr_cont.split(" "))

                with open(argv[2], "w") as h:
                    cont = " ".join(cont)
                    h.write(cont)

            elif type_of_ls == "ol":
                with open(argv[2], "r") as h:
                    cont = h.readlines()

                # First occurrence of <li>
                str_cont = " ".join(cont)
                index = str_cont.find("<li>")
                nstr_cont = str_cont[:index] + "<ol>\n " + str_cont[index:]
                cont = list(nstr_cont.split(" "))

                # Last occurence of </li>
                str_cont = " ".join(cont)
                index = str_cont.rfind("</li>")
                nstr_cont = (str_cont[:index+len("</li>\n")] +
                             "</ol>\n " + str_cont[index+len("</li>\n"):])
                cont = list(nstr_cont.split(" "))

                with open(argv[2], "w") as h:
                    cont = " ".join(cont)
                    h.write(cont)
        exit(0)
