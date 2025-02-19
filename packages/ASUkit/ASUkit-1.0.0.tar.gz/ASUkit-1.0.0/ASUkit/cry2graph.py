import numpy as np
import ase
from ase.spacegroup import get_spacegroup
import os
import json
import copy
import warnings
import pkg_resources
from scipy import interpolate
from ._utility._funs import *
from .MatgenKit import matgen_xrdsim

class CrystalParser:
    """
    A parser class to process crystallographic data from an ASE database.
    
    This class extracts various graph-related data structures for use in graph neural networks.
    
    Reference:
        Cao, B., Anderson, D., & Davis, L. (2025). ASUGNN: an asymmetric-unit-based graph neural network for crystal property prediction.
        Applied Crystallography, 58(1). https://journals.iucr.org/paper?ei5123
    
    GitHub Repository:
        https://github.com/AI4Cr/ASUGNN/tree/main/paper
    
    Attributes:
        database (ase.db.connect): ASE database connection.
        entry_id (int): ID of the entry to be processed.
        cgcnn_emb (dict): Preloaded CGCNN atom embeddings.
    """
    def __init__(self, database, entry_id):
        """
        Initializes the CrystalParser with a given database and entry ID.
        
        Args:
            database (ase.db.connect): The database containing crystallographic structures.
            entry_id (int): The ID of the structure to be parsed.
        """
        self.database = ase.db.connect(database)
        self.entry_id = entry_id
        warnings.filterwarnings("ignore")
        _loc = pkg_resources.resource_filename('ASUkit', '')
        with open(os.path.join(_loc, 'CGCNN_atom_emb.json'), 'r') as file:
            self.cgcnn_emb = json.load(file)

    def get(self):
        """
        Extracts graph-related information from the crystal structure.
        
        Returns:
            tuple: (node_embedding, adjacency_matrix, distance_matrix, global_graph_info)
        """
        try:
            atoms = self.database.get_atoms(id=self.entry_id)
            G_latt_consts, _, c_atom = prim2conv(atoms)  # Convert to conventional lattice
            
            N_symbols = c_atom.get_chemical_symbols()
            G_spacegroup = get_spacegroup(c_atom).no
            G_latt_vol = c_atom.get_volume()
            G_ASUnum = c_atom.get_global_number_of_atoms()
            asu_atom_mass = c_atom.get_masses()
            G_mass = sum(asu_atom_mass)
            
            positions = c_atom.get_scaled_positions()
            if len(positions) > 500:
                return None  # Too large to process
            
            # Convert conventional lattice to asymmetric unit (ASU)
            asu_positions, asu_symbols, sites, kinds = conlattcell2asu(c_atom, positions, N_symbols)
            element_encode = symbol_to_atomic_number(asu_symbols)
            
            # Construct global feature vector
            global_info = [
                G_latt_consts[0], G_latt_consts[1], G_latt_consts[2], G_latt_consts[3],
                G_latt_consts[4], G_latt_consts[5], G_spacegroup, G_ASUnum, len(asu_positions),
                G_latt_vol, G_mass
            ]
            
            # Construct node embeddings (106-d)
            node_emd = []
            for index, code in enumerate(kinds):
                _code = element_encode[code]
                value = self.cgcnn_emb[str(_code)]
                node_emd.append(np.array(value + sites[index].tolist() + global_info))
            
            # Generate global graph information
            _, global_graph = matgen_xrdsim(atoms)
            
            # Compute distance and adjacency matrices
            distance_matrix = c_atom.get_all_distances()
            asu_dis_matrix = copy.deepcopy(distance_matrix)
            np.fill_diagonal(asu_dis_matrix, asu_dis_matrix.diagonal() + 1)
            asu_dis_matrix = 1 / asu_dis_matrix
            
            adj_matrix = copy.deepcopy(asu_dis_matrix)
            for i in range(len(kinds)):
                for j in range(len(kinds)):
                    if kinds[i] == kinds[j]:
                        adj_matrix[i, j] = 1
            
            adj_matrix = np.array(adj_matrix)
            adj_matrix[adj_matrix > 1.1] = 1.1  # Threshold for connections
            
            return np.array(node_emd), adj_matrix, distance_matrix, global_graph
        
        except Exception as e:
            print(f"An error occurred: crystal id = {self.entry_id}", e)
            return None

