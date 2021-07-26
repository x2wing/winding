import os
import subprocess
import time
from random import randint, choice

sizes = (600, 800, 1024, 1280, 1440, 1080)

while True:
    try:
        windows_size= f'{choice(sizes)},{choice(sizes)}' #'800,600'
        timeout = randint(20, 35)
        firefox = r'C:\Program Files (x86)\Google\Chrome Beta\Application\chrome.exe'
        cmd = [firefox, 'csdb.ufanet.ru/content/view/1148/281/', '--incognito', f'--window-size={windows_size}', ]
        subprocess.run(cmd, timeout=timeout, )
        # time.sleep(20)

        # os.system("taskkill /im chrome.exe")
        # os.system("taskkill /im tor.exe")
        # time.sleep(5)
    except Exception as e:
        print(e)
