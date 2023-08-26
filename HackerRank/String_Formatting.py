def print_formatted(number):
    string = ""
    for x in range(1, number+1):
        string = ""
        string +="{Decimal}".format(Decimal=x).rjust(len(bin(number)[2:]))
        string +="{Octal:o}".format(Octal=x).rjust(len(bin(number)[2:])+1)
        string +="{Hexadecimal:X}".format(Hexadecimal=x).rjust(len(bin(number)[2:])+1)
        string +="{Binary:b}".format(Binary=x).rjust(len(bin(number)[2:])+1)
        string +='\n'
        print(string.rstrip()) 
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)