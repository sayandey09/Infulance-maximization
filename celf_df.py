import matplotlib.pyplot as plt
from random import uniform, seed
import numpy as np
import pandas as pd
import time
from igraph import *
import random
from collections import Counter
from IC_df import IC

def celf(G,k,p=0.5,mc=1000):   
    """
    Inputs: G:  Ex2 dataframe of directed edges. Columns: ['source','target']
            k:  Size of seed set
            p:  Disease propagation probability
            mc: Number of Monte-Carlo simulations
    Return: A seed set of nodes as an approximate solution to the IM problem
    """
      
    # --------------------
    # Find the first node with greedy algorithm
    # --------------------
    
    # Compute marginal gain for each node
    candidates, start_time = np.unique(G['source']), time.time()
    marg_gain = [IC(G,[node],p=p,mc=mc) for node in candidates]

    # Create the sorted list of nodes and their marginal gain 
    Q = sorted(zip(candidates,marg_gain), key = lambda x: x[1],reverse=True)

    # Select the first node and remove from candidate list
    S, spread, Q = [Q[0][0]], Q[0][1], Q[1:]
    timelapse = [time.time() - start_time]
    
    # --------------------
    # Find the next k-1 nodes using the CELF list-sorting procedure
    # --------------------
    
    for _ in range(k-1):    

        check = False      
        while not check:
            
            # Recalculate spread of top node
            current = Q[0][0]
            
            # Evaluate the spread function and store the marginal gain in the list
            Q[0] = (current,IC(G,S+[current],p=p,mc=mc) - spread)

            # Re-sort the list
            Q = sorted(Q, key = lambda x: x[1], reverse=True)

            # Check if previous top node stayed on top after the sort
            check = Q[0][0] == current

        # Select the next node
        S.append(Q[0][0])
        spread = Q[0][1]
        timelapse.append(time.time() - start_time)
        
        # Remove the selected node from the list
        Q = Q[1:]
    
    return(sorted(S),timelapse)