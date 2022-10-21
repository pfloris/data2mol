#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 14:13:40 2021

@author: ponneso
"""

from math import nan
import os

def write_dihedrals(data_filename, data_lines):
    wdir = os.path.dirname(data_filename)
    dihedrals_filename = os.path.join(wdir, 'dihedrals')
    dihedrals_file = open(dihedrals_filename, 'w')
    
    index = nan
    for i in range(0, len(data_lines)):
        l = data_lines[i].split()
        if(len(l) == 2 and l[1] == 'dihedrals'):
            n_dihedrals = int(l[0])
        if(l != [] and l[0] == 'Dihedrals'):
            index = i + 2
            max_index = index + n_dihedrals
        if(i >= index and i < max_index):
            dihedral_id = l[0]
            dihedral_type = l[1]
            atom_id1 = l[2]
            atom_id2 = l[3]
            atom_id3 = l[4]
            atom_id4 = l[5]
            
            dihedral_str = dihedral_id + ' ' + dihedral_type + ' ' + atom_id1 + ' ' + atom_id2 + ' ' + atom_id3 + ' ' + atom_id4
            dihedrals_file.write(dihedral_str)
            dihedrals_file.write('\n')
    return dihedrals_filename, n_dihedrals
