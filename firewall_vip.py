print('nazev;portforward;extip;mappedip;extport;mappedport')

f = open("c:/data/srani/VIP/a.conf","r")
line = f.readline()

while line:

    if "edit" in line:
            kde = line.find("edit") + 4
            nazev=line[kde:].strip()
    if "portforward" in line:
            kde = line.find("portforward") + 11
            portforward=line[kde:].strip()
    if "extip" in line:
            kde = line.find("extip") + 5
            extip=line[kde:].strip()
    if "mappedip" in line:
            kde = line.find("mappedip") + 8
            mappedip=line[kde:].strip()
    if "extport" in line:
            kde = line.find("extport") + 7
            extport=line[kde:].strip()
    if "mappedport" in line:
            kde = line.find("mappedport") + 10
            mappedport=line[kde:].strip()
    if "next" in line:
            print(nazev + ";" + portforward + ";"  + extip + ";" + mappedip + ";" + extport + ";" + mappedport)
    line = f.readline()
f.close()
