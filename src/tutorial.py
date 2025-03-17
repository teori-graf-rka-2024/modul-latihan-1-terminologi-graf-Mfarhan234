import networkx as nx
from graph import (
    create_graph,
    get_degree,
    dfs_traversal,
    bfs_traversal,
    find_shortest_path,
    visualize_graph
)

def main():
    # Daftar edges untuk graf
    edges = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 1), (2, 5)]
    
    # 1. Buat graf
    G = create_graph(edges)
    print("Graf berhasil dibuat!")
    print(f"Nodes: {list(G.nodes)}")
    print(f"Edges: {list(G.edges)}\n")

    # 2. Hitung derajat simpul
    node = 2
    degree = get_degree(G, node)
    print(f"Derajat node {node}: {degree}\n")

    # 3. Traversal DFS
    dfs_result = dfs_traversal(G, start=1)
    print(f"Hasil DFS traversal mulai dari simpul 1: {dfs_result}\n")

    # 4. Traversal BFS
    bfs_result = bfs_traversal(G, start=1)
    print(f"Hasil BFS traversal mulai dari simpul 1: {bfs_result}\n")

    # 5. Shortest path dari simpul 1 ke 4
    shortest_path_result = find_shortest_path(G, source=1, target=4)
    print(f"Jalur terpendek dari node 1 ke 4: {shortest_path_result}\n")

    # 6. Visualisasi graf
    print("Menampilkan dan menyimpan visualisasi graf ke graph_visualization.png")
    visualize_graph(G)

if __name__ == "__main__":
    main()
