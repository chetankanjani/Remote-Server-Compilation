import socket,os
import sys,time
import pyqtgraph as pg
import numpy as np
from PySide.QtCore import *
from PySide.QtGui import *
from PySide import QtGui
import pickle

class MyPopup(QWidget):
    def __init__(self,fileToBeShared):
        QWidget.__init__(self)
        self.vbox2 = QVBoxLayout()
        self.setLayout(self.vbox2)
        self.sharewith = QLabel()
        self.sharewith.setText("Share With :-")
        self.userList = QListWidget()

        print "waiting for user list"
        userslist=receive()
        items=pickle.loads(userslist)
        self.file=fileToBeShared
        for i in items:
            item = QListWidgetItem(i)
            self.userList.addItem(item)

        # print "before func",fileToBeShared
        self.ok_button = QPushButton('&Ok')
        self.ok_button.clicked.connect(self.shareFile)
        self.vbox2.addWidget(self.sharewith)
        self.vbox2.addWidget(self.userList)
        self.vbox2.addWidget(self.ok_button)



    def shareFile(self):

        send(self.file)
        # send(fileToBeShared)
        send(self.userList.currentItem().text())
        print "sending filename and username "

        print receive()

        QWidget.close(self)

class ExampleApp(QDialog):
    ''' An example application for PyQt. Instantiate
        and call the run method to run. '''
    def __init__(self):
        # create a Qt application --- every PyQt app needs one
        self.qt_app = QApplication(sys.argv)
        # Call the parent constructor on the current object
        QDialog.__init__(self, None)
        # Set up the window
        self.setWindowTitle('Login/Signup')
        self.setMinimumSize(250, 150)
        # Add a vertical layout
        self.vbox = QVBoxLayout()
        # self.vbox.addStretch(100)
        self.setLayout(self.vbox)

        self.usernamelabel = QLabel()
        self.usernamelabel.setText("Username:")
        self.username = QLineEdit()
        self.passwordlabel = QLabel()
        self.passwordlabel.setText("Password:")
        self.password = QLineEdit()
        self.password.setEchoMode(QLineEdit.Password)
        self.login_button = QPushButton('&Login')
        self.login_button.clicked.connect(self.login)
        self.signup_button = QPushButton('&Signup')
        self.signup_button.clicked.connect(self.signup)
        self.vbox.addWidget(self.usernamelabel)
        self.vbox.addWidget(self.username)
        self.vbox.addWidget(self.passwordlabel)
        self.vbox.addWidget(self.password)
        self.vbox.addWidget(self.login_button)
        self.vbox.addWidget(self.signup_button)


######## GUI FOR CODE COMPILATION ########
        self.languages = ['C', 'C++', 'python']
        # The language combo box
        self.language = QComboBox()
        # Add the languages
        list(map(self.language.addItem, self.languages))
        self.osOptions = ['ALL', 'Native Ubuntu', 'Virtual Ubuntu 15.04','Virtual Linux Mint']
        self.os = QComboBox()
        list(map(self.os.addItem, self.osOptions))
        self.input_box = QTextEdit('')
        self.outputbox = QTextEdit('')
        self.open_button=QPushButton('&Open File')
        self.open_button.clicked.connect(self.openFile)

        # The Go button
        self.go_button = QPushButton('&Go')
        self.go_button.clicked.connect(self.GoButton)


######## GUI FOR CLOUD DRIVE ########
        # The Browse button
        self.browse_button = QPushButton('&Browse')
        # Connect the Go button to its callback
        self.browse_button.clicked.connect(self.showDialog)
        # The input_file textbox
        self.input_file = QLineEdit('')
        # The available languages
        self.virtual_os = ['Ubuntu Server', 'Mint Server']
        # # The language combo box
        self.os_box = QComboBox()
        # # Add the languages
        list(map(self.os_box.addItem, self.virtual_os))
        # The Go button
        self.upload_button = QPushButton('&Upload')
        self.upload_button.clicked.connect(self.sendFile)
        # The file list
        self.file_list = QtGui.QTreeWidget()
        self.file_list.headerItem().setText(0, "Name")
        self.file_list.headerItem().setText(1, "Type")
        self.file_list.headerItem().setText(2, "Size")
        self.file_list.setColumnWidth(0, 300)
        self.file_list.setColumnWidth(1, 150)
        self.file_list.setColumnWidth(2, 150)
        self.file_list.setSortingEnabled(True)
        self.file_list.itemSelectionChanged.connect(self.selectFile)
        # The share button
        self.share_button = QPushButton('&Share')
        self.share_button.clicked.connect(self.sharePopup)
        # The download button
        self.download_button = QPushButton('&Download')
        self.download_button.clicked.connect(self.recvFile)
        # The refresh button
        self.refresh_button = QPushButton('&Refresh')
        self.refresh_button.clicked.connect(self.refreshList)



