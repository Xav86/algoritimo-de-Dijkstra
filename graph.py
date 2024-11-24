"""
Este script cria um grafo representando cidades da região de Criciúma e as rotas de transporte entre elas.
Cada nó representa uma cidade e cada aresta representa uma rota, com o peso indicando a distância ou custo da rota.

Bibliotecas Utilizadas:
- networkx: Para criação e manipulação do grafo.
- matplotlib: Para visualização do grafo.

Funções do Script:
1. Definir as cidades e suas correspondências com os nós do grafo.
2. Criar o grafo e adicionar as arestas que representam as rotas entre as cidades.
3. Definir a posição dos nós para replicar o layout da imagem fornecida.
4. Plotar e exibir o grafo com os nomes das cidades e os pesos das arestas.

Cidades:
- Criciúma, Içara, Nova Veneza, Cocal do Sul, Morro da Fumaça, Balneário Esplanada, Balneário Arroio Corrente, Sangão, Siderópolis

Rotas e Pesos:
- Cada aresta tem um peso que representa a distância entre as cidades conectadas.

"""

import networkx as nx
import matplotlib.pyplot as plt

# Lista das cidades
cidades = {
    0: "Criciúma",
    1: "Içara",
    2: "Nova Veneza",
    3: "Cocal do Sul",
    4: "Morro da Fumaça",
    5: "Balneário Esplanada",
    6: "Balneário Arroio Corrente",
    7: "Sangão",
    8: "Siderópolis"
}

# Criar o grafo
G = nx.Graph()

# Adicionar arestas conforme a Figura 01
arestas = [
    (0, 1, 4), (0, 7, 8), (1, 2, 8), (1, 7, 11),
    (2, 8, 2), (2, 5, 4), (2, 3, 7),
    (3, 4, 9), (3, 5, 14),
    (4, 5, 10),
    (5, 6, 2), (6, 7, 1), (6, 8, 6), (7, 8, 7)
]

# Adicionar as arestas e os pesos ao grafo
for aresta in arestas:
    G.add_edge(aresta[0], aresta[1], weight=aresta[2])

# Obter os pesos das arestas para exibi-los no grafo
pesos = nx.get_edge_attributes(G, 'weight')

# Definir a posição dos nós para replicar o layout da imagem
pos = {
    0: (0, 2),
    1: (1, 3),
    2: (3, 3),
    3: (5, 3),
    4: (6, 2),
    5: (5, 1),
    6: (3, 1),
    7: (1, 1),
    8: (3, 2)
}

# Plotar o grafo
plt.figure(figsize=(10, 8))

# Desenhar o grafo
nx.draw(G, pos, with_labels=True, labels=cidades, node_color='lightcoral', node_size=2000, font_size=10, font_color='white', font_weight='bold')
nx.draw_networkx_edge_labels(G, pos, edge_labels=pesos, font_size=9, font_color='black')

# Exibir o grafo
plt.title("Mapa das cidades e rotas de transporte")
plt.show()
