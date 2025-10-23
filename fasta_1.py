from Bio import SeqIO
fasta_file = "sequence.fasta"

sequences = list(SeqIO.parse ("sequence.fasta", "fasta"))
with open("fasta_summary.txt", "w") as out:
     out.write("ID\tLength\tgc_content(%)\tat_content(%)\treverse_complement(first10bp)\n")

for record in sequences:
    print("ID:", record.id)
    print("Length:", len(record.seq))
    print("Sequence:", record.seq)
    print("-" * 40)

    gc_content = 100*float(record.seq.count ("G") + record.seq.count ("C"))/len(record.seq)
    print("GC content (%):",round (gc_content,2))
    at_content = 100*float(record.seq.count ("A") + record.seq.count ("T"))/len(record.seq)
    print("AT content (%):",round (at_content,2))

    reverse_complement = record.seq.reverse_complement()[:10]

    print("Reverse complement (first 10 bp):", record.seq.reverse_complement()[:10])

    print("="*40)

    out.write(f"{record.id}\t{len(record.seq)}\t{round(gc_content, 2)}\t{round(at_content, 2)}\t{reverse_complement}\n")

print("✅ Summary saved as 'fasta_summary.txt'")


         







