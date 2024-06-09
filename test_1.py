from special_function_runner import its_function_time

def test_function():
    for x in range(6900):
        y = x ** x
    print('I AM A VAMPIRE BAT')
    position = 0
    direction = 1
    width = 128
    for x in range(42069):
        y = x ** (x % 256)
        if y % 2048 == 0:
            for j in range(width):
                if j == position:
                    print('0', end='')
                else: print('-', end='')
            print('')
            position += direction
            if position == 0 or position >= width - 1:
                direction *= -1

its_function_time(test_function)
