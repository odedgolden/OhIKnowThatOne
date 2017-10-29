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
        markedSet =set()
        workStack = [root]
        
        while workStack:
            print(workStack)
            v = workStack.pop()
            if v not in markedSet:
                markedSet.add(v)
                workStack.extend(list(graph[v] - markedSet))
        return markedSet
    
D = DFS()
G = D.dfs(D.graph, 1)
print(G)
