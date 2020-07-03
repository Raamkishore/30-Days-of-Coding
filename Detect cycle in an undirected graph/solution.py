'''
This solution would be more similar to geeksforgeeks solution as I went through
the algorithm first before solving the problem.
'''

def recur(g, i, visit, parent):
    
    visit[i] = True
    
    for j in g[i]:
        if visit[j] == False:
            if recur(g, j, visit, i) == True:
                return 1
        elif visit[j] and j != parent:
            return 1
            
    return 0

def isCyclic(g,n):
    
    visit = [False] * n
    
    for i in range(n):
        if visit[i] == False:
            if recur(g, i, visit, -1) == True:
                return 1
                
    return 0

'''
The code part given below is already provided by gfg
'''

import atexit
import io
import sys
from collections import defaultdict

class Graph():
    def __init__(self,vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self,u,v): 
        self.graph[u].append(v)

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        N,E = map(int,input().strip().split())
        g = Graph(N)
        edges = list(map(int,input().strip().split()))

        for i in range(0,len(edges),2):
            u,v = edges[i],edges[i+1]
            g.addEdge(u,v) 
            g.addEdge(v,u)
        print(isCyclic(g.graph,N))
