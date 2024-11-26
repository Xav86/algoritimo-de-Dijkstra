import networkx as nx
import numpy as np

# Distancia entre as cidades
distancias = [
                [0, 4, 0, 0, 0, 0, 0, 8, 0   ],
                [4, 0, 8, 0, 0, 0, 0, 11, 0  ],
                [0, 8, 0, 7, 0, 4, 0, 0, 2  ],
                [0, 0, 7, 0, 9, 14, 0, 0, 0  ],
                [0, 0, 0, 9, 0, 10, 0, 0, 0  ],
                [0, 0, 4, 14, 10, 0, 2, 0, 0],
                [0, 0, 0, 0, 0, 2, 0, 1, 6   ],
                [8, 11, 0, 0, 0, 0, 1, 0, 7  ],
                [0, 0, 2, 0, 0, 0, 6, 7, 0   ]
            ]

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