#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 12:27:44 2021

@author: ponneso
"""

from math import nan
import os

def write_bonds(data_filename, data_lines):
    wdir = os.path.dirname(data_filename)
    bonds_filename = os.path.join(wdir, 'bonds')
    bonds_file = open(bonds_filename, 'w')
    
    index = nan
    for i in range(0, len(data_lines)):
        l = data_lines[i].split()
        if(len(l) == 2 and l[1] == 'bonds'):
            n_bonds = int(l[0])
        if(l != [] and l[0] == 'Bonds'):
            index = i + 2
            max_index = index + n_bonds
        if(i >= index and i < max_index):
            bond_id = l[0]
            bond_type = l[1]
            atom_id1 = l[2]
            atom_id2 = l[3]
            
            bond_str = bond_id + ' ' + bond_type + ' ' + atom_id1 + ' ' + atom_id2
            bonds_file.write(bond_str)
            bonds_file.write('\n')
    return bonds_filename, n_bonds
