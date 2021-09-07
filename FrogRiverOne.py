def solution(X, A):
    B = [0]*X
    s=0
    for K in range(0, len(A)):
        if(B[A[K]-1]==0 and A[K] <= X):
            s+=1
            B[A[K]-1] = 1
        if(s==X):
            return K
    return -1
        #print("Positions:",A[K], "seconds:", K, "B:", B[K])
    print(B)      

A = [1,3,1,4,2,3,5,4]
C = [0,1,2,3,4,5,6,7]
print(A)
print(C)
solution(5, A)