# Problem 1: Counting DNA Nucleotides
# https://rosalind.info/problems/dna/

def countNucleotides(dna):
  dict = {"A":0, "C":0, "G":0, "T":0} #Harcode dictionary with A,C,G,T keys
  for nt in dna:
    if nt in dict:
      dict[nt] += 1 # increment value if it is found in list of nt's

  print(*list(dict.values()))

countNucleotides(input())

''' 
An alternative approach that is much faster computationally

Code:
print(*map(input().count, "ACGT"))

Explanation:
- map(input().count, "ACGT"): This applies input().count to each of 'A', 'C', 'G', and 'T'. 
It counts how many times each of these nucleotides appears in the DNA string entered by the user.
- * (Unpacking Operator): The asterisk * is used to unpack the map object. 
This turns the map object into individual elements.
'''