# Criando uma lista com os 10 filmes mais bem avaliados no IMDb
filmes = [
    "The Shawshank Redemption",
    "The Godfather",
    "The Dark Knight",
    "Pulp Fiction",
    "The Lord of the Rings: The Return of the King",
    "Schindler's List",
    "The Good, the Bad and the Ugly",
    "Forrest Gump",
    "Inception",
    "Fight Club"
]

# Imprimindo a lista original
print("Lista original de filmes:")
print(filmes)

# Simulando a movimentação do ranking
filmes.insert(0, filmes.pop(1))  # Troca o primeiro e o segundo filme

# Imprimindo o resultado após a troca
print("\nLista após a movimentação do ranking:")
print(filmes)


# Simulando a duplicação dos três últimos filmes da lista
filmes.extend(filmes[-3:])  # Duplicando os últimos 3 filmes

# Imprimindo a lista após duplicação
print("\nLista após duplicação dos últimos 3 filmes:")
print(filmes)

# Removendo duplicatas usando set e convertendo de volta para lista
filmes_unicos = list(set(filmes))

# Imprimindo a lista sem duplicatas
print("\nLista após remover duplicatas:")
print(filmes_unicos)


# Repetindo os exercícios com dicionários
filmes_dict = [
    {
        'nome': "The Shawshank Redemption",
        'ano': 1994,
        'sinopse': "Dois prisioneiros estabelecem uma amizade ao longo de vários anos, encontrando consolo e, eventualmente, redenção através de atos de decência."
    },
    {
        'nome': "The Godfather",
        'ano': 1972,
        'sinopse': "Um patriarca de uma dinastia criminosa italiana transfere o controle do seu império para seu filho relutante."
    },
    {
        'nome': "The Dark Knight",
        'ano': 2008,
        'sinopse': "Quando o caos e o crime se espalham em Gotham City, o vigilante Batman se une ao promotor de justiça e ao policial para lutar contra o crime."
    },
    {
        'nome': "Pulp Fiction",
        'ano': 1994,
        'sinopse': "As vidas de dois assassinos, um boxeador, a esposa de um chefe da máfia e dois ladrões se cruzam em uma série de histórias interligadas."
    },
    {
        'nome': "The Lord of the Rings: The Return of the King",
        'ano': 2003,
        'sinopse': "A luta final pela Terra-média começa, enquanto Frodo e Sam se aproximam de Mordor para destruir o Um Anel."
    },
    {
        'nome': "Schindler's List",
        'ano': 1993,
        'sinopse': "A história de Oskar Schindler, um empresário que salvou a vida de mais de mil refugiados judeus durante o Holocausto."
    },
    {
        'nome': "The Good, the Bad and the Ugly",
        'ano': 1966,
        'sinopse': "Um caçador de recompensas e dois ladrões de sepulturas tentam encontrar um baú de ouro escondido durante a Guerra Civil Americana."
    },
    {
        'nome': "Forrest Gump",
        'ano': 1994,
        'sinopse': "A vida de um homem com QI baixo que testemunha e participa de muitos dos eventos mais significativos da história americana."
    },
    {
        'nome': "Inception",
        'ano': 2010,
        'sinopse': "Um ladrão que rouba segredos corporativos através do uso da tecnologia de compartilhamento de sonhos é dado a uma tarefa inversa: enfiar uma ideia na mente de um executivo."
    },
    {
        'nome': "Fight Club",
        'ano': 1999,
        'sinopse': "Um homem insatisfeito com sua vida forma um clube de luta como forma de escapismo e encontra um novo sentido de propósito."
    }
]

# Imprimindo a lista original de dicionários
print("\nLista original de filmes (dicionários):")
for filme in filmes_dict:
    print(filme)

# Simulando a movimentação do ranking
filmes_dict[0], filmes_dict[1] = filmes_dict[1], filmes_dict[0]  # Troca o primeiro e o segundo filme

# Imprimindo o resultado após a troca
print("\nLista após a movimentação do ranking (dicionários):")
for filme in filmes_dict:
    print(filme)