######## GUI FOR MAIN WINDOW ########
        self.options=['Remote Server Code Compilation','Cloud Drive']
        self.option=QComboBox()
        list(map(self.option.addItem, self.options))
        self.option.currentIndexChanged.connect(self.changeGUI)



    def login(self):


        if(self.username.text()==''):
            QtGui.QMessageBox.warning(self,'Error','Username is missing')
        elif(self.password.text()==''):
            # QtGui.QErrorMessage('Password')
            QtGui.QMessageBox.warning(self,'Error','Password is missing')
        else:

            send("login")

            send(self.username.text())
            send(self.password.text())
            response = receive()
            # print "the response is ",response
            if(response=='success'):
                print "success"
                self.showDefault()
            else:
                print "failure"
                QtGui.QMessageBox.warning(self,'Error','Incorrect Username or Password')

        # self.showDefault()

    def signup(self):


        if(self.username.text()==''):
            QtGui.QMessageBox.warning(self,'Error','Username is missing')
        elif(self.password.text()==''):
            # QtGui.QErrorMessage('Password')
            QtGui.QMessageBox.warning(self,'Error','Password is missing')
        else:
            send("signup")
            send(self.username.text())
            send(self.password.text())
            response = receive()
            if (response=="success"):
                print "success"
                self.showDefault()
            else:
                print "failure"
                QtGui.QMessageBox.warning(self,'Error','Username Not Available')


    def changeGUI(self):
        if(self.options[self.option.currentIndex()].title()=='Remote Server Code Compilation'):
            self.show1()

        elif(self.options[self.option.currentIndex()].title()=='Cloud Drive'):
            self.show2()

    def showDefault(self):
        self.setMinimumSize(600, 400)
        self.removeWidg(self.usernamelabel)
        self.removeWidg(self.username)
        self.removeWidg(self.passwordlabel)
        self.removeWidg(self.password)
        self.removeWidg(self.login_button)
        self.removeWidg(self.signup_button)
        self.vbox.addWidget(self.option)
        self.show1()

    def show1(self):
        self.setWindowTitle(self.options[self.option.currentIndex()].title())
        self.removeWidg(self.browse_button)
        self.removeWidg(self.input_file)
        self.removeWidg(self.os_box)
        self.removeWidg(self.upload_button)
        self.removeWidg(self.file_list)
        self.removeWidg(self.download_button)
        self.removeWidg(self.share_button)
        self.removeWidg(self.refresh_button)
        self.vbox.addWidget(self.language)
        self.vbox.addWidget(self.os)
        self.vbox.addWidget(self.input_box)
        self.vbox.addWidget(self.outputbox)
        self.vbox.addWidget(self.open_button)
        self.vbox.addWidget(self.go_button)

    def show2(self):
        self.setWindowTitle(self.options[self.option.currentIndex()].title())
        self.removeWidg(self.language)
        self.removeWidg(self.os)
        self.removeWidg(self.input_box)
        self.removeWidg(self.outputbox)
        self.removeWidg(self.go_button)
        self.removeWidg(self.open_button)
        self.vbox.addWidget(self.browse_button)
        self.vbox.addWidget(self.input_file)
        self.vbox.addWidget(self.os_box)
        self.vbox.addWidget(self.upload_button)
        self.vbox.addWidget(self.file_list)
        self.vbox.addWidget(self.download_button)
        self.vbox.addWidget(self.share_button)
        self.vbox.addWidget(self.refresh_button)
        self.refreshList()
        self.selectedFile=""



    def openFile(self):

        fname, _ = QtGui.QFileDialog.getOpenFileName(self, 'Open file',
                    '/home')
        fp=open(fname,'rb')
        data=fp.read()
        self.input_box.setText(data)
        fp.close()

    def GoButton(self):
        code=self.input_box.toPlainText()
        # print code
        # print self.language.displayText()

        send(self.options[self.option.currentIndex()].title())
        send(self.languages[self.language.currentIndex()].title())

        # time.sleep(1)

        send(self.osOptions[self.os.currentIndex()].title())



        # time.sleep(1)
        send(code)
        # print "before recieving"
        f=open("executionTimeClient.text","w")

        if(self.osOptions[self.os.currentIndex()].title()=="All"):

            print "Reciving Ex Time"
            output1 = receive()
            # time.sleep(1)
            time1=receive()
            f.write(str(time1))
            print time1
            f.write("\n")
            output2 = receive()
            # time.sleep(1)
            time2=receive()
            f.write(str(time2))
            f.write("\n")
            print time2
            output = receive()
            # time.sleep(1)
            time3=receive()
            f.write(str(time3))
            f.write("\n")
            print time3

            x=["Virtual Ubuntu","Native Ubuntu","Virual Linux Mint"]

            # f=open("executionTimeClient.text",'r+')
            y=[]
            a=float(time1)
            b=float(time2)
            c=float(time3)

            y.append(a)
            y.append(c)
            y.append(b)
            # # y.append(float(f.readline()))
            # # y.append(float(f.readline()))
            # # y.append(float(f.readline()))

            # # y = [3.00123, 4.3123123, 3.555]
            xdict=dict(enumerate(x))

            win = pg.GraphicsWindow(title="Performance On Different OS")
            stringaxis = MyStringAxis(xdict, orientation='bottom')
            plot = win.addPlot(axisItems={'bottom': stringaxis})
            curve = plot.plot(xdict.keys(),y, pen=(200,200,200), symbolBrush=(255,0,0), symbolPen='w')



        if(self.osOptions[self.os.currentIndex()].title()!="All"):
            output = receive()
            execution_time=receive()


        # time.sleep(1)
        # print "Waiting for output"
        # output=receive()
        print "output recieved"
        # print "after recieving"
        # print " i m here "
        # print output


        self.outputbox.setText(output)


    def showDialog(self):

        fname, _ = QtGui.QFileDialog.getOpenFileName(self, 'Open file',
                    '/home')
        self.input_file.setText(fname)

    def sendFile(self):

        if(self.input_file.displayText()==None):
            QtGui.QMessageBox.warning(self,'Error','Please select a File First')




        else:
            send(self.options[self.option.currentIndex()].title())
            send("upload")
            time.sleep(1)
            send(self.virtual_os[self.os_box.currentIndex()].title())
            time.sleep(1)
            path = self.input_file.displayText()
            self.input_file.setText('')
            name = path.split('/')
            name = name[len(name)-1]
            print "Opening file - ",name
            send(name)
            time.sleep(1)
            fp = open(path,'rb')
            # data = fp.read()
            size = os.path.getsize(path)
            size = str(size)
            send(size)
            time.sleep(1)
            # send(data)
            # client_socket.send(data)
            #############
            l = fp.read(3000000)
            while (l):
               client_socket.send(l)
               # print('Sent ',repr(l))
               l = fp.read(3000000)



            ##############
            fp.close()

            time.sleep(1)

            client_socket.send("-1Done")

            print "Data sent successfully"

    def selectFile(self):
        # print self.file_list.currentItem().text()
        self.selectedFile = self.file_list.currentItem().text(0)
        # print self.selectedFile

    def recvFile(self):

        if(self.selectedFile==None):
            QtGui.QMessageBox.warning(self,'Error','Please select a File First')



        else:
            send(self.options[self.option.currentIndex()].title())
            send("download")
            time.sleep(1)
            send(self.selectedFile)
            # fname = client_socket.recv(1024)
            # print "recieved file "+fname
            size = receive()
            size = int(size)
            print "The file size is - ",size," bytes"
            size = size*2
            strng = receive()
            fp = open(self.selectedFile,'wb')
            fp.write(strng)
            fp.close()
            print "Data Received successfully"

    def sharePopup(self):



