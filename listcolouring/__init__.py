import random

import networkx as nx

def list_init(G, colours, k, seed):
    """Assign a random subset of k colours to the list of permissible colours for every edge of G."""
    random.seed(seed)
    for u, v, permissible in G.edges.data("permissible"):
        G[u][v]["permissible"] = random.sample(colours, k)
        
    for u, v, colour in G.edges.data("colour"):
        G[u][v]["colour"] = None

    return(G)

def list_init_node(G, colours, k, seed):
    """Assign a random subset of k colours to the list of permissible colours for every node of G."""
    random.seed(seed)

    permissible_colours = [random.sample(colours, k) for i in range(G.order())]
    permissible_dict = dict(zip(G.nodes, permissible_colours))

    nx.set_node_attributes(G, permissible_dict, "permissible")
    nx.set_node_attributes(G, None, "colour")

    return(G)

def colours_incident_with(G, u):
    """The list of colours on edges incident with vertex u in graph G."""
    return(set([G[u][v]["colour"] for v in nx.neighbors(G, u)]))

def colours_on_neighbours(G, n):
    """The set of all colours on neighbours of a node n in a graph G."""
    return(set([nx.get_node_attributes(G, "colour")[m] for m in G.neighbors(n)]))

def first_permissible_or_none(G, u, v):
    """
    Returns the first element of A if A is non-empty otherwise returns None.
    Where A is P minus (X union Y).
    X is the list of colours on edges incident with u.
    Y is the list of colours on edges incident with v.
    P is the list of permissible colours for edge uv.
    """
    X = colours_incident_with(G, u)
    Y = colours_incident_with(G, v)
    P = set(G[u][v]["permissible"])
    choices = P - X.union(Y)
    if(len(choices) > 0):
        choice = list(choices)[0]
    else:
        choice = None
    return(choice)

def greedy_list_edge_colouring(G):
    """Assign the first permissible colour to every edge (or None if all permissible
    colours already used on incident edges)."""
    for u, v, colour in G.edges.data("colour"):
        G[u][v]["colour"] = first_permissible_or_none(G, u, v) # random.choice(colours)
    return(G)

def print_list_edge_colouring(G):
    """Print assigned colours and lists of permissible colours for all edges in G."""
    for n, nbrs in G.adj.items():
        for nbr, eattr in nbrs.items():
            perm = eattr['permissible']
            col = eattr['colour']
            print(f"({n}, {nbr}, {perm}, {col})")
        
