a=list(map(int,input().split()))
EvenList=[]
count=0
for i in a:
    if i%2==0:
        count+=1
    EvenList.append(count)
# Query=list(map(int,input().split()))
while(1):
    a,b=map(int,input().split())
    if a==0:
        print(EvenList[b])
        continue
    print(EvenList[b]-EvenList[a-1])
