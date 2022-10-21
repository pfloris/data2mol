#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 13:55:00 2021

@author: ponneso
"""

from math import nan
from natsort import natsorted
import os

def write_coords(data_filename, data_lines):
    wdir = os.path.dirname(data_filename)
    coords_filename = os.path.join(wdir, 'coords')
    coords_file = open(coords_filename, 'w')
    
    index = nan
    coords_list = []
    for i in range(0, len(data_lines)):
        l = data_lines[i].split()
        if(len(l) == 2 and l[1] == 'atoms'):
            n_atoms = int(l[0])
        if(l != [] and l[0] == 'Atoms'):
            index = i + 2
            max_index = index + n_atoms
        if(i >= index and i < max_index):
            atom_id = l[0]
            x_crd = l[4]
            y_crd = l[5]
            z_crd = l[6]
            
            coord_str = atom_id + ' ' + x_crd + ' ' + y_crd + ' ' + z_crd
            coords_list.append(coord_str)
            
    for line in natsorted(coords_list):
        coords_file.write(line)
        coords_file.write('\n')
    
    return coords_filename, n_atoms
