from __future__ import division
def get_at_content(dna):
    length = len(dna)
    a_count = dna.upper().count('A')
    t_count = dna.upper().count('T')
    at_content = (a_count + t_count) / length
    return round(at_content, 2)

#we want out function to properly execute the following four lines
my_at_content = get_at_content("ATGCGCGATCGATCGAATCG")
print str(my_at_content)
print get_at_content("ATGCATGCAACTGTAGC")
print get_at_content("aactgtagctagctagcagcgta")

#for bonus, the script needs to calculate AT content for for sequences like "TTCGNNN" and "tnnacgnnat". This program already does that without any additions...

