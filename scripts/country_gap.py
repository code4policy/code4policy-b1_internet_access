import csv

with open('country_gap.tsv', 'w') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerow(['country', 'gap'])
    writer.writerow(['Algeria', '.05'])
    writer.writerow(['Kenya', '.07'])
    writer.writerow(['Mozambique', '.27'])
    writer.writerow(['Nigeria', '.04'])
    writer.writerow(['Bangladesh', '.24'])
    writer.writerow(['India', '.15'])
    writer.writerow(['Pakistan', '.34'])
    writer.writerow(['Guatemala', '.08'])

