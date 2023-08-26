import textwrap

def wrap(string, max_width):
    # output=""
    # for i in range(0,round(len(string)),max_width):
    #     output+=string[i:i+max_width]+'\n'
    # return output.strip()
    return textwrap.fill(string,max_width)
    

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
    
