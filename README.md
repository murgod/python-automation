# python-automation

* [ssh_remote_server_run_commands_as_root_user.py](https://github.com/murgod/python-automation/blob/master/ssh_remote_server_run_commands_as_root_user.py) - 
This script can be used as blue print to automate the SSH login to remote server, copy file to remote server and execute the shell commands as 'root' user or to switching to any custom users.
- Installations : (For Mac OS X) 
1. pip install --upgrade pip
2. pip install --user paramiko
3. pip install --user scp


**Validate_ip.py**
Usage: python validate_ip.py <ip-address>
  Note : Works with Python2.7. For Pyhton3 change print statements. (add ())
```
LM-NWT:work murgod$ python validate_ip.py 2556.168.1.1
invalid ipv4 address
LM-NWT:work murgod$ python validate_ip.py 2556.168.1.10000
invalid ipv4 address
LM-NWT:work murgod$ python validate_ip.py 254.168.1.100
Valid ipv4 address
LM-NWT:work murgod$ python validate_ip.py 254.168.1.murgod
invalid ipv4 address

```









