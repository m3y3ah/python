N = int(input())
numbers=[]
for i in range(N):
    numbers.append(tuple(input().split()))
for a,b in numbers : 
    try :
        print(int(a)//int(b))
    except ZeroDivisionError as e: 
        print(f"Error Code: {e}")
    except ValueError as Ve: 
        print(f"Error Code: {Ve}")
        
        
