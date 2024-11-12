from math import inf
import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_pydot import graphviz_layout

class BinaryHeap:
    def __init__(self, color, title, initial_array=None) -> None:
        self.arr = [inf] + (initial_array if initial_array is not None else [])
        self.color = color
        self.title = title

    def get_high_priority(self):
        return self.arr[1]
    
    def heap_sort(self, method="up"):
        """
        Ordena o array de forma crescente e exibe o heap após cada troca.
        """
        if method == "down":
            for i in range(len(self.arr) - 1, 1, -1):
                self.arr[1], self.arr[i] = self.arr[i], self.arr[1]
                self.__down(1, i - 1)
                self.display_heap(self.color, f"{self.title} (heap_sort down)")
        else:
            for i in range(1, len(self.arr)):
                self.__up(i)
                self.display_heap(self.color, f"{self.title} (heap_sort up)")

    def change_priority(self, index: int, new_value: int):
        self.arr[index] = new_value
        self.heap_sort()
        self.display_heap(self.color, self.title)

    def remove(self):
        last_item = len(self.arr) - 1
        if last_item >= 1:
            self.arr[1], self.arr[last_item] = self.arr[last_item], self.arr[1]
            self.arr.pop()
            self.__down(1)
            self.display_heap(self.color, self.title)

    def insert(self, new_value: int):
        self.arr.append(new_value)
        self.__up(len(self.arr) - 1)
        self.display_heap(self.color, self.title)

    def __up(self, target_index: int):
        parent_index = target_index // 2
        if parent_index >= 1 and self.arr[parent_index] < self.arr[target_index]:
            self.arr[target_index], self.arr[parent_index] = self.arr[parent_index], self.arr[target_index]
            self.__up(parent_index)

    def __down(self, target_index: int, end=None):
        last_item = end if end is not None else len(self.arr) - 1
        child_index = 2 * target_index
        if child_index <= last_item:
            if child_index < last_item and self.arr[child_index + 1] > self.arr[child_index]:
                child_index += 1
            if self.arr[child_index] > self.arr[target_index]:
                self.arr[target_index], self.arr[child_index] = self.arr[child_index], self.arr[target_index]
                self.__down(child_index, end)

    def display_heap(self, graph_color="skyblue", title="Binary Heap"):
        T = nx.DiGraph()
        for index in range(1, len(self.arr)):
            T.add_node(index)
            if index > 1:
                parent_index = index // 2
                T.add_edge(parent_index, index)
        labels = {i: self.arr[i] for i in range(1, len(self.arr))}
        pos = graphviz_layout(T, prog="dot")
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

bh_copy = BinaryHeap("#ffaff0", "teste 1 copy")
bh_copy.arr = bh.arr.copy()
bh_copy.heap_sort("down")

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

bh_copy1 = BinaryHeap("#fffff0", "teste 2 copy")
bh_copy1.arr = bh.arr.copy()
bh_copy1.heap_sort("down")

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

bh_copy2 = BinaryHeap("#0fadf0", "teste 3 copy")
bh_copy2.arr = bh.arr.copy()
bh_copy2.heap_sort("down")

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

bh_copy3 = BinaryHeap("#afafaf", "teste 2 copy")
bh_copy3.arr = bh.arr.copy()
bh_copy3.heap_sort("down")

bh3.change_priority(7, 35)
bh3.change_priority(10, 12)

bh3.remove()
bh3.remove()
bh3.remove()
bh3.remove()

print("Nó de maior prioridade: ", bh3.get_high_priority())
plt.savefig("teste4.png")

