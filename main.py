from cProfile import label
from platform import node
import time
from igraph import *
import igraph as ig
from greedy_df import greedy
from celf_df import celf
# from plot import plot
from ris import ris
import pandas as pd
from IC_df import IC
import matplotlib.pyplot as plt
from generate_graph import generate
from compare_algo_main import *
from business_algo_main import *


#generate graph
# G = Graph.Barabasi(n=1000, m=3,directed=True)

# # Transform into dataframe of edges

file = open("twitter/12831.edges")
G = Graph.Read_Ncol(file, directed=True)
source_nodes = [edge.source for edge in G.es]
target_nodes = [edge.target for edge in G.es]
df = pd.DataFrame({'source': source_nodes,'target': target_nodes})
# plt.plot(G)
# ig.plot(G,target="static/images/plot.png")
# G = pd.read_csv('twitter/12831.csv')
# itr = int(input("Enter the number of iterations : "))
# print("Enter the values of k seperated by space : ")
# k = [int(x) for x in input().split()]
# mc = int(input("Enter the value of mc : "))

# timeSet_G = []
# influenceSet_G = []
# timeSet_C = []
# influenceSet_C = []

# for i in k:

#     print ('\nPlease wait for the next k output...')
#     print ('\nCalculating...\n')
    
#     grS,grSpread,grTimelapse = greedy(g,i,0.5,mc)
#     timeSet_G.append(sum(grTimelapse))
#     influenceSet_G.append(sum(grSpread))
    
#     celfS,celfSpread,celfTimelapse,celfLookup = celf(g,i,0.5,mc)
#     timeSet_C.append(sum(celfTimelapse))
#     influenceSet_C.append(sum(celfSpread))
    
#     print ("For the value of k = ",i)
#     print ('\nGREEDY\n')
#     print ('Seed Nodes = ',grS)
#     print ('Spread of each seed = ',grSpread)
#     print ('Time Taken = ',grTimelapse)
#     print ('\nCELF\n')
#     print ('Seed Nodes = ',celfS)
#     print ('Spread of each seed = ',celfSpread)
#     print ('Time Taken = ',celfTimelapse)
#     print ('Lookups = ',celfLookup)
    

# plot(k,timeSet_G,influenceSet_G,timeSet_C,influenceSet_C)
mc = 100
print ('\nCalculating...\n')
risS,risT = ris(df,10,0.1,mc = mc)
print("RIS Seed: ",risS)
print("RIS Timelapse:")
print(risT)
print ('\nCalculating...\n')
celfS,celfTimelapse = celf(df,10,0.1,mc = mc)
print ('Seed Nodes = ',celfS)
# print ('Spread of each seed = ',celfSpread)
print ('Time Taken = ',celfTimelapse)
# print ('Lookups = ',celfLookup)
grS,grSpread,grTimelapse = greedy(df,10,0.1,mc = mc)
print ('\nGREEDY\n')
print ('Seed Nodes = ',grS)
print ('Spread of each seed = ',grSpread)
print ('Time Taken = ',grTimelapse)
# celf_spread = IC(df,celfS,0.1,mc=mc)
# ris_spread  = IC(df,risS,0.1,mc=mc)
# gr_spread = IC(df,grS,0.1,mc=mc)
# print("Ris Spread:",ris_spread)
# print("celf Spread:",celf_spread)
# print("Greedy Spread:",gr_spread)

# plot([1,2,3,4,5,6,7,8,9,10],grTimelapse,celfTimelapse,risT)

# nodeList = [i for i in range(100,5*100+1,100)]
# print(nodeList)
# graphList = generate(5,100)
# compare(5,50,graphList,[100,200,300,400,500])

# business_algo(file, 5)