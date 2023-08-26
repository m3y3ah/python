import string
def print_rangoli(size):
    # copy paste ... after 2hrs :( 
    n = 4*(size - 1) + 1
    l = [chr(size - i + 96) for i in range(size)]
    r = [chr(i + 97) for i in range(size)]
    for i in range(size):
        print('-'.join(l[:i + 1] + r[size - i:]).center(n, '-'))
    for i in range(size - 1):
        print('-'.join(l[:size - i - 1] + r[i + 2:]).center(n, '-'))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
    
    
