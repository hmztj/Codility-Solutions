def solution(A, B, K):
    # write your code in Python 3.6
    divs = B//K - A//K
    if(A%K == 0):
        divs+=1
    return divs