import re
import ast
import sys

# ─────────────────────────────────────────
# Q9. Full Address Construction
# ─────────────────────────────────────────
def normalizeAddress(dataset):
    def clean_zipcode(z):
        if z and isinstance(z, str) and re.fullmatch(r'\d{6}', z.strip()):
            return z.strip()
        return None

    def clean_city(c):
        if c is None: return None
        c = c.strip()
        return c if c else None

    def clean_state(s):
        if s is None: return None
        s = s.strip().upper()
        return s if re.fullmatch(r'[A-Z]{2}', s) else None

    def clean_street(st):
        if st is None: return None
        st = st.strip()
        return st if st else None

    result = []
    for rec in dataset:
        r = dict(rec)
        r['street']  = clean_street(r.get('street'))
        r['city']    = clean_city(r.get('city'))
        r['state']   = clean_state(r.get('state'))
        r['zipcode'] = clean_zipcode(r.get('zipcode'))

        if None in (r['street'], r['city'], r['state'], r['zipcode']):
            r['full_address'] = 'None'
        else:
            r['full_address'] = f"{r['street']}, {r['city']}, {r['state']}, {r['zipcode']}"
        result.append(r)
    return result

lines = sys.stdin.read().strip().split('\n')
dataset = [ast.literal_eval(line) for line in lines]
print(normalizeAddress(dataset))
