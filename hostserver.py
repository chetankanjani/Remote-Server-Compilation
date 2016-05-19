import socket               # Import socket module
from Tkinter import *
import paramiko
import thread

import time

def receive(c):

    length=c.recv(100)

    # print length
    data=""



    while(len(data)!=int(length)):

        data=c.recv(int(length))
        # print data

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



def handleclient(c,addr):
    count=1
    while True:

            count+=1
            language=receive(c)
            os=receive(c)

            word=receive(c)


            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())


            if(os=='All'):


                if (language=='Python') :

###########################VIRTUAL UBUNTU#######################################

                    print "Virtual Ubuntu Processing"
                    ssh.connect('192.168.56.101', username='chetan', password='ggmu')

                    sftp = ssh.open_sftp()

                    file=open("/home/chetan19/PycharmProjects/Minor/code/%s.py"%count,"w")


                    file.write('import time\n')
                    file.write('start_time = time.time()\n')

                    file.write(word)
                    file.write('\nprint("--- %s seconds ---" % (time.time() - start_time))')
                    file.close()
                    # print "here"


                    sftp.put('/home/chetan19/PycharmProjects/Minor/code/%s.py'%count,'/home/chetan/code/%s.py'%count)
                    stdin, stdout, ssh_stderr = ssh.exec_command('python /home/chetan/code/%s.py'%count,get_pty=True)
                    #stdin, stdout, ssh_stderr = ssh.exec_command('ls')
                    # c.send(stdout.read()
                    output=stdout.read()
                    Etime=output.split()
                    # print time[len(time)-3]
                    f=open("/home/chetan19/PycharmProjects/Minor/code/executionTime.text","w")
                    f.write(Etime[len(Etime)-3])
                    f.write("\n")
                    send(c,Etime[len(Etime)-3])




############################LINUX MINT################################################333333

                    print "Linux MINT processing"


                    ssh.connect('192.168.56.102', username='chetanm', password='ggmu')

                    sftp = ssh.open_sftp()


                    file=open("/home/chetan19/PycharmProjects/Minor/code/%s.py"%count,"w")


                    file.write('import time\n')
                    file.write('start_time = time.time()\n')

                    file.write(word)
                    file.write('\nprint("--- %s seconds ---" % (time.time() - start_time))')
                    file.close()
                    # print "here"


                    sftp.put('/home/chetan19/PycharmProjects/Minor/code/%s.py'%count,'/home/chetanm/code/%s.py'%count)
                    stdin, stdout, ssh_stderr = ssh.exec_command('python /home/chetanm/code/%s.py'%count,get_pty=True)
                    output=stdout.read()
                    Etime=output.split()

                    f.write(Etime[len(Etime)-3])
                    f.write("\n")
                    send(c,Etime[len(Etime)-3])



