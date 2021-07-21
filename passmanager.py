import random
import sqlite3
import time




'''
Hamza Elansari HK-GANG
'''
head = '''
                                      by Hamza07-w
                        .:'         Tool :passwords manager     `:.
                        ::'Contact Me hamzaelansari453@gmail.com `::
                        :: :.                                  .: ::
                         `:. `:.             .             .:'  .:'
                          `::. `::           !           ::' .::'
                              `::.`::.    .' ! `.    .::'.::'
                                `:.  `::::'':!:``::::'   ::'
                                :'*:::.  .:' ! `:.  .:::*`:
                               :: HAM::.   ` ! '   .::ZA  ::
                              ::: `ANSA::.  `!'  .::RI M' :::
                              ::..  `HKG :`:   :':HHHA'  ..::
                              `::      `T: `. .' :T'      ::'
                                `:. .   :         :   . .:'
                                  `::'               `::'
                                    :'  .`.  .  .'.  `:
                                    :' ::.       .:: `:
                                    :' `:::     :::' `:
                                     `.  ``     ''  .'
                                      :`...........':
                                      ` :`.     .': '
                                       `:  `"""'  :'
'''
print(head)



passdb = sqlite3.connect("passwoedDatabase.db")

cr = passdb.cursor()

cr.execute("CREATE TABLE if not exists  passmanager(website text, passwd text)")


#user options
msg_to_usr = """
Genarat New password = [1]
Add Password         = [2]
Update Password      = [3]
Delete Password      = [4]
Show Password        = [5]
save all passwords   = [6]
Exit                 = [0]
"""

def input_usr():
	optins = [ 1 , 2 , 3 , 4 , 5 , 6 , 0 ]
	usr_input = int(input(msg_to_usr))
	if usr_input in optins:
		return usr_input
	else:
		pass

def saveChanges():
	passdb.commit()
	passdb.close()

def genpass():
	#genarate password
	lower = "abcefghijklmnopqrstuvwxyz"
	nembers = "0123456789"
	symbols = "[]{/}()*;%&^-"
	alle = lower + lower.upper() + nembers + symbols
	length = random.randint(8, 20)
	password = "".join(random.sample(alle, length))
	return password


def addpass():
	#add password
	site = input("[+] Enter website  >> ")
	pswd = input("[+] Enter password >> ")
	cr.execute(f"INSERT INTO passmanager(website, passwd) values('{site}','{pswd}')")
	table = f"""
	------------------------------
	|   website    |   password  |
	------------------------------
	|{site}        | {pswd}      |
	------------------------------
	"""
	print(table)
	print("password added seccesfuly!")
	saveChanges()


def updatepass():
	#update password
	site = input("[+] Enter website      >> ")
	pswd = input("[+] Enter New password >> ")
	cr.execute(f"update passmanager set passwd = '{pswd}' where website = '{site}'")
	table = f"""
	------------------------------
	|   website    |   password  |
	------------------------------
	|{site}        | {pswd}      |
	------------------------------
	"""
	print("password updated seccesfuly!")
	saveChanges()

def deletepass():
	#delete password
	cr.execute("select website, passwd from passmanager")
	data = cr.fetchall()
	site = input("[+] Enter website  >> ")
	cr.execute("select * from passmanager")
	exists = False
	for el in data:
		if site == el[0]:
			cr.execute(f"delete from passmanager where website = '{site}'")
			exists = True
			saveChanges()
			break
		else:
			exists = False

	if exists:
		print("password deleted seccesfuly!")
	else:
		print("website not exists!")
	

def showpass():
	#show password
	cr.execute("select website, passwd from passmanager")
	data = cr.fetchall()
	msg = """
	show selected wbsite password = [1]
	show all websites passwords    = [2]
	"""
	select = input(msg)
	if select == "1":
		site_name = input("website >> ")
		for el in data:
			try:
				er_msg = ""
				if el[0] == site_name:
					table = f"""
					------------------------------
					|   website    |   password  |
					------------------------------
						{site_name}  ==>  {el[1]}     
					------------------------------
					"""
					print(table)
				else:
					time.sleep(1)
					print("checking database\n")
					time.sleep(1)
					print("website not found!")

			except:
				pass

	elif select == "2":
		for el in data:
			print(el[0] + "	  ==>  " + el[1])

def savefill():
	res = """ """
	cr.execute("select website, passwd from passmanager")
	data = cr.fetchall()
	for el in data:
		res += el[0] + " : " + el[1]

	with open("passwords.txt", 'w') as file:
		file.write(res)


def Exit():
	#exit programm
	exit()


#print(genpass())
#addpass()
#updatepass()
#deletepass()
#showpassword()
#savefill()

if __name__ == '__main__':

	userselect = input_usr()

	if userselect == 1:
		print(f"password genarated seccesfuly! ==> {genpass()}")

	elif userselect == 2:
		addpass()


	elif userselect == 3:
		updatepass()

	elif userselect == 4:
		deletepass()

	elif userselect == 5:
		showpass()

	elif userselect == 6:
		savefill()

	elif userselect == 0:
		exit()

	else:
		print("accune options")
