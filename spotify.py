import random
import time
from colorama.ansi import Fore
import httpx
from colorama import Fore
import os
import sys
import time
import string


url = "https://spclient.wg.spotify.com/signup/public/v1/account"


headers = {
  'authority': 'spclient.wg.spotify.com',
  'sec-ch-ua': '"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"',
  'sec-ch-ua-mobile': '?0',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
  'sec-ch-ua-platform': '"Windows"',
  'content-type': 'application/x-www-form-urlencoded',
  'accept': '*/*',
  'origin': 'https://www.spotify.com',
  'sec-fetch-site': 'same-site',
  'sec-fetch-mode': 'cors',
  'sec-fetch-dest': 'empty',
  'referer': 'https://www.spotify.com/',
  'accept-language': 'en-US,en;q=0.9'
}

g = Fore.GREEN
r = Fore.RED
b = Fore.BLUE
y = Fore.YELLOW
re = Fore.RESET
l = Fore.LIGHTBLACK_EX
blue = Fore.BLUE
letters = ["a", "b","c", "d","e", "f","g", "h","i", "j","k", "l","m", "n",
           "o", "p","q", "r","s", "t","u", "v","w", "x","y", "z",]

def random_char(char_num):
       return ''.join(random.choice(string.ascii_letters) for _ in range(char_num))



def drawsign():
    print(f'''
    
    {blue}

╔═╗┌─┐┌─┐┌┬┐┬┌─┐┬ ┬
╚═╗├─┘│ │ │ │├┤ └┬┘
╚═╝┴  └─┘ ┴ ┴└   ┴ 

    {re}
    
    
    ''')




def mainfunctional():
    os.system("cls")
    drawsign()
    dhook = input(f'[{blue}DISCORD{re}] Webhook > ')
    recdata = {'content':'**Spotify Generator 2.0** Succesfully Attached @everyone'}
    receiveme = httpx.post(dhook,json=recdata)
    os.system("cls")
    print(f"[{y}INITIALIZING{re}] Loading...")
    time.sleep(3)
    print(f'[{g}Spotify{re}] Starting Now')
    while True:
                   Email = random_char(17)+"@protonmail.com"
                   password = random_char(5)+"revenge-1337"
                   payload=f'birth_day=2&birth_month=02&birth_year=1989&collect_personal_info=undefined&creation_flow=&creation_point=https%3A%2F%2Fwww.spotify.com%2Fus%2F&displayname=Revengeis1337&gender=male&iagree=1&key=a1e486e2729f46d6bb368d6b2bcda326&platform=www&referrer=&send-email=0&thirdpartyemail=1&email={Email}&password={password}&password_repeat={password}'
                   createacc = httpx.post(url,headers=headers,data=payload)
                   accdata = {
                       'content':f'```css\n{Email}:{password}``` '
                   }
                   sendacc = httpx.post(dhook,json=accdata)



    



if __name__ == '__main__':
    mainfunctional()
