# Problem 2: Transcribing DNA into RNA
# https://rosalind.info/problems/rna/

# Solution 1:
file_path = 'data/rosalind_rna.txt'
with open(file_path, 'r') as file:
  data = list(file.read())

for index, char in enumerate(data):
  if char == "T":
    data[index] = "U"

print(''.join(data))

# Solution 2: (more efficient; it read the file into memory as a string and uses the built-in
# replace method. Much faster than using a list which is memory intensive.
file_path = 'data/rosalind_rna.txt'
with open(file_path, 'r') as file:
  transcribe_data = file.read().replace("T","U")
  print(transcribe_data)

# Alternative solution that is better for very large datasets
# It reads each line of the file and does a replace and prints immediately before moving on to next line
'''
file_path = 'data/rosalind_rna.txt'
with open(file_path, 'r') as file:
    for line in file:
        transcription = line.replace('T', 'U')
        print(transcription, end='')
'''

