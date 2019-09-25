def pdb_to_fasta(input_file):
    
    file_name = str(input_file).replace('.pdb','')
    input_file = open(input_file)
    letters = {'ALA':'A','ARG':'R','ASN':'N','ASP':'D','CYS':'C','GLU':'E','GLN':'Q','GLY':'G','HIS':'H',
               'ILE':'I','LEU':'L','LYS':'K','MET':'M','PHE':'F','PRO':'P','SER':'S','THR':'T','TRP':'W',
               'TYR':'Y','VAL':'V'}
    
    with open('%s.fasta'%str(file_name), 'w') as f:
        f.write('>%s\n'%file_name)
        prev = '-1'
        for line in input_file:
            toks = line.split()
            if len(toks) < 1: continue
            if toks[0] != 'ATOM': continue
            if toks[5] != prev:
                f.write('%c' % letters[toks[3]])
            prev = toks[5]
    
    input_file.close()
