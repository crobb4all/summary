# от 0 до stop (не включая значение stop)
for i in range(7):
    print(i, end=' ')

#> 0 1 2 3 4 5 6

# от start до stop
for i in range(4, 11):
    print(i, end=' ')

#> 4 5 6 7 8 9 10

# от start до stop с шагом step
for i in range(4, 11, 2):
    print(i, end=' ')

#> 4 6 8 10

# последовательность в обратном порядке (не включая значение stop)
for i in range(10, 0, -1):
    print(i, end=' ')

#> 10 9 8 7 6 5 4 3 2 1
