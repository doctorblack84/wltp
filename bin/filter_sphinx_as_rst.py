#!/usr/bin/python3
"""
Sed-file to clean-up Sphinx-only constructs (ie from README.rst),
so that *PyPi* can format it properly.

To check for remaining errors, install ``sphinx`` and run::

        python setup.py --long-description | sed -file 'this_file.sed' | rst2html.py  --halt=warning

"""

from __future__ import division, print_function, unicode_literals

import re
import sys, io


def clean_sphinx_only_markup(file_inp=None, file_out=None):
    """
    :param file_inp:     a `filename` or ``sys.stdin``?
    :param file_out:     a `filename` or ``sys.stdout`?`

    """
    substs = [
        ## Selected Sphinx-only Roles.
        #
        (r':abbr:`([^`]+)`',        r'\1'),
        (r':ref:`([^`]+)`',         r'`\1`_'),
        (r':term:`([^`]+)`',        r'**\1**'),
        (r':dfn:`([^`]+)`',         r'**\1**'),
        (r':(samp|guilabel|menuselection):`([^`]+)`',        r'``\2``'),


        ## Sphinx-only roles:
        #        :foo:`bar`   --> foo(``bar``)
        #        :a:foo:`bar` XXX afoo(``bar``)
        #
        #(r'(:(\w+))?:(\w+):`([^`]*)`', r'\2\3(``\4``)'),
        (r':(\w+):`([^`]*)`', r'\1(``\2``)'),


        ## Sphinx-only Directives.
        #
        (r'\.\. +doctest',           r'code-block'),
        (r'\.\. +plot::',            r'.. '),
        (r'\.\. +seealso',           r'info'),
        (r'\.\. +glossary',          r'rubric'),
        (r'\.\. +figure::',          r'.. '),


        ## Other
        #
        (r'\|version\|',              r'x.x.x'),
    ]

    regex_subs = [ (re.compile(regex, re.IGNORECASE), sub) for (regex, sub) in substs ]

    def clean_line(line):
        try:
            for (regex, sub) in regex_subs:
                line = regex.sub(sub, line)
        except Exception as ex:
            print("ERROR: %s, (line(%s)"%(regex, sub))
            raise ex

        return line

    if not file_inp:
        file_inp = sys.stdin
    if not file_out:
        file_out = sys.stdout

    with io.open(file_inp) if isinstance(file_inp, str) else file_inp as fd_in:
        with io.open(file_out) if isinstance(file_out, str) else file_out as fd_out:
            line = fd_in.readline()
            while line:
                line = clean_line(line)
                print(line, file=fd_out, end='')
                line = fd_in.readline()



if __name__ == '__main__':
    clean_sphinx_only_markup(*sys.argv[1:])
