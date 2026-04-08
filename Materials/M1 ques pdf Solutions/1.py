import re
import sys
import ast
# db = {'name': 'Alice', 'email': 'ALICE@Example.COM'},
#  {'name': 'Bob', 'email': None},
#  {'name': 'Carol', 'email': 'not-an-email'}


def cleanEmails():
    rdata = sys.stdin.read().strip().split('\n')
    data = [ast.literal_eval(l) for l in rdata]
    for i in data:
        e = i.get('email')
        
        if e is None or re.fullmatch(r'^[a-zA-Z0-9_%.+-]+@[a-zA-Z0-9_.]+\.[A-Za-z]+$', e) is None:
            i['email'] = 'invalidEmail'
        else:
            i['email'] = e.lower()
        
    return data

print(cleanEmails())

'''
expected:
[{'name': 'Alice', 'email': 'alice@example.com'},
 {'name': 'Bob', 'email': 'invalidEmail'},
 {'name': 'Carol', 'email': 'invalidEmail'}]
'''
