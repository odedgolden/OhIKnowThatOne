class BFS:

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

    def bfs(self, graph, root):
        markedArray = []
        workQueue = [root]

        while workQueue:
            print(workQueue)
            v = workQueue.pop(0)
            if v not in markedArray:
                markedArray.append(v)
                for u in graph[v]:
                    if u not in markedArray:
                        workQueue.append(u)
        return markedArray
    
B = BFS()
G = B.bfs(B.graph, 1)
print(G)

        
