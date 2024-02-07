
from organization import Organization
from fichier import Fichier
db1=Organization()
paspremier=False
x=Fichier("./welcome","index.html").lire()
options=x.split("name=\"organization")[1].split("</select>")[0].split("</option>")
for y in options:
    if paspremier:
        value1=y.split("value=\"")[1].split("\">")
        db1.create({"name":value1[1],"value":value1[0]})
    paspremier=True
