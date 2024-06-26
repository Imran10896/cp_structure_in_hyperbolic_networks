import numpy as np

def find_node_with_minimum_degree(d):
    w = np.divide(1, d, out=np.zeros_like(d, dtype=float), where=d!=0)
    min_degree = float('inf')
    min_degree_node = None
    for node in range(d.shape[1]):
        degree = np.sum(w[node])
        if degree < min_degree:
            min_degree = degree
            min_degree_node = node
    return min_degree_node

def calculate_phi_S(S, d):
    numerator = 0.0
    denominator = 0.0

    for i in S:
        for j in S:
            if d[i][j] != 0:
                numerator += 1 / d[i][j]

    for i in S:
        for j in range(d.shape[1]):  # Iterate over all nodes
            if d[i][j] != 0:
                denominator += 1 / d[i][j]

    phi_S = numerator / denominator if denominator != 0 else 0
    return phi_S

def core_periphery_profile(d):
    S = set()  # Set of selected nodes
    phi = {}   # Dictionary to store node and its phi value

    # Step 1: Find first node with minimum degree
    min_degree_node = find_node_with_minimum_degree(d)
    S.add(min_degree_node)
    phi[min_degree_node] = 0  # phi_1 is 0

    # Step 2 onwards: Iteratively select nodes to form core-periphery profile
    while len(S) < d.shape[1]:
        min_phi = float('inf')
        best_node = None

        for node in range(d.shape[1]):
            if node not in S:
                Sk = S.union({node})
                phi_k = calculate_phi_S(Sk, d)

                if phi_k < min_phi:
                    min_phi = phi_k
                    best_node = node

        S.add(best_node)
        phi[best_node] = min_phi

    return phi

def coreness(d):
    phi = core_periphery_profile(d)
    ordered_phi = {key: phi[key] for key in sorted(phi.keys())}
    return ordered_phi
