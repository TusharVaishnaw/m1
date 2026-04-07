db = [{'title': ' harry potter '}, {'title': None}, {'title': 'the great GATSBY'}]

def normalizeTitles(dataset):
    
    for i in dataset:
        t = i.get('title')
        if t == None:
            i['title'] = 'Unknown'
        else:
            i['title'] = t.strip().title()
        
    return dataset
print(normalizeTitles(db))

















