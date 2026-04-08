import re
import ast
import sys

# ─────────────────────────────────────────
# Q15. Validate Hotel Booking Records
# ─────────────────────────────────────────
def validateBookings(dataset):
    def clean_booking_id(b):
        if b and re.fullmatch(r'HB\d{5}', str(b)):
            return b
        return 'invalidBookingID'

    def clean_name(n):
        if n is None: return 'Unknown'
        return n.strip().title()

    def clean_room_type(rt):
        if rt is None: return 'STANDARD'
        return rt.strip().upper()

    def clean_nights(n):
        try:
            n = int(n)
            return n if n > 0 else 1
        except:
            return 1

    def clean_price(p):
        try:
            p = float(p)
            return p if p > 0 else 0.0
        except:
            return 0.0

    result = []
    for rec in dataset:
        r = dict(rec)
        r['booking_id']      = clean_booking_id(r.get('booking_id'))
        r['guest_name']      = clean_name(r.get('guest_name'))
        r['room_type']       = clean_room_type(r.get('room_type'))
        r['nights']          = clean_nights(r.get('nights'))
        r['price_per_night'] = clean_price(r.get('price_per_night'))
        r['total_cost']      = round(r['nights'] * r['price_per_night'], 2)
        result.append(r)
    return result

lines = sys.stdin.read().strip().split('\n')
dataset = [ast.literal_eval(line) for line in lines]
print(validateBookings(dataset))
