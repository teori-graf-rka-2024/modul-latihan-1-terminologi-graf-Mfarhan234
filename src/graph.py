import networkx as nx
import matplotlib.pyplot as plt

def create_graph(edges: list[tuple[int, int]]) -> nx.Graph:
    #Membuat graf tidak berarah berdasarkan daftar sisi.
    G = nx.Graph()
    G.add_edges_from(edges)
    return G

def get_degree(G: nx.Graph, node: int) -> int:
    #Menghitung derajat dari simpul tertentu.
    return G.degree[node]

def dfs_traversal(G: nx.Graph, start: int) -> list[int]:
    # Melakukan pencarian DFS mulai dari simpul tertentu.
    return list(nx.dfs_preorder_nodes(G, start))

def bfs_traversal(G: nx.Graph, start: int) -> list[int]:
    #Melakukan pencarian BFS mulai dari simpul tertentu.
    return list(nx.bfs_tree(G, start).nodes)

def find_shortest_path(G: nx.Graph, source: int, target: int) -> list[int]:
    # Mencari jalur terpendek antara dua simpul.
    return nx.shortest_path(G, source=source, target=target)

def visualize_graph(G: nx.Graph) -> None:
    #Memvisualisasikan graf dan menyimpannya ke file .png
    pos = nx.spring_layout(G)
    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=500, edge_color='gray', font_size=12)
    plt.title("Visualisasi Graf")
    plt.savefig("graph_visualization.png")  # Export ke file PNG
    plt.show()
