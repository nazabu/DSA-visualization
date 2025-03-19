import networkx as nx
import matplotlib.pyplot as plt

tree = nx.Graph()

tree.add_edges_from([(1, 2), (1, 3), (2, 4), (2, 5)])

pos = nx.spring_layout(tree)
nx.draw(tree, pos, with_labels=True, node_size=700, node_color='lightblue', font_size=10)
plt.show()