# Table structure for pre and post numbers
table = [
    ['Node', 'Pre', 'Post'],
    ['A', '1', '14'],
    ['B', '15', '16'],
    ['C', '2', '13'],
    ['D', '3', '10'],
    ['E', '11', '12'],
    ['F', '4', '9'],
    ['G', '5', '6'],
    ['H', '7', '8']
]

def print_table():
    print("Pre and Post Numbers Table")
    print("=" * 30)
    for row in table:
        print(f"{row[0]:<6} | {row[1]:<6} | {row[2]:<6}")
    print("=" * 30)

def print_sources_sinks():
    print("Sources: A, B")
    print("Sinks: G, H")

def print_topological_ordering():
    print("\nTOPOLOGICAL ORDERING AND # OF ORDERINGS")
    print("Ordering: B,A,C,E,D,F,H,G")
    print("Number: 8")

def print_SCC_order_sinks_sources_graph2():
    print("\nSCC ORDER, SINK AND SOURCE SCCS, AND MINIMUM EDGES TO MAKE GRAPH STRONGLY CONNECTED")
    print("Order: A; B; C,D,F,J; E; G,H,I")
    print("Sources: B; E")
    print("Sinks: C,D,F,J; G,H,I")
    print("Minimum edges: 2")

def print_SCC_connections_graph2():
    print("\nSCC CONNECTIONS")
    print("B -> A")
    print("E -> A")
    print("A -> C,D,F,J")
    print("A -> G,H,I")
    print("E -> G,H,I")

def print_SCC_order_sinks_sources_graph3():
    print("\nSCC ORDER, SINK AND SOURCE SCCS, AND MINIMUM EDGES TO MAKE GRAPH STRONGLY CONNECTED")
    print("Order: A,B,E; C; D,G,H,I; F")
    print("Sources: A; B; E")
    print("Sinks: F")
    print("Minimum edges: 1")

def print_SCC_connections_graph3():
    print("\nSCC CONNECTIONS")
    print("A,B,E -> C")
    print("A,B,E -> D,G,H,I")
    print("C -> F")
    print("D,G,H,I -> F")


if __name__ == "__main__":
    print("\n========GRAPH 1========")
    print_table()
    print_sources_sinks()
    print_topological_ordering()
    print("\n========GRAPH 2========")
    print_SCC_order_sinks_sources_graph2()
    print_SCC_connections_graph2()
    print("\n========GRAPH 3========")
    print_SCC_order_sinks_sources_graph3()
    print_SCC_connections_graph3()