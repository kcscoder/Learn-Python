"""
Codecademy < Learn Python 
12 File Input and Output
========================================================
DNA Analysis 
========================================================
Scenario:
    A spy deleted important files from a computer. There were a
    few wtinesses at the scene of the crime, but no one is sure 
    who exactly the spy was. Three possible suspects were 
    apprehended based on surveillance video. Each suspect had a 
    sample of DNA taken from them. The computer's keyboard was 
    also swabbed for DNA evidence and, luckily, one small DNA 
    sample was successfully retrieved from the computer's keyboard. 

    Given the three suspects's DNA and the sample DNA retrieved
    from the keyboard, it's up to you to figure out who the spy 
    is!

    The project should have methods for each of the following:
        - Given a file, read in the DNA for each suspect and 
          save it as a string. 
        - Take a DNA string and plsit into a list of codons.
        - Iterate through a suspect's codon list to see how many 
          of their codons match the sample codons.
        - Pick the right suspect to continue the investigation 
          on. 

"""
sample = ['GTA','GGG','CAC']


def read_dna(dna_file):
    dna_data = ""
  
    with open(dna_file,"r") as f:
        for line in f:
            dna_data += line
    return dna_data


def dna_codons(dna):
    codons = []
  
    for i in range(0,len(dna),3):
        if (i+3 < len(dna)):
            codons.append(dna[i:i+3])
    return codons

def match_dna(dna):
    matches = 0
    for codon in dna:
        if (codon in sample):
            matches += 1
    return matches


def is_criminal(dna_sample):
    dna_data = read_dna(dna_sample)
    codons = dna_codons(dna_data)
    num_matches = match_dna(codons)
  
    if (num_matches >= 3):
        print "There are %d matches. Suspicious!" % (num_matches)
    else: 
        print "There are only %d matches. This is not the person we want. " % (num_matches)
    
def main():
    is_criminal('suspect1.txt')
    is_criminal('suspect2.txt')
    is_criminal('suspect3.txt')

if __name__=="__main__":
    main()
