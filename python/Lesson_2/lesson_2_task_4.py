def fizz_buzz(n):
     for i in range(0, n + 1):
        if i % 3 == 0 and i % 5 ==0:
            print(i, 'FizzBuzz')
        elif i % 3 == 0:
            print(i, 'Fizz')
        elif i % 5 ==0:
            print(i, 'Buzz')
        else:
            print(i)

fizz_buzz(30)