import re

db = [
    {'book_id': 'B1234', 'title': ' harry potter ', 'price': '250.75'},
    {'book_id': '123', 'title': ' lord of the rings ', 'price': '-50'},
    {'book_id': 'B5678', 'title': None, 'price': '300'}
]

def validateBooks(dataset):
    for i in dataset:
        b = i.get('book_id')
        t = i.get('title')
        p = i.get('price')

        if b is None or re.fullmatch(r'^B\d{4}', b) is None:
            i['book_id'] = 'invalidBookID'

        if t is None:
            i['title'] = 'Unknown'
        else:
            i['title'] = t.strip().title()

        if p is None or re.fullmatch(r'^\d+(\.\d+)?$',p) is None:
                i['price'] = 0.0
        else:
            i['price'] = float(p)

                

    return dataset

print(validateBooks(db))
