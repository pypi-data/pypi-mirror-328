'''
SPDX-License-Identifier: GPL-3.0-or-later
Copyright (C) 2023 Andre Zettel <musipadcom@gmail.com>

Demonstration of mbdyn-lexer plugin.

Usage:
From within examples folder of source package with
files:

exam17.py  # this file
exam17_body.sub
exam17_joint.sub
exam17_nlink_pendulum.mbd
exam17_node.sub

run the script:
 
python exam17.py checkfiles
python exam17.py stripcomments


Examples for pygmentize (pygments command line tool):

# check if lexer is installed
pygmentize -H lexer mbdyn

# output highlight in terminal
pygmentize exam17_nlink_pendulum.mbd

# output stand alone html
pygmentize -l mbdyn -O full,style=emacs,linenos="table",debug_token_types -o exam17_nlink_pendulum.html exam17_nlink_pendulum.mbd 
'''
import sys
from pygments.lexers import get_lexer_by_name
from pygments.token import Token
from pathlib import Path


LEXER = get_lexer_by_name("mbdyn")
FILE = "exam17_nlink_pendulum.mbd"


def create_the_generator():
    with Path(FILE).open() as f:
        inputfile = f.read()
    return LEXER.get_tokens(inputfile)


def collect_double_quote_strings_from_includes(t):
    subfiles = set()
    for ttyp, tstr in t:
        if ttyp == Token.Generic.Strong and tstr.strip() == "include:":
            ttyp, tstr = t.__next__()
            if ttyp == Token.Literal.String.Double:
                subfiles.add(tstr.strip()[1:-1])
    return subfiles


def check_file_existence(s):
    for subfile in s:
        path = Path(subfile)
        if path.is_file():
            print("File found: ", path)
        else:
            print("File missing: ", path)


def check_mbd_include_filepaths():
    token = create_the_generator()
    subfilenames = collect_double_quote_strings_from_includes(token)
    check_file_existence(subfilenames)


def show_stripped_version():
    to_strip = [
        Token.Comment.Single,
        Token.Comment.Multiline,
        Token.Error]
    
    token = create_the_generator()

    stripped_input = []
    for ttyp, tstr in token:
        if ttyp not in to_strip:
            stripped_input.append(tstr)

    print(''.join(stripped_input))
    return


def main():
    if len(sys.argv) == 2:
        arg = sys.argv[1]
        
        if arg == "checkfiles":
            check_mbd_include_filepaths()

        elif arg == "stripcomments":
            show_stripped_version()
            
        else:
            print(__doc__)
    else:
        print(__doc__)


if __name__ == "__main__":
    main()
    