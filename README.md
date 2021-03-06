# Filtro de ruas

Um mapa de ruas do Porto catalogadas por género e outros critérios. Iniciado no **Date With WikiData** em 3 de novembro de 2018.

O objetivo é ter um mapa interativo que ilustre ruas particulares de acordo com vários filtros. Começámos por fazer um filtro de género -- entre as ruas com nomes de pessoas, assinalar de forma distinta as ruas com nomes de mulheres e as com nomes de homens.

Ainda está em curso e é de ficar atento ao [Twitter do Transparência Hackday Portugal](https://twitter.com/thackdaypt) para novidades neste empreendimento.

Para já, usamos valores aleatórios para colorir as ruas e ainda vamos dar umas grandes maquilhagens ao interface. 

![Screenshot do interface](/img/screenshot.png)


## Dados

Na pasta `dados/` estão os datasets utilizados:

* `nomes-genero.csv` - Lista de nomes próprios e o seu género (retirado do dataset de [nomes próprios](http://centraldedados.pt/nomes_proprios). Usado para gerar o `ruas-genero.csv`.
* `ruas-porto.csv` - Lista de ruas do Porto (retirado do dataset de [códigos postais](http://centraldedados.pt/codigos_postais). Usado para gerar o `ruas-genero.csv`.
* **`ruas-genero.csv`** - Lista com os nomes de ruas do Porto (apenas nomes, sem prefixos como "Rua" e "Dr.") e o género determinado. Gerado com o script em `scripts/lista-ruas-genero.py` para cruzar os dois datasets acima.

# Autoria

* Jorge Gustavo Rocha
* Ana Isabel Carvalho
* Marta Pinto
* Ricardo Lafuente
* João Antunes
* Rui Cavaco
* João Barrosa



