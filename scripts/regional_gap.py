import csv

with open('regional_gap.tsv', 'wt') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerow(['Region', 'Gender Gap'])
    writer.writerow(['East Asia & Pacific', '.03'])
    writer.writerow(['Latin America & Caribbean', '.02'])
    writer.writerow(['Europe & Central Asia', '.04'])
    writer.writerow(['Middle East & North Africa', '.17'])
    writer.writerow(['Sub-Saharan Africa', '.37'])
    writer.writerow(['South Asia', '.36'])