def solution(N):
    # write your code in Python 3.6
    #num = 1
    count = 0 
    bi = []
    
    while N != 0:
        if N == 1: 
            bi.append(1) 
            break
        else:
            bi.append(N%2)
            N = N//2

    print(bi)
    count = 0
    ind = 0
    gap = []
    
    for i in range(len(bi)-1, -1, -1):
        if bi[i] == 0:
            count+=1        
            gap.insert(ind, count)
        else: 
            ind += 1
            gap.append(0)
            count = 0   
    print(gap)

    return max(gap)

N = 100

print(solution(N))