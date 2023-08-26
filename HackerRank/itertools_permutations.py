from itertools import permutations as prem
word, r=input().split()
l=list(prem(word,int(r)))
l.sort()
print('\n'.join([''.join(x) for x in l]))

# AC
# AH
# AK
# CA
# CH
# CK
# HA
# HC
# HK
# KA
# KC
# KH