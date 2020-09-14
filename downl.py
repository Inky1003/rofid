# coding: utf-8
# NÃO TIRE A LINHA ACIMA!
appversion = "0.3.0"

import winsound
import requests
import sys



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
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)


def download(url, ondeSalvar, nomeSalvar, notificarerro = "s", notificarsucesso = "n"):
    try:
        r2 = requests.head(url)
        total_length = int(r2.headers.get("content-length"))
        r = requests.get(url, stream=True)
        print(f"Tamanho de {nomeSalvar}: {total_length}")
        with open(ondeSalvar.replace("'", "") +"\\"+ nomeSalvar + ".mp4", "wb") as fopen:

            if total_length is None:
                printProgressBar(0, 1000, "Baixando " + nomeSalvar, " 0 bytes, indefinidamente.", 1, 30, "█")
                fopen.write(r.content)
                printProgressBar(100, 100, "Baixando " + nomeSalvar, str(os.stat(ondeSalvar.replace("'", "") +"\\"+ nomeSalvar + ".mp4").st_size) + " bytes, indefinidamente.", 1, 30, "█")

            else:
                total_length = int(total_length)
                printProgressBar(0, total_length, "Baixando " + nomeSalvar," completados. " + "0" + "/" + int(total_length / 1024).__str__() + " KB", 1, 30, "█")
                for data in r.iter_content(chunk_size=36768):
                    fopen.write(data)
                    printProgressBar((os.stat(ondeSalvar.replace("'", "") +"\\"+ nomeSalvar + ".mp4").st_size), total_length, "Baixando " + nomeSalvar[:17]+"...", " completados. " + str(int(os.stat(ondeSalvar.replace("'", "") +"\\"+ nomeSalvar + ".mp4").st_size/1024)) + "/" + int(total_length / 1024).__str__() + " KB", 1, 30,"█")
    except Exception as e:
        if (notificarerro == "s" or notificarerro == "S"):
            winsound.MessageBeep(winsound.MB_ICONHAND)
        return e.__str__()
    else:
        if (notificarsucesso == "s" or notificarsucesso == "S"):
            winsound.MessageBeep(winsound.MB_ICONASTERISK)
        return "ok"
print("Downl versão " + appversion)
print("")
scodo = download(sys.argv[1],sys.argv[2],sys.argv[3], sys.argv[4], sys.argv[5])
if (scodo != "ok"):
    print("?")
    print("")
    print("Erro ao baixar o vídeo!")
    print(scodo)
else:
    print("Rotina de download finalizada com sucesso!")