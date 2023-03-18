def merge(first, second):
    sorted = []
    i = 0
    j = 0
    while i < len(first) and j < len(second):
        if first[i] <= second[j]:
            sorted.append(first[i])
            i = i + 1
        else:
            sorted.append(second[j])
            j = j + 1
    
    if i < len(first):
        while i < len(first):
            sorted.append(first[i])
            i = i + 1
    else:
        while j < len(second):
            sorted.append(second[j])
            j = j + 1

    return sorted


