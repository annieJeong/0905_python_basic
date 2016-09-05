"""
단어변경
"""


def add_ay (in_word):
    """ 입력받은 단어를 받아 첫글자를 맨뒤에 붙이고, ay를 그 뒤에 붙이는함수"""
    add_last = 'ay'
    if in_word.replace(" ","").isalpha() and len(in_word) > 0:
        add_first = a_input[0:1]
        remain = a_input[1:]
        return 'space is not allow : ' +remain + add_first + add_last
    else :
        return 'please input alphabet'


a_input = input('단어를 하나 입력해 주세요 : ')

print(add_ay(a_input))