############################Native Ubuntu################################################333333


                    print "Native Ubuntu Processing"

                    ssh.connect('127.0.01', username='chetan19', password='ggmu')

                    sftp = ssh.open_sftp()


                    file=open("/home/chetan19/PycharmProjects/Minor/code/%s.py"%count,"w")


                    file.write('import time\n')
                    file.write('start_time = time.time()\n')

                    file.write(word)
                    file.write('\nprint("--- %s seconds ---" % (time.time() - start_time))')
                    file.close()
                    # print "here"


                    sftp.put('/home/chetan19/PycharmProjects/Minor/code/%s.py'%count,'/home/chetan19/code/%s.py'%count)
                    stdin, stdout, ssh_stderr = ssh.exec_command('python /home/chetan19/code/%s.py'%count,get_pty=True)
                    output=stdout.read()
                    Etime=output.split()

                    f.write(Etime[len(Etime)-3])

                    send(c,Etime[len(Etime)-3])


                    import time
                    time.sleep(2)

                    # print output
                    send(c,output)

                    print "Process Completed"
                    f.close()




                if ( language=='C'):

                    file=open("/home/chetan19/PycharmProjects/Minor/code/%s.c"%count,"w")
                    file.write(word)
                    file.close()

                    # time.sleep(100)

                    print count
                    sftp.put('/home/chetan19/PycharmProjects/Minor/code/%s.c'%count,'/home/chetan/code/%s.c'%count)
                    stdin, stdout, ssh_stderr = ssh.exec_command('gcc /home/chetan/code/%s.c'%count,get_pty=True)

                    # time.sleep(5)
                    stdinoutput, stdoutoutput, ssh_stderroutput = ssh.exec_command('time ./a.out')

                    codeOutput=stdoutoutput.read()

                    send(c,codeOutput)
                    # print codeOutput



                if ( language=='C++'):

                    file=open("/home/chetan19/PycharmProjects/Minor/code/%s.cpp"%count,"w")
                    file.write(word)
                    file.close()

                    # time.sleep(100)

                    # print count
                    sftp.put('/home/chetan19/PycharmProjects/Minor/code/%s.cpp'%count,'/home/chetan/code/%s.cpp'%count)
                    stdin, stdout, ssh_stderr = ssh.exec_command('g++ /home/chetan/code/%s.cpp'%count,get_pty=True)

                    # time.sleep(5)
                    stdinoutput, stdoutoutputAll, ssh_stderroutput = ssh.exec_command('time ./a.out')

                    codeOutput=stdoutoutputAll.read()
                    send(c,codeOutput)
                    # print codeOutput




            if(os=='Native Ubuntu'):


                if (language=='Python') :

                    ssh.connect('127.0.0.1', username='chetan19', password='ggmu')

                    sftp = ssh.open_sftp()
                    file=open("/home/chetan19/PycharmProjects/Minor/code/%s.py"%count,"w")


                    file.write('import time\n')
                    file.write('start_time = time.time()\n')

                    file.write(word)
                    file.write('\nprint("--- %s seconds ---" % (time.time() - start_time))')
                    file.close()
                    # print "here"


                    sftp.put('/home/chetan19/PycharmProjects/Minor/code/%s.py'%count,'/home/chetan19/code/%s.py'%count)
                    stdin, stdout, ssh_stderr = ssh.exec_command('python /home/chetan19/code/%s.py'%count,get_pty=True)
                    #stdin, stdout, ssh_stderr = ssh.exec_command('ls')
                    send(c,stdout.read())

                if ( language=='C'):

                    print " Processing in Native Ubuntu Language : C"
                    ssh.connect('127.0.0.1', username='chetan19', password='ggmu')

                    sftp = ssh.open_sftp()

                    file=open("/home/chetan19/PycharmProjects/Minor/code/%s.c"%count,"w")
                    file.write(word)
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
                        print "error"
                    # print ssh_stderr.read()
                    if(error==""):
                        stdinoutput, stdoutoutput, ssh_stderroutput = ssh.exec_command('./a.out')

                        codeOutput=stdoutoutput.read()
                        send(c,codeOutput)
                        print codeOutput
                        print "output sent"


                if ( language=='C++'):

                    print " Processing in Native Ubuntu Language : C++"
                    ssh.connect('127.0.0.1', username='chetan19', password='ggmu')

                    sftp = ssh.open_sftp()

                    file=open("/home/chetan19/PycharmProjects/Minor/code/%s.cpp"%count,"w")
                    file.write(word)
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
                        print "error"
                    # print ssh_stderr.read()
                    if(error==""):
                        stdinoutput, stdoutoutput, ssh_stderroutput = ssh.exec_command('./a.out')

                        codeOutput=stdoutoutput.read()
                        send(c,codeOutput)
                        print codeOutput
                        print "output sent"

            if(os=='Virtual Ubuntu 15.04'):

                ssh.connect('192.168.56.101', username='chetan', password='ggmu')

                sftp = ssh.open_sftp()


                if (language=='Python') :

                    print "Processing in Virtual Ubuntu Language : Python"
                    file=open("/home/chetan19/PycharmProjects/Minor/code/%s.py"%count,"w")


                    file.write('import time\n')
                    file.write('start_time = time.time()\n')

                    file.write(word)
                    file.write('\nprint("--- %s seconds ---" % (time.time() - start_time))')
                    file.close()
                    # print "here"


                    sftp.put('/home/chetan19/PycharmProjects/Minor/code/%s.py'%count,'/home/chetan/code/%s.py'%count)
                    stdin, stdout, ssh_stderr = ssh.exec_command('python /home/chetan/code/%s.py'%count,get_pty=True)
                    #stdin, stdout, ssh_stderr = ssh.exec_command('ls')
                    send(c,stdout.read())

                if ( language=='C'):

                    print " Processing in Virtual Ubuntu Language : C"


                    file=open("/home/chetan19/PycharmProjects/Minor/code/%s.c"%count,"w")
                    file.write(word)
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
                        print "error"
                    # print ssh_stderr.read()
                    if(error==""):
                        stdinoutput, stdoutoutput, ssh_stderroutput = ssh.exec_command('./a.out')

                        codeOutput=stdoutoutput.read()
                        send(c,codeOutput)
                        print codeOutput
                        print "output sent"


                if ( language=='C++'):


                    print " Processing in Virtual Ubuntu Language : C++"


                    file=open("/home/chetan19/PycharmProjects/Minor/code/%s.cpp"%count,"w")
                    file.write(word)
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
                        print "error"
                    # print ssh_stderr.read()
                    if(error==""):
                        stdinoutput, stdoutoutput, ssh_stderroutput = ssh.exec_command('./a.out')

                        codeOutput=stdoutoutput.read()
                        send(c,codeOutput)
                        print codeOutput
                        print "output sent"



            if(os=='Virtual Linux Mint'):

                ssh.connect('192.168.56.102', username='chetanm', password='ggmu')

                sftp = ssh.open_sftp()


                if (language=='Python') :
                    file=open("/home/chetan19/PycharmProjects/Minor/code/%s.py"%count,"w")


                    file.write('import time\n')
                    file.write('start_time = time.time()\n')

                    file.write(word)
                    file.write('\nprint("--- %s seconds ---" % (time.time() - start_time))')
                    file.close()
                    # print "here"


                    sftp.put('/home/chetan19/PycharmProjects/Minor/code/%s.py'%count,'/home/chetanm/code/%s.py'%count)
                    stdin, stdout, ssh_stderr = ssh.exec_command('python /home/chetanm/code/%s.py'%count,get_pty=True)
                    #stdin, stdout, ssh_stderr = ssh.exec_command('ls')
                    send(c,stdout.read())

                if ( language=='C'):

                    print " Processing in Mint Language : C"


                    file=open("/home/chetan19/PycharmProjects/Minor/code/%s.c"%count,"w")
                    file.write(word)
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
                        print "error"
                    # print ssh_stderr.read()
                    if(error==""):
                        stdinoutput, stdoutoutput, ssh_stderroutput = ssh.exec_command('./a.out')

                        codeOutput=stdoutoutput.read()
                        send(c,codeOutput)
                        print codeOutput
                        print "output sent"

                if ( language=='C++'):

                    print " Processing in MINT Language : C++"


                    file=open("/home/chetan19/PycharmProjects/Minor/code/%s.cpp"%count,"w")
                    file.write(word)
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
                        print "error"
                    # print ssh_stderr.read()
                    if(error==""):
                        stdinoutput, stdoutoutput, ssh_stderroutput = ssh.exec_command('./a.out')

                        codeOutput=stdoutoutput.read()
                        send(c,codeOutput)
                        print codeOutput
                        print "output sent"



server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

server_socket.bind(("", 12345))
server_socket.listen(10000)

while True:
    client_socket, address = server_socket.accept()
    print "Connected to - ",address[0],"\n"
    thread.start_new_thread(handleclient,(client_socket,address,))










