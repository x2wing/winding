import os
import subprocess
import time



while True:
    try:
        firefox = r'D:\Tor Browser\Browser\firefox.exe'
        cmd = [firefox, "-tray", ]
        subprocess.run(cmd)
        time.sleep(60)

        os.system("taskkill /im firefox.exe")
        # os.system("taskkill /im tor.exe")
        time.sleep(3)
    except Exception as e:
        print(e)
