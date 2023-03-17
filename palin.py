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


list_one = [1,2,"Espresso", "Madeline",2,1]
list_two = ['a', True, False, False, True, 'a']
list_three = [3,4,6,"Espresso",6,4,3]
print(palindrome(list_one))
print(palindrome(list_two))
print(palindrome(list_three))