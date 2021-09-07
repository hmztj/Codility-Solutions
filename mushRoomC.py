'''def prefix_sums(A):
    n = len(A)
    P = [0] * (n + 1)
    for k in range(1, n + 1):
        P[k] = P[k - 1] + A[k - 1]
    return P'''
    
def prefix_sums(A):
    n = len(A)
    P = [0] * (n)
    for k in range(1, n ):
        P[0] = A[0] 
        P[k] = P[k-1] + A[k]
    return P

def count_total(P, x, y):
    return P[y] - P[x-1]

def mushrooms(A, k, m):
    n = len(A)
    result = 0
    pref = prefix_sums(A)
    
    for p in range(min(m, k) + 1):
        
        left_pos = k - p
        #print("left:", left_pos)
        right_pos = min(n - 1, max(k, k + m - 2 * p))
        #print("right_pos_index",k + m - (2 * p), " : ", k)
        #print("right:",right_pos)
        #print("left_pos:",left_pos,"right_pos:",right_pos)
        result = max(result, count_total(pref, left_pos, right_pos))
        print("result:", result,"\n")
        
    for p in range(min(m + 1, n - k)):
        right_pos = k + p
        #print("right:",right_pos)
        left_pos = max(0, min(k, k - (m - 2 * p)))
        #print("left_pos_index",k - (m - 2 * p),":", k)
        #print("right:",right_pos)
        #print("left_pos2:",left_pos,"right_pos2:",right_pos)
        result = max(result, count_total(pref, left_pos, right_pos))
        print("result:", result,"\n")
    return result

A = [2,3,7,5,1,3,9]
P = prefix_sums(A)
mushrooms(A,4,6)
#print(mushrooms(A,4,6))

print(A)
print(P)
#print(count_total(P,2,5))