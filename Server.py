import socket               # Import socket module
from Tkinter import *
import paramiko
import thread
import config
import pickle
import os

import time

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())


def returneExTimeFromTime(word):

    # print "time is ",word
    time=word.split()
    time1=time[1]
    n=len(time1[1])
    # print time1
    j=0
    ans=""
    # print "whole word is ",time1
    # print "length is",n
    for i in time1:
        # print i
        if(j>1 ):
            ans+=i
        j=j+1

    new_ans=ans.replace("s","")
    return new_ans


def receive(c):

    length=c.recv(100)

    # print length
    data=""

    time.sleep(1)

    while(len(data)!=int(length)):

        data=c.recv(int(length))
        # print data

        # print "actual length is ",length
        # print "actual length is ",length
        # print "present length is ",len(data)

        if(len(data)==int(length)):
            c.send("success")

        else:
            c.send("failure")

    return data



def send(s,data):

    data=str(data)
    s.send(str(len(data)))

    time.sleep(1)

    # print "len sent"

    response="failure"

    while(response!="success"):

        s.send(data)

        # print "data sent"

        response=s.recv(8)
        # print response

def virtualUbuntuCodeCompilation(language,c,count,code):


    print "Virtual Ubuntu Processing"


    ssh.connect(config.ip_ubuntu, username=config.vm_ubuntu_username, password=config.password_vm_ubuntu)

    sftp = ssh.open_sftp()

    if(language=="Python"):


        file=open("/home/chetan19/PycharmProjects/Minor/code/%s.py"%count,"w")


        file.write('import time\n')
        file.write('start_time = time.time()\n')

        file.write(code)
        file.write('\nprint("--- %s seconds ---" % (time.time() - start_time))')
        file.close()
        # print "here"


        sftp.put('/home/chetan19/PycharmProjects/Minor/code/%s.py'%count,'/home/chetan/code/%s.py'%count)
        stdin, stdout, ssh_stderr = ssh.exec_command('python /home/chetan/code/%s.py'%count,get_pty=True)
        #stdin, stdout, ssh_stderr = ssh.exec_command('ls')
        # c.send(stdout.read()
        output=stdout.read()
        Etime=output.split()
        send(c,output)
        print "output sent"
        # print Etime
        # print Etime[len(Etime)-3]
        f=open("/home/chetan19/PycharmProjects/Minor/code/executionTime.text","w")
        f.write(Etime[len(Etime)-3])
        f.write("\n")
        send(c,Etime[len(Etime)-3])
        print "Execution time sent"


    if ( language=='C'):

        print " Processing in Virtual Ubuntu Language : C"


        file=open("/home/chetan19/PycharmProjects/Minor/code/%s.c"%count,"w")
        file.write(code)
        file.close()

        # time.sleep(100)

        # print count

        sftp.put('/home/chetan19/PycharmProjects/Minor/code/%s.c'%count,'/home/chetan/code/%s.c'%count)

        stdin, stdout, ssh_stderr = ssh.exec_command('gcc /home/chetan/code/%s.c'%count,get_pty=True)

        # time.sleep(5)
        # print stdin.read()
        error=stdout.read()
        if (error):
            send(c,error)
            send(c,0)
            print "error"
        # print ssh_stderr.read()
        if(error==""):
            stdinoutput, stdoutoutput, ssh_stderroutput = ssh.exec_command('time ./a.out')


            # for line in stdoutoutput:
            #     print line
            ssh_stderroutput.readline()
            # print "a"
            # print ssh_stderroutput.readline()
            extime=returneExTimeFromTime(ssh_stderroutput.readline())
            f=open("/home/chetan19/PycharmProjects/Minor/code/executionTime.text","w")
            f.write(extime)
            f.write("\n")
            # print extime

            # print "b"
            # print ssh_stderroutput.readline()
            #
            # for line in ssh_stderroutput:
            #     print i
            #     print line
            #     i=i+1

            codeOutput=stdoutoutput.read()
            send(c,codeOutput)
            print codeOutput
            print "output sent"
            send(c,extime)
            print "Excution time sent"


    if ( language=='C++'):


        print " Processing in Virtual Ubuntu Language : C++"


        file=open("/home/chetan19/PycharmProjects/Minor/code/%s.cpp"%count,"w")
        file.write(code)
        file.close()

        # time.sleep(100)

        # print count

        sftp.put('/home/chetan19/PycharmProjects/Minor/code/%s.cpp'%count,'/home/chetan/code/%s.cpp'%count)

        stdin, stdout, ssh_stderr = ssh.exec_command('g++ /home/chetan/code/%s.cpp'%count,get_pty=True)

        # time.sleep(5)
        # print stdin.read()
        error=stdout.read()
        if (error):
            send(c,error)
            send(c,0)

            print "error"
        # print ssh_stderr.read()
        if(error==""):
            stdinoutput, stdoutoutput, ssh_stderroutput = ssh.exec_command('time ./a.out')

            ssh_stderroutput.readline()
            # print "a"
            # print ssh_stderroutput.readline()
            extime=returneExTimeFromTime(ssh_stderroutput.readline())
            f=open("/home/chetan19/PycharmProjects/Minor/code/executionTime.text","w")
            f.write(extime)
            f.write("\n")

            codeOutput=stdoutoutput.read()
            send(c,codeOutput)
            print codeOutput
            print "output sent"
            send(c,extime)
            print "Execution time sent"


def virtualMintCodeCompilation(language,c,count,code):

    print "Linux MINT processing"


    ssh.connect(config.ip_mint, username=config.vm_mint_username, password=config.password_vm_mint)

    sftp = ssh.open_sftp()


    if(language=="Python"):



        file=open("/home/chetan19/PycharmProjects/Minor/code/%s.py"%count,"w")


        file.write('import time\n')
        file.write('start_time = time.time()\n')

        file.write(code)
        file.write('\nprint("--- %s seconds ---" % (time.time() - start_time))')
        file.close()
        # print "here"


        sftp.put('/home/chetan19/PycharmProjects/Minor/code/%s.py'%count,'/home/chetanm/code/%s.py'%count)
        stdin, stdout, ssh_stderr = ssh.exec_command('python /home/chetanm/code/%s.py'%count,get_pty=True)
        output=stdout.read()
        Etime=output.split()

        send(c,output)
        print "output sent"

        f=open("/home/chetan19/PycharmProjects/Minor/code/executionTime.text","w")

        f.write(Etime[len(Etime)-3])
        f.write("\n")
        send(c,Etime[len(Etime)-3])
        print "Execution time sent"

    if ( language=='C'):

        print " Processing in Mint Language : C"


        file=open("/home/chetan19/PycharmProjects/Minor/code/%s.c"%count,"w")
        file.write(code)
        file.close()

        # time.sleep(100)

        # print count

        sftp.put('/home/chetan19/PycharmProjects/Minor/code/%s.c'%count,'/home/chetanm/code/%s.c'%count)

        stdin, stdout, ssh_stderr = ssh.exec_command('gcc /home/chetanm/code/%s.c'%count,get_pty=True)

        # time.sleep(5)
        # print stdin.read()
        error=stdout.read()
        if (error):
            send(c,error)
            send(c,0)

            print "error"
        # print ssh_stderr.read()
        if(error==""):
            stdinoutput, stdoutoutput, ssh_stderroutput = ssh.exec_command('time ./a.out')

            ssh_stderroutput.readline()
            # print "a"
            # print ssh_stderroutput.readline()
            extime=returneExTimeFromTime(ssh_stderroutput.readline())
            f=open("/home/chetan19/PycharmProjects/Minor/code/executionTime.text","w")
            f.write(extime)
            f.write("\n")

            codeOutput=stdoutoutput.read()
            send(c,codeOutput)
            print codeOutput
            print "output sent"
            send(c,extime)
            print "Execution time sent"

    if ( language=='C++'):

        print " Processing in MINT Language : C++"


        file=open("/home/chetan19/PycharmProjects/Minor/code/%s.cpp"%count,"w")
        file.write(code)
        file.close()

        # time.sleep(100)

        # print count

        sftp.put('/home/chetan19/PycharmProjects/Minor/code/%s.cpp'%count,'/home/chetanm/code/%s.cpp'%count)

        stdin, stdout, ssh_stderr = ssh.exec_command('g++ /home/chetanm/code/%s.cpp'%count,get_pty=True)

        # time.sleep(5)
        # print stdin.read()
        error=stdout.read()
        if (error):
            send(c,error)
            send(c,0)
            print "error"
        # print ssh_stderr.read()
        if(error==""):
            stdinoutput, stdoutoutput, ssh_stderroutput = ssh.exec_command('time ./a.out')

            ssh_stderroutput.readline()
            # print "a"
            # print ssh_stderroutput.readline()
            extime=returneExTimeFromTime(ssh_stderroutput.readline())
            f=open("/home/chetan19/PycharmProjects/Minor/code/executionTime.text","w")
            f.write(extime)
            f.write("\n")

            codeOutput=stdoutoutput.read()
            send(c,codeOutput)
            print codeOutput
            print "output sent"
            # print "output sent"
            send(c,extime)
            print "Execution time sent"


def nativeUbuntuCodeCompilation(language,c,count,code):

    print "Native Ubuntu Processing"

    ssh.connect('127.0.01', username=config.ubuntu_username, password=config.password_native_ubuntu)

    sftp = ssh.open_sftp()

    if(language=="Python"):


        file=open("/home/chetan19/PycharmProjects/Minor/code/%s.py"%count,"w")


        file.write('import time\n')
        file.write('start_time = time.time()\n')

        file.write(code)
        file.write('\nprint("--- %s seconds ---" % (time.time() - start_time))')
        file.close()
        # print "here"


        sftp.put('/home/chetan19/PycharmProjects/Minor/code/%s.py'%count,'/home/chetan19/code/%s.py'%count)
        stdin, stdout, ssh_stderr = ssh.exec_command('python /home/chetan19/code/%s.py'%count,get_pty=True)
        output=stdout.read()
        Etime=output.split()
        f=open("/home/chetan19/PycharmProjects/Minor/code/executionTime.text","w")

        f.write(Etime[len(Etime)-3])
        send(c,output)
        print "output sent"
        send(c,Etime[len(Etime)-3])
        print "Execution time sent"

        import time
        time.sleep(2)

        # print output

        print "Process Completed"
        f.close()

    if ( language=='C'):

        print " Processing in Native Ubuntu Language : C"


        file=open("/home/chetan19/PycharmProjects/Minor/code/%s.c"%count,"w")
        file.write(code)
        file.close()

        # time.sleep(100)

        # print count

        sftp.put('/home/chetan19/PycharmProjects/Minor/code/%s.c'%count,'/home/chetan19/code/%s.c'%count)

        stdin, stdout, ssh_stderr = ssh.exec_command('gcc /home/chetan19/code/%s.c'%count,get_pty=True)

        # time.sleep(5)
        # print stdin.read()
        error=stdout.read()
        if (error):
            send(c,error)
            send(c,0)
            print "error"
        # print ssh_stderr.read()
        if(error==""):
            stdinoutput, stdoutoutput, ssh_stderroutput = ssh.exec_command('time ./a.out')

            ssh_stderroutput.readline()
            # print "a"
            # print ssh_stderroutput.readline()
            extime=returneExTimeFromTime(ssh_stderroutput.readline())
            f=open("/home/chetan19/PycharmProjects/Minor/code/executionTime.text","w")
            f.write(extime)
            f.write("\n")
            codeOutput=stdoutoutput.read()
            send(c,codeOutput)
            print codeOutput
            print "output sent"

            send(c,extime)
            print "Execution time sent"


    if ( language=='C++'):

        print " Processing in Native Ubuntu Language : C++"


        file=open("/home/chetan19/PycharmProjects/Minor/code/%s.cpp"%count,"w")
        file.write(code)
        file.close()

        # time.sleep(100)

        # print count

        sftp.put('/home/chetan19/PycharmProjects/Minor/code/%s.cpp'%count,'/home/chetan19/code/%s.cpp'%count)

        stdin, stdout, ssh_stderr = ssh.exec_command('g++ /home/chetan19/code/%s.cpp'%count,get_pty=True)

        # time.sleep(5)
        # print stdin.read()
        error=stdout.read()
        if (error):
            send(c,error)
            send(c,0)
            print "error"
        # print ssh_stderr.read()
        if(error==""):
            stdinoutput, stdoutoutput, ssh_stderroutput = ssh.exec_command('time ./a.out')


            ssh_stderroutput.readline()
            # print "a"
            # print ssh_stderroutput.readline()
            extime=returneExTimeFromTime(ssh_stderroutput.readline())
            f=open("/home/chetan19/PycharmProjects/Minor/code/executionTime.text","w")
            f.write(extime)
            f.write("\n")

            codeOutput=stdoutoutput.read()
            send(c,codeOutput)
            print codeOutput
            print "output sent"
            send(c,extime)

            print "Execution time sent"


def returnAllUsers():

    list=[]
    with open('/home/chetan19/PycharmProjects/Minor/username.txt') as openfileobject:
        for line in openfileobject:

            # print line
            b=line.split()

            list.append(b[0])


    # print list
    return list



def checkUsername(username):


    flag=0

    with open('/home/chetan19/PycharmProjects/Minor/username.txt') as openfileobject:
        for line in openfileobject:

            # print line
            b=line.split()

            if(b[0]==username):

                flag=1
                break


    if(flag==1):

        return True

    else:
        return False



