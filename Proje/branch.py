from dataclasses import dataclass
from email.mime import image
import matplotlib.pyplot as plt
import networkx as nx
from parsing import * 
import PIL



icons = {
    "server":"icons\icons8-servers-group-100.png",
    "pc": "icons\icons8-computer-100.png",
    "root":"icons\icons8-root-server-100.png",
    "switch":"icons\icons8-switches-100.png",
    "user":"icons\icons8-user-80.png",
}

images = {k: PIL.Image.open(fname) for k, fname in icons.items()}



@dataclass
class node:
    name: str = "hunterhound" 
    part: str = "body"
    img: str = "img"
    parent: str = "_"


class myGraph(nx.Graph):

    def __init__(self, nodes: list, **kwargs):
        self.G = nx.Graph()
        self.make_graph(nodes, **kwargs)


    def make_graph(self, nodes: list, **kwargs):
        root_nodes = [node for node in nodes if node.part == 'root']
        body_nodes = [node for node in nodes if node.part == 'body']
        branch_nodes = [node for node in nodes if node.part == 'branch']

        for node in root_nodes:
            self.G.add_node(node.name, image=images[node.img])

        for node in body_nodes:
            self.G.add_node(node.name, image=images[node.img])
            self.G.add_edge(node.parent, node.name)

        for node in branch_nodes:
            self.G.add_node(node.name, image=images[node.img])
            self.G.add_edge(node.parent, node.name)


        pos=nx.spring_layout(self.G, seed=kwargs.get("seed",42))
        fig, ax = plt.subplots(figsize=kwargs.get("figsize",(10,10)))

        nx.draw_networkx_edges(
            self.G,
            pos=pos,
            ax=ax,
            arrows=True,
            arrowstyle="->",
            min_source_margin=15,
            min_target_margin=15,
        )

        tr_figure = ax.transData.transform

        tr_axes = fig.transFigure.inverted().transform

        icon_size = (ax.get_xlim()[1] - ax.get_xlim()[0]) * 0.025
        icon_center = icon_size / 2.0
        
        for n in self.G.nodes:
            xf, yf = tr_figure(pos[n])
            xa, ya = tr_axes((xf, yf))
            a = plt.axes(
                [xa - icon_center, ya - icon_center, icon_size, icon_size])
            a.imshow(self.G.nodes[n]["image"])
            a.text(1.5, 2.5, n, ha="right", va="top")
            a.axis("off")
        plt.savefig("graph.png")
        plt.show()      






