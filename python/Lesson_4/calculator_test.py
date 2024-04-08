from calculator import Calculator

calculator = Calculator()

def test_sum_positive_nums():
    calculator = Calculator()
    res = calculator.sum(4, 5)
    assert res == 9

def test_sum_negative_nums():
    calculator = Calculator()
    res = calculator.sum(-6, -10)
    assert res == -16

def test_sum_pos_negat_nums():
    calculator = Calculator()
    res = calculator.sum(5, -5)
    assert res == 0



# res = calculator.sum(6.6, 3.3)
# res = round(res, 1)
# assert res == 9.9

# res = calculator.sum(3, 0)
# assert res == 3

# numbers = []
# res = calculator.avg(numbers)
# assert res == 0

# numbers = [1,2,3,4,5,6,7,8,9,5]
# res = calculator.avg(numbers)
# assert res == 5

# res = calculator.div(10, 0)
# assert res == None