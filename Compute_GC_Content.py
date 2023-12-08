# Problem 5: Computing GC Content
# https://rosalind.info/problems/gc/

# Attempt Number 1:
def compute_GC_content(dna):
  if dna is not None:
    return (dna.count("G") + dna.count("C"))*100 / len(dna) # return the gc ratio
  else:
    pass

def parse_fasta(f_path):
  file_path = f_path
  with open(file_path, 'r') as file:
    fasta_dictionary = {}
    current_key = ""
    dna_string = ""
    list_of_gc_ratios = []
    # the dictionary will be of the form {header: [dna_string, gc_ratio]}

    for line in file:
      line = line.strip()
      #if there is a '>', store the text from there up to the end of the line as a dict key
      if line.startswith(">"):
        current_key = line[1:]
        fasta_dictionary[current_key] = ["",0]  # placeholder values for dict
      # If there is no >, store the dna string
      # this accounts for newlines that have more dna string
      # this keeps going, additively, until we encounter the next >
      else:
        dna_string += line 
        fasta_dictionary[current_key][0] += line

    # Iterate over the existing dictionary items, compute the gc_ratio based on the dna_strand stored
    # store that gc_ratio as the second value in the dictionary list
    for key, value in fasta_dictionary.items():
      fasta_dictionary[key][1] = compute_GC_content(fasta_dictionary[key][0])

    # (header, gc_ratio) tuples stored in a list
    for key,value in fasta_dictionary.items():
      list_of_gc_ratios.append((key, value[1]))

    # reverse sort the list based on gc_ratio values
    list_of_gc_ratios = sorted(list_of_gc_ratios, key=lambda x: x[1], reverse=True)
    
    # print the highest value
    print(list_of_gc_ratios[0][0],list_of_gc_ratios[0][1], sep = "\n")

parse_fasta("data/rosalind_gc.txt")