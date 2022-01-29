# Bozhko_Elena_dz_8
Домашнее задание по уроку 8

ДЗ 1


import re
EMAIL = re.compile(r'([a-z0-9_\.]+)@([a-z0-9]+\.[a-z]+)')
def email_parse(email):
    found_info = EMAIL.findall(email)
    if found_info:
        name, addr = found_info[0]
    else:
        raise ValueError(f'wrong email: {email}')
    print(name, addr)

email_parse('someone@geekbrains.ru')
email_parse('someone@geekbrainsru')


ДЗ 2

import re
import requests

PAD = re.compile(r'((?:[0-9]{,3}[.]){3}[0-9]{,3}) - - '
                 r'(.[0-9]{,2}/\w+/[0-9]{4}:(?:[0-9]{2}:){2}[0-9]{2} \+[0-9]{4}]) .(\w+) '
                 r'([/\w+]{0,}) (?:[^\"]*)\" ([0-9]+) ([0-9]+)')
url = 'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nqinx_logs/nqinx_logs'
content = requests.get(url).text
for arg in PAD.findall(content):
    addr, datetime, r_type, resource, code, size = arg
    print(addr, datetime, r_type, resource, code, size)
    
    ДЗ 3
    
from functools import wraps
def type_logger(func):
    @wraps(func)
    def wrapper(*args):
        for arg in args:
            print(f'{func.__name__}({arg}: {type(arg)})', end=', ')
        return func(*args)

    return wrapper

@type_logger
def calc_cube(*args):
    return list(map(lambda x: x ** 3, args))


a = calc_cube(5, 3)
print(a)
print(calc_cube.__name__)
 
    
