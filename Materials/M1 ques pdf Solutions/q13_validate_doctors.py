import re
import ast
import sys

# ─────────────────────────────────────────
# Q13. Validate Doctor Records
# ─────────────────────────────────────────
def validateDoctors(dataset):
    def clean_doc_id(d):
        if d and re.fullmatch(r'D\d{4}', str(d)):
            return d
        return 'invalidDocID'

    def clean_name(n):
        if n is None: return 'Unknown'
        return n.strip().title()

    def clean_specialization(s):
        if s is None: return 'General'
        return s.strip().title()

    def clean_email(e):
        if e is None: return 'invalidEmail'
        e = e.strip().lower()
        return e if re.fullmatch(r'[^@\s]+@[^@\s]+\.[^@\s]+', e) else 'invalidEmail'

    result = []
    for rec in dataset:
        r = dict(rec)
        r['doc_id']          = clean_doc_id(r.get('doc_id'))
        r['name']            = clean_name(r.get('name'))
        r['specialization']  = clean_specialization(r.get('specialization'))
        r['contact_email']   = clean_email(r.get('contact_email'))
        result.append(r)
    return result

lines = sys.stdin.read().strip().split('\n')
dataset = [ast.literal_eval(line) for line in lines]
print(validateDoctors(dataset))
