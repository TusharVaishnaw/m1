import re
import ast
import sys

# ─────────────────────────────────────────
# Q10. Validate Employee Records
# ─────────────────────────────────────────
def validateEmployees(dataset):
    def clean_emp_id(e):
        if e and re.fullmatch(r'E\d{5}', str(e)):
            return e
        return 'invalidEmpID'

    def clean_name(n):
        if n is None: return 'Unknown'
        return n.strip().title()

    def clean_age(a):
        try:
            a = int(a)
            return a if 18 <= a <= 65 else -1
        except:
            return -1

    def clean_email(e):
        if e is None: return 'invalidEmail'
        e = e.strip().lower()
        return e if re.fullmatch(r'[^@\s]+@[^@\s]+\.[^@\s]+', e) else 'invalidEmail'

    result = []
    for rec in dataset:
        r = dict(rec)
        r['emp_id'] = clean_emp_id(r.get('emp_id'))
        r['name']   = clean_name(r.get('name'))
        r['age']    = clean_age(r.get('age'))
        r['email']  = clean_email(r.get('email'))
        result.append(r)
    return result

lines = sys.stdin.read().strip().split('\n')
dataset = [ast.literal_eval(line) for line in lines]
print(validateEmployees(dataset))
