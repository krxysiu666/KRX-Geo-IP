import os
import requests
import smtplib
from colorama import Fore
import webbrowser
from pypresence import Presence
import time
import json

rpc = Presence("881225694166806559")
rpc.connect()
rpc.update(state="Connected",large_image="nookk",start=time.time())

def ResetTool():
    while 1:
        Design()
        os.system("pause")



def Design():
    os.system("cls && title KRX GeoIP")
    print(f'''
{Fore.GREEN}                            _  _______  __   __    _____ ___{Fore.MAGENTA}___ ____     _____ _____  
{Fore.GREEN}                           | |/ /  __ \ \ \ / /   / ____|  _{Fore.MAGENTA}___/ __ \   |_   _|  __ \ 
{Fore.GREEN}                           | ' /| |__) | \ V /   | |  __| |_{Fore.MAGENTA}_ | |  | |    | | | |__) |
{Fore.GREEN}                           |  < |  _  /   > <    | | |_ |  _{Fore.MAGENTA}_|| |  | |    | | |  ___/ 
{Fore.GREEN}                           | . \| | \ \  / . \   | |__| | |_{Fore.MAGENTA}__| |__| |   _| |_| |     
{Fore.GREEN}                           |_|\_\_|  \_\/_/ \_\   \_____|___{Fore.MAGENTA}___\____/   |_____|_|  
                                        
                                              {Fore.GREEN}By Krzysiu &{Fore.MAGENTA} Kedix  


    ''')
    print(f'{Fore.LIGHTWHITE_EX}    [1] -{Fore.MAGENTA} Cred{Fore.GREEN}its')
    print(f'{Fore.LIGHTWHITE_EX}    [2] -{Fore.MAGENTA} Geo{Fore.GREEN} IP')

    answer = input("> ")


    if answer == "1":
        webbrowser.open_new_tab("https://github.com/ZoltyPies")
        webbrowser.open_new_tab("https://github.com/krxysiu666")

    if answer == "2":
        os.system("cls && title KRX GEO IP")
        print(f'''
{Fore.GREEN}                            _  _______  __   __    _____ ___{Fore.MAGENTA}___ ____     _____ _____  
{Fore.GREEN}                           | |/ /  __ \ \ \ / /   / ____|  _{Fore.MAGENTA}___/ __ \   |_   _|  __ \ 
{Fore.GREEN}                           | ' /| |__) | \ V /   | |  __| |_{Fore.MAGENTA}_ | |  | |    | | | |__) |
{Fore.GREEN}                           |  < |  _  /   > <    | | |_ |  _{Fore.MAGENTA}_|| |  | |    | | |  ___/ 
{Fore.GREEN}                           | . \| | \ \  / . \   | |__| | |_{Fore.MAGENTA}__| |__| |   _| |_| |     
{Fore.GREEN}                           |_|\_\_|  \_\/_/ \_\   \_____|___{Fore.MAGENTA}___\____/   |_____|_|                                                                                                    
        ''')

        target = input(  "\u001b[38;5;46m╚\u001b[38;5;47m══\u001b[38;5;48m[Tar\u001b[38;5;49mget\u001b[38;5;50m\u001b[38;5;51m]═>\u001b[38;5;7m")
        api = "http://ip-api.com/json/"

        response = urlopen(api + target)

        data = response.read()
        f = json.loads(data)

        print(f"{Fore.GREEN} - IP Address : " + f['query'])
        print(f"{Fore.MAGENTA} - Status: " + f['status'])
        print(f"{Fore.GREEN} - Country: " + f['country'])
        print(f"{Fore.MAGENTA} - City: " + f['city'])


    else:
        print("")
        Design()    

ResetTool()

os.system("pause")