def calculate_p_value(adjacency_matrix):
    """
    Calculate the p-value for the centralization of the given graph.

    Parameters:
    adjacency_matrix (numpy.ndarray): Adjacency matrix of the graph.

    Returns:
    float: The p-value.
    """
    original_graph = nx.from_numpy_array(adjacency_matrix)
    degree_sequence = [d for n, d in original_graph.degree()]
    
    C_100 = []
    for i in range(100):
        hh_graph = nx.havel_hakimi_graph(degree_sequence)
        C = cp_centralization(hh_graph)
        if C is not None:
            C_100.append(C)
    
    C = cp_centralization(original_graph)
    
    # Calculate p-value
    C_100 = np.array(C_100)
    p_value = np.sum(C_100 >= C) / len(C_100)
    return p_value

# Example usage with a random adjacency matrix
adjacency_matrix = np.random.randint(0, 2, (10, 10)) # Example adjacency matrix, replace with actual data
p_value = calculate_p_value(adjacency_matrix)
print(f"The p-value of the given graph is: {p_value}")
