def solution(A):
    # write your code in Python 3.6
    sumEast = 0
    totalSum = 0
    for i in A:
        if(i == 0):
            sumEast += 1
        else:
            totalSum += sumEast
    if(totalSum > 1000000000):
        return -1
    return totalSum