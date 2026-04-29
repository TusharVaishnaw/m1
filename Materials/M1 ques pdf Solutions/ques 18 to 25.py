import re
import ast
import sys

# ─────────────────────────────────────────
# Q18. Validate and Enrich User Profiles
# ─────────────────────────────────────────
def validateProfiles(dataset):
    def clean_user_id(u):
        if u and re.fullmatch(r'U\d{6}', str(u)):
            return u
        return 'invalidUserID'

    def clean_name(n):
        if n is None: return 'Unknown'
        return n.strip().title()

    def clean_dob(d):
        if d is None: return 'invalidDOB'
        if re.fullmatch(r'\d{4}-\d{2}-\d{2}', str(d).strip()):
            return d.strip()
        return 'invalidDOB'

    def clean_email(e):
        if e is None: return 'invalidEmail'
        e = e.strip().lower()
        return e if re.fullmatch(r'[^@\s]+@[^@\s]+\.[^@\s]+', e) else 'invalidEmail'

    def clean_phone(p):
        if p is None: return 'invalidPhone'
        digits = re.sub(r'\D', '', str(p))
        return digits if len(digits) == 10 else 'invalidPhone'

    def clean_address(addr):
        if not isinstance(addr, dict):
            return {'street': None, 'city': None, 'state': None, 'zipcode': None, 'full_address': 'None'}

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

        a = dict(addr)
        a['street']  = clean_street(a.get('street'))
        a['city']    = clean_city(a.get('city'))
        a['state']   = clean_state(a.get('state'))
        a['zipcode'] = clean_zipcode(a.get('zipcode'))

        if None in (a['street'], a['city'], a['state'], a['zipcode']):
            a['full_address'] = 'None'
        else:
            a['full_address'] = f"{a['street']}, {a['city']}, {a['state']}, {a['zipcode']}"
        return a

    result = []
    for rec in dataset:
        r = dict(rec)
        r['user_id'] = clean_user_id(r.get('user_id'))
        r['name']    = clean_name(r.get('name'))
        r['dob']     = clean_dob(r.get('dob'))
        r['email']   = clean_email(r.get('email'))
        r['phone']   = clean_phone(r.get('phone'))
        r['address'] = clean_address(r.get('address'))
        result.append(r)
    return result

lines = sys.stdin.read().strip().split('\n')
dataset = [ast.literal_eval(line) for line in lines]
print(validateProfiles(dataset))


# ─────────────────────────────────────────
# Q19. Multi-Level Product Inventory Validation
# ─────────────────────────────────────────
def validateInventory(dataset):
    def clean_product_id(p):
        if p and re.fullmatch(r'P\d{5}', str(p)):
            return p
        return 'invalidProductID'

    def clean_name(n):
        if n is None: return 'Unnamed'
        return n.strip().title()

    def clean_warehouse_id(w):
        if w and re.fullmatch(r'WH\d{3}', str(w)):
            return w
        return 'invalidWarehouseID'

    def clean_non_neg_int(v):
        try:
            v = int(v)
            return v if v >= 0 else 0
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
        r['product_id']    = clean_product_id(r.get('product_id'))
        r['name']          = clean_name(r.get('name'))
        r['warehouse_id']  = clean_warehouse_id(r.get('warehouse_id'))
        r['stock']         = clean_non_neg_int(r.get('stock'))
        r['reorder_level'] = clean_non_neg_int(r.get('reorder_level'))
        r['unit_price']    = clean_price(r.get('unit_price'))
        r['reorder_needed']   = r['stock'] <= r['reorder_level']
        r['inventory_value']  = round(r['stock'] * r['unit_price'], 2)
        result.append(r)
    return result

lines = sys.stdin.read().strip().split('\n')
dataset = [ast.literal_eval(line) for line in lines]
print(validateInventory(dataset))


# ─────────────────────────────────────────
# Q20. Validate and Score Loan Applications
# ─────────────────────────────────────────
def validateLoanApplications(dataset):
    def clean_app_id(a):
        if a and re.fullmatch(r'LA\d{7}', str(a)):
            return a
        return 'invalidAppID'

    def clean_name(n):
        if n is None: return 'Unknown'
        return n.strip().title()

    def clean_pos_float(v):
        try:
            v = float(v)
            return v if v > 0 else 0.0
        except:
            return 0.0

    def clean_credit_score(c):
        try:
            c = int(c)
            return c if 300 <= c <= 900 else 0
        except:
            return 0

    def clean_pos_int(v):
        try:
            v = int(v)
            return v if v > 0 else 0
        except:
            return 0

    result = []
    for rec in dataset:
        r = dict(rec)
        r['app_id']           = clean_app_id(r.get('app_id'))
        r['applicant_name']   = clean_name(r.get('applicant_name'))
        r['annual_income']    = clean_pos_float(r.get('annual_income'))
        r['credit_score']     = clean_credit_score(r.get('credit_score'))
        r['loan_amount']      = clean_pos_float(r.get('loan_amount'))
        r['loan_term_months'] = clean_pos_int(r.get('loan_term_months'))

        if r['annual_income'] > 0:
            r['debt_to_income'] = round(r['loan_amount'] / r['annual_income'], 4)
        else:
            r['debt_to_income'] = None

        r['eligible'] = (
            r['credit_score'] >= 650 and
            r['debt_to_income'] is not None and
            r['debt_to_income'] <= 0.4
        )
        result.append(r)
    return result

