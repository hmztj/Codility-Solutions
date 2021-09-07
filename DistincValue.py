def solution(A):
    A.sort()
    if(len(A )== 1):
        return A[0]
    N = len(A)
    for i in range(0, N-1, 2):
        if(A[i]  != A[i+1]):
            return A[i]
    return A[N-1]
        
A = [1,1,2,2,2,3,3,3,3]

print(solution(A))
    