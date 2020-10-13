'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

def count_th(word):
    print('full word: ', word)
    print('first two letters: ', word[0:2])
    if len(word) < 2:
        return 0 
    if word[0:2] == 'th':
        x = word[2:len(word)]
        print('passed, remaining: ', x)
        return 1 + count_th(x)

    y = word[1:len(word)]
    print('failed, remaining: ', y)
    return count_th(y)
