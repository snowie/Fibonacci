num=int(input())
n1,n2=0,1
count=0
while count<num :
  print(n1)
  s=n1+n2
  n1=n2
  n2=s
  count+=1
