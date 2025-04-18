'''
[1,3,4,2,6]
'''

def getCount(arr:list[int])->list[int]:
    N = len(arr)
    res = [0]*N
    for i in range(N):
        for j in range(N):
            if i==j:
                continue
            if arr[i]%arr[j]==0:
                res[i]+=1
                res[j]+=1
    return res

getCount([1,3,4,2,6])
getCount([5,2,4,3,7])
