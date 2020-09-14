import sys
import os
from slugify import slugify
from subprocess import *
import requests
appversion = "0.1.0"


try:
    data2 = sys.argv[1]
    print("Obtendo valores do video...")
    print("", end="\r")
    f = requests.get(data2, allow_redirects=True)

    print("Lendo valores do vídeo...")
    print("", end="\r")
    fc = f.content
    print("Verificando (1/3)...")
    videofind = fc.decode("utf-8").find("http://media.bcc.org.br/video/telenovela/mp4/640x480/")
    if videofind != -1:
        print("", end="\r")
        videofinded = fc.decode("utf-8")[videofind:]
    else:
        print ("Verificando (2/3)...")
        print("", end="\r")
        videofind = fc.decode("utf-8").find("http://media.bcc.org.br/video/telejornal/mp4/640x480/")
        if videofind != -1:
            videofinded = fc.decode("utf-8")[videofind:]
        else:
            print("", end="\r")
            print("Verificando (3/3)...")
            videofind = fc.decode("utf-8").find("http://media.bcc.org.br/video/filme/mp4/640x480/")
            if videofind != -1:
                videofinded = fc.decode("utf-8")[videofind:]
            else:
                print("", end="\r")
                print("Erro: o vídeo não parece ser da cinemateca, ou o site mudou. Por favor, atualize o programa.")
                sys.exit(2)

    titlefind = fc.decode("utf-8").find("<h1 class=\"title\">")
    titleendfind = fc.decode("utf-8")[titlefind:].find("</h1>")
    titleenfim = fc.decode("utf-8")[(titlefind+18):(titlefind+titleendfind)]

    titlefind2 = fc.decode("utf-8").find("<strong>Código:</strong>")
    titleendfind2 = fc.decode("utf-8")[titlefind2:].find("</p>")
    titleenfim2 = fc.decode("utf-8")[titlefind2+24:titlefind2+titleendfind2]


    print("Localizando vídeo...")

    videofinded = videofinded[:(videofinded.find("480.mp4")+7)]

    print("Verificando se já existe...")

    if (os.path.exists(sys.argv[2].replace("'", "") +"\\"+ slugify(titleenfim) + " (" + slugify(titleenfim2) + ")" + ".mp4")):
        print("Você já baixou o vídeo. Para baixar de novo, apague-o.")
    else:
        print("Iniciando processo de Download...")
        Popen(["downl.exe",videofinded,sys.argv[2],slugify(titleenfim) + " (" + slugify(titleenfim2) + ")", "S","N"]).wait()
        sys.exit()
except Exception as eee:
    print("erro: " + eee.__str__())
    teste = input("Aperte enter para sair.")
    sys.exit(2)