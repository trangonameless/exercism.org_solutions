def to_rna(dna_strand):
    mapping_table = str.maketrans({'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'})
    rna = dna_strand.translate(mapping_table)
    return rna

