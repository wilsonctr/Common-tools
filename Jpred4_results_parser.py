import os
import re
from Bio import SeqIO
import pandas as pd
from __future__ import division

# Parsing secondary structures from each sequence and store them in 
# a dictionary ss_dict

ss_dict = {}

for i in os.listdir('.'):
    
    if i[0:2] == 'jp':
        
        with open('%s/%s.fasta'%(i, i), 'r') as f1:
            Gene_name = f1.read().split('\n')[0].replace('>','').replace('_','')
            
        with open('%s/%s.simple.html'%(i, i), 'r') as f:
            results = f.read().split('<code>')[1].split('</code>')[0]
            ss = re.sub(r'<.+?>', '', results).split('\n')[1]
            
        ss_dict[Gene_name] = ss
        
 
