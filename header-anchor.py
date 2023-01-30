#!/usr/bin/env python3

from panflute import *

def anchor(elem, doc):
    anchor_str = doc.get_metadata('header_anchor_str', '¶')
    return Link(Str(anchor_str), url="#" + elem.identifier)

def append_anchor(elem, doc):
    elem.content.append(Str(' '))
    elem.content.append(anchor(elem, doc))
    return elem

def prepend_anchor(elem, doc):
    elem.content.insert(0, Str(' '))
    elem.content.insert(0, anchor(elem, doc))
    return elem

def append_anchor_to_header(elem, doc):
    if type(elem) == Header:
        side = doc.get_metadata('header_anchor_side', 'left')
        if side == 'left':
            elem = prepend_anchor(elem, doc)
        elif side == 'right':
            elem = append_anchor(elem, doc)
        else:
            raise ValueError('Expected: \'left\' | \'right\'. Got: \'' + side + '\'')
        return elem

def main(doc=None):
    return run_filter(append_anchor_to_header, doc=doc)

if __name__ == '__main__':
    main()
