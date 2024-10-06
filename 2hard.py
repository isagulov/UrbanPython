num = 5 #int(input('Введите число от 1 до 25:'))
result = ""
for i in range(3, 21 ):

    for j in range(1, i +1):
        if i % (i + j) == 0:
           result = result + str(i)
           result = result + str(j)
           print(result)


