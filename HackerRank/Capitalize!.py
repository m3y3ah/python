import math
import os
import random
import re
import sys
# Complete the solve function below.
def solve(s:str):
    listt=s.split(" ")
    name=""
    for x in listt:
        if x.isalpha():
            name+=x.capitalize()+" "
        else : 
            name+=x+" "
    return f"{name}"
if __name__ == '__main__':
    s = input()
    result = solve(s)
    print(result)