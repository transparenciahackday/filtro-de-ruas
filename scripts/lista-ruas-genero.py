import csv

'''
A ideia é cruzarmos dois datasets:
    - Nomes de pessoas e género (colunas: `nome`, `genero`)
    - Nomes das ruas do Porto (texto simples, com um nome por linha)

para obtermos um dataset com os nomes das ruas e, quando o nome da rua é um nome
de pessoa, com o género.
'''

# Fazer uma lista com cada nome de rua que temos
ruas = [n.strip() for n in open('ruas-porto.txt', 'r').readlines()]

# Abrir o CSV dos nomes e género
nomescsv = csv.DictReader(open('../dados/nomes-genero.csv', 'r'))
# Criar um dicionário com o conteúdo do CSV - o DictReader não é realmente um
# dicionário e não suporta certas coisas)
nomes = {}
for n in nomescsv:
    nomes[n['nome']] = n['genero']

# Preparar também uma lista só com os primeiros nomes, para poder cruzar cada
# nome de rua e ver se lá está. Podíamos usar o nomes.keys() no loop abaixo,
# mas parece-me que assim é mais prático
nomes_lista = nomes.keys()

# Abrir já o ficheiro onde vamos deitar o dataset resultante
output = csv.writer(open('ruas-genero.csv', 'w'))
# Passar por cada nome de rua
for name in ruas:
    # Só vamos verificar o primeiro nome, que é o que determina o género
    firstname = name.split(' ')[0]
    # Ver se está na lista de primeiros nomes
    if firstname in nomes_lista:
        # Está - guardar "Nome da rua" e "Género" no CSV
        output.writerow([name, nomes[firstname]])
    else:
        # Não está, campo de género vazio
        output.writerow([name, ''])
