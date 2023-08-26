if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    x = list(arr)
    maxNum = max(*x)
    runner_up = min(*x)
    for number in x:
        if number < maxNum and number > runner_up : 
            runner_up =number
    print(runner_up)
    
########################################
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    print(sorted(set(arr))[-2])