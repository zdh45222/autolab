#Fernando Ramon da Cruz
#Version: 0.1
#Script Born in 21/07/2018
import getpass
import telnetlib
import time

routerid=1
routercount=0
addrouter=True
HOST = "127.0.0.1"
PORT = 5000
routerlist = [0,1,2,3,4,5,6,7,8,9]

class Router:
    name = ""
    neighborcount = 0
    neighbor1 = ""
    intneighbor1 = ""

    def __init__(self,name):
        self.name = name

    def showName(self):
        print("Router: "+self.name)

    def addNeighbor(self,neigh,interface):
        if neigh == "R1":
            self.neighbor1
############################################################################################################
#MAIN
############################################################################################################
while addrouter:

    connect=True
    op = input("O Router R"+str(routerid)+" esta nessa topologia? (y/n)")
    if op == 'y':
        router = Router("R"+str(routerid))
        router.showName()
        time.sleep(5)
        routerlist[routercount] = router
        tn = telnetlib.Telnet(HOST, PORT)
        tn.write(b"conf t \r")
        tn.write(b"int l0 \r")
        loop0 = ("ip add "+str(routerid)+"."+str(routerid)+"."+str(routerid)+"."+str(routerid)+" 255.255.255.0\r").encode()
        tn.write(loop0)
        while connect:
            neighbor = input("Conectado a qual router? (1,2,3?)")
            intf = input("Atraves de qual interface? (ex. g1/0)")
            intf = ("int "+intf+" \r").encode()
            tn.write(intf)
            if int(neighbor) < routerid:
                ip = ("ip add 192.168."+neighbor+""+str(routerid)+"."+str(routerid)+" 255.255.255.0\r").encode()
            else:
                ip = ("ip add 192.168." + str(routerid) + "" + neighbor + "." + str(routerid) + " 255.255.255.0\r").encode()
            tn.write(ip)
            tn.write(b"no shut \r")
            tn.write(b"exit \r")
            anyrouter = input("Esta conectado a mais algum? (y/n)")
            if anyrouter == 'n':
                routerid += 1
                PORT += 1
                connect=False
                tn.close()
    else:
        addrouter=False

print("Bom LAB Guerreiro!! CCNP ROUTE PASS!! ")

print(tn.read_all().decode('ascii'))