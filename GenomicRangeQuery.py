def solution(S, P, Q):
    # write your code in Python 3.6
    R = []
    A = [0]*len(S)
    C = [0]*len(S)
    G = [0]*len(S)
    T = [0]*len(S)
    
    a=c=g=t=0
    
    for i in range(0, len(S)):
        if(S[i] == 'A'):
            a+=1
        elif(S[i] == 'C'):
            c+=1
        elif(S[i] == 'G'):
            g+=1
        elif(S[i] == 'T'):
            t+=1
        A[i] = a
        C[i] = c
        G[i] = g
        T[i] = t

    for i in range(0,len(P)):
        if P[i] == Q[i] :
            if S[P[i]] == 'A' :
                R.append(1)
            elif S[P[i]] == 'C' :
                R.append(2)
            elif S[P[i]] == 'G' :
                R.append(3)
            elif S[P[i]] == 'T' :
                R.append(4)

        elif A[P[i]] < A[Q[i]] or S[P[i]] == 'A' :
            R.append(1)
        elif C[P[i]] < C[Q[i]] or S[P[i]] == 'C' :
            R.append(2)
        elif G[P[i]] < G[Q[i]] or S[P[i]] == 'G' :
            R.append(3)
        elif T[P[i]] < T[Q[i]] or S[P[i]] == 'T' :
            R.append(4)
    return R