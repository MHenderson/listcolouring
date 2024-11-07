import networkx as nx

import listcolouring
from listcolouring import first_permissible_or_none_node

def test_first_permissible_or_none_node():
    G = nx.complete_graph(3)
    permissible_dict = {0: [0, 1], 1: [1, 2], 2: [2, 3]}
    nx.set_node_attributes(G, permissible_dict, "permissible")
    assert first_permissible_or_none_node(G, 0) == 0
    assert first_permissible_or_none_node(G, 1) == 1
    assert first_permissible_or_node_node(G, 2) == 2
