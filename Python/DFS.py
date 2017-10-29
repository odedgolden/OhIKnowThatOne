class DFS:

    graph = {1: set([4]),
             2: set([1, 2, 3, 5, 6]),
             3: set([2, 4, 5, 9, 10]),
             4: set([1, 2, 3, 5, 6]),
             5: set([3, 4, 6, 7, 9]),
             6: set([4, 5, 8]),
             7: set([5, 8]),
             8: set([6, 7]),
             9: set([3, 5]),
             10: set([3])}
    
    def dfs(self, graph, root):
        markedArray = []
        workStack = [root]
        
        while workStack:
            print(workStack)
            v = workStack.pop()
            if v not in markedArray:
                markedArray.append(v)
                for u in graph[v]:
                    if u not in markedArray:
                        workStack.append(u)
        return markedArray
    
D = DFS()
G = D.dfs(D.graph, 1)
print(G)
