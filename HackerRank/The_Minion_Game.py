def minion_game(string):
    vowels = "AEIOU"
    stuart_score = 0
    Kevin_score = 0
    for x in range(len(string)):
        if string[x] in vowels:
            Kevin_score+=len(string[x:])
        else:
            stuart_score+=len(string[x:])
    if stuart_score > Kevin_score :
        print(f"Stuart {stuart_score}")
    elif Kevin_score >stuart_score:
        print(f"Kevin {Kevin_score}")
    else : 
        print("Draw")
if __name__ == '__main__':
    s = input()
    minion_game(s)
