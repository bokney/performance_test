from special_function_runner import its_function_time

def test_function():
    for x in range(6900):
        y = x ** x
    print('I AM A VAMPIRE BAT')
    for x in range(6942069):
        y = x ** ((x % 64) % 32)
        if (y % 2048 == 0): print(y)

its_function_time(test_function)
