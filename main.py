# coding: utf-8
# NÃO TIRE A LINHA ACIMA!
# Dependencias ja vem com python
from subprocess import *
from tkinter import Tk, filedialog
import tkinter
import os
import time
import requests
import winsound
import sys
# Dependências precisam instalar com pip
import pyperclip
import time





appversion = "0.6.2"
rofidtitle = "RoFiD Downloader Versão " + appversion + " by EternoÍndio"
os.system("title " + "RoFiD " + appversion)
print("RoFiD Versão "+appversion)
if (not any("naoatualizar" in s for s in sys.argv)):
    updatetxt = str(requests.get("https://raw.githubusercontent.com/Inky1003/rofid/master/update.txt").content)
    if (updatetxt != "b'"+appversion+"'"):
        print("Há uma nova atualização para o RoFiD.")
        print("Versão atual: " + appversion)
        print("Versão nova: " + updatetxt)
        input("aperte enter para atualizar agora ou feche para sair. para não detectar atualizações abra o programa usando 'rofid naoatualizar'.")
        try:
            r2 = requests.head("https://api.github.com/repos/Inky1003/rofid/releases/latest")
            total_length = int(r2.headers.get("content-length"))
            r = requests.get(url, stream=True)
            print(f"Tamanho de {nomeSalvar}: {total_length}")
            with open(ondeSalvar.replace("'", "") + "\\" + nomeSalvar + ".mp4", "wb") as fopen:

                if total_length is None:
                    printProgressBar(0, 1000, "Baixando " + nomeSalvar, " 0 bytes, indefinidamente.", 1, 30, "█")
                    fopen.write(r.content)
                    printProgressBar(100, 100, "Baixando " + nomeSalvar, str(os.stat(
                        ondeSalvar.replace("'", "") + "\\" + nomeSalvar + ".mp4").st_size) + " bytes, indefinidamente.",
                                     1, 30, "█")

                else:
                    total_length = int(total_length)
                    printProgressBar(0, total_length, "Baixando " + nomeSalvar,
                                     " completados. " + "0" + "/" + int(total_length / 1024).__str__() + " KB", 1, 30,
                                     "█")
                    for data in r.iter_content(chunk_size=36768):
                        fopen.write(data)
                        printProgressBar((os.stat(ondeSalvar.replace("'", "") + "\\" + nomeSalvar + ".mp4").st_size),
                                         total_length, "Baixando " + nomeSalvar[:17] + "...", " completados. " + str(
                                int(os.stat(ondeSalvar.replace("'",
                                                               "") + "\\" + nomeSalvar + ".mp4").st_size / 1024)) + "/" + int(
                                total_length / 1024).__str__() + " KB", 1, 30, "█")

        sys.exit(2)

try:
    firstargument = sys.argv[1]
    if (firstargument == "salve"):
        if os.path.exists(sys.argv[3]):
            saveas = sys.argv[3]
            Popen(["handler", data2, saveas])
        else:
            tkw = Tk()
            tkw.title("Escolha um lugar para salvar os vídeos")
            saveas = filedialog.askdirectory(title="Escolha um lugar para salvar os downloads", mustexist="true")
            while (saveas == ""):
                saveas = filedialog.askdirectory(title="Escolha um lugar para salvar os downloads", mustexist="true")
            tkw.destroy()
            Popen(["handler", data2, saveas])


    if (firstargument == "lista"):
        if os.path.exists(sys.argv[2]):
            with open(sys.argv[2], "r") as a_file:
                for line in a_file:
                    stripped_line = line.strip()
                    Popen(["handler", stripped_line, sys.argv[2]]).wait()
        else:
            print("Lista inexistente")
            sys.exit()


except:
    print(rofidtitle)
    print("")
    print("O propósito desse downloader é preservar a história da TV Brasileira, seja quem estiver fazendo")
    print("isso. A Cinemateca não tem mais condições de guardar, pois notícias recentes dizem: a infraestrutura")
    print("está dando sinal de vida.")
    print("")
    print("Por isso, faça o favor de baixar e guardar com o maior cuidado. Obrigado.")
    print("")
    print("INSTRUÇÕES:")
    print("")
    print("Para usar esse downloader vá no site do bcc.org e copie o link da página do vídeo.")
    print("Deixa que o RoFiD faz o resto :)")
    print("Ao copiar, volte ao programa e dê o nome do arquivo")
    print("No próximo diálogo selecione o local onde quer guardar os downloads")
    print("")
    time.sleep(2)
    tkw = Tk()
    tkw.title("Escolha um lugar para salvar os vídeos")
    saveas = filedialog.askdirectory(title="Escolha um lugar para salvar os downloads", mustexist="true")
    while (saveas == ""):
        saveas = filedialog.askdirectory(title="Escolha um lugar para salvar os downloads", mustexist="true")
    tkw.destroy()
    print("Os downloads serão salvos em " + saveas)
    print("")
    print("")
    print("Enquanto você estiver baixando alguma coisa, o programa pode continuar baixando outra coisa,")
    print("mas caso você se incomode com bugs visuais")
    print("não baixe, mas eu garanto: ele baixa direitinho.")
    print("")
    print("")
    print("")
    print("Agora pode começar a copiar os links e baixar!")
    print("")
    data1 = pyperclip.paste()

    while ('true'):
        data2 = pyperclip.paste()
        if (data1 != data2):
            data1 = data2
            if (data2.startswith("http://bcc.org.br/filmes/")):
                Popen(["handler",data2,saveas,], creationflags=CREATE_NEW_CONSOLE)


