def sort_dictionary(dict):
    listkeys = list(dict.keys())
    listvals = list(dict.values())
    sortedlist = []
    i = 0
    j = 0
    smallest = 0
    while i < len(dict):
        while j < len(listkeys):
            if listvals[smallest][1] > listvals[j][1]:
                smallest = j
            j += 1
        sortedlist.append((listkeys[smallest], listvals[smallest][0]))
        del listkeys[smallest]
        del listvals[smallest]
        i += 1
        smallest = 0

    return sortedlist

