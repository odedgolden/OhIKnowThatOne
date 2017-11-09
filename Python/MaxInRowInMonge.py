
class MaxInRowInMonge:

    def findMaxValuesForRows(self,M):
        m = len(M) # Number of rows
        n = len(M[0]) # Number of columns
        resultArray = [0]*m
        lastMaximumColumnIndex = n-1
        # For every row from upside down
        for i in range(m):
            resultArray[i] = M[i][-1]
            # For every element to the left of the lastMaximumColumnIndex
            for j in range(lastMaximumColumnIndex, -1, -1):
                #print("i,j = " + str(i) +" "+ str(j))
                #print("lastMaximumColumnIndex: "+str(lastMaximumColumnIndex))
                #print(resultArray)
                if M[i][j] > resultArray[i]:
                    resultArray[i] = M[i][j]
                    lastMaximumColumnIndex = j
        return resultArray

    def printMatrix(self, M):
        for row in M:
            print(row)

M = [[10,17, 13,28,23],
     [17,22,16,29,23],
     [24,28,22,34,24],
     [11,13,6,17,7],
     [45,44,32,37,23],
     [36,33,19,21,6],
     [75,66,51,53,34]]
mrm = MaxInRowInMonge()
result = mrm.findMaxValuesForRows(M)
print(result)
