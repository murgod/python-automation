#!/usr/bin/python 

import paramiko
import sys
import time
from paramiko import SSHClient
from scp import SCPClient



hostname=sys.argv[1]
username=sys.argv[2]
ssh_pwd=sys.argv[3]


######################################################################################
def jobprogress(filename, size, sent):
    sys.stdout.write("%s\'s progress: %.2f%%   \r" % (filename, float(sent)/float(size)*100) )

def send_command_and_wait(command, wait_time, print):
    shell.send(command)
    time.sleep(wait_time)
    data = shell.recv(1024)
    if print:
        print data
    

######################################################################################
#create Client
ssh_client=paramiko.SSHClient()
#set hostkey to TRUE
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#SSH connect
ssh_client.connect(hostname=hostname,username=username ,password=ssh_pwd)


stdin,stdout,stderr=ssh_client.exec_command('ls')


with SCPClient(ssh_client.get_transport(), progress=jobprogress) as scp:
    scp.put('source_file.txt', 'source_file.txt')

#Get Shell prompt
shell = ssh_client.invoke_shell()

#Send the su command
send_command_and_wait("sudo su - paydiant\n", 2, True)

#Send the client's su password followed by a newline
send_command_and_wait(ssh_pwd+"\n", 3, True)

send_command_and_wait("cd path/to/directory\n", 3, True)
send_command_and_wait("ls\n", 3, True)
send_command_and_wait("mv file1.txt file2.txt.newbkp\n", 4, True)
send_command_and_wait("ls\n", 3, True)
 
ssh_client.close()
