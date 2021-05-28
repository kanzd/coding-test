# Solution Function
def check(ls):
    val1=sum(ls[0])
    val2=sum(ls[1])
    val3=sum(ls[2])
    if val1-val2==0 or val2-val3==0 or val3-val1==0:
        return "no"
    return "yes"

#  Taking Input
no=int(input())
ls=[]
for i in range(no):
    temp=[]
    temp.append(list(map(int,input().split())))
    temp.append(list(map(int,input().split())))
    temp.append(list(map(int,input().split())))
    ls.append(temp)

# Showing Output
for i in ls:
    print(check(i))




