import urllib.request
from time import sleep

n=0
while True:
    try:
        n+=1
        response = urllib.request.urlopen('http://csdb.ufanet.ru/component/option,com_wrapper/Itemid,235/')
        print(n)
    except Exception as err:
        print(err)
    sleep(5)