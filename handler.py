import sys
import os
from slugify import slugify
from subprocess import *
import requests

appversion = "0.2.2"
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    whatoprint = f'\r{prefix} |{bar}| {percent}% {suffix}'
    lenofwhatoprint = len(whatoprint)
    print(whatoprint, end=endline)
    return lenofwhatoprint




maxprogressbar = 9
try:
    data2 = sys.argv[1]
    print(" " * toftp, end="\r")
    toftp = printProgressBar(0, maxprogressbar, 'Iniciando análise ('+data2+')...', decimals=0, length=30, fill='█', printEnd="\r")
    f = requests.get(data2, allow_redirects=True)

    print(" " * toftp, end="\r")
    toftp = printProgressBar(1, maxprogressbar, 'Extraindo conteúdo (' + data2 + ')...', decimals=0, length=30, fill='█',printEnd="\r")
    fc = f.content

    print(" " * toftp, end="\r")
    toftp = printProgressBar(2, maxprogressbar, 'Extraindo conteúdo (' + data2 + ')...', decimals=0, length=30, fill='█',printEnd="\r")
    videofind = fc.decode("utf-8").find("http://media.bcc.org.br/video/telenovela/mp4/640x480/")

    if videofind != -1:
        print(" " * toftp, end="\r")
        toftp = printProgressBar(3, maxprogressbar, 'Decodificando (' + data2 + ')...', decimals=0, length=30, fill='█', printEnd="\r")
        videofinded = fc.decode("utf-8")[videofind:]

    else:
        print(" " * toftp, end="\r")
        toftp = printProgressBar(4, maxprogressbar, 'Verificando (' + data2 + ')...', decimals=0, length=30, fill='█', printEnd="\r")
        videofind = fc.decode("utf-8").find("http://media.bcc.org.br/video/telejornal/mp4/640x480/")
        if videofind != -1:
            videofinded = fc.decode("utf-8")[videofind:]
        else:
            print(" " * toftp, end="\r")
            toftp = printProgressBar(5, maxprogressbar, 'Verificando (' + data2 + ')...', decimals=0, length=30, fill='█', printEnd="\r")
            videofind = fc.decode("utf-8").find("http://media.bcc.org.br/video/filme/mp4/640x480/")
            if videofind != -1:
                videofinded = fc.decode("utf-8")[videofind:]
            else:
                print("")
                print("Erro: o vídeo não parece ser da cinemateca, ou o site mudou. Por favor, atualize o programa.")
                sys.exit(2)

    print(" " * toftp, end="\r")
    toftp = printProgressBar(6, maxprogressbar, 'Gerando Título 1/2 (' + data2 + ')...', decimals=0, length=30, fill='█', printEnd="\r")
    titlefind = fc.decode("utf-8").find("<h1 class=\"title\">")
    titleendfind = fc.decode("utf-8")[titlefind:].find("</h1>")
    titleenfim = fc.decode("utf-8")[(titlefind+18):(titlefind+titleendfind)]

    print(" " * toftp, end="\r")
    toftp = printProgressBar(7, maxprogressbar, 'Gerando Título 2/2 (' + data2 + ')...', decimals=0, length=30, fill='█', printEnd="\r")
    titlefind2 = fc.decode("utf-8").find("<strong>Código:</strong>")
    titleendfind2 = fc.decode("utf-8")[titlefind2:].find("</p>")
    titleenfim2 = fc.decode("utf-8")[titlefind2+24:titlefind2+titleendfind2]

    print(" " * toftp, end="\r")
    toftp = printProgressBar(8, maxprogressbar, 'Localizando vídeo (' + data2 + ')...', decimals=0, length=30, fill='█', printEnd="\r")

    videofinded = videofinded[:(videofinded.find("480.mp4")+7)]

    print(" " * toftp, end="\r")
    toftp = printProgressBar(9, maxprogressbar, 'Procurando se já foi baixado... (' + data2 + ')...', decimals=0, length=30, fill='█', printEnd="\r")

    if (os.path.exists(sys.argv[2].replace("'", "") +"\\"+ slugify(titleenfim) + " (" + slugify(titleenfim2) + ")" + ".mp4")):
        print("")
        print("Você já baixou o vídeo. Para baixar de novo, apague-o.")
    else:
        print("")
        print("Iniciando processo de Download...")
        Popen(["downl.exe",videofinded,sys.argv[2],slugify(titleenfim) + " (" + slugify(titleenfim2) + ")", "S","N"]).wait()
        sys.exit()
except Exception as eee:
    print("erro: " + eee.__str__())
    teste = input("Aperte enter para sair.")
    sys.exit()