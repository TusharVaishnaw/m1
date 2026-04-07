
import re

db = [{'book_id': 'B1234'}, {'book_id': '123'}, {'book_id': None}]

def validateBookIDs(dataset):
    
    for i in dataset:
        bid = i['book_id']
        if bid==None or re.fullmatch(r'B\d{4}',bid)== None:
            i['book_id'] = 'invalidBookID'
    return dataset
print(validateBookIDs(db))

















