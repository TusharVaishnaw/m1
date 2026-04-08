import re
import ast
import sys

# ─────────────────────────────────────────
# Q12. Normalize Product Catalog
# ─────────────────────────────────────────
def normalizeProducts(dataset):
    def clean_product_id(p):
        if p and re.fullmatch(r'P\d{5}', str(p)):
            return p
        return 'invalidProductID'

    def clean_name(n):
        if n is None: return 'Unnamed'
        return n.strip().title()

    def clean_category(c):
        if c is None: return 'UNCATEGORIZED'
        return c.strip().upper()

    def clean_price(p):
        try:
            p = float(p)
            return p if p > 0 else 0.0
        except:
            return 0.0

    result = []
    for rec in dataset:
        r = dict(rec)
        r['product_id'] = clean_product_id(r.get('product_id'))
        r['name']       = clean_name(r.get('name'))
        r['category']   = clean_category(r.get('category'))
        r['price']      = clean_price(r.get('price'))
        result.append(r)
    return result

lines = sys.stdin.read().strip().split('\n')
dataset = [ast.literal_eval(line) for line in lines]
print(normalizeProducts(dataset))
