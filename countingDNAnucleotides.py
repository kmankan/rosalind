# Problem 1: Counting DNA Nucleotides
# https://rosalind.info/problems/dna/

def countNucleotides(dna):
  dict = {"A":0, "C":0, "G":0, "T":0} #Harcode dictionary with A,C,G,T keys
  nucleotides = list(dna)
  for nt in nucleotides:
    if nt in dict:
      dict[nt] += 1 # increment value if it is found in list of nt's

  print(*list(dict.values()))

countNucleotides(input())
