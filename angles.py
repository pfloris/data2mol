#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 12:50:41 2021

@author: pfloris
"""

from math import nan
import os

def write_angles(data_filename, data_lines):
    wdir = os.path.dirname(data_filename)
    angles_filename = os.path.join(wdir, 'angles')
    angles_file = open(angles_filename, 'w')
    
    index = nan
    for i in range(0, len(data_lines)):
        l = data_lines[i].split()
        if(len(l) == 2 and l[1] == 'angles'):
            n_angles = int(l[0])
        if(l != [] and l[0] == 'Angles'):
            index = i + 2
            max_index = index + n_angles
        if(i >= index and i < max_index):
            angle_id = l[0]
            angle_type = l[1]
            atom_id1 = l[2]
            atom_id2 = l[3]
            atom_id3 = l[4]
            
            angle_str = angle_id + ' ' + angle_type + ' ' + atom_id1 + ' ' + atom_id2 + ' ' + atom_id3
            angles_file.write(angle_str)
            angles_file.write('\n')
    return angles_filename, n_angles
