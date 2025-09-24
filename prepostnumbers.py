# Table structure for pre and post numbers
table = [
    ['Node', 'Pre', 'Post'],
    ['A', '1', ''],
    ['B', '', ''],
    ['C', '', '13'],
    ['D', '', ''],
    ['E', '', ''],
    ['F', '', '9'],
    ['G', '5', ''],
    ['H', '', '']
]

def print_table():
    print("Pre and Post Numbers Table\n")
    print("=" * 30)
    for row in table:
        print(f"{row[0]:<6} | {row[1]:<6} | {row[2]:<6}")
    print("=" * 30)

if __name__ == "__main__":
    print_table()
