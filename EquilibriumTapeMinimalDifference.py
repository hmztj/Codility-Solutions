def prefixSum(A):
    P = [0]*len(A)
    P[0] = A[0]
    for i in range(1, len(A)):       
        P[i] = P[i-1] + A[i]
    return P

def difference(i, P):
    N = len(P)
    totalSum = P[N-1]
    firstSum = P[i-1]
    secondSum = totalSum - firstSum
    return abs(secondSum - firstSum)

def solution(A):
    P = prefixSum(A)
    diff =  difference(1,P)
    for i in range(1,len(P)):
        diff = min(diff, difference(i,P))
    return diff

A = [3,1,2,4,3]

print(solution(A))