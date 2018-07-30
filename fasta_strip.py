#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 29 21:19:01 2018
This program strips internal newline ('\n') characters from FASTA files to
make it compatible with MSTgold and other programs that interpret the newline
character as the end of the sequence. The program requires a filename as an
argument and the output file name as a second argument.
@author: Shannon
"""

import sys
import re

# input file name
filename = sys.argv[1].lstrip('-')
# output file name
outfile = sys.argv[2].lstrip('-')
out = open(outfile, 'w')
first_line = True
# holds the string representing the current sequence
seq = ''
# Reads through the file
for line in open(filename):
    # looks to see if this line represents a new entry
    m = re.match(r'>.*', line)
    if m:
        if first_line == False:
            out.write(seq + '\n')
            seq = ''
        out.write(line)
        first_line = False
    else:
        seq += line.strip('\n')
out.write(seq + '\n')
out.close()