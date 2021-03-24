import pandas as ps
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import scipy

### import données
mobilites = ps.read_csv('mobilites.csv',sep=",")
#création objet graphe orienté
G = nx.DiGraph()

### création des sommets et arêtes
G = nx.from_pandas_edgelist(mobilites,source='residence',target='travail',edge_attr='workers', create_using=G)

### affichage graphe
pos = nx.circular_layout(G) #placement des sommets
edge_labels_list=nx.get_edge_attributes(G,'workers') # dico poids des arêtes

nx.draw_networkx(G,pos,with_labels=True)
nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels_list)
plt.show()
