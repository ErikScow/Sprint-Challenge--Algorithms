'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

def count_th(word):
    global count 
    count = 0

    high = len(word) - 1
    low = 0

    mid = (high + low) // 2

    right = word[mid:high + 1]
    left = word[low:mid]

    print(right, left)
    
    if len(word) == 0:
        return 0
    if len(word) == 2:
        if word == 'th':
            count = count + 1
            return count
    else:
        count_th(left)
        count_th(right)

    print(count)
    return count
