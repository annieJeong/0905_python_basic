"""
hello.py
author  : Jeong inwoo
date    : 2016_09_05
"""

print('hello, world')

a=3
b=4

print(a+b)

print(r'안녕하세요 \n "정인우"님')

my_str = 'Hello my name is jeong inwoo. you can call me jeong or annie'
print(my_str[23:28])
print(my_str[17:22])

my_name = my_str.split(' ')[5][:-1]
print(my_name)

from datetime import datetime
my_time = datetime.now()

print(my_time)

import math

print(math.sqrt(13131))

def distance_from_zero(distance):
    if type(distance) == int or type(distance) == float:
        return math.fabs(distance)
    else :
        return 'Nope'


print(distance_from_zero(-4560))


def param_test(a=10, b=20):
    """
    기존. ordered parameter.
     param_test(3) 이라고 호출할경우 == a에게만 적용됨
     param_test(b=30, a=20)  == 순서상관없이 적용가능함.
     파라미터를 지정하여 넘김. -> Named parameter // 권장됨
     param_test(b=2) == b=2라고 순서상관없이. 값변경하여 함수실행됨

     """
    return a+b


print(param_test(b=2))

def var_param_test(*p):
    for item in p:
        print(item)

def double_return():
    return 3,4,5

import calculator
print(calculator.add(3,5))
print(calculator.sub(5,3))


import sys

print(sys.path)