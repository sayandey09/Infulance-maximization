import time
from igraph import *
import igraph as ig
from ris import ris
import pandas as pd
from IC import IC
import matplotlib.pyplot as plt
import os

def business_algo(file,seed,mc):
    # g = Graph.Read_Ncol(file, directed=True)
    G = pd.read_csv('twitter/12831.csv')
    G = Graph.Read_Ncol(file, directed=True)
    source_nodes = [edge.source for edge in G.es]
    target_nodes = [edge.target for edge in G.es]
    df = pd.DataFrame({'source': source_nodes,'target': target_nodes})
    risS,risT = ris(df,seed,0.1,mc = mc)
    ris_spread  = IC(G,risS,0.1,mc=1)
    G.vs["color"] = "grey"
    for i in risS:
        G.vs[i]["color"] = "red"
    for i in ris_spread[0][5:]:
        G.vs[i]["color"] = "green"
    ig.plot(G,target="static/cache/graph.png")
    return risS,len(ris_spread[0])
