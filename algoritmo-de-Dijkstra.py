import networkx as nx
import numpy as np
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

noInicial = 0
noFinal = 4

# Distancia entre as cidades
distancias = [
    [0, 4, 0, 0, 0, 0, 0, 8, 0],
    [4, 0, 8, 0, 0, 0, 0, 11, 0],
    [0, 8, 0, 7, 0, 4, 0, 0, 2],
    [0, 0, 7, 0, 9, 14, 0, 0, 0],
    [0, 0, 0, 9, 0, 10, 0, 0, 0],
    [0, 0, 4, 14, 10, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 1, 6],
    [8, 11, 0, 0, 0, 0, 1, 0, 7],
    [0, 0, 2, 0, 0, 0, 6, 7, 0]
]

# Posições dos nós
posicao = {
    0: [0, 2],  # Criciúma
    1: [1, 3],  # Içara
    2: [2, 3],  # Nova Veneza
    3: [3, 3],  # Cocal do Sul
    4: [4, 2],  # Morro da Fumaça
    5: [3, 1],  # Balneário Esplanada
    6: [2, 1],  # Balneário Arroio Corrente
    7: [1, 1],  # Sangão
    8: [2, 2]   # Siderópolis
}

# Criar o grafo
G = nx.from_numpy_array(np.array(distancias))

# Calcular o caminho mínimo
caminhoMinimo = nx.dijkstra_path(G, noInicial, noFinal)
arcosCaminho = [(caminhoMinimo[i], caminhoMinimo[i+1]) for i in range(len(caminhoMinimo) - 1)]

# Cor das arestas 
corArcos = [
    "red" if (arco in arcosCaminho or arco[::-1] in arcosCaminho) else "black"
    for arco in G.edges()
]

# Obter os pesos (distâncias) para exibi-los nas arestas
pesos = nx.get_edge_attributes(G, 'weight')

# Plotar o grafo
plt.figure(figsize=(10, 8))

# Desenhar o grafo
nx.draw_networkx(
    G,
    pos=posicao,
    node_color="white",
    edgecolors="black",
    edge_color=corArcos,
    # with_labels=False,
    font_weight="bold",
    width=[2 if color == "red" else 1 for color in corArcos],
)

# Adicionar os rótulos das cidades
# nx.draw_networkx_labels(G, posicao, labels=cidades, font_size=10, font_color="black")
nx.draw_networkx_labels(
    G, 
    posicao, font_size=10, 
    font_color="black", 
    font_weight="bold"
)

# Adicionar os pesos
nx.draw_networkx_edge_labels(
    G, 
    posicao, 
    edge_labels = pesos, 
    font_size = 9, 
    font_color="blue"
)

plt.title("Mapa das cidades e menor caminho \n 0: Criciúma, 1: Içara3: Cocal do Sul,4: Morro da Fumaça, 5: Balneário Esplanada, 6: Balneário Arroio Corrente, 7: Sangão, 8: Siderópolis")
plt.show()
