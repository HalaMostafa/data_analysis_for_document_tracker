import matplotlib.pyplot as plt
import numpy as np
# from graphviz import Digraph
# import tempfile


def createHistogram(x_Axis,y_axis,x_label,y_label,title,rotate=False):
    # Fixing random state for reproducibility
    np.random.seed(19680801)
    plt.hist(x = x_Axis, weights=y_axis)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    if rotate:
        plt.xticks(rotation = 90)
        plt.tight_layout()
    plt.grid(True,axis='y')
    plt.show()

def show_dict_histo(dictionary,title='',x='',y=''):
    plt.xticks(rotation=90)
    plt.xlabel(x)
    plt.ylabel(y)        
    plt.title(title)   
    plt.bar(dictionary.keys(),dictionary.values(),width=0.5)
    plt.show()
    