lines = sys.stdin.read().strip().split('\n')
dataset = [ast.literal_eval(line) for line in lines]
print(validateLoanApplications(dataset))


# ─────────────────────────────────────────
# Q21. Validate Medical Records
# ─────────────────────────────────────────
def validateMedicalRecords(dataset):
    VALID_BLOOD_GROUPS = {'A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-'}

    def clean_patient_id(p):
        if p and re.fullmatch(r'P\d{6}', str(p)):
            return p
        return 'invalidPatientID'

    def clean_name(n):
        if n is None: return 'Unknown'
        return n.strip().title()

    def clean_dob(d):
        if d is None: return 'invalidDOB'
        if re.fullmatch(r'\d{4}-\d{2}-\d{2}', str(d).strip()):
            return d.strip()
        return 'invalidDOB'

    def clean_blood_group(b):
        if b is None: return 'Unknown'
        b = b.strip().upper()
        return b if b in VALID_BLOOD_GROUPS else 'Unknown'

    def clean_allergies(a):
        if not isinstance(a, list): return []
        return [str(item).strip().title() for item in a]

    def clean_email(e):
        if e is None: return 'invalidEmail'
        e = e.strip().lower()
        return e if re.fullmatch(r'[^@\s]+@[^@\s]+\.[^@\s]+', e) else 'invalidEmail'

    result = []
    for rec in dataset:
        r = dict(rec)
        r['patient_id']    = clean_patient_id(r.get('patient_id'))
        r['name']          = clean_name(r.get('name'))
        r['dob']           = clean_dob(r.get('dob'))
        r['blood_group']   = clean_blood_group(r.get('blood_group'))
        r['allergies']     = clean_allergies(r.get('allergies'))
        r['contact_email'] = clean_email(r.get('contact_email'))
        result.append(r)
    return result

lines = sys.stdin.read().strip().split('\n')
dataset = [ast.literal_eval(line) for line in lines]
print(validateMedicalRecords(dataset))


# ─────────────────────────────────────────
# Q22. Validate E-Commerce Transactions
# ─────────────────────────────────────────
def validateTransactions(dataset):
    def clean_txn_id(t):
        if t and re.fullmatch(r'TXN\d{8}', str(t)):
            return t
        return 'invalidTxnID'

    def clean_user_id(u):
        if u and re.fullmatch(r'U\d{6}', str(u)):
            return u
        return 'invalidUserID'

    def clean_items(items):
        if not isinstance(items, list) or len(items) == 0:
            return []
        result = []
        for item in items:
            if not isinstance(item, dict):
                continue
            i = dict(item)
            pid = i.get('product_id')
            i['product_id'] = pid if pid and re.fullmatch(r'P\d{5}', str(pid)) else 'invalidProductID'
            try:
                q = int(i.get('quantity'))
                i['quantity'] = q if q > 0 else 0
            except:
                i['quantity'] = 0
            result.append(i)
        return result

    def clean_pct(p):
        try:
            p = float(p)
            return p if 0 <= p <= 100 else 0.0
        except:
            return 0.0

    result = []
    for rec in dataset:
        r = dict(rec)
        r['txn_id']       = clean_txn_id(r.get('txn_id'))
        r['user_id']      = clean_user_id(r.get('user_id'))
        r['items']        = clean_items(r.get('items'))
        r['discount_pct'] = clean_pct(r.get('discount_pct'))
        r['tax_pct']      = clean_pct(r.get('tax_pct'))
        result.append(r)
    return result

lines = sys.stdin.read().strip().split('\n')
dataset = [ast.literal_eval(line) for line in lines]
print(validateTransactions(dataset))


