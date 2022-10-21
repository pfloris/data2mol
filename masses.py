#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 17:04:01 2021

@author: pfloris
"""

import os

def write_masses(atomtypes_filename):
    wdir = os.path.dirname(atomtypes_filename)
    masses_filename = os.path.join(wdir, 'masses')
    masses_file = open(masses_filename, 'w')
    
    coeffs_filename = os.path.join(wdir, 'coeffs')
    coeffs_file = open(coeffs_filename, 'r')
    coeffs_lines = coeffs_file.readlines()
    
    atomtypes_file = open(atomtypes_filename, 'r')
    atomtypes_lines = atomtypes_file.readlines()
    
    masses_dict = {}
    for line in coeffs_lines:
        l = line.split()
        if(l != [] and l[0] == 'mass'):
            masses_dict[l[1]] = l[2]

    for line in atomtypes_lines:
        l = line.split()
        atom_id = l[0]
        atom_type = l[1]
        mass = atom_id + ' ' + masses_dict[atom_type] + '\n'
        masses_file.write(mass)
    return masses_filename
