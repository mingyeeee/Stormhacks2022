import wikipediaapi

def print_first_level_sections(sections, numberofsections):
    counter = 0
    for s in sections:
        print("\t" + s.title)
        page = wiki_wiki.page(s.title)
        if(page.exists()):
            print("\t" + page.fullurl)
        else:
            print("\tPage does not exist")
        counter += 1
        if counter == numberofsections:
            break

wiki_wiki = wikipediaapi.Wikipedia('en')

#topic = 'projectile_motion'
topic = "gravity"

wikipage = wiki_wiki.page(topic)
if(not wikipage.exists()):
    print("Page does not exist")
    exit()

# title
print(wikipage.title)

# summary
#print("Page - Summary: %s" % wikipage.summary)

# url
print(wikipage.fullurl)

# sections
#print_sections(wikipage.sections)
def print_second_level_sections(page, numberoftopics):
    # navigate to 2nd level of sections
    branchingCounter = 0
    deadendCounter = 0
    for slevel1 in page.sections:
        for slevel2 in slevel1.sections:
            # check if there exist an article for the 2nd level section
            wikisectionpage = wiki_wiki.page(slevel2.title)
            if(not wikisectionpage.exists()):
                if deadendCounter == 3:
                    continue
                # check if page does not exist or the title is not correct
                try:
                    print(slevel2.title.encode('utf-8'))
                    print(page.fullurl+"#"+slevel2.title.replace(" ", "_"))
                except:
                    print("Page does not exist")
                
                print("Futher pages do not exist")

                print(deadendCounter)
                deadendCounter += 1
                
            elif(wikisectionpage.exists()):
                print(slevel2.title.encode('utf-8'))
                print(page.fullurl+"#"+slevel2.title.replace(" ", "_"))
                print_first_level_sections(wikisectionpage.sections, 3)

                branchingCounter += 1
                if branchingCounter == numberoftopics:
                    break


print_second_level_sections(wikipage, 3)

