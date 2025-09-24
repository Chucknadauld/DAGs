import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph
G = nx.DiGraph()

# Add nodes
G.add_nodes_from(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'])

# Add edges (directed connections)
G.add_edges_from([('A', 'C'), ('B', 'C'), ('C', 'D'), ('C', 'E'), ('D', 'F'), ('E', 'F'), ('F', 'G'), ('F', 'H')])

# Visualize the graph with hierarchical layout
plt.figure(figsize=(20, 8))

# Create hierarchical layout manually to match the image
pos = {
    'A': (0, 1),
    'B': (0, -1),
    'C': (2, 0),
    'D': (4, 1),
    'E': (4, -1),
    'F': (6, 0),
    'G': (8, 1),
    'H': (8, -1)
}

nx.draw(G, pos=pos, with_labels=True, node_color='lightblue', 
        node_size=1500, font_size=16, font_weight='bold', 
        arrows=True, arrowsize=20, edge_color='gray')
plt.title("Directed Graph", fontsize=18, fontweight='bold')
plt.axis('off')
plt.tight_layout()
plt.show()
