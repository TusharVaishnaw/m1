import re
import ast
import sys

# ─────────────────────────────────────────
# Q16. Validate Vehicle Records
# ─────────────────────────────────────────
def validateVehicles(dataset):
    def clean_vin(v):
        if v and re.fullmatch(r'[A-Za-z0-9]{17}', str(v)):
            return v
        return 'invalidVIN'

    def clean_text(t):
        if t is None: return 'Unknown'
        return t.strip().title()

    def clean_year(y):
        try:
            y = int(y)
            return y if 1900 <= y <= 2025 else 0
        except:
            return 0

    def clean_price(p):
        try:
            p = float(p)
            return p if p > 0 else 0.0
        except:
            return 0.0

    result = []
    for rec in dataset:
        r = dict(rec)
        r['vin']   = clean_vin(r.get('vin'))
        r['make']  = clean_text(r.get('make'))
        r['model'] = clean_text(r.get('model'))
        r['year']  = clean_year(r.get('year'))
        r['price'] = clean_price(r.get('price'))
        result.append(r)
    return result

lines = sys.stdin.read().strip().split('\n')
dataset = [ast.literal_eval(line) for line in lines]
print(validateVehicles(dataset))
