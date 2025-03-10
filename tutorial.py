import networkx as nx
import matplotlib.pyplot as plt

def create_graph(edges: list[tuple[int, int]]) -> nx.Graph:
    #Membuat graf tidak berarah berdasarkan daftar sisi yang diberikan.
    G = nx.Graph()
    G.add_edges_from(edges)
    return G

def get_degree(G: nx.Graph, node: int) -> int:
    # Menghitung derajat dari simpul tertentu.
    if node not in G:
        raise ValueError(f"Node {node} tidak ada dalam graf.")
    return G.degree[node]

def dfs_traversal(G: nx.Graph, start: int) -> list[int]:
    # Melakukan traversal DFS mulai dari simpul tertentu.
    if start not in G:
        raise ValueError(f"Node {start} tidak ada dalam graf.")
    return list(nx.dfs_preorder_nodes(G, start))

def bfs_traversal(G: nx.Graph, start: int) -> list[int]:
    # Melakukan traversal BFS mulai dari simpul tertentu.
    if start not in G:
        raise ValueError(f"Node {start} tidak ada dalam graf.")
    return list(nx.bfs_tree(G, start).nodes)

def find_shortest_path(G: nx.Graph, source: int, target: int) -> list[int]:
    # Mencari jalur terpendek antara dua simpul dalam graf.
    if source not in G or target not in G:
        raise ValueError(f"Salah satu simpul {source} atau {target} tidak ada dalam graf.")
    try:
        path = nx.shortest_path(G, source=source, target=target)
        return path
    except nx.NetworkXNoPath:
        return []  # Tidak ada jalur

def visualize_graph(G: nx.Graph) -> None:
    #Memvisualisasikan graf menggunakan matplotlib dan menyimpannya ke file PNG.
    pos = nx.spring_layout(G)  # Posisi simpul
    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=500, font_size=12, edge_color='gray')
    
    plt.title("Visualisasi Graf")
    plt.savefig("graph_visualization.png")  # Simpan file PNG
    plt.show()  # Tampilkan graf
