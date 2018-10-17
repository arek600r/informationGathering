from ftplib import FTP

ftp = FTP('jakwpracy.pl')
ftp.login(user='pokojelu', passwd='Marta1kawasaki636')
ftp.cwd('/domains')

def grabFile():
    fileName = 'zalog.php'
    localfile = open(fileName, 'wb')
    ftp.retribinary('RETR ' + fileName, localfile.write, 1024)
    ftp.quit()
    localfile.close()

def placeFile():
    fileName = 'zalog.php'
    ftp.storbinary('STOR '+fileName, open(fileName, 'rb'))
    ftp.quit()