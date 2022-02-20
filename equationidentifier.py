def initial_formatter(text_query):
    text = text_query.lower().split("\n")
    return list(text)

def sampler(text_data):
    f = open(text_data)
    organized = f.read().split()
    
    return organized

def negative_nums (lines):
    state = 0
    for line in range(len(lines)):
        for char in range(line):
            print (lines[line][char])
            if lines[line][char].isnumeric():
                state += 1
        if state >= 3:
            return True
    return False

def symbol(lines, reference_point):
    counter = 0
    for line in lines:
        for char in line:
            if str(char.strip()) in reference_point:
                counter += 1
    
        if counter >= 3: 
            return True
    
    return False
     
#sample run
""" 
#brackets, symbols for equations, equals and plus signs, asterisk, units (have spaces surrounding them)
x = initial_formatter("-1.40 m = (0 m/s)(t) + 0.5(-1.67 m/s?)(t) \n -1.40 m = (0 m/s)(t) + 0.5(-1.67 m/s?)(t)? \n -1.40 m =0 + (-0.835 m/s’)*(t)? \n (-1.40 m)/(-0.835 m/s)? = (t)? \n 1.68 s? = t? \n V1.68 s? = vt?")


j = sampler("symbols.txt")
print(symbol(x,j))
             """
