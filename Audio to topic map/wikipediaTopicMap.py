import wikipediaapi
import json
import os
import time

# read the json file
with open('query_words.json') as json_file:
    data = json.load(json_file)
    query_words = data['query_words']

def print_first_level_sections(sections, numberofsections):
    counter = 0
    for s in sections:
        print("\t" + s.title)
        page = wiki_wiki.page(s.title)
        if(page.exists()):
            print("\t" + page.fullurl)
        else:
            print("\tPage does not exist")
        if len(nodelabels) <=13:
            nodelabels.append(s.title)
        counter += 1
        if counter == numberofsections:
            break

#topic = 'projectile_motion'
#topic = "gravity"
#topic = "acceleration"
#topic = "velocity"

# title
#print(wikipage.title)

# summary
#print("Page - Summary: %s" % wikipage.summary)

# url
#print(wikipage.fullurl)

# sections
#print_sections(wikipage.sections)
def print_second_level_sections(page, numberoftopics):
    # navigate to 2nd level of sections
    branchingCounter = 0
    deadendCounter = 0
    append = False
    for slevel1 in page.sections:
        for slevel2 in slevel1.sections:
            # check if there exist an article for the 2nd level section
            wikisectionpage = wiki_wiki.page(slevel2.title)
            if(not wikisectionpage.exists()):
                if deadendCounter == 0:
                    continue
                # check if page does not exist or the title is not correct
                try:
                    print(slevel2.title.encode('utf-8'))
                    print(page.fullurl+"#"+slevel2.title.replace(" ", "_"))
                    links.append(page.fullurl+"#"+slevel2.title.replace(" ", "_"))
                except:
                    print("Page does not exist")
                
                print("Futher pages do not exist")

                print(deadendCounter)
                deadendCounter += 1
                
            elif(wikisectionpage.exists()):
                print(slevel2.title.encode('utf-8'))
                print(page.fullurl+"#"+slevel2.title.replace(" ", "_"))
                print_first_level_sections(wikisectionpage.sections, 3)
                links.append(page.fullurl+"#"+slevel2.title.replace(" ", "_"))
                
                if len(nodelabels) <=13:
                    nodelabels.append(slevel2.title)
                branchingCounter += 1
                if branchingCounter == numberoftopics:
                    break

for topic in query_words:
    wiki_wiki = wikipediaapi.Wikipedia('en')
    links = []
    nodelabels = []
    wikipage = wiki_wiki.page(topic)
    if(not wikipage.exists()):
        print("Page does not exist")
        exit()

    print_second_level_sections(wikipage, 3)
    # write links to file 
    with open(f'{topic}_links.txt', "w") as f:
        for link in links:
            f.write(link + "\n")
    nodelabels = nodelabels[0:12]
    print(nodelabels)

    if len(nodelabels) <12:
        print("Not enough nodes")
        continue
    nodelabels.insert(0,nodelabels[3])
    nodelabels.pop(4)
    nodelabels.insert(1,nodelabels[7])
    nodelabels.pop(8)
    nodelabels.insert(2,nodelabels[11])
    nodelabels.pop(12)
    
    print(len(nodelabels))

    if len(nodelabels) != 12:
        for i in range(12-len(nodelabels)):
            nodelabels.append(" ")
    nodelabels.insert(0,topic)
    print("saving to json file")
    #save nodelabels to json file
    nodejson = {"nodemap":nodelabels}
    with open('nodemap.json', 'w') as outfile:
        json.dump(nodejson, outfile)

    print("running mapmaker.py to create a topic map")
    cmd = "python mapmaker.py"
    returned_value = os.system(cmd)
    time.sleep(5)