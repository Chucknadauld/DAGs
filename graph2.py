import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph
G = nx.DiGraph()

G.add_nodes_from(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])

# Add edges (directed connections)
G.add_edges_from([
    ('A', 'C'), ('A', 'H'),
    ('B', 'A'), ('B', 'G'),
    ('C', 'D'),
    ('D', 'F'),
    ('E', 'A'), ('E', 'I'),
    ('F', 'J'),
    ('G', 'I'),
    ('H', 'G'), ('H', 'F'),
    ('I', 'H'),
    ('J', 'C')
])

plt.figure(figsize=(20, 8))

pos = {
    'A': (4, 8),
    'B': (0, 6),
    'C': (6, 6), 
    'D': (8, 6),
    'E': (3, 5),
    'F': (8, 4),
    'G': (0, 2),
    'H': (5, 3),
    'I': (2, 0),
    'J': (8, 0)
}

nx.draw(G, pos=pos, with_labels=True, node_color='lightblue', 
        node_size=1500, font_size=16, font_weight='bold', 
        arrows=True, arrowsize=20, edge_color='gray')
plt.title("Directed Graph", fontsize=18, fontweight='bold')
plt.axis('off')
plt.tight_layout()

plt.savefig('graph2.png', dpi=300, bbox_inches='tight')
print("Graph saved as 'graph2.png' in the project root")
plt.close()
