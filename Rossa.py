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
