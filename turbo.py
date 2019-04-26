import requests
import json
import threading
import time
import sys
import random
from urllib3 import ProxyManager, make_headers



c = 0

with open("config.json") as file:
    config = json.load(file)

username = config['username']
password = config['password']

targets = config['targetUsernames']

endpoint = "https://instagram.com/<username>"


proxies = {
  'https': 'http://104.131.116.184:3128',
}

def turbo(nam):

    s = requests.session()

    print(f"[{nam}] Logging Into {username}...")
    url1 = "https://www.instagram.com/accounts/login/"

    r1 = s.get(url1)

    csrf1 = r1.cookies.get_dict()['csrftoken']

    url2 = 'https://www.instagram.com/accounts/login/ajax/'

    h2 = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://www.instagram.com',
        'referer': 'https://www.instagram.com/accounts/login/',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
        'x-csrftoken': csrf1,
        'x-instagram-ajax': '1',
        'x-requested-with': 'XMLHttpRequest'
    }

    data2 = {
        'username': username,
        'password': password,
        'queryParams': '{}'
    }

    r2 = s.post(url2, headers=h2, data=data2)

    if r2.json()['authenticated'] == False:
        print(f'[{nam}] ERROR LOGGING IN...')
        exit()
    else:
        csrf = r2.cookies.get_dict()['csrftoken']
        print(f'[{nam}] Logged In Initiating Turbo...')
        print("")
    turboin = True
    #start monitoring the username
    while turboin == True:
        res = requests.get(endpoint.replace("<username>", nam))
        if res.status_code == 404:
            print(f'[{nam}] NAME AVAILABLE TAKING IT')
            urlf = "https://www.instagram.com/accounts/edit/"

            hf = {
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-US,en;q=0.9',
                'content-type': 'application/x-www-form-urlencoded',
                'origin': 'https://www.instagram.com',
                'referer': 'https://www.instagram.com/accounts/edit/',
                'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
                'x-csrftoken': csrf,
                'x-instagram-ajax': '1',
                'x-requested-with': 'XMLHttpRequest'
            }

            df = {
                'first_name': 'sdouhfwufv sdvcwc',
                'email': "xanax.{}@goat.si".format(str(random.randint(11111111, 99999999))),
                'username': nam,
                'phone_number':'',
                'gender': '3',
                'biography':'turbo by humanlike',
                'external_url':'https://www.humanlike.com',
                'chaining_enabled': 'on'
            }
            #change the acc to the turbo name
            rf = s.post(urlf, headers=hf, data=df)
            print(f'[{nam}] Completed Turbo Killing Thread')
            turboin = False
        else:
            global c
            c = c+1
            print("({}) [{}] Name Unavailable <{}>".format(str(c), nam, res.status_code))
            print("")
            if res.status_code == 429:
                print("You've been spam blocked!")
                res = requests.get(endpoint.replace("<username>", nam),proxies=proxies)
if __name__ == '__main__':
    print("turbo is ready")
    tin = input("Would you like to start (y/n)?: ")
    if tin.lower() == "y":
        for x in targets:
            #print(x)
            t = threading.Thread(target=turbo, args=(x, ))
            t1 = threading.Thread(target=turbo, args=(x, ))
            t2 = threading.Thread(target=turbo, args=(x, ))
            t3 = threading.Thread(target=turbo, args=(x, ))
            t.start()
            time.sleep(0.8)
            t1.start()
            time.sleep(0.8)
            t2.start()
            time.sleep(0.8)
            t3.start()
            print("\n\n\n\nALL THREADS STARTED\n\n\n\n")
    else:
        exit()
