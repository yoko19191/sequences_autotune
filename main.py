

# read sequences
file_sequence = open("FASTA/smallet_genome_goose_circovirus/Goose circovirus, complete genome.fasta", 'r')

try:
    while True:
        line = file_sequence.readline()
        if line:
            print("line=", line)
        else:
            break
finally:
    file_sequence.close()



