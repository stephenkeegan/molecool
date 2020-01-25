"""
Functions for manipulating pdb files.
"""

import numpy as np


def open_pdb(file_location):
    with open(file_location) as f:
        data = f.readlines()
    
    coordinates = []
    symbols = []
    
    for line in data:
        if 'ATOM' in line[0:6] or 'HETATM' in line[0:6]:
            symbols.append(line[76:79].strip())
            
            atom_coordinates = [float(x) for x in line[30:55].split()]
            coordinates.append(atom_coordinates)

    # convert lits to numpy array        
    coordinates = np.array(coordinates)
    symbols = np.array(symbols)

    return symbols, coordinates