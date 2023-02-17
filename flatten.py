#! usr/bin/env python3
"""
Flatten a list
 from http://rightfootin.blogspot.com/2006/09/more-on-python-flatten.html
Flat2 from Python Cookbook, recipe 4.14
"""

from collections import Iterable


def flatten(l, ltypes=(list, tuple, set)):
    ltype = type(l)
    l = list(l)
    i = 0
    while i < len(l):
        while isinstance(l[i], ltypes):
            if not l[i]:
                l.pop(i)
                i -= 1
                break
            else:
                l[i:i + 1] = l[i]
        i += 1
    return ltype(l)


def flat2(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from flat2(x, ignore_types)
        else:
            yield x


a = []
for i in range(20):
  a = [a, i]
a = flatten(a)

#   ___________my version

# def flatten(mylist):
#     flatlist = []
#     for x in mylist:
#         if type(x) == tuple or type(x) == list or type(x) == set:
#             for y in x:
#                 flatlist.append(y)
#         else:
#             flatlist.append(x)
#
#         if type(x) == list:
#             x = flatten(x)
#             continue
#
#     return flatlist
