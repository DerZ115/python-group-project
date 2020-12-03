#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 09:25:26 2020

@author: annazoechner
"""


def mirror_string(s):
    """Mirrors string. Replaces characters that have counterparts, keeps the rest."""

    assert '\n' not in s

    # Create dictionary with counterparts
    cat_dict = {ord("/"): "\\", ord("\\"): "/", ord(")"): "(", ord("("): ")"}

    return s.translate(cat_dict)


def mirror(s):
    """Mirrors multi-line string. Breaks it up into strings, mirrors them,
    puts them back together.

    What about padding/alignment?
    """
    splitcat = s.split('\n')  # splits string into single lines

    mirror1 = [mirror_string(i) for i in splitcat]  # replaces /, ( with \, )
    mirror2 = [i[::-1] for i in mirror1]  # reverses each item of mirror 1
    mirror3 = [i.rjust(21, " ") for i in mirror2]  # aligns lines to the right

    mirrorcat = str.join('\n', mirror3)  # joins items to one string

    return mirrorcat


cat1 = r"""
                  _ 
                 / )
                ( (
  A.-.A  .-""-.  ) )
 / , , \/      \/ /
=\  t  ;=    /   /
  '--,'  .""|   /
      || |  \\ \
     ((,_|  ((,_\
"""

cat2 = r"""
                  _ 
                 / )
                ( (
  A.-.A  .-""-.  ) )
 / , , \/      \/ /
=\  t  ;=    /   /
  '--,'  .""|   /
      || |  \\ \
     ((,_|  ((,_\
"""

print("Cat 1:", mirror(cat1))
print("Cat 2:", mirror(cat2))
