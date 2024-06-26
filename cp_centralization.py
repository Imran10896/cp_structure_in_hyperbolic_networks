# %%capture
# This command captures the output of the following commands
!pip install cpnet

import cpnet
import numpy as np
import pandas as pd
import networkx as nx

def cp_centralization(G):
    """
    Calculate the core periphery centralization(cp-centralization) of a graph.

    Parameters:
    G (networkx.Graph): The input graph.

    Returns:
    float: The (cp-centralization) value of the graph.
    """
    # Instantiate the Rossa algorithm from cpnet
    alg = cpnet.Rossa()
    
    # Detect the core-periphery structure of the graph
    alg.detect(G)
    
    # Get the coreness of each node
    x = alg.get_coreness()
    
    # Convert coreness dictionary to a numpy array
    x_core = np.array(pd.DataFrame(list(x.items()))[1])
    
    # Calculate the centralization score
    C = 1 - (2 / (G.number_of_nodes() - 2)) * (sum(x_core) - 1)
    
    return C

# Example graph: Karate Club Graph
G = nx.karate_club_graph()

# Calculate the cp-centralization of the example graph
centralization = cp_centralization(G)

# Print the cp-centralization 
print(f"The cp-centralization score of the Karate Club graph is: {centralization}")
