N=int(input())
a=list()
i=0
if N<=1000000:
    for i in range(N):
        n=input()
        a.append(n)
        i=i+1
        a.sort(reverse=True)
print(a)
