def solution(A):

    A.sort()
    min = 1
    for elem in A:
        if elem == min:
            min+=1
            print(min)
    print(min)
    return min

A = [1, 3, 6, 4, 1, 2]

solution(A)

def solution2(A):
    A.sort()
    N = len(A)
    if A[N-1]<= 0: 
        return 1
    flag = False
    for i in range(0,N):
        if A[i] == 1:
            flag = True
    if flag == False:
        return 1
    
    for i in range(0, N-1):
        if (A[i] > 0 and (A[i+1] - A[i]) > 1):
            return A[i]+1
    return A[N-1]+1
        