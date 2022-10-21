#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 14:16:30 2021

@author: ponneso
"""

from math import nan
import os

def write_impropers(data_filename, data_lines):
    wdir = os.path.dirname(data_filename)
    impropers_filename = os.path.join(wdir, 'impropers')
    impropers_file = open(impropers_filename, 'w')
    
    index = nan
    for i in range(0, len(data_lines)):
        l = data_lines[i].split()
        if(len(l) == 2 and l[1] == 'impropers'):
            n_impropers = int(l[0])
        if(l != [] and l[0] == 'Impropers'):
            index = i + 2
            max_index = index + n_impropers
        if(i >= index and i < max_index):
            improper_id = l[0]
            improper_type = l[1]
            atom_id1 = l[2]
            atom_id2 = l[3]
            atom_id3 = l[4]
            atom_id4 = l[5]
            
            improper_str = improper_id + ' ' + improper_type + ' ' + atom_id1 + ' ' + atom_id2 + ' ' + atom_id3 + ' ' + atom_id4
            impropers_file.write(improper_str)
            impropers_file.write('\n')
    return impropers_filename, n_impropers
