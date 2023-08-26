n, m = map(int, input().split())
for x in range(1,n,2):
    print((".|."*x).center(m, '-'))
print("WELCOME".center(m, '-'))
for x in range(n-2,0,-2):
    print((".|."*x).center(m, '-'))
   
