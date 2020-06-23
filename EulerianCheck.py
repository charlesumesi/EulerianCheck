# -*- coding: utf-8 -*-
"""
Created on 16 Feb 2020

@author: Charles Umesi
"""

import networkx as nx
import matplotlib.pyplot as plt

def network_links_andEulerian_check():
    
    '''For Eulerian cycle and path analyses'''
    
    '''There are two parts to this function'''
    
    
    '''Part 1 - Network construction and visualisation'''
   
    # Network details
    a = input('Give the name for your network : ')
    b = (input('Enter the nodes for your network (separated by commas) : ')).split(',')
    c = int(input('How many links will your network have? '))
    d = "Enter one link connecting two nodes in the following manner: For example, if linking 'A' to 'B', type, 'A' LINK 'B' : "
    e = [list(input(d)) for _ in [0]*c]
    f = []
    
    # Processing of input data so that it is suitable for nx 
    for i in e:
        g = (''.join(i)).replace('LINK'.upper(), ',')
        f.append(g)
    
    # Final pre-nx processing before transferring to nx for further handling
    G = nx.Graph()
    G.add_nodes_from(b)
    for i in f:
        eval("G.add_edge(" + i + ")")
    
    nx.draw(G, with_labels = True)
    plt.savefig(a + '.png')
    plt.show()

    
    '''Part 2 - Eulerian cycle and path analyses of network'''
    
    # For the logic behind the code for the analyses, see the illustrations at:
    # https://www.geeksforgeeks.org/eulerian-path-and-circuit/  
    h = G.degree(b)
    j = []
    
    for i in h:
        if (i[1])%2 != 0: j.append(i[1])
    
    if nx.is_eulerian(G) == True and len(j) == 0:
        print('The network has a Eulerian cycle.')
    elif nx.is_eulerian(G) == False and len(j) == 2:
        print('The network has a Eulerian path.')
    elif nx.is_eulerian(G) == False and (len(j) != 0 or len(j) != 2):
        print('The network neither has a Eulerian path or Eulerian cycle.')
    
    print(h)
    
network_links_andEulerian_check()