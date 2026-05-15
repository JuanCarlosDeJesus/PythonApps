from ftplib import FTP

# user data in the future create env files to hide this
# acct for testing purpose only
host = "videoftptut.bplaced.net"
user = "videoftptut"
password = "neural123"

with FTP(host) as ftp:
    ftp.login(user=user, passwd=password)
    print(ftp.getwelcome)

    # download
    # with open('test.txt', 'wb') as f:
    #     ftp.retrbinary("RETR " + "mytest.txt", f.write, 1024)

    # download - not in main directory
    ftp.cwd("mydir")

    with open('test.txt', 'wb') as f:
        ftp.retrbinary('RETR ' + 'otherfile.txt', f.write, 1024)


    # upload
    # with open('myupload.txt', 'rb') as f:
    #     ftp.storebinary('STOR ' + 'upload.txt', f)


    ftp.quit()


