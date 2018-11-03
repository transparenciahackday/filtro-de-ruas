import csv

ruas = [n.strip() for n in open('ruas-porto.txt', 'r').readlines()]
nomescsv = csv.DictReader(open('../dados/nomes-genero.csv', 'r'))
nomes = {}
for n in nomescsv:
    nomes[n['nome']] = n['genero']

nomes_lista = nomes.keys()

output = csv.writer(open('out.csv', 'w'))
for name in ruas:
    firstname = name.split(' ')[0]
    if firstname in nomes_lista:
        output.writerow([name, nomes[firstname]])
    else:
        output.writerow([name, ''])

