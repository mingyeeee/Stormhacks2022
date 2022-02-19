import wikipediaapi

def print_sections(sections, level=0):
    for s in sections:
        print("%s: %s - %s" % ("*" * (level + 1), s.title, s.text[0:40]))
        print_sections(s.sections, level + 1)


wiki_wiki = wikipediaapi.Wikipedia('en')

topic = 'Kinematics'

wikipage = wiki_wiki.page(topic)
if(not wikipage.exists()):
    print("Page does not exist")
    exit()

# title
print(wikipage.title)

# summary
print("Page - Summary: %s" % wikipage.summary)

# url
print(wikipage.fullurl)

# sections
print_sections(wikipage.sections)