def checkPassword(username,password):


    with open('/home/chetan19/PycharmProjects/Minor/username.txt') as openfileobject:
        for line in openfileobject:

            # print line
            b=line.split()
            if(b[0]==username and b[1]==password):

                return True



    return False




def handleclient(c,addr):

    count=1

    loginProccess=1


    while(loginProccess):
        requestType=receive(c)
        username=receive(c)
        password=receive(c)


        if(requestType=='signup'):

            print "signup request"
            if(checkUsername(username)==False):
                f=open("/home/chetan19/PycharmProjects/Minor/username.txt","rw+")

                f.read()
                f.write(username)
                f.write(" ")
                f.write(password)
                f.write("\n")
                f.close()

                send(c,"success")
                print "success"
                loginProccess=0


            else:
                send(c,"username already exist")
                print "username already exist"

        if(requestType=='login'):

            print "login request"
            if(checkUsername(username)==True):

                if(checkPassword(username,password)==True):
                    send(c,"success")
                    print "success"
                    loginProccess=0

                else:
                    send(c,"Incorrect password")
                    print "Incorrect password"

            else :

                send(c,"username doesn't exist")
                print "username doesn't exist"



    while True:


        print "waiting for operation"

        option=receive(c)

        if(option=='Remote Server Code Compilation'):

            count+=1
            language=receive(c)
            os=receive(c)
            code=receive(c)

            if(os=='All'):

                virtualUbuntuCodeCompilation(language,c,count,code)
                virtualMintCodeCompilation(language,c,count,code)
                nativeUbuntuCodeCompilation(language,c,count,code)

            if(os=='Native Ubuntu'):

                nativeUbuntuCodeCompilation(language,c,count,code)


            if(os=='Virtual Ubuntu 15.04'):

               virtualUbuntuCodeCompilation(language,c,count,code)

            if(os=='Virtual Linux Mint'):

                virtualMintCodeCompilation(language,c,count,code)

        elif(option=="Cloud Drive"):


            hostname=username


            # while True:

            choice = receive(c)

            if(choice == "upload"):
                virtual_os = receive(c)
                print virtual_os
                # fname = client_socket.recv(1024)
                fname=receive(c)
                print "receiving file "+fname
                # size = client_socket.recv(1024)
                size=receive(c)
                size = int(size)
                print "The file size is - ",size," bytes"
                # size = size*2
                # strng = c.recv(size)
                # strng=receive(c)
                #####################
                f = open(fname,'wb')
                while True:
                    # print('receiving data...')

                    data = c.recv(3000000)


                    if (data=='-1Done'):
                        print "done"
                        break
                    # print('data=%s', (data))

                    # write data to a file
                    f.write(data)



                ######################
                # time.sleep(1)
                f.close()
                print "File received on server"


                if(virtual_os=="Mint Server"):
                    print "Virtual Mint Processing"
                    ssh.connect(config.ip_mint, username=config.vm_mint_username, password=config.password_vm_mint)
                    sftp = ssh.open_sftp()

                    # stdin1, stdout1, ssh_stderr1 = ssh.exec_command('cd fileserver')
                    # print hostname
                    # stdin2, stdout2, ssh_stderr2 = ssh.exec_command('ls')
                    # print stdout2.read()

                    stdin, stdout, ssh_stderr = ssh.exec_command('mkdir fileserver/%s'%hostname)
                    # print stdout.read()
                    # sftp.mkdir(hostname)
                    # print '/home/chetan/fileserver/%s/%s'%(hostname,fname)
                    sftp.put('/home/chetan19/PycharmProjects/Minor/%s'%fname,'/home/chetanm/fileserver/%s/%s'%(hostname,fname))

                if(virtual_os=="Ubuntu Server"):

                    print "Virtual Ubuntu Processing"
                    ssh.connect(config.ip_ubuntu, username=config.vm_ubuntu_username, password=config.password_vm_ubuntu)
                    sftp = ssh.open_sftp()

                    # stdin1, stdout1, ssh_stderr1 = ssh.exec_command('cd fileserver')
                    # print hostname
                    # stdin2, stdout2, ssh_stderr2 = ssh.exec_command('ls')
                    # print stdout2.read()

                    stdin, stdout, ssh_stderr = ssh.exec_command('mkdir fileserver/%s'%hostname)
                    # print stdout.read()
                    # sftp.mkdir(hostname)
                    # print '/home/chetan/fileserver/%s/%s'%(hostname,fname)
                    sftp.put('/home/chetan19/PycharmProjects/Minor/%s'%fname,'/home/chetan/fileserver/%s/%s'%(hostname,fname))


                print "Uploaded Server"


            elif(choice == "download"):
                # fname = client_socket.recv(1024)
                fname = receive(c)



                ssh.connect(config.ip_ubuntu, username=config.vm_ubuntu_username, password=config.password_vm_ubuntu)


                sftp = ssh.open_sftp()

                stdin, stdout, ssh_stderr = ssh.exec_command('ls fileserver/%s'%hostname)
                ls1=stdout.read()

                objects=ls1.split("\n")
                flag=0
                for i in objects:
                    if(i==fname):
                        flag=1

                if(flag==1):
                    sftp.get('/home/chetan/fileserver/%s/%s'%(hostname,fname),'/home/chetan19/PycharmProjects/Minor/%s'%(fname))




                ssh.connect(config.ip_mint, username=config.vm_mint_username, password=config.password_vm_mint)
                sftp = ssh.open_sftp()
                stdin, stdout, ssh_stderr = ssh.exec_command('ls fileserver/%s'%hostname)
                ls1=stdout.read()

                objects=ls1.split("\n")
                flag=0
                for i in objects:
                    if(i==fname):
                        flag=1

                if(flag==1):
                    sftp.get('/home/chetanm/fileserver/%s/%s'%(hostname,fname),'/home/chetan19/PycharmProjects/Minor/%s'%(fname))



                print "sending file "+fname
                fp = open(fname,'rb')
                data = fp.read()
                fp.close()
                import os
                size = os.path.getsize(fname)
                size = str(size)
                # client_socket.send(size)
                send(c,size)
                time.sleep(1)
                # client_socket.send(data)
                send(c,data)
                print "Data sent successfully"
                send(c,"success")

            elif(choice == "refresh"):


                print "refreshing list .... "

                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(config.ip_mint, username=config.vm_mint_username, password=config.password_vm_mint)

                sftp = ssh.open_sftp()
                stdin, stdout, ssh_stderr = ssh.exec_command('ls fileserver/%s'%hostname)
                ls1=stdout.read()
                ssh.connect(config.ip_ubuntu, username=config.vm_ubuntu_username, password=config.password_vm_ubuntu)

                sftp = ssh.open_sftp()
                stdin, stdout1, ssh_stderr = ssh.exec_command('ls fileserver/%s'%hostname)
                ls2=stdout1.read()
                objects1=ls1.split("\n")
                objects2=ls2.split("\n")
                # print objects1
                # print objects2

                list=[]

                for i in range(0,len(objects1)):
                    list.append(objects1[i])

                for i in range(0,len(objects2)):
                    list.append(objects2[i])

                data=pickle.dumps(list)
                # client_socket.send(data)
                send(c,data)
                # time.sleep(1)
                # send(c,data)
                # client_socket.send(data)

                # client_socket.send(data)
                print "refresh completed"




            elif(choice == "share"):

                print "sharing operation in progress"
                print "fetching user list "

                allUsers=returnAllUsers()
                # print allUsers
                data=pickle.dumps(allUsers)
                send(c,data)
                filename=receive(c)
                user=receive(c)
                print filename
                print user



                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(config.ip_mint, username=config.vm_mint_username, password=config.password_vm_mint)
                stdin, stdout, ssh_stderr = ssh.exec_command('mkdir fileserver/%s'%user)

                sftp = ssh.open_sftp()
                stdin, stdout, ssh_stderr = ssh.exec_command('cp fileserver/%s/%s  fileserver/%s/%s'%(hostname,filename,user,filename))
                # print "hi",stdout.read()

                print stdout.read()
                print ssh_stderr.read()


                ssh.connect(config.ip_ubuntu, username=config.vm_ubuntu_username, password=config.password_vm_ubuntu)
                stdin, stdout, ssh_stderr = ssh.exec_command('mkdir fileserver/%s'%user)

                sftp = ssh.open_sftp()
                stdin, stdout, ssh_stderr = ssh.exec_command('cp fileserver/%s/%s  fileserver/%s/%s'%(hostname,filename,user,filename))
                # print "hi1",stdout.read()
                print stdout.read()
                print ssh_stderr.read()
                print "file successfully shared"
                send(c,"success")
                # print filename
                # print username






server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

server_socket.bind(("", 12345))
server_socket.listen(10000)

while True:

    # print returnAllUsers()
    client_socket, address = server_socket.accept()
    print "Connected to - ",address[0],"\n"
    thread.start_new_thread(handleclient,(client_socket,address,))










