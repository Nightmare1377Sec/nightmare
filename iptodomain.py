import urllib3, re, time, random, sys, os, socket
color = ["\033[31m", "\033[32m", "\033[33m", "\033[34m","\033[35m", "\033[36m", "\033[37m", "\033[39m"]
try: import requests; s = requests.Session()
except:print("{w}Require {g}requests {w}module\n{y}pip install {g}requests".format(w=color[6], y=color[2], g=color[1])); exit()
try: from multiprocessing.dummy import Pool as tpool
except:print("{w}Require {g}multiprocessing {w}module\n{y}pip install {g}multiprocessing".format(w=color[6], y=color[2], g=color[1])); exit()
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
thread = 100
outputFile = open("_Reversed.txt", "a")
tmpSites = []
ipsList = []
def logo():
    os.system(["clear", "cls"][os.name == 'nt'])
    Logo = '''
        ______  __      ____            ____
       / ___/ |/ /     / __ \___ _   __/  _/___
       \__ \|   /_____/ /_/ / _ \ | / // // __ \\
      ___/ /   /_____/ _, _/  __/ |/ // // /_/ /
     /____/_/|_|    /_/ |_|\___/|___/___/ .___/ 
     {y}nopebee7 {w}[{g}@{w}] {y}skullxploit          /_/ {w}v2.2\n'''.format(g=color[1], w=color[7], m=color[4], y=color[2], r=color[0])
    for Line in Logo.split('\n'):
        print(random.choice(color)+Line)
        time.sleep(0.1)
def opt():
    siteList = []
    fileName = raw_input(
        " {w}[{g}+{w}] {y}the list {w}> ".format(w=color[6], g=color[1], y=color[2]))
    if os.path.exists(fileName):
        siteList = open(fileName, "r+").readlines()
    else:
        print(" {A}[{B}x{A}] {B}The list not found in current dir".format(
            A=color[6], B=color[5]))
        exit()
    theThread = raw_input(
        " {w}[{g}+{w}] {y}thread {w}({y}default{w}:{y}100{w}) {w}> ".format(w=color[6], g=color[1], y=color[2]))
    if theThread == "":
        theThread = 100
    if siteList == []:
        print(" {A}[{B}x{A}] {B}Empty list".format(A=color[6], B=color[5]))
        exit()
    else:
        if len(siteList) < int(theThread):
            theThread = len(siteList)
        return siteList, int(theThread)
def rev(url):
    global tmpSites, outputFile, ipsList
    if url.startswith("http://"):
        url = url.replace("http://", "")
    elif url.startswith("https://"):
        url = url.replace("https://", "")
    url = url.replace("\n", "").replace("\r", "").replace("/", "")
    if url == "": return


    try:
        ip = socket.gethostbyname(url)
        if ip in ipsList:
            print(" \033[41;1m -- SAME IP -- \033[0m "+url)
            return
        ipsList.append(ip)
    except:
        print(" \033[41;1m -- ERROR -- \033[0m "+url)
        return
    # Variable
    res = []
    api = "https://securitytrails.com/app/api/v1/list_new/ip/"
    jalan = True
    first = 0
    page = 0
    ##################
    while jalan:
        try:
            if first == 0:
                req = requests.get((api+ip)).json()
            else:
                req = requests.get((api+ip+"?page="+str(page))).json()
        except: continue
        try:
            for arr in req['records']:
                site = arr['hostname']
                site = site.replace("www.", "").replace('cpanel.', '').replace('webmail.', '').replace('webdisk.', '').replace('ftp.', '').replace(
                'cpcalendars.', '').replace('cpcontacts.', '').replace('mail.', '').replace('ns1.', '').replace('ns2.', '').replace('autodiscover.', '')
                if site != "" and site not in tmpSites:
                    res.append(site)
                    outputFile.write(site+"\n")
                    tmpSites.append(site)
        except: pass
        if first == 1:
            if page >= req['meta']['max_page']:
                jalan = False
            page += 1
        first = 1
    if len(res) == 0:
        print(" \033[41;1m -- NULL -- \033[0m "+url)
    else:
        print(" \033[42;1m -- "+str(len(res))+" SITES -- \033[0m "+url)
if __name__ == "__main__":
    try:
        logo()
        sx = opt()
        print("\n")
        pool = tpool(sx[1])
        pool.map(rev, sx[0])
        pool.close()
        pool.join()
        print("\n {A}[{B}+{A}] {Y}Done {A}: {Y}{S} sites".format(Y=color[2],A=color[6], B=color[5], S=(str(len(tmpSites)))))
    except KeyboardInterrupt:
        print("\n {w}[{r}-{w}] {b}Goodbye >//< ".format(w=color[6], r=color[0], b=color[3]))