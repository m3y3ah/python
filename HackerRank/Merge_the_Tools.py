def merge_the_tools(string: str, k: int):
    
    a = ''
    b= ''
    for i in string:
        if i in a:
            b = b+i
        else:
            a = a+i
            b = b+i
        if len(b)/k==1:
            print(a)
            a = ''
            b = ''

               #######################
    ############                    ############
  ######  note: the code below is very silly ######
######################################################
                
    # my_list = [(string[x:x+k])for x in range(0, len(string), k)]
    # for word in my_list:
    #     sub = ""
    #     i = 0
    #     x = len(word)
    #     while i < x:
    #         temp = word
    #         if word[i] in word[i+1:]:
    #             sub += word[i]
    #             sub += word.replace(word[i], '')
    #             i += (len(temp)-len(temp.replace(word[i], ''))+1)
    #         elif word[i] not in sub and word[i] in word[i+1:]:
    #             sub += word[i]
    #             i += +1
    #         else:
    #             sub += word[i]
    #             i += 1              
    #     print(sub)
    # 
#AAABCADDE
#AABCAAADA
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)