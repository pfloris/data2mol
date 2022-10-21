#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 13:37:26 2021

@author: pfloris
"""

import os

from angles import write_angles
from atom_types import write_atomtypes
from bonds import write_bonds
from charges import write_charges
from coords import write_coords
from dihedrals import write_dihedrals
from impropers import write_impropers
from masses import write_masses

def main():
    atom_style = input('What is your target atom_style?\n' +
                       'Possible options: full, molecular\n')
    rel_path = input('Insert relative or full path of the LAMMPS datafile you want to convert:\n')
    data_filename = os.path.realpath(rel_path)  #get absolute path from relative path
    
    #Read the LAMMPS data file and extract the lines
    data_file = open(data_filename, 'r')
    data_lines = data_file.readlines()
    
    #Write sections of molecule file
    if(atom_style == 'full'):
        angles_filename, n_angles = write_angles(data_filename, data_lines)
        atomtypes_filename = write_atomtypes(data_filename, data_lines)
        bonds_filename, n_bonds = write_bonds(data_filename, data_lines)
        charges_filename = write_charges(data_filename, data_lines)
        coords_filename, n_atoms = write_coords(data_filename, data_lines)
        dihedrals_filename, n_dihedrals = write_dihedrals(data_filename, data_lines)
        impropers_filename, n_impropers = write_impropers(data_filename, data_lines)
        masses_filename = write_masses(atomtypes_filename)
        
        angles_file = open(angles_filename, 'r')
        atomtypes_file = open(atomtypes_filename, 'r')
        bonds_file = open(bonds_filename, 'r')
        charges_file = open(charges_filename, 'r')
        coords_file = open(coords_filename, 'r')
        dihedrals_file = open(dihedrals_filename, 'r')
        impropers_file = open(impropers_filename, 'r')
        masses_file = open(masses_filename, 'r')
    
    if(atom_style == 'molecular'):
        angles_filename, n_angles = write_angles(data_filename, data_lines)
        atomtypes_filename = write_atomtypes(data_filename, data_lines)
        bonds_filename, n_bonds = write_bonds(data_filename, data_lines)
        coords_filename, n_atoms = write_coords(data_filename, data_lines)
        dihedrals_filename, n_dihedrals = write_dihedrals(data_filename, data_lines)
        impropers_filename, n_impropers = write_impropers(data_filename, data_lines)
        masses_filename = write_masses(atomtypes_filename)
        
        angles_file = open(angles_filename, 'r')
        atomtypes_file = open(atomtypes_filename, 'r')
        bonds_file = open(bonds_filename, 'r')
        coords_file = open(coords_filename, 'r')
        dihedrals_file = open(dihedrals_filename, 'r')
        impropers_file = open(impropers_filename, 'r')
        masses_file = open(masses_filename, 'r')
    
    wdir = os.path.dirname(data_filename)
    mol_filename = os.path.join(wdir, 'molecule')
    mol_file = open(mol_filename, 'a')
    
    print('LAMMPS Molecule file\n', file=mol_file)
    print(n_atoms, 'atoms', file=mol_file)
    print(n_bonds, 'bonds', file=mol_file)
    print(n_angles, 'angles', file=mol_file)
    print(n_dihedrals, 'dihedrals', file=mol_file)
    print(n_impropers, 'impropers', file=mol_file)
    
    print('\nCoords\n', file=mol_file)
    mol_file.write(coords_file.read())
    
    print('\nTypes\n', file=mol_file)
    mol_file.write(atomtypes_file.read())
    
    print('\nCharges\n', file=mol_file)
    mol_file.write(charges_file.read())
    
    print('\nMasses\n', file=mol_file)
    mol_file.write(masses_file.read())
    
    print('\nBonds\n', file=mol_file)
    mol_file.write(bonds_file.read())
    
    print('\nAngles\n', file=mol_file)
    mol_file.write(angles_file.read())
    
    print('\nDihedrals\n', file=mol_file)
    mol_file.write(dihedrals_file.read())
    
    print('\nImpropers\n', file=mol_file)
    mol_file.write(impropers_file.read())
    
    mol_file.close()

if __name__ == '__main__':
    main()
