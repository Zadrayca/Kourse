
import csv

with open('tst.csv', 'r') as f:
    for row in csv.reader(f, delimiter=';'):
        print(row)


with open('tst2.csv', 'w') as f:
    w = csv.writer(f, delimiter=';', quotechar='|')
    w.writerow(['14', '13', '135'])
    w.writerow(['14', '10;20', '31'])