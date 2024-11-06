from math import inf
import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_pydot import graphviz_layout

class BinaryHeap:
    def __init__(self, color, title) -> None:
        self.arr = [inf]
        self.color = color
        self.title = title

    def get_high_priority(self):
        """
            Retorna o nó de maior prioridade da heap.
        """
        return self.arr[1]

    def heap_sort(self):
        """
            Ordena o array de forma crescente.
        """
        
        for i in range(len(self.arr) // 2, 0, -1):
            self.__down(i)

    def change_priority(self, index: int, new_value: int):
        """
            Altera a prioridade de um nó da heap e reordena a heap.
            
            Exemplo:
            [inf, 95, 73, 78, 39, 60, 66, 70, 33, 25, 28]
            - Altera o valor 95 para 28
            [inf, 28, 73, 78, 39, 60, 66, 70, 33, 25, 28]
            - Reordena a heap
            [inf, 78, 73, 66, 39, 60, 28, 70, 33, 25, 28]
        """

        self.arr[index] = new_value
        self.heap_sort()
        self.display_heap(self.color, self.title)

    def remove(self):
        """
            Remove o nó de maior prioridade da heap da seguinte forma:
            - Troca o nó de maior prioridade com o último nó da heap
            - Remove o último nó da heap
            - Reordena a heap

            Exemplo:
            [inf, 95, 73, 78, 39, 60, 66, 70, 33, 25, 28]
            - Troca o valor 95 com 28
            [inf, 28, 73, 78, 39, 60, 66, 70, 33, 25, 95]
            - Remove o valor 95
            [inf, 28, 73, 78, 39, 60, 66, 70, 33, 25]
            - Reordena a heap
            [inf, 78, 73, 66, 39, 60, 28, 70, 33, 25]
        """

        last_item = len(self.arr) - 1
        if last_item >= 1:
            self.arr[1], self.arr[last_item] = self.arr[last_item], self.arr[1]
            self.arr.pop()
            self.__down(1)
            self.display_heap(self.color, self.title)

    def insert(self, new_value: int):
        """
            Insere um novo nó na heap e reordena a heap.

            Exemplo:
            [inf, 73, 78, 39, 60, 66, 70, 33, 25, 28]
            - Insere o valor 95
            [inf, 73, 78, 39, 60, 66, 70, 33, 25, 28, 95]
            - Reordena a heap
            [inf, 95, 73, 78, 39, 60, 66, 70, 33, 25, 28]
        """

        self.arr.append(new_value)
        self.__up(len(self.arr) - 1)
        self.display_heap(self.color, self.title)

    def __up(self, target_index: int):
        """
            Reordena a heap de baixo para cima.
            - Se o valor do nó pai for menor que o valor do nó filho, troca os valores.
            - Repete o processo até que o nó pai seja maior que o nó filho.
        """

        parent_index = target_index // 2
        if parent_index >= 1 and self.arr[parent_index] < self.arr[target_index]:
            self.arr[target_index], self.arr[parent_index] = self.arr[parent_index], self.arr[target_index]
            self.__up(parent_index)

    def __down(self, target_index: int):
        """
            Reordena a heap de cima para baixo.
            - Se o valor do nó pai for menor que o valor do nó filho, troca os valores.
            - Repete o processo até que o nó pai seja maior que o nó filho.
        """

        last_item = len(self.arr) - 1
        child_index = 2 * target_index
        if child_index <= last_item:
            if child_index < last_item and self.arr[child_index + 1] > self.arr[child_index]:
                child_index += 1
            if self.arr[child_index] > self.arr[target_index]:
                self.arr[target_index], self.arr[child_index] = self.arr[child_index], self.arr[target_index]
                self.__down(child_index)

    def display_heap(self, graph_color="skyblue", title="Binary Heap"):
        T = nx.DiGraph()

        """
            Para cada índice do array, adiciona um nó no grafo
            e cria uma aresta para o nó pai, exceto para o índice 1.
        """
        for index in range(1, len(self.arr)):
            T.add_node(index)
            if index > 1:
                parent_index = index // 2
                T.add_edge(parent_index, index)

        """
            Adiciona os valores do array como labels dos nós, exemplo para o array [inf, 95, 73, 78, 39, 60, 66, 70, 33, 25, 28]
            o nó 1 terá o label 95, o nó 2 terá o label 73 e assim por diante
        """
        labels = {i: self.arr[i] for i in range(1, len(self.arr))}
        pos = graphviz_layout(T, prog="dot")

        """
            Limpa o gráfico atual e desenha o novo grafo com as novas posições dos nós em intervalos de 1 segundo
        """
        plt.clf()
        nx.draw(T, pos, labels=labels, with_labels=True, node_size=500, node_color=graph_color)
        plt.title(title)
        plt.draw() 
        plt.pause(0.75)


######## Testes 1 ########

plt.ion()
plt.figure(figsize=(3, 5))

bh = BinaryHeap("#ffcc00", "teste 1")
values = [10, 5, 20, 1, 15, 30, 25]
for value in values:
    bh.insert(value)

bh.change_priority(3, 50)
bh.change_priority(1, 8)

bh.remove()
bh.remove()
bh.remove()

print("Nó de maior prioridade: ", bh.get_high_priority())
plt.savefig("teste1.png")

######## Testes 2 ########


bh1 = BinaryHeap("#ccf0f0", "teste 2")
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for value in values:
    bh1.insert(value)

bh1.change_priority(4, 15)
bh1.change_priority(8, 3)

bh1.remove()
bh1.remove()
bh1.remove()
bh1.remove()
bh1.remove()

print("Nó de maior prioridade: ", bh1.get_high_priority())
plt.savefig("teste2.png")

######## Testes 3 ########

plt.ion()

bh2 = BinaryHeap("#ffacff", "teste 3")
values = [50, 40, 30, 20, 10, 5, 3]
for value in values:
    bh2.insert(value)

bh2.change_priority(2, 60)
bh2.change_priority(5, 1)

bh2.remove()
bh2.remove()
bh2.remove()

print("Nó de maior prioridade: ", bh2.get_high_priority())
plt.savefig("teste3.png")

######## Testes 4 ########

plt.ion()

bh3 = BinaryHeap("#aaffaf", "teste 4")
values = [13, 26, 19, 17, 24, 31, 22, 11, 8, 20, 5, 27, 18]
for value in values:
    bh3.insert(value)

bh3.change_priority(7, 35)
bh3.change_priority(10, 12)

bh3.remove()
bh3.remove()
bh3.remove()
bh3.remove()

print("Nó de maior prioridade: ", bh3.get_high_priority())
plt.savefig("teste4.png")

