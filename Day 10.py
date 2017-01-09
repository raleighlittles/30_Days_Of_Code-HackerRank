#!/bin/python

import sys


n = int(raw_input())
dec_int = bin(n)
dec_int = dec_int[2:]
max_count, current_count = 0, 0
for i in range(len(dec_int)):
    if (dec_int[i] == '1'):
        current_count = current_count + 1
        if (current_count > max_count):
            max_count = current_count
    else:
        current_count = 0
        
print max_count