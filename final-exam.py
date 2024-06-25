def num_records() :
    """returns the number of records/sequences in the FASTA file"""
    f = open("dna.example.fasta")
    count = 0
    for line in f:
        if line[0] == '>':
            count += 1

    return count

def sequence_lens() :
    """finds lengths of all sequences"""
    f = open("dna.example.fasta")
    count = 0
    sequence = ""
    counter = []

    for line in f:
        if line[0] == '>':
            sequence = sequence.replace("\n", "")
            #print(count, " : ", len(sequence))
            counter.append(len(sequence))
            count += 1
            sequence = ""

        else:
            sequence += line
    
    sequence = sequence.replace("\n", "")
    #print(count, " : ", len(sequence))
    counter.append(len(sequence))

    return counter

def longest_len() :
    """returns longest dna sequence length"""
    print("longest: ", max(sequence_lens()))

def shortest_len() :
    """returns shortest dna sequence length"""
    seq = sequence_lens()
    seq.pop(0)
    print("shortest: ", min(seq))

def split_dna_into_codons(reading_frame, sequence) :
    """
    splits each dna sequence into codon triplets
    """    
    codon_array = []

    for i in range (reading_frame - 1, len(sequence), 3) :
        codon_array.append(sequence[i:i+3])

    return codon_array;

def get_specific_sequence(record_number) :
    """get the specific sequence given a record number 1 - 18"""
    f = open("dna.example.fasta")
    count = 0;
    sequence = ""

    for line in f :
        if line[0] == '>' and count == record_number :
            sequence = sequence.replace("\n", "")
            return sequence
        
        elif line[0] == ">" :
            count += 1
            sequence = ""
        
        else:
            sequence += line

    sequence = sequence.replace("\n", "")
    return sequence

def get_orfs(codon_array) :
    longest_orf = 0
    shortest_orf = 10000000
    long_idx = -1
    short_idx = -1
    temp = 0

    """
    for loop 1: finds the atg
        for loop 2: finds the first occurence of taa, tag, or tga --> grabs its len and idx
        check for shortest/longest stuff and then swap len and idx if necessary
    """
    for i in range (0, len(codon_array)) : # traversing the entire array of codons
        if codon_array[i] == "ATG" : # if it is the starting codon
            for j in range (i + 1, len(codon_array)) : # start trying to find the first end codon
                if codon_array[j] in ["TAA", "TAG", "TGA"]:
                    temp = (j - i + 1) * 3

                    if temp > longest_orf :
                        long_idx = i
                        longest_orf = temp
                    
                    if temp < shortest_orf :
                        short_idx = i
                        shortest_orf = temp

                    break
    
    print("longest orf is ", longest_orf, " starting at index ", long_idx)
    print("shortest orf is ", shortest_orf, "starting at index ", short_idx)

def find_all_repeats(len_repeat) :
    """
    3 for loops
    grab first sequence in first for loop
    second for loop grabs the first substring of length len_repeat
    third for loop goes thru all the other sequences and checks the count
    then compare and whatever
    """
    sequence = ""
    most_freq = 0
    count = 0
    most_freq_seq = ""

    for i in range (0, 18) :



#running the programs
print(num_records())
sequence_lens()
longest_len()
shortest_len()
reading_frame = 3
#seq = "ATGGCCGCCGCCATATAAATGAAATAA"
sequence = [] #split_dna_into_codons(reading_frame, seq)
print()
for i in range (0, num_records()) :
    sequence = split_dna_into_codons(reading_frame, get_specific_sequence(i + 1))
    print("Sequence Number ", i+1)
    get_orfs(sequence)
    print()





#print(len(codon_array))

"""making code for the find_orfs method
s = "ATGATATATGGCGCTAAAAAATGATCGGATTAAATGATATAA"
n = 3 #splitting count

temp = []; out = []

for i in range (a - 1, len(s), n) :
    temp.append(s[i:i+n])

print(out)

#print(out[0].find('ATG'))
lens = []
fin = 1000000000000
idxs = []

while out[0].find('ATG') is not -1 :
    b = out[0].find('ATG')
    idxs.append(out[0][b+3:].find('TAA')); idxs.append(out[0][b+3:].find('TAG')); idxs.append(out[0][b+3:].find('TGA'))
    for i in range (0, len(idxs)) :
        if idxs[i] is not -1 and idxs[i] < fin:
            fin = idxs[i]
    idxs.clear()
    lens.append(out[0][b:fin+3])
    out[0] = out[0][fin+4:]
    fin = 1000000000000

print(lens)"""
