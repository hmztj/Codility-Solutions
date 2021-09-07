def solution(A):

    #sort array, check first two values' product with each of the last three and compare with the product of the last three
    #reason for comparing the first two is to consider the negative pair of the values as two product of two negatives is a positve value
    A.sort()
    N = len(A)
    firstProduct = A[0]*A[1]  
    lastProduct = A[N-1]*A[N-2]*A[N-3]
    
    for i in range(N-3, N):
        maxProduct = max(firstProduct*A[i], lastProduct)
    return maxProduct