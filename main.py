a=list(map(int , input().split()))
EvenList=[]
count=0
for i in a:
    if i%2==0:
        count+=1
    EvenList.append(count)
while(1):
    Input=input()
    if Input =="":
        break
    a,b=map(int,Input.split())
    if a==0:
        print(EvenList[b])
        continue
    print(EvenList[b]-EvenList[a-1])
