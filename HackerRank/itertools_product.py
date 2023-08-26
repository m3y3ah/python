import itertools
list_1=map(int ,input().split())
list_2=map(int,input().split())
print(*list(itertools.product(list_1,list_2)))
