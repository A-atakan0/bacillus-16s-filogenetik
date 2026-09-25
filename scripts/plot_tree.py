from Bio import Phylo, SeqIO
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Accession -> tür ismi eşlemesi oluştur
name_map = {}
for record in SeqIO.parse("../data/bacillus_16s_raw.fasta", "fasta"):
    acc = record.id
    parts = record.description.split()
    species = " ".join(parts[1:3])  # "Bacillus subtilis" gibi
    name_map[acc] = species

tree = Phylo.read("../results/bacillus_tree.treefile", "newick")

# Yaprak isimlerini değiştir
for leaf in tree.get_terminals():
    if leaf.name in name_map:
        leaf.name = name_map[leaf.name]

fig = plt.figure(figsize=(14, 9))
ax = fig.add_subplot(1, 1, 1)
Phylo.draw(tree, axes=ax, do_show=False)

plt.title("Bacillus Türleri - 16S rRNA Filogenetik Ağacı")
plt.tight_layout()
plt.savefig("../figures/bacillus_tree_labeled.png", dpi=300)
print("Etiketli ağaç kaydedildi: figures/bacillus_tree_labeled.png")
