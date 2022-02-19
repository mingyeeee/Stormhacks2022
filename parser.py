def starter_format(text_file):
    f = open(text_file)
    text = f.read()
    text = text.lower().split()
    return list(text)


def format_dataset(name):
    data = open(name)
    n = data.read().lower().split()
    
    return n
    

def filter(sample, text):
    counter = 0
   
    while counter < len(sample):
        if sample[counter] in text:
            sample.remove(sample[counter])
        else:
            counter += 1

    return sample



    