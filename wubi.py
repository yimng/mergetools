#!/usr/bin/python
# -*- coding: utf-8 -*-
from collections import defaultdict

fh = open(r'2018_6_6.txt', encoding='utf16')
fh2 = open(r'xiuzhengban.txt', encoding='utf16')
lines = fh.read().splitlines() + fh2.read().splitlines()

d = defaultdict(set)
for line in lines:
    li = line.split(' ')
    # print(li)
    d[li[0]].update(set(li[1:]))


w = open(r'final.txt', 'w', encoding='utf16')
for k in d:
    w.write(k + ' ' + ' '.join(d[k]) + '\n')

