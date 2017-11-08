import sys

class MaxSubSumDAC:
    def maxSubSum(self, A, l, r):
        # Base case:
        if l>=r-1:
            if A[l]>0:
                return A[l]
            else:
                return 0

        # Devide:
        center = (l+r)//2
        print("center: "+str(center))
        print("left:"+str(l)+", right:"+str(r))
        maxRight = self.maxSubSum(A, l, center)
        maxLeft = self.maxSubSum(A, center, r)

        # Conquer:
        result = self.maxSubSumConcuer(A, center, l, r)
            
        return max(max(maxRight, maxLeft),result)

    def maxSubSumConcuer(self, A, center, l, r):
        maxRight = -sys.maxint - 1
        maxLeft = -sys.maxint - 1
        tempSum = 0
        for i in range(center,r+1):
            tempSum = tempSum + A[i]
            if tempSum > maxRight:
                maxRight = tempSum
        tempSum = 0
        for i in range(center-1, l,-1):
            tempSum = tempSum + A[i]
            if tempSum > maxLeft:
                maxLeft = tempSum

        return maxRight + maxLeft

#A = [0,5,2,-8,8,6,0,5,-8,7,3,2,-7,4,7]
A = [0,-1,2,-1,1,-1,3,-1,1,0]
h = MaxSubSumDAC()
result = h.maxSubSum(A, 0, len(A)-1)
print(result)
