import re
import ast
import sys

# ─────────────────────────────────────────
# Q14. Validate Order Records
# ─────────────────────────────────────────
def validateOrders(dataset):
    def clean_order_id(o):
        if o and re.fullmatch(r'ORD\d{6}', str(o)):
            return o
        return 'invalidOrderID'

    def clean_name(n):
        if n is None: return 'Unknown'
        return n.strip().title()

    def clean_quantity(q):
        try:
            q = int(q)
            return q if q > 0 else 0
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
        r['order_id']       = clean_order_id(r.get('order_id'))
        r['customer_name']  = clean_name(r.get('customer_name'))
        r['quantity']       = clean_quantity(r.get('quantity'))
        r['price_per_unit'] = clean_price(r.get('price_per_unit'))
        r['total_price']    = round(r['quantity'] * r['price_per_unit'], 2)
        result.append(r)
    return result

lines = sys.stdin.read().strip().split('\n')
dataset = [ast.literal_eval(line) for line in lines]
print(validateOrders(dataset))
