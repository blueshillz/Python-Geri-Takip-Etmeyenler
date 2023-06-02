from instagrapi import Client
from getpass import getpass
from instagrapi.exceptions import BadPassword, ClientError, PrivateError
import sys
import time
import threading
import os

class GeriTakipEtmeyenler:
    def __init__(self):
        self.cl = Client()
        if os.name == 'nt':
            self.clearcmd = 'cls'
        else:
            self.clearcmd = 'clear'
        os.system(self.clearcmd)
    def login(self):
        global username
        global password
        print('Dikkat!\nGiriş yapabilmek için 2 faktörlü doğrulamanın kapatılmış olması gerekmektedir!')
        username = input('Kullanıcı adı:\n')
        password = getpass(prompt='Şifre:\n')
        try:
            self.cl.login(username,password)
        except BadPassword:
            print('Hatalı şifre!')
            sys.exit(1)
            
    def loading(self):
        animation = "|/-\\"
        idx = 0
        while not tamamlandi:
            print('Takipçi ve takip bilgisi çekiliyor lütfen bekleyiniz '+animation[idx % len(animation)], end="\r")
            idx += 1
            time.sleep(0.1)
            os.system(self.clearcmd)
        print('Takipçi ve takip bilgisi çekildi!')

    def getGeriTakipEtmeyenler(self):
        global tamamlandi
        tamamlandi = False
        loadTh = threading.Thread(target=self.loading)
        loadTh.start()
        followers = self.cl.user_followers(self.cl.user_id,amount=0)
        following = self.cl.user_following(self.cl.user_id,amount=0)
        followerList = []
        followingList = []
        for follow in following:
            followingList.append(following[follow].username)
        for follower in followers:
            followerList.append(followers[follower].username)

        gtEtmeyenler = set(followingList)-set(followerList)
        tamamlandi = True
        loadTh.join()
        return gtEtmeyenler
        
    def main(self):
        gtEtmeyenler = self.getGeriTakipEtmeyenler()
        print('*-'*50+'\nGeri takip etmeyen kullanıcılar:\n')
        for i in gtEtmeyenler:
            print(i)

if __name__=='__main__':
    gt = GeriTakipEtmeyenler()
    gt.login()
    gt.main()
