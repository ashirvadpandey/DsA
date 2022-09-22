prices=[3,1,4,8,7,2,5]
l1=[]
mx=-9999
res=0
n=len(prices)
for i in range(n-1,0,-1):
    mx=max(mx,prices[i])
    l1.append(mx)

for j,k in zip(prices,reversed(l1)):
    if k-j>res:
        res=k-j
    continue
return res
