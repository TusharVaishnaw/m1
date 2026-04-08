
import re
db = [{'phone': '123-456-7890'}, {'phone': '(123) 45 678'}, {'phone': None}]

def cleanPhones(dataset):
    
    for i in dataset:
        p = i.get('phone')
        if p is not None:
            ans=re.sub(r'\D','',i['phone'])
            if re.fullmatch(r'\d{10}',ans) is None:
                i['phone'] = 'invalidPhone'
            else:
                i['phone'] = ans
        else:
            i['phone'] = 'invalidPhone'
        
    return dataset
print(cleanPhones(db))

# e= [{'phone': '1234567890'}, {'phone': 'invalidPhone'}, {'phone': 'invalidPhone'}]















