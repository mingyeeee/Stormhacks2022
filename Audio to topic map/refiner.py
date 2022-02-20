def starter_format(text_query):
    text = text_query.lower().split()
    return list(text)


def format_dataset(name):
    data = open(name, encoding = "utf8")
    
    out = {}
    for line in data:
        if ":" in line:
            line = line.lower().split(":")

            out[line[0]] = line[1:]
    
    return out

def lstmkr(words_file):
    data = open(words_file)
    n = data.read().lower().split() 
    return n

def misc(text, common_words):
    counter = 0
   
    while counter < len(text):
        if text[counter] in common_words:
            text.remove(text[counter])
        else:
            counter += 1


def filter(sample, text):
    counter = 0
    keyword = []
    while counter < len(sample):
        
        if sample[counter] in text:
            keyword.append(sample[counter])
            
        counter += 1
    final = set(keyword)
    return final



#Sample run
""" x = starter_format("All right, today we're going to have a look at a physics. All right, today we're going to have a look at the physics kinematics problem. So the question we have is the feather is dropped on the moon from a height of 1.4 meters. The acceleration of gravity on the moon is one point 67 meters/second squared. Determine the time for the feather to fall to the surface of the Moon. All right, so from this word problem, we can drive a few things, such as our knowns and unknowns. So our known variables, such as initial velocity is 0 meter/second, our displacement is one 4 meters in the negative direction, and our acceleration is 167 meters per second squared. In the negative direction, we have one unknown, which is time. And that is the time which it takes for the feather to fall to the surface of the Moon. We can use our formula, displacement equals the initial times time plus half times acceleration times time squared. And we can arrange that to solve for time. So here we're just plugging in our known values and then we can solve the left side and right side. Here we're dividing negative zero point 85 meters/second squared from time in order to isolate the variable. And from that, we get one point 68 seconds squared is equal to time squared. And if we take the square root of both sides, we get one point 29 seconds squared for time. So there we have it. Our conclusion. The feather takes one point, 29 seconds to fall to the surface of the moon.")
common_list = lstmkr("common.txt")
misc (x, common_list)
trial = format_dataset("other.txt")
print(filter(x, trial)) """
