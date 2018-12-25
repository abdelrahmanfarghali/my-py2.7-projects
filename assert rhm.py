import sys
import readline

def remove_tmlh_m(s):
    tag = False
    quote = False
    out = ""

    for c in s:
        if c == '<' and not quote:
            tag = True
        elif c == '>' and not quote:
            tag = False
        elif c == '"' or c == "'" and tag:
                quote = not quote
        elif not tag:
            out = out + c

    assert out.find('<') == -1
    return out
