if __name__ == '__main__':
    N = int(input())
    list = []
    commands=[]
    for _ in range(N):
        commands.append(input())
    for in_command in commands:
        if in_command.startswith("insert"):
            list.insert(int(in_command.split()[1]),int(in_command.split()[-1]))
        elif in_command.startswith("print"):
            print(list)
        elif in_command.startswith("remove"):
            list.remove(int(in_command.split()[-1]))
        elif in_command.startswith("append"):
            list.append(int(in_command.split()[-1]))
        elif in_command.startswith("sort"):
            list.sort()
        elif in_command.startswith("pop"):
            list.pop()
        elif in_command.startswith("reverse"):
            list.reverse()
    
