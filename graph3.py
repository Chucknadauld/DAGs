import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph
G = nx.DiGraph()

G.add_nodes_from(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'])

# Add edges (directed connections)
G.add_edges_from([
    ('A', 'B'), ('A', 'D'),
    ('B', 'C'), ('B', 'E'),
    ('C', 'F'),
    ('D', 'H'),
    ('E', 'H'), ('E', 'A'),
    ('F', 'I'),
    ('G', 'D'),
    ('H', 'F'), ('H', 'I'), ('H', 'G'),
    ('I', 'H')
])

plt.figure(figsize=(20, 8))

pos = {
    'A': (1, 3), 'B': (2, 3), 'C': (3, 3), 
    'D': (1, 2), 'E': (2, 2), 'F': (3, 2),
    'G': (1, 1), 'H': (2, 1), 'I': (3, 1)
}

nx.draw(G, pos=pos, with_labels=True, node_color='lightblue', 
        node_size=1500, font_size=16, font_weight='bold', 
        arrows=True, arrowsize=20, edge_color='gray')
plt.title("Directed Graph", fontsize=18, fontweight='bold')
plt.axis('off')
plt.tight_layout()

plt.savefig('graph3.png', dpi=300, bbox_inches='tight')
print("Graph saved as 'graph3.png' in the project root")
plt.close()
