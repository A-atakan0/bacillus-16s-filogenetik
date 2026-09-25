# Bacillus Türlerinin 16S rRNA Temelli Filogenetik Analizi

## Amaç
Bu proje, halka açık NCBI veri tabanından elde edilen 16S rRNA dizileri kullanılarak
15 farklı *Bacillus* türü arasındaki evrimsel ilişkiyi filogenetik ağaç ile
görselleştirmeyi amaçlamaktadır. Proje, biyoinformatik iş akışlarını (veri toplama,
hizalama, ağaç kurma, görselleştirme) uçtan uca uygulamak amacıyla hazırlanmış bir
öğrenme/portföy çalışmasıdır.

## Veri Kaynağı
- NCBI Nucleotide veritabanı (Entrez API üzerinden Biopython ile otomatik indirildi)
- Arama kriteri: Bacillus[Organism] AND 16S ribosomal RNA[Title] AND 1200:1600[Sequence Length]
- 15 farklı tür, her türden tek örnek

## Yöntem
1. Veri indirme: Biopython (Entrez) ile NCBI'dan FASTA formatında dizi indirme
2. Çoklu dizilim: MAFFT (--auto) ile hizalama
3. Filogenetik ağaç: IQ-TREE (ModelFinder Plus ile model seçimi, 1000 ultrafast bootstrap)
4. Görselleştirme: Biopython Phylo + Matplotlib

## Kullanılan Araçlar
Python 3.10, Biopython, BLAST, MAFFT, IQ-TREE, Matplotlib (Conda ortamı: biyoinfo)

## Nasıl Çalıştırılır
conda create -n biyoinfo python=3.10 -y
conda activate biyoinfo
conda install -c bioconda -c conda-forge blast mafft iqtree biopython matplotlib -y
cd scripts
python download_data.py
mafft --auto ../data/bacillus_16s_raw.fasta > ../data/bacillus_16s_aligned.fasta
iqtree -s ../data/bacillus_16s_aligned.fasta -m MFP -bb 1000 -nt AUTO -pre ../results/bacillus_tree
python plot_tree.py

## Sonuçlar
Ağaç, bilinen taksonomik gruplarla tutarlı sonuçlar vermiştir:
- B. cereus, B. anthracis, B. paramycoides: "Bacillus cereus grubu" olarak bilinen kümede birlikte (bootstrap %100/%62)
- B. licheniformis, B. paralicheniformis: yüksek bootstrap (%100) ile birlikte
- B. pumilus, B. altitudinis, B. stratosphericus: "Bacillus pumilus grubu" ile örtüşen kümede

![Filogenetik Agac](figures/bacillus_tree_labeled.png)

## Sinirliliklar
- Tek gen bolgesi (16S rRNA) kullanilmistir; bu bolge yakin akraba turleri ayirt etmekte sinirli cozunurluge sahiptir.
- Bazi dallanmalarda bootstrap degerleri dusuktur (%15-32), bu dallanmalarin istatistiksel guveni sinirlidir.
- Kucuk orneklem (15 tur, tur basina tek dizi) nedeniyle sonuclar genellenebilir bir taksonomik revizyon niteligi tasimamaktadir; bu bir portfoy/ogrenme calismasidir.

## Yazar
Atakan Aslan - Molekuler Biyoloji ve Genetik, Sivas Cumhuriyet Universitesi
