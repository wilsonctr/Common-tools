from urllib2 import urlopen

class Uniprot_parse(object):
    
    def __init__( self , uniprot_id):
        xml = urllib2.urlopen('http://www.uniprot.org/uniprot/%s.xml' % uniprot_id)
        fasta = urllib2.urlopen('http://www.uniprot.org/uniprot/%s.fasta' % uniprot_id)
        self.record = str(SeqIO.read(xml, 'uniprot-xml')).split('\n')
        self.id = self.record[0].split(' ')[1]
        self.full_id = self.record[1].split(' ')[1]
        self.description = ' '.join(self.record[2].split(' ')[1:])
        
        for i in SeqIO.parse(fasta, 'fasta'): self.sequence = str(i.seq)   
            
        for item in self.record:
            if item.split('=')[0] == '/organism':
                self.organism = item.split('=')[1]
            if item.split('=')[0] == '/taxonomy':
                self.taxonomy = eval(item.split('=')[1])
            if item.split(':')[0] == 'Database cross-references':
                pdb_list = []
                for i in item.split(','):
                    if i.split(':')[0] == ' PDB':
                        pdb_list.append(i.split(':')[1])
                self.pdb = pdb_list

                interpro_list = []
                for i in item.split(','):
                    if i.split(':')[0] == ' InterPro':
                        interpro_list.append(i.split(':')[1])
                self.interpro_id = interpro_list
                
                supfam_list = []
                for i in item.split(','):
                    if i.split(':')[0] == ' SUPFAM':
                        supfam_list.append(i.split(':')[1])
                self.supfam_id = supfam_list
                
                pfam_list = []
                for i in item.split(','):
                    if i.split(':')[0] == ' Pfam':
                        pfam_list.append(i.split(':')[1])
                self.pfam_id = pfam_list
