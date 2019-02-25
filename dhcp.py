print('MAC;IP;popis')

f = open("c:/data/srani/VIP/dhcp.conf","r")
line = f.readline()
p1 = "set ip"
p2 = "set mac"
p3 = "set action"
p4 = "set description"



while line:
    if p1 in line:
            kde = line.find(p1) + len(p1)
            ip =line[kde:].strip()
    if p2 in line:
            kde = line.find(p2) + len(p2)
            mac =line[kde:].strip()
    if p3 in line:
            kde = line.find(p3) + len(p3)
            ip =line[kde:].strip()
    if p4 in line:
            kde = line.find(p4) + len(p4)
            popis =line[kde:].strip()
    if "next" in line:
            print(mac + ";" + ip + ";"  + popis)
    line = f.readline()
f.close()
