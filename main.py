import time
from colorama import Fore, Style

from excel_to_word import main


while True:
    try:
        main()
        print(Fore.LIGHTGREEN_EX + "\nLes fichiers ont été modifiés." + Style.RESET_ALL)
        time.sleep(1.5)
        break
    except PermissionError:
        print(Fore.LIGHTRED_EX + "\nVous devez fermer les fichiers words avant de relancer le scripts\n")

