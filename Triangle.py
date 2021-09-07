def solution(A):
    if(len(A) < 1):
        return 0
    A.sort()
    N = len(A)
    for p in range(0, N-2):
        #print(p)
        q = p+1
        r = p+2
        if(A[p]+A[q]>A[r] and A[q]+A[r]>A[p] and A[r]+A[p]>A[q]):
            return 1
    return 0
    

A = [1, 2]

print(solution(A))