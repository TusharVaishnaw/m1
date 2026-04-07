
import re

db = [{'price': '250.75'}, {'price': '-50'}, {'price': 'abc'}, {'price': None}]

def validatePrice(dataset):
    
    for i in dataset:
        
        p = i.get('price')
        try:
            val = float(p)
            if val<0:
                i['price']=0.0
            else:
                i['price'] = val
        except (TypeError, ValueError):
            i['price'] = 0.0
        
    return dataset
print(validatePrice(db))

