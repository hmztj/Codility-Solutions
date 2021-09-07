def solution(A):
    
    if(len(A) < 1):
        return 0
    elif(len(A)==1):
        return 1
    A.sort()
    A.append(A[len(A)-1])
    count = 1
    for i in range(0, len(A)-1):
        if(A[i] != A[i+1]):
            count+=1
    return count

A=[1,2,3,4,5,6,7]
#print(len(A))
#print(solution(A))

print(len(A)-3, len(A))
