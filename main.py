# coding: utf-8
# NÃO TIRE A LINHA ACIMA!
# Dependencias ja vem com python
from subprocess import *
from tkinter import Tk, filedialog
import os
import time
import requests
import sys
import webbrowser
# Dependências precisam instalar com pip
import pyperclip


appversion = "0.6.3"
rofidtitle = "RoFiD Downloader Versão " + appversion + " by EternoÍndio"
os.system("title " + "RoFiD " + appversion)
print("RoFiD Versão " + appversion)

try:
    firstargument = sys.argv[1]
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
    while saveas == "":
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

    while 'true':
        data2 = pyperclip.paste()
        if data1 != data2:
            data1 = data2
            if data2.startswith("http://bcc.org.br/filmes/"):
                Popen(["handler", data2, saveas], creationflags=CREATE_NEW_CONSOLE)
try:
    if (not any("naoatualizar" in s for s in sys.argv)):
        updatetxt = str(requests.get("https://raw.githubusercontent.com/Inky1003/rofid/master/update.txt").content)
        if (updatetxt[2:7] != appversion):
            print("Há uma nova atualização para o RoFiD.")
            print("Versão atual: " + appversion)
            print("Versão nova: " + updatetxt[2:7])
            input(
                "aperte enter para abrir o navegador e baixar a atualização agora ou feche para sair. Para não detectar atualizações abra o programa usando 'rofid naoatualizar'.")
            webbrowser.open(updatetxt[7:][:-3])
            sys.exit()

    if sys.argv[1] == "salvar":
        print(rofidtitle)
        onde = sys.argv[3]
        url = sys.argv[2]
        if os.path.isdir(onde):
            print("Iniciando análise...")
            Popen(["handler", url, onde])
        else:
            tkw = Tk()
            tkw.title("Escolha um lugar para salvar os vídeos")
            saveas = filedialog.askdirectory(title="Escolha um lugar para salvar os downloads", mustexist="true")
            while (saveas == ""):
                saveas = filedialog.askdirectory(title="Escolha um lugar para salvar os downloads", mustexist="true")
            tkw.destroy()
            print("Iniciando análise...")
            Popen(["handler", url, saveas])

    if sys.argv[1] == "lista":
        print(rofidtitle)
        try:
            if sys.argv[3] in globals():
                if os.path.isdir(sys.argv[3]):
                    saveas = sys.argv[3]
        except:
            tkw = Tk()
            tkw.title("Escolha um lugar para salvar os vídeos")
            saveas = filedialog.askdirectory(title="Escolha um lugar para salvar os downloads", mustexist="true")
            while (saveas == ""):
                saveas = filedialog.askdirectory(title="Escolha um lugar para salvar os downloads", mustexist="true")
            tkw.destroy()
            if os.path.exists(sys.argv[2]):
                with open(sys.argv[2], "r") as a_file:
                    for line in a_file:
                        stripped_line = line.strip()
                        Popen(["handler", stripped_line, saveas]).wait()
        else:
            print("Lista inexistente.")
            sys.exit()
finally:
    print("Programa encerrado.")