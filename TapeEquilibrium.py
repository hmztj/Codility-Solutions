def prefixSum(A):
    P = [0]*len(A)
    P[0] = A[0]
    for i in range(1, len(A)):       
        P[i] = P[i-1] + A[i]
    return P

def difference(i, P):
    return abs(((P[len(P)-1] - P[i-1])) - P[i-1])

def solution(A):
    P = prefixSum(A)
    diff =  difference(1,P)
    for i in range(1,len(P)):
        diff = min(diff, difference(i,P))
    return diff