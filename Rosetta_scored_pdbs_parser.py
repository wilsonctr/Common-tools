import os
import pandas as pd

design_name = []
ligand_energy = []
ligand_hbond_energy = []
total_constraint = []
label = '''fa_atr fa_rep fa_sol fa_intra_rep fa_intra_sol_xover4 lk_ball_wtd fa_elec pro_close hbond_sr_bb hbond_lr_bb hbond_bb_sc hbond_sc dslf_fa13 atom_pair_constraint coordinate_constraint angle_constraint dihedral_constraint omega fa_dun p_aa_pp yhh_planarity ref rama_prepro total'''.split()
label_1 = '''fa_atr fa_rep fa_sol fa_intra_rep fa_intra_sol_xover4 lk_ball_wtd fa_elec pro_close hbond_sr_bb hbond_lr_bb hbond_bb_sc hbond_sc dslf_fa13 omega fa_dun p_aa_pp yhh_planarity ref rama_prepro total'''.split()

df = pd.DataFrame(columns=label)

for i in os.listdir('./'):
    if i[-4:] == '.pdb':
        with open(i, 'r') as f:
            design_name.append(i)
            for line in f.readlines():
                if 'pose' in line:
                    df = df.append(pd.Series([float(j) for j in line.split()[1:]], index=label), ignore_index=True)
                if 'NMN_' in line:
                    ligand_energy.append(float(line.split()[-1]))
                if 'NMN_' in line:
                    ligand_hbond_energy.append(float(line.split()[11]))
                    
df['Design_names'] = design_name
df['Ligand_energy'] = ligand_energy
df['Ligand_hbond_energy'] = ligand_hbond_energy
df = df.set_index('Design_names')

def parse_totE_from_scored_pdbs(folder):
    
    df = pd.DataFrame()
    energy_list = []
    name_list = []
    
    def total_energy_in_scored_pdb(pdb_file):
    
        with open(pdb_file, 'r') as f:
            pdb_file = f.read().split('\n')
        line = [i for i in pdb_file if 'pose' in i]
        total_energy = line[0].split()[-1]

        return total_energy
    
    for pdb in os.listdir(folder):
        if pdb[-4:] == '.pdb':
            energy = total_energy_in_scored_pdb('%s/%s'%(folder, pdb))
            name_list.append(pdb)
            energy_list.append(float(energy))
            
    df['PDB_name'] = name_list
    df['energy_list'] = energy_list
    df = df.sort_values('energy_list')
    
    return df