#######################################################fix##############
        if(self.selectedFile!=""):

            send(self.options[self.option.currentIndex()].title())
            send("share")
            self.popup = MyPopup(self.selectedFile)
            self.popup.show()

        else:
            QtGui.QMessageBox.warning(self,'Error','Please Select A file which you want to share')



    def refreshList(self):
        send(self.options[self.option.currentIndex()].title())
        # client_socket.send("refresh")
        send("refresh")
        data=receive()
        items1=pickle.loads(data)
        data=receive()
        items2=pickle.loads(data)
        data=receive()
        items3=pickle.loads(data)
        self.file_list.clear()
        for i in range (0,len(items1)):
            item = QTreeWidgetItem(self.file_list)
            item.setText(0,items1[i])
            item.setText(1,items2[i])
            item.setText(2,items3[i])

    def quit(self):
        send("quit")
        exit()

    def removeWidg(self,x):
        self.vbox.removeWidget(x)
        x.setParent(None)

    def run(self):
        ''' Run the app and show the main form. '''
        self.show()
        self.qt_app.exec_()

def receive():

    length=client_socket.recv(100)
    # print length
    data=""

    while(len(data)!=int(length)):

        data=client_socket.recv(int(length))

        if(len(data)==int(length)):
            client_socket.send("success")
        else:
            client_socket.send("failure")

    return data


def send(data):

    data=str(data)
    client_socket.send(str(len(data)))
    time.sleep(1)
    response="failure"

    while(response!="success"):
        client_socket.send(data)
        # print "data sent"
        response=client_socket.recv(9)
        # print response

class MyStringAxis(pg.AxisItem):
    def __init__(self, xdict, *args, **kwargs):
        pg.AxisItem.__init__(self, *args, **kwargs)
        self.x_values = np.asarray(xdict.keys())
        self.x_strings = xdict.values()

    def tickStrings(self, values, scale, spacing):
        strings = []
        for v in values:
            # vs is the original tick value
            vs = v * scale
            # if we have vs in our values, show the string
            # otherwise show nothing
            if vs in self.x_values:
                # Find the string with x_values closest to vs
                vstr = self.x_strings[np.abs(self.x_values-vs).argmin()]
            else:
                vstr = ""
            strings.append(vstr)
        return strings


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# # client_socket.connect(("localhost", 5005))
client_socket.connect(("localhost", 12345))
# host = socket.gethostname() # Get local machine name
# client_socket.send(host)
app = ExampleApp()
app.run()