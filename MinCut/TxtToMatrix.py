from random import choice

M={}

with open ('MinCut/MinCut.txt') as f:
    for i in range(1,201):
        dat = f.readline()
        dat = list(map(int, dat.split()))
        M[(dat[0],)] = tuple((i,) for i in dat[1:])


def Contract():
    while len(M) > 2:
        K = list(M.keys())
        vert1 = choice(K)               #tuple
        vert2 = choice(M[vert1])        #tuple
        
        newVert = vert1 + vert2
        
        newEdge = tuple(i for i in M[vert1]+M[vert2] if i not in (vert1,vert2))
        
        
        del M[vert1]
        del M[vert2]
        
        for i in M.keys():
            inst = M[i].count(vert1)+M[i].count(vert2)
            M[i] = tuple(j for j in M[i] if (j!= vert1 and j!= vert2))+((newVert, )*inst)
        
        M[newVert] = newEdge
        
    
    return tuple(len(M[i]) for i in M.keys())
        

print(Contract())