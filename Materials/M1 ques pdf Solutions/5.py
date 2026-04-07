
import re

db = [{'state': ' ka '}, {'state': 'Maharashtra'}, {'state': None}]

def normalizeState(dataset):
    
    for i in dataset:
        s = i.get('state')
        if s is  None or re.fullmatch(r'[a-zA-Z]{2}',s.strip()) is None:
            i['state'] = None
        else:
            i['state']=s.strip().upper()
        
    return dataset
print(normalizeState(db))

# EXPECTED: [{'state': 'KA'}, {'state': None}, {'state': None}]
















