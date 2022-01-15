import csv

with open('regional_gap.tsv', 'w') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerow(['region', 'gap'])
    writer.writerow(['East Asia & Pacific', '.03'])
    writer.writerow(['Latin America & Caribbean', '.02'])
    writer.writerow(['Europe & Central Asia', '.04'])
    writer.writerow(['Middle East & North Africa', '.17'])
    writer.writerow(['Sub-Saharan Africa', '.37'])
    writer.writerow(['South Asia', '.36'])