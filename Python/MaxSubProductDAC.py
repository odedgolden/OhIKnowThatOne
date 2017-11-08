import sys

class MaxSubProduct:
    def maxSubProduct(self, A, l, r):
        # Base case:
        if l>=r-1:
            if A[l]>1:
                return A[l]
            else:
                return 1

        # Devide:
        center = (l+r)//2
        print("center: "+str(center))
        print("left:"+str(l)+", right:"+str(r))
        maxRight = self.maxSubProduct(A, l, center)
        maxLeft = self.maxSubProduct(A, center, r)

        # Conquer:
        result = self.maxSubProductConcuer(A, center, l, r)
            
        return max(max(maxRight, maxLeft),result)

    def maxSubProductConcuer(self, A, center, l, r):
        maxRight = -sys.maxint - 1
        maxLeft = -sys.maxint - 1
        tempProduct = 1
        for i in range(center,r+1):
            tempProduct = tempProduct*A[i]
            if tempProduct > maxRight:
                maxRight = tempProduct
        tempProduct = 1
        for i in range(center-1, l,-1):
            tempProduct = tempProduct*A[i]
            if tempProduct > maxLeft:
                maxLeft = tempProduct

        return maxRight*maxLeft

A = [5,0.1,4,0.5,5,6,0.5]
m = MaxSubProduct()
result = m.maxSubProduct(A, 0, len(A)-1)
print(result)
