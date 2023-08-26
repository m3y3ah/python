def swap_case(s):
    str=""
    for char in s: 
        if char.isalpha():
            if char.isupper():
                str+=char.lower()
            elif char.islower():
                str+=char.upper()
        else:
            str+=char
    return str
        
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

# def swap_case(s):
#     return s.swapcase() #LOL