# ─────────────────────────────────────────
# Q23. Validate School Timetable Records
# ─────────────────────────────────────────
def validateTimetable(dataset):
    VALID_DAYS = {'mon': 'Mon', 'tue': 'Tue', 'wed': 'Wed', 'thu': 'Thu', 'fri': 'Fri'}

    def clean_record_id(r):
        if r and re.fullmatch(r'TT\d{4}', str(r)):
            return r
        return 'invalidRecordID'

    def clean_teacher_id(t):
        if t and re.fullmatch(r'T\d{4}', str(t)):
            return t
        return 'invalidTeacherID'

    def clean_subject(s):
        if s is None: return 'Unknown'
        return s.strip().title()

    def clean_day(d):
        if d is None: return 'Unknown'
        return VALID_DAYS.get(d.strip().lower(), 'Unknown')

    def clean_time(t):
        if t is None: return 'invalidTime'
        t = str(t).strip()
        if re.fullmatch(r'([01]\d|2[0-3]):[0-5]\d', t):
            return t
        return 'invalidTime'

    def clean_room_id(r):
        if r and re.fullmatch(r'R\d{3}', str(r)):
            return r
        return 'invalidRoomID'

    result = []
    for rec in dataset:
        r = dict(rec)
        r['record_id']  = clean_record_id(r.get('record_id'))
        r['teacher_id'] = clean_teacher_id(r.get('teacher_id'))
        r['subject']    = clean_subject(r.get('subject'))
        r['day_of_week'] = clean_day(r.get('day_of_week'))
        r['start_time'] = clean_time(r.get('start_time'))
        r['end_time']   = clean_time(r.get('end_time'))
        r['room_id']    = clean_room_id(r.get('room_id'))

        r['valid_slot'] = (
            r['start_time'] != 'invalidTime' and
            r['end_time'] != 'invalidTime' and
            r['start_time'] < r['end_time']
        )
        result.append(r)
    return result

lines = sys.stdin.read().strip().split('\n')
dataset = [ast.literal_eval(line) for line in lines]
print(validateTimetable(dataset))


# ─────────────────────────────────────────
# Q24. Validate Research Paper Records
# ─────────────────────────────────────────
def validatePapers(dataset):
    def clean_paper_id(p):
        if p and re.fullmatch(r'RP\d{6}', str(p)):
            return p
        return 'invalidPaperID'

    def clean_title(t):
        if t is None: return 'Untitled'
        return t.strip().title()

    def clean_authors(a):
        if not isinstance(a, list) or len(a) == 0:
            return ['Unknown']
        cleaned = [str(x).strip().title() for x in a if str(x).strip()]
        return cleaned if cleaned else ['Unknown']

    def clean_year(y):
        try:
            y = int(y)
            return y if 1900 <= y <= 2025 else 0
        except:
            return 0

    def clean_doi(d):
        if d is None: return 'invalidDOI'
        d = str(d).strip()
        return d if re.fullmatch(r'10\.\d{4,}/.+', d) else 'invalidDOI'

    def clean_citation_count(c):
        try:
            c = int(c)
            return c if c >= 0 else 0
        except:
            return 0

    result = []
    for rec in dataset:
        r = dict(rec)
        r['paper_id']       = clean_paper_id(r.get('paper_id'))
        r['title']          = clean_title(r.get('title'))
        r['authors']        = clean_authors(r.get('authors'))
        r['published_year'] = clean_year(r.get('published_year'))
        r['doi']            = clean_doi(r.get('doi'))
        r['citation_count'] = clean_citation_count(r.get('citation_count'))
        result.append(r)
    return result

lines = sys.stdin.read().strip().split('\n')
dataset = [ast.literal_eval(line) for line in lines]
print(validatePapers(dataset))


# ─────────────────────────────────────────
# Q25. Validate and Summarize Sales Records
# ─────────────────────────────────────────
def validateSales(dataset):
    def clean_sale_id(s):
        if s and re.fullmatch(r'S\d{8}', str(s)):
            return s
        return 'invalidSaleID'

    def clean_salesperson_id(s):
        if s and re.fullmatch(r'SP\d{5}', str(s)):
            return s
        return 'invalidSPID'

    def clean_region(r):
        if r is None: return 'Unknown'
        return r.strip().title()

    def clean_date(d):
        if d is None: return 'invalidDate'
        if re.fullmatch(r'\d{4}-\d{2}-\d{2}', str(d).strip()):
            return d.strip()
        return 'invalidDate'

    def clean_products(products):
        if not isinstance(products, list) or len(products) == 0:
            return []
        result = []
        for item in products:
            if not isinstance(item, dict):
                continue
            p = dict(item)
            pid = p.get('product_id')
            p['product_id'] = pid if pid and re.fullmatch(r'P\d{5}', str(pid)) else 'invalidProductID'
            try:
                u = int(p.get('units_sold'))
                p['units_sold'] = u if u > 0 else 0
            except:
                p['units_sold'] = 0
            try:
                up = float(p.get('unit_price'))
                p['unit_price'] = up if up > 0 else 0.0
            except:
                p['unit_price'] = 0.0
            p['line_total'] = round(p['units_sold'] * p['unit_price'], 2)
            result.append(p)
        return result

    result = []
    for rec in dataset:
        r = dict(rec)
        r['sale_id']        = clean_sale_id(r.get('sale_id'))
        r['salesperson_id'] = clean_salesperson_id(r.get('salesperson_id'))
        r['region']         = clean_region(r.get('region'))
        r['sale_date']      = clean_date(r.get('sale_date'))
        r['products']       = clean_products(r.get('products'))
        r['grand_total']    = round(sum(p['line_total'] for p in r['products']), 2)
        result.append(r)
    return result

lines = sys.stdin.read().strip().split('\n')
dataset = [ast.literal_eval(line) for line in lines]
print(validateSales(dataset))
