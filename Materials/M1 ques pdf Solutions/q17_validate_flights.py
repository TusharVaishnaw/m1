import re
import ast
import sys

# ─────────────────────────────────────────
# Q17. Validate Flight Records
# ─────────────────────────────────────────
def validateFlights(dataset):
    def clean_flight_id(f):
        if f and re.fullmatch(r'[A-Z]{2}\d{4}', str(f)):
            return f
        return 'invalidFlightID'

    def clean_location(loc):
        if loc is None: return 'UNKNOWN'
        loc = loc.strip().upper()
        return loc if loc else 'UNKNOWN'

    def clean_duration(d):
        try:
            d = int(d)
            return d if d > 0 else 0
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
        r['flight_id']     = clean_flight_id(r.get('flight_id'))
        r['origin']        = clean_location(r.get('origin'))
        r['destination']   = clean_location(r.get('destination'))
        r['duration_mins'] = clean_duration(r.get('duration_mins'))
        r['price']         = clean_price(r.get('price'))
        result.append(r)
    return result

lines = sys.stdin.read().strip().split('\n')
dataset = [ast.literal_eval(line) for line in lines]
print(validateFlights(dataset))
