from graphnode import GraphNode
import hashlib
import matplotlib.pyplot as plt
import networkx as nx
from typing import Any

class LinkedList():
    def __init__(self, element, next=None, parent=None):
        self.element = element
        self.next = next
        self.parent = parent
    
    def add_node(self, next_node):
        tmp = self
        while tmp.next != None:
            tmp = tmp.next
        tmp.next = next_node

    def add_nodes(self, elements: list | tuple, parent=None):
        for x in [*filter(lambda x: not isinstance(x, LinkedList), elements)]:
            self.add_node(LinkedList(x, parent=parent))

    def add_nodes2x(self, lst2x):
        dct = {}
        for lst in list(lst2x):
            for s in list(lst):
                s.pop()
                s = s[::-1]
                strng = str(s)
                hashed = hashlib.sha256(strng.encode("utf-8")).hexdigest()
                dct[hashed] = strng
        print(dct)

    def from_graphnode(self):
        tmp = self
        data = []
        while tmp != None:
            if isinstance(tmp.element, GraphNode):
                data.append(tmp.element)
            else: raise TypeError("Should have type of GraphNode")
            tmp = tmp.next
        return data

    def graph(self, custom_figsize=(8, 8)):
        names = {}
        data = self.from_graphnode()
        for element in data:
            names[element.name] = (element.x, element.y)

        ## modified the code from networkx example ## 

        G = nx.Graph()
        G.pos = {}
        G.pop = {}
        i = 0
        last = None
        for data in data:
            G.pos[i] = (data.x, data.y)
            G.pop[i] = data.size * 100
            if last is None:
                last = i
            else:
                G.add_edge(i, last)
                
                last = i
            i += 1

        plt.figure(1, figsize=custom_figsize)
        plt.clf()
        nx.draw_networkx_edges(G, G.pos, width=4, alpha=0.5)
        nx.draw_networkx_nodes(G, G.pos, node_size=[G.pop[n] for n in G], alpha=0.5)
        nx.draw_networkx_nodes(G, G.pos, node_size=5, node_color="red")

        for key in names:
            x, y = names[key]
            plt.text(x, y + 0.1, key)


