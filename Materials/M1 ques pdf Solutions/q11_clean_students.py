import re
import ast
import sys

# ─────────────────────────────────────────
# Q11. Clean Student Records
# ─────────────────────────────────────────
def cleanStudents(dataset):
    def clean_student_id(s):
        if s and re.fullmatch(r'S\d{3}', str(s)):
            return s
        return 'invalidStudentID'

    def clean_name(n):
        if n is None: return 'Unknown'
        return n.strip().title()

    def clean_grade(g):
        try:
            g = float(g)
            return g if 0.0 <= g <= 10.0 else 0.0
        except:
            return 0.0

    def clean_email(e):
        if e is None: return 'invalidEmail'
        e = e.strip().lower()
        return e if re.fullmatch(r'[^@\s]+@[^@\s]+\.[^@\s]+', e) else 'invalidEmail'

    result = []
    for rec in dataset:
        r = dict(rec)
        r['student_id'] = clean_student_id(r.get('student_id'))
        r['name']       = clean_name(r.get('name'))
        r['grade']      = clean_grade(r.get('grade'))
        r['email']      = clean_email(r.get('email'))
        result.append(r)
    return result

lines = sys.stdin.read().strip().split('\n')
dataset = [ast.literal_eval(line) for line in lines]
print(cleanStudents(dataset))
