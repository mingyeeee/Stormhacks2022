
import glob
 
html = ""

for file in glob.glob("*.png"):
   
	##html += f'<img src ={file}/>'
    html += "<img src=\"" + file + "\"><br>"
 
with open("index.html", "w") as outputfile:
	outputfile.write(html)

