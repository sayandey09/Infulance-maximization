import time
from igraph import *
import igraph as ig
from greedy_df import greedy
from celf_df import celf
from plot import  plot_graph_k, plot_graph_size
from ris import ris
import pandas as pd
from IC_df import IC
import matplotlib.pyplot as plt
import os

def get_df(G):
    source_nodes = [edge.source for edge in G.es]
    target_nodes = [edge.target for edge in G.es]
    df = pd.DataFrame({'source': source_nodes,'target': target_nodes})
    return df

def compare(valK,valMc,graphList,nodeList):
    # print("start")
    # print([i for i in range(1,valK+1)])
    df = []
    for _ in graphList:
        df.append(get_df(_))
    
    risS,risT = ris(df[0],valK,0.1,mc = valMc)
    celfS,celfTimelapse = celf(df[0],valK,0.1,mc = valMc)
    grS,grSpread,grTimelapse = greedy(df[0],valK,0.1,mc = valMc)

    # print("graph done")

    greedyTotalTime = [sum(grTimelapse)]
    celfTotalTime = [sum(celfTimelapse)]
    risTotalTime = [sum(risT)]

    plot_graph_k([i for i in range(1,valK+1)],grTimelapse,celfTimelapse,risT)

    for i in df[1:]:
        risS,risT = ris(i,valK,0.1,mc = valMc)
        celfS,celfTimelapse = celf(i,valK,0.1,mc = valMc)
        grS,grSpread,grTimelapse = greedy(i,valK,0.1,mc = valMc)
        greedyTotalTime.append(sum(grTimelapse))
        celfTotalTime.append(sum(celfTimelapse))
        risTotalTime.append(sum(risT))
        # print("graph done")

    plot_graph_size(nodeList,greedyTotalTime,celfTotalTime,risTotalTime)

def clearCache():
    if(os.path.exists("./static/cache/test_plot_size.png")):
        os.remove("./static/cache/test_plot_size.png")
    if(os.path.exists("./static/cache/test_plot_k.png")):
        os.remove("./static/cache/test_plot_k.png")
    if(os.path.exists("./static/cache/graph.png")):
        os.remove("./static/cache/graph.png")