from collections import defaultdict
A , B =map(int,input().split())
A_list=defaultdict(list)
B_list=[]
for index in range(1,A+1):
    A_list[input()].append(index)
for index in range(1,B+1):
    B_list.append(input())
for x in B_list :
    if x in A_list :
        print(*A_list.get(x))
    else :
        print(-1)  



# 5 2
# a
# a
# b
# a
# b
# a
# b




# 5 2
# a
# a
# b
# a
# b
# a
# c
