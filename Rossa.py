import numpy as np

class Graph:
    def __init__(self, adj_matrix):
        self.adj_matrix = adj_matrix
        self.num_nodes = adj_matrix.shape[0]

    def find_node_with_minimum_degree(self):
        w = np.divide(1, self.adj_matrix, out=np.zeros_like(self.adj_matrix, dtype=float), where=self.adj_matrix != 0)
        min_degree = float('inf')
        min_degree_node = None
        for node in range(self.num_nodes):
            degree = np.sum(w[node])
            if degree < min_degree:
                min_degree = degree
                min_degree_node = node
        return min_degree_node

    def calculate_phi_S(self, S):
        numerator = 0.0
        denominator = 0.0

        for i in S:
            for j in S:
                if self.adj_matrix[i][j] != 0:
                    numerator += 1 / self.adj_matrix[i][j]

        for i in S:
            for j in range(self.num_nodes):  # Iterate over all nodes
                if self.adj_matrix[i][j] != 0:
                    denominator += 1 / self.adj_matrix[i][j]

        phi_S = numerator / denominator if denominator != 0 else 0
        return phi_S

    def core_periphery_profile(self):
        S = set()  # Set of selected nodes
        phi = {}   # Dictionary to store node and its phi value

        # Step 1: Find first node with minimum degree
        min_degree_node = self.find_node_with_minimum_degree()
        S.add(min_degree_node)
        phi[min_degree_node] = 0  # phi_1 is 0

        # Step 2 onwards: Iteratively select nodes to form core-periphery profile
        while len(S) < self.num_nodes:
            min_phi = float('inf')
            best_node = None

            for node in range(self.num_nodes):
                if node not in S:
                    Sk = S.union({node})
                    phi_k = self.calculate_phi_S(Sk)

                    if phi_k < min_phi:
                        min_phi = phi_k
                        best_node = node

            S.add(best_node)
            phi[best_node] = min_phi

        return phi

    def coreness(self):
        phi = self.core_periphery_profile()
        ordered_phi = {key: phi[key] for key in sorted(phi.keys())}
        return ordered_phi

# Example usage:
# Create a graph object with your adjacency matrix (weights as inverse distances)
adj_matrix = np.array([
    [0, 1/2, 1/3, 0],
    [1/2, 0, 0, 1],
    [1/3, 0, 0, 1/4],
    [0, 1, 1/4, 0]
])

graph = Graph(adj_matrix)
coreness_profile = graph.coreness()
print(coreness_profile)
