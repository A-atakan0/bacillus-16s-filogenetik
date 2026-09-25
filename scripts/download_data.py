from Bio import Entrez, SeqIO

Entrez.email = "atakanaslan5022@gmail.com"

search_term = "Bacillus[Organism] AND 16S ribosomal RNA[Title] AND 1200:1600[Sequence Length] NOT sp.[Title]"
handle = Entrez.esearch(db="nucleotide", term=search_term, retmax=100)
record = Entrez.read(handle)
id_list = record["IdList"]

handle = Entrez.efetch(db="nucleotide", id=id_list, rettype="fasta", retmode="text")
sequences = list(SeqIO.parse(handle, "fasta"))

# Aynı türden sadece bir örnek al (tür çeşitliliği için)
seen_species = set()
filtered = []
for seq in sequences:
    parts = seq.description.split()
    species = " ".join(parts[1:3])  # örn: "Bacillus subtilis"
    if species not in seen_species:
        seen_species.add(species)
        filtered.append(seq)

filtered = filtered[:15]  # en fazla 15 farklı tür al

SeqIO.write(filtered, "../data/bacillus_16s_raw.fasta", "fasta")
print(f"{len(filtered)} farklı tür indirildi.")
for s in filtered:
    print(s.description)
