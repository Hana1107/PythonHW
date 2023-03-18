def cacti_number(arr):
    counter = 0
    availability = True
    for i in range(len(arr)): # i = row(left)
        for j in range(len(arr[0])): # j = column(right)
            if arr[i][j] == 1:
                availability = False
            elif i > 0 and arr[i - 1][j] == 1: # checks up
                availability = False
            elif i < len(arr) - 1 and arr[i + 1][j] == 1: # checks down
                availability = False
            elif j < len(arr) - 1 and arr[i][j + 1] == 1: # checks right
                availability = False
            elif j > 0 and arr[i][j - 1] == 1: # checks left
                availability = False

            if availability:
                arr[i][j] = 1
                counter += 1
            
            availability = True

    return counter