# Problem 3: Complementing a Strand of DNA
# https://rosalind.info/problems/revc/

# Question: Given a DNA string s, find the reverse complement s^ of s

file_path = 'data/rosalind_revc.txt'
with open(file_path, 'r') as file:
  strand = file.read()

def reverse_complement(strand):
  translation_table = str.maketrans({"A":"T", "T":"A", "C":"G", "G":"C"})
  reversedStrand = strand[::-1]
  complementStrand = reversedStrand.translate(translation_table)

  print(complementStrand)

reverse_complement(strand)

# A more elegant solution:
# print(strand[::-1].translate(maketrans('ACGT', 'TGCA')))