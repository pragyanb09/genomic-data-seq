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

def get_sequences():
    with open("dna.example.fasta") as f:
        count = 0;
        sequence = ""
        sequences = []

        for line in f :
            if line[0] == '>' and count != 0 :
                sequence = sequence.replace("\n", "")
                sequences.append(sequence)
                sequence = ""
            
            elif count == 0 :
                count += 1
            
            else:
                sequence += line

        sequence = sequence.replace("\n", "")
        sequences.append(sequence)
        return sequences

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
    4 for loops
    grab first sequence in first for loop
    second for loop grabs the first substring of length len_repeat
    third for loop goes thru all the other sequences and checks ea individual substring if it is equal
    then compare and whatever
    """
    all_sequences = get_sequences()
    sequence = ""
    most_freq = 0
    most_freq_seq = ""
    count = 0
    substring = ""
    temp_sequence = ""
    temp_substring = ""

    for i in range (0, 18) : # loops thru every single sequence to find all the substrings
        sequence = all_sequences[i] # the sequence where the substrings are coming from currently
        # print (i)
        
        for j in range (0, len(sequence) - len_repeat + 1) : # looping thru all the possible substrings
            substring = sequence[j:j+len_repeat] # a substring
            #print(substring)
            
            for k in range(0, 18) : # looping thru every single sequence now to get the count
                temp_sequence = all_sequences[k] # gets the sequence for comparison
                # print(temp_sequence)
                
                for m in range (0, len(temp_sequence) - len_repeat + 1) : # looping thru all those substrings in my temp_sequence
                    temp_substring = temp_sequence[m:m+len_repeat] # getting my temp_substring value
                    
                    if substring == temp_substring : # if the substrings are equal, increase the count
                        count += 1

            if count > most_freq : # i have now looped thru all the sequences and all their substrings and checked
                most_freq = count
                most_freq_seq = substring # changed my most_freq variables successfully
            
            count = 0 # must reset each time no matter what

    print("The most frequent substring of length ", len_repeat, " is ", most_freq_seq, " with a count of ", most_freq)

                


#running the programs
print(num_records())
sequence_lens()
longest_len()
shortest_len()
reading_frame = 3
#seq = "ATGGCCGCCGCCATATAAATGAAATAA"
sequence = [] #split_dna_into_codons(reading_frame, seq)

"""print()
for i in range (0, num_records()) :
    sequence = split_dna_into_codons(reading_frame, get_specific_sequence(i + 1))
    print("Sequence Number ", i+1)
    get_orfs(sequence)
    print()"""

find_all_repeats(6)