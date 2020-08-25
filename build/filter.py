#!/Users/zietzm/miniconda3/envs/manubot/bin/python3.7
"""
Panflute filter to allow file includes

Each include statement has its own line and has the syntax:

    $include ../somefolder/somefile

Each include statement must be in its own paragraph. That is, in its own line
and separated by blank lines.
"""

import os
import panflute as pf


def is_include_line(elem):
    if len(elem.content) < 3:
        return False
    elif not all (isinstance(x, (pf.Str, pf.Space)) for x in elem.content):
        return False
    elif elem.content[0].text != '$include':
        return False
    elif type(elem.content[1]) != pf.Space:
        return False
    else:
        return True


def get_filename(elem):
    return pf.stringify(elem, newlines=False).split(maxsplit=1)[1]


def action(elem, doc):
    if isinstance(elem, pf.Para) and is_include_line(elem):
        fn = get_filename(elem)
        if not os.path.isfile(fn):
            return
        with open(fn) as f:
            raw = f.read()
        new_elems = pf.convert_text(raw)
        return new_elems


def main(doc=None):
    return pf.run_filter(action, doc=doc)


if __name__ == '__main__':
    main()
