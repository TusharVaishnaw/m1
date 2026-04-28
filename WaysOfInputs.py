
#bhavik soln

    cart = ast.literal_eval(input().strip())
    
    res = {}

   final = []
      
  for item in res.values():
      item['total'] = item['price'] * item['qty']
      final.append(item)

#for comma separated input
    raw_input_data = sys.stdin.read().strip()

# for input format:
'''
{}
{}
{}
'''
    lines = sys.stdin.read().strip().split('\n')
    dataset = []
    for line in lines:
        if line.strip():  # skip empty lines
            record = ast.literal_eval(line)
            dataset.append(record)

    return dataset


# another way for some inputs
data=[]
for line in sys.stdin:
    line = line.strip()
    if line:
        data.append(ast.literal_eval(line))
