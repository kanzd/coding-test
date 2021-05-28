# Solution Function
def check(st):
    map={}
    for i in st:
        if i in map:
            map[i]+=1
        else:
            map[i]=1
    ls=list(map.values())
    
    for i in ls:
     k=0
     while k<len(ls)-1:
        if ((i-ls[k+1]) in ls) or ((ls[k+1]-i) in ls):
            return "Dynamic"
        k+=1
    return "Not"


# Taking Input
i=int(input())
ls=[]
for k in range(i):
    ls.append(input())



# Outputs
for i in ls:
    print(check(i))