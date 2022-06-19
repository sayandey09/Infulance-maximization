import matplotlib.pyplot as plt
from random import uniform, seed
import numpy as np
import pandas as pd
import time
from igraph import *
import random
from collections import Counter

def IC(G,S,p=0.5,mc=1000):  
    """
    Input:  G:  Ex2 dataframe of directed edges. Columns: ['source','target']
            S:  Set of seed nodes
            p:  Disease propagation probability
            mc: Number of Monte-Carlo simulations
    Output: Average number of nodes influenced by the seed nodes
    """
    
    # Loop over the Monte-Carlo Simulations
    spread = []
    for _ in range(mc):
        
        # Simulate propagation process      
        new_active, A = S[:], S[:]
        while new_active:
            
            # Get edges that flow out of each newly active node
            temp = G.loc[G['source'].isin(new_active)]

            # Extract the out-neighbors of those nodes
            targets = temp['target'].tolist()

            # Determine those neighbors that become infected
            success  = np.random.uniform(0,1,len(targets)) < p
            new_ones = np.extract(success, targets)
            
            # Create a list of nodes that weren't previously activated
            new_active = list(set(new_ones) - set(A))
            
            # Add newly activated nodes to the set of activated nodes
            A += new_active
            
        spread.append(len(A))
        
    return(np.mean(spread))