def solution(N,A):
    counter = [0]*N
    b = 0
    m = 0
    for i in range(0, len(A)):
        X = A[i]
        if X <= N:
            counter[X-1] = max(b, counter[X-1])+1
            m = max(m, counter[X-1])
        else:
            b = m
    for i in range(0, len(counter)):
        if counter[i] < b: 
            counter[i] = b    
    
    return counter