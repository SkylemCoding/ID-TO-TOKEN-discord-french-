import os
import base64
try:
    from colorama import Fore, init
except:
    os.system("py -m pip install colorama")
    from colorama import Fore, init
init()

banner = (Fore.MAGENTA + """
ID A TOKEN TOOL DISCORD/Développer par : xeno9365
""" + Fore.LIGHTCYAN_EX)
print(banner)
userid = input(" [INPUT] ID DE L'UTILISATEUR : ")
encodedBytes = base64.b64encode(userid.encode("utf-8"))
encodedStr = str(encodedBytes, "utf-8")
print(f'\n [LOGS] PREMIERE PARTIE DU TOKEN DE LA CIBLE : {encodedStr}')
os.system('pause >nul')  