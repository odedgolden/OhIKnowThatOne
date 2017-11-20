
class MaxInRowInMonge:

    def findMaxValuesForRows(self,M):
        m = len(M) # Number of rows
        if m==0:
            return []
        n = len(M[0]) # Number of columns
        middleRow = m//2
        resultArray = [0]*m

        if n==1:
            resultArray= M[0]
            
        # Find the maximum for the middle row:
        middleRowMax = M[middleRow][0]
        maxColumnIndex = 0
        for i in range(len(M[middleRow])):
            if M[middleRow][i] > middleRowMax:
                middleRowMax = M[middleRow][i]
                maxColumnIndex = i
        # Divide the matrix to two smaller matrices:
        upperRowsMaximas = self.findMaxValuesForRows([row[maxColumnIndex:] for row in M[:middleRow]])
        lowerRowsMaximas = self.findMaxValuesForRows([row[:maxColumnIndex+1] for row in M[middleRow+1:]])

        # Concour - return the current array of maximas:
        return upperRowsMaximas+[middleRowMax]+lowerRowsMaximas

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
