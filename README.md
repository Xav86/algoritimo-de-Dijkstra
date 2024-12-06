<h1 align="center"> Algoritmo de Dijkstra </h1>

<p align="center">
  <a href="#-tecnologias">Tecnologias</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-projeto">Descrição</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-projeto">Projeto</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-projeto">Pesquisa</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
</p>

# Algoritmo de Dijkstra

## 🚀 Tecnologias Utilizadas

Este projeto foi desenvolvido utilizando as seguintes tecnologias e ferramentas:

- Python
- Google Colabatory
- Biblioteca NetworkX
- Biblioteca Matplotlib
- Biblioteca NumPy

## 📋 Descrição do Problema

Uma pequena empresa transportadora realiza entregas diárias em diversas cidades. A quantidade de cidades a serem visitadas varia conforme a demanda de entregas, e o administrador da empresa precisa planejar a rota do caminhão de maneira eficiente.

Em alguns casos, existem múltiplos caminhos possíveis entre as cidades, o que pode resultar em um itinerário subótimo se não for planejado adequadamente. Isso implica maiores distâncias percorridas, maior tempo entre as entregas e aumento no consumo de combustível, levando a um custo mais elevado e à redução da margem de lucro da empresa.

Este projeto utiliza o algoritmo de Dijkstra para encontrar a menor distância entre a cidade de origem da empresa e cada uma das demais cidades do grafo, garantindo o menor percurso para cada rota planejada.

## 💻 Projeto

Este é o projeto final da disciplina de Estruturas de Dados do curso de Engenharia de Software da UNISATC. O objetivo é aplicar o algoritmo de Dijkstra em um grafo que representa as cidades e as rotas de transporte. Os passos do projeto são:

1. **Reconstrução do Grafo**: Representar o grafo original com cidades reais, atribuindo a cada nó um nome de cidade.
2. **Pesquisa sobre o Algoritmo de Dijkstra**: Entender o funcionamento do algoritmo e apresentá-lo graficamente aplicado ao grafo.
3. **Implementação do Grafo em Python**: Criar o grafo utilizando Python e as bibliotecas adequadas.
4. **Implementação do Algoritmo de Dijkstra**: Aplicar o algoritmo ao grafo para determinar a menor distância entre a cidade de origem e cada um dos demais nós.

## 🔍 Pesquisa sobre o Algoritmo de Dijkstra

### O que é o Algoritmo de Dijkstra?

O algoritmo de Dijkstra é utilizado para encontrar o caminho mais curto entre dois vértices em um grafo ponderado. Ele calcula a menor distância entre um nó inicial e todos os outros nós do grafo, construindo uma árvore de custo mínimo. Este algoritmo tem aplicações práticas em sistemas de navegação, redes de telecomunicações e logística.

### Breve Histórico

O algoritmo foi criado pelo matemático holandês Edsger W. Dijkstra em 1956, originalmente para resolver problemas de roteamento em redes de telecomunicação. Em 1959, Dijkstra publicou um artigo explicando seu algoritmo, que rapidamente se tornou uma ferramenta essencial em diversas áreas, como sistemas de navegação e logística.

### Como Funciona?

O algoritmo funciona construindo uma árvore de caminho mínimo a partir de um vértice inicial. Ele explora todos os vizinhos do vértice atual, atualizando os custos para alcançá-los. Em seguida, seleciona o vértice com o menor custo e repete o processo até calcular o caminho mais curto para todos os vértices.

### Grafos Ponderados

Um grafo ponderado é aquele cujas arestas têm um peso ou custo associado. Esses pesos podem representar distância, tempo ou custo financeiro. O algoritmo de Dijkstra funciona apenas com grafos de pesos positivos, pois utiliza a soma dos pesos para determinar o menor custo. Caso haja pesos negativos, o algoritmo pode falhar em encontrar o caminho correto.

### Aplicabilidade para Empresas

O algoritmo de Dijkstra é uma ferramenta poderosa para resolver problemas de otimização de rotas, como planejamento logístico. Empresas que precisam determinar a rota mais eficiente para entregas ou atendimentos podem se beneficiar ao usar o algoritmo para encontrar o caminho de menor custo ou distância. Ele pode ser aplicado tanto na gestão de frotas quanto no planejamento de rotas de técnicos de campo, proporcionando economia de recursos e maior eficiência operacional.

### Importância para Desenvolvedores de Software

Para desenvolvedores de software, o algoritmo de Dijkstra é essencial para resolver problemas que envolvem caminhos mínimos em grafos. Ele é amplamente usado em aplicações de navegação, redes de computadores e sistemas de logística. Compreender este algoritmo permite criar soluções eficientes e otimizadas para uma ampla gama de problemas no mundo real.
