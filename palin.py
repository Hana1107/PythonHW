def palindrome(list):
    if len(list) <= 1:
        return True
    i = 0
    j = len(list) - 1
    while i < j:
        if list[i] != list[j]:
            return False
        i = i + 1
        j = j - 1

    return True