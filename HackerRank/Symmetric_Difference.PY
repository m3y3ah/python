set_1_size = int(input())
set_1 = set(map(int, input().split()))
set_2_size=int(input())
set_2 = set(map(int, input().split()))
out=list(set_1.symmetric_difference(set_2))
out.sort()
print(*out,sep='\n')


# 4
# 2 4 5 9 
# 4
# 2 4 11 12


# 2
# 8 -10
# 3
# 5 6 7