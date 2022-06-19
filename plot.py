import matplotlib
matplotlib.use("Agg")
from cProfile import label
import matplotlib.pyplot as plt

def plot_graph_k(k,timeSet_G,timeSet_C,risT):
    plt.plot(k,timeSet_G, label="Greedy")
    plt.plot(k,timeSet_C, label="CELF")
    plt.plot(k,risT, label="RIS")
    plt.xlabel("No. of Seed nodes")
    plt.ylabel("Time(second)")
    plt.title("Performance based on Time")
    plt.legend()
    plt.savefig( "./static/cache/test_plot_k.png")
    plt.clf()
    
def plot_graph_size(graphList,greedyTotalTime,celfTotalTime,risTotalTime):
    plt.plot(graphList,greedyTotalTime, label="Greedy")
    plt.plot(graphList,celfTotalTime, label="CELF")
    plt.plot(graphList,risTotalTime, label="RIS")
    plt.xlabel("Size of Graph(nodes)")
    plt.ylabel("Time(second)")
    plt.title("Performance based on Network Size")
    plt.legend()
    plt.savefig( "./static/cache/test_plot_size.png")
    plt.clf()
