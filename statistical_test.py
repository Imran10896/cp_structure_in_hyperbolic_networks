import numpy as np
import networkx as nx

def calculate_p_value(G):
    """
    Calculate the p-value for the cp-centralization of the given graph.

    Parameters:
    G (networkx.Graph): The input graph.

    Returns:
    float: The p-value.
    """
    degree_sequence = [d for n, d in G.degree()]
    
    C_100 = []
    for i in range(100):
        hh_graph = nx.havel_hakimi_graph(degree_sequence)
        C = cp_centralization(hh_graph)
        if C is not None:
            C_100.append(C)
    
    C = cp_centralization(G)
    
    # Calculate p-value
    C_100 = np.array(C_100)
    p_value = np.sum(C_100 >= C) / len(C_100)
    return p_value

# Example graph: Karate Club Graph
G = nx.karate_club_graph()  # Example graph, replace with actual graph
p_value = calculate_p_value(G)
print(f"The p-value of the given graph is: {p_value}")
