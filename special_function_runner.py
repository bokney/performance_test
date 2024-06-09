
import time
from datetime import datetime
from datetime import date
from random import randrange

def get_random():
    random_number = 5
    # i rolled a dice and it landed on 5
    return random_number

def get_insightful_ponder():
    insightful_ponders = [
        ">>> it's function time heck yeah",
        ">>> time to run a function",
        ">>> woo function time let's go",
        ">>> who's ready for function time",
        ">>> can you believe it's function time again already",
        ">>> whats that, another function huh",
        ">>> imminent function call, function being ran",
        ">>> i run the function for you now",
        ">>> let's navigate to function island",
        ">>> buckle up buddy, a function is being ran",
        ">>> octopus says it's time for a function",
        ">>> it's happening: function activation" ]
    return print(insightful_ponders[randrange(len(insightful_ponders))])

def function_introduction(func):
    pleasant_introductions = [
        lambda var: f'>>> today\'s function is {var}',
        lambda var: f'>>> we are looking at function {var}',
        lambda var: f'>>> inspecting function {var}',
        lambda var: f'>>> running function {var}' ]
    print(pleasant_introductions[randrange(4)](func))

def its_function_time(func):
    get_insightful_ponder()
    function_introduction(func)
    now = datetime.now()
    today = date.today()
    print(f'>>> at {now.strftime("%H:%M:%S")} on {today.strftime("%d-%m-%y")}')
    start = time.perf_counter()
    func()
    end = time.perf_counter()
    print(f'start time:\t{start}\nend time:\t{end}\ntotal time:\t{end - start}')
