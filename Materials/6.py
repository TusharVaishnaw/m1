import re
db = [{'zipcode': '560001'}, {'zipcode': '12345'}, {'zipcode': 'ABCDEF'}, {'zipcode': None}]


def validateZipcode(data):

    for i in data:
        z = i['zipcode']
        if z is None or re.fullmatch(r'\d{6}', z) is None:
            i['zipcode'] = None
        
    return data

print(validateZipcode(db))
