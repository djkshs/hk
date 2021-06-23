import os
import requests
import urllib 
import json
from Core.Support import Font
from Core.Support import Creds
from Core.Support import Proxies
from datetime import datetime
from time import sleep

class MrHolmes:

    @staticmethod
    def Google_dork(username,report):
        nomefile = "Site_lists/Username/Google_dorks.txt"
        f = open (report ,"a")
        f.write("\nGOOGLE DORKS LINKS:\n")
        f.close()
        print(Font.Color.GREEN + "\n[+]" +Font.Color.WHITE + "GENERATING POSSIBLE GOOGLE DORKS LINK...")
        sleep(3)
        f = open(nomefile,"r")
        for sites in f:
            site = sites.rstrip("\n")
            site = site.replace("{}", username)
            print(Font.Color.GREEN + "[+]" + Font.Color.WHITE + site)
            f = open(report,"a")
            f.write(site + "\n")
            sleep(2)
        f.close()
        f.close()

    @staticmethod
    def search(username):
        f = open("Banners/Banner2.txt","r")
        banner = f.read()
        f.close()
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
        }
        succ = 0
        failed = 0
        nomefile = "Site_lists/Username/lists.txt"
        report = "Reports/Usernames/" + username + ".txt"
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        Date = "Date: " + str(dt_string)
        if os.path.isfile(report):
            os.remove(report)
        f = open(report, "a")
        f.write("SCANNING EXECUTED ON" + Date + "\r\n")
        f.close()
        f = open(nomefile, "r")
        choice = int(input(
            Font.Color.BLUE + "\n[+]" + Font.Color.WHITE + "WOULD YOU LIKE TO USE A PROXY 'IT MAY CAUSE SOME PROBLEMS AND THE PROCESS WILL SLOW DOWN'(1)YES(2)NO\n\n" + Font.Color.GREEN + "[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
        if choice == 1:
            http_proxy = Proxies.proxy.final_proxis
            http_proxy2 = Proxies.proxy.choice3
            source = "http://ip-api.com/json/" + http_proxy2
            access = urllib.request.urlopen(source)
            content = access.read()
            final = json.loads(content)
            identity = "YOUR PROXY IP IS LOCATED IN: " + final ["regionName"]
        else:
            http_proxy = None
            http_proxy2 = str(http_proxy)
            identity="None"
        os.system("clear")
        print(Font.Color.GREEN + banner)
        print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE + "YOUR PROXY IP ADDRES IS: {} ".format(http_proxy2))
        if identity != "None":
            print(Font.Color.GREEN + "[+]" + Font.Color.WHITE + identity)
        else:
            pass
        for sites in f:
            site = sites.rstrip("\n")
            site = site.replace("{}", username)
            print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE + "TRYING ON: {} ".format(site))
            try:
                searcher = requests.get(site, headers=headers, proxies=http_proxy, timeout=None)
                status = str(searcher.status_code)
                f = open(report, "a")
                if searcher.status_code == 200:
                    print(Font.Color.YELLOW + "[+]" + Font.Color.WHITE + "USERNAME FOUND WITH STATUS CODE:" + status)
                    f.write(site + "\r\n")
                    succ = succ + 1
                    succ2 = str(succ)
                else:
                    print(Font.Color.RED + "[!]" + Font.Color.WHITE + "USERNAME NOT FOUND WITH STATUS CODE:" + status)
                    failed = failed + 1
                    failed2 = str(failed)
            except Exception as e:
                print(Font.Color.RED + "\n[!]" + Font.Color.WHITE + "ERROR..TRYNG WITH NO PROXIES")
                searcher = requests.get(site, headers=headers, proxies=None, timeout=None)
                status = str(searcher.status_code)
                f = open(report, "a")
                if searcher.status_code == 200:
                    print(Font.Color.YELLOW + "[+]" + Font.Color.WHITE + "USERNAME FOUND WITH STATUS CODE:" + status)
                    f.write(site + "\r\n")
                    succ = succ + 1
                    succ2 = str(succ)
                else:
                    print(Font.Color.RED + "[!]" + Font.Color.WHITE + "USERNAME NOT FOUND WITH STATUS CODE:" + status)
                    failed = failed + 1
                    failed2 = str(failed)

        f.write("USERNAME FOUND IN: " + succ2 + " SITES" + "\r\n")
        f.write("USERNAME NOT FOUND IN: " + failed2 + " SITES" + "\r\n")
        f.close()
        count = 1
        if count == 1:
            choice = int(input(
            Font.Color.BLUE + "\n[+]" + Font.Color.WHITE + "WOULD YOU LIKE TO PERFORM A GOOGLE DORK ATTACK?(1)YES(2)NO\n\n" + Font.Color.GREEN + "[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
            if choice == 1:
                MrHolmes.Google_dork(username,report)
            os.system("Core/Support/./Notification.sh")
            print(Font.Color.WHITE + "\nREPORT WRITTEN IN: " + os.getcwd() + "/" + report)
            Creds.Sender.mail(report, username)