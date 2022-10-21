#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 18:46:19 2021

@author: pfloris
"""

from math import nan
from natsort import natsorted
import os

def write_charges(data_filename, data_lines):
    wdir = os.path.dirname(data_filename)
    charges_filename = os.path.join(wdir, 'charges')
    charges_file = open(charges_filename, 'w')
    
    index = nan
    charges_list = []
    for i in range(0, len(data_lines)):
        l = data_lines[i].split()
        if(len(l) == 2 and l[1] == 'atoms'):
            n_atoms = int(l[0])
        if(l != [] and l[0] == 'Atoms'):
            index = i + 2
            max_index = index + n_atoms
        if(i >= index and i < max_index):
            atom_id = l[0]
            charge = l[3]
            
            charges_str = atom_id + ' ' + charge
            charges_list.append(charges_str)
            
    for line in natsorted(charges_list):
        charges_file.write(line)
        charges_file.write('\n')
    return charges_filename
