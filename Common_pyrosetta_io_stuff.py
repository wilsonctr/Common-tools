#Only keep top ten lowest energy pdbs                                                 
energies_dict = {}
for i in os.listdir('results/.'):
    if i[-4:] == '.pdb':
        with open('results/%s'%i, 'r') as f:
            for j in f.readlines():
                if j[0:4] == 'pose':
                    energies_dict[i] = float(j.split()[-1])

top_pdbs = []
for top_pdb in sorted(energies_dict.iteritems(), key=operator.itemgetter(1))[0:100]:
    top_pdbs.append(top_pdb[0])

for i in os.listdir('results/'):
    if i in top_pdbs:
        pass
    else:
        os.system('rm results/%s'%i)
