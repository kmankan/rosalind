# Problem 6: Counting Point Mutations
# https://rosalind.info/problems/hamm/

def countPointMutations(file_path):
  dna = [] # a list to store each strand of dna
  hamming_distance = 0

  with open(file_path, 'r') as file:
      for line in file:
          dna.append(line.strip()) # add each dna line to the list
      
      s,t = dna[0], dna[1] # create two variables representing the strands

      # we know the length of each strand
      # iterate over each letter in each strand and compare whether they are the same
      # if not the same, increase hamming distance by 1

      # approach 1
      for i in range(len(s)):
          if s[i] != t[i]:
              hamming_distance += 1 

      # approach 2
      for a,b in zip(s,t):
          if a != b:
              hamming_distance += 1

  print(hamming_distance)

countPointMutations('data/rosalind_hamm.txt')