# Import csv library

import csv

# Open and write a new tsv through context manager

with open('../data/country_gap.tsv', 'w') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerow(['country', 'gap'])
    writer.writerow(['Algeria', '.08'])
    writer.writerow(['Guatemala', '.11'])
    writer.writerow(['Nigeria', '.29'])
    writer.writerow(['India', '.33'])
    writer.writerow(['Mozambique', '.36'])
    writer.writerow(['Bangladesh', '.41'])
    writer.writerow(['Kenya', '.42'])
    writer.writerow(['Pakistan', '.43'])