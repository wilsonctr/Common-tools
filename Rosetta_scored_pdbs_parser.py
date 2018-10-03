import os
import pandas as pd

design_name = []
label = '''fa_atr fa_rep fa_sol fa_intra_rep fa_intra_sol_xover4 lk_ball_wtd fa_elec pro_close hbond_sr_bb hbond_lr_bb hbond_bb_sc hbond_sc dslf_fa13 omega fa_dun p_aa_pp yhh_planarity ref rama_prepro total'''.split()
df = pd.DataFrame(columns=label)

for i in os.listdir('./'):
    if i[-4:] == '.pdb':
        with open(i, 'r') as f:
            design_name.append(i)
            for line in f.readlines():
                if 'pose' in line:
                    df = df.append(pd.Series([float(j) for j in line.split()[1:]], index=label), ignore_index=True)

df['Design_names'] = design_name
df.set_index('Design_names').sort_values('total')
