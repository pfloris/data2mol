#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 18:31:44 2021

@author: ponneso
"""

from math import nan
from natsort import natsorted
import os

def write_atomtypes(data_filename, data_lines):
    wdir = os.path.dirname(data_filename)
    atomtypes_filename = os.path.join(wdir, 'atom_types')
    atomtypes_file = open(atomtypes_filename, 'w')
    
    index = nan
    atomtypes_list = []
    for i in range(0, len(data_lines)):
        l = data_lines[i].split()
        if(len(l) == 2 and l[1] == 'atoms'):
            n_atoms = int(l[0])
        if(l != [] and l[0] == 'Atoms'):
            index = i + 2
            max_index = index + n_atoms
        if(i >= index and i < max_index):
            atom_id = l[0]
            atom_type = l[2]
            
            atomtypes_str = atom_id + ' ' + atom_type
            atomtypes_list.append(atomtypes_str)
            
    for line in natsorted(atomtypes_list):
        atomtypes_file.write(line)
        atomtypes_file.write('\n')
    
    return atomtypes_filename
