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

def print_sources():
    print("\nSources: A, B")
    
def print_sinks():
    print("\nSinks: G, H")

if __name__ == "__main__":
    print_table()
    print_sources()
    print_sinks()