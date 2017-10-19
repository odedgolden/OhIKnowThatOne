class Solution:

    
    def fetchGraph(self, path):
        with open(path) as f:
            lines = [line.split("\t")[:-1] for line in f.read().splitlines()]
            G = {int(line[0]) : line[1:] for line in lines}
            return G

    def runDijkstra(self, G, s):
        maximum_distance = 1000000
        X = [s]
        Y = list(G.keys())
        A = [0 for x in range(201)]
        A[s] = 0
        S = dict(G)

        while Y:
            print(A)
            print(X)
            print(Y)
            min_distance = maximum_distance
            min_head = X[0]
            min_tail = X[0]
            for v in X:
                for t in G[v]:
                    e = t.split(",")
                    if int(e[0]) not in Y:
                        continue
                    #print(e)
                    if min_distance > int(e[1]):
                        min_distance = int(e[1])
                        min_head = int(e[0])
                        min_tail = v
            X.append(min_head)
            #print(A)
            A[min_head] = A[min_tail] + min_distance
            #print(min_head)
            #print(Y)
            Y.remove(min_head)
        return A
                    
            



s = Solution()
G = s.fetchGraph("dijkstraData.txt")
A = s.runDijkstra(G,1)
print(sorted(A)[:10])
print(A[7])
print(str(A[7])+","+str(A[37])+","+str(A[59])+","+str(A[82])+","+str(A[99])+","+str(A[115])+","+str(A[133])+","+str(A[165])+","+str(A[188])+","+str(A[197]))
print(A)
