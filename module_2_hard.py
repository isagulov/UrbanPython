for i in range(3, 21):
    result = ""
    for j in range(1, i):
        for k in range(j, i):
            #print(i, j, k)
            if i % (j + k) == 0 and j != k:
                result += str(j) + str(k)

    print(i, '-', result)
