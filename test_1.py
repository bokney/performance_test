from special_function_runner import its_function_time
from super_special_function_runner import run_and_analyze
from sprint import sprint, wait

def test_function():
    for x in range(4096):
        y = x ** x
    print('🦇 🦇 🦇 🦇 🦇 🦇 🦇 🦇 🦇 🦇 🦇 🦇 🦇 🦇 🦇 🦇 ')
    position = 0
    direction = 1
    width = 128
    for x in range(1024):
        y = x ** (x % 256)
        if y % 2048 == 0:
            line = []
            for j in range(width):
                if j == position:
                    line.append('0')
                else: line.append('-')
            sprint("".join(line))
            position += direction
            if position == 0 or position >= width - 1:
                direction *= -1

# its_function_time(test_function)

do_it = run_and_analyze(test_function)
do_it()
sprint("Wasn't that fun?")
wait(0.8)
sprint("Let's do it again!")
wait(1.8)
do_it()
