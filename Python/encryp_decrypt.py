import os
import subprocess as sp
import getpass
input_file=os.environ['NAUTILUS_SCRIPT_SELECTED_FILE_PATHS'].strip()

while(True):
    print("Please enter password for Encryption/Decryption\n")
    password=getpass.getpass().strip()
    #tmp = sp.call('clear',shell=True)
    print("Please re-enter password\n")
    rpassword=getpass.getpass().strip()
    if(password==rpassword):
        break
    else:
        tmp = sp.call('clear',shell=True)
        print("Password didn't matched try again")


def get_password_integer_list(password):
    s=[]
    for x in password:
        s.append(ord(x))
    return s

def encrypt(data,password):
    a=[]
    for x,y in zip(data,password):
        a.append(x^y)
    return a

file=open(input_file,'rb')
file2_name=input_file+".endc"
if(input_file.split('.')[-1]=="endc"):
    file2_name=input_file.rsplit(".endc",1)
    file2_name="".join(file2_name)
file2=open(file2_name,'wb')



s=get_password_integer_list(password)
print(s)
while(True):
    z=file.read(6)
    z=list(z)
    file2.write(bytes(encrypt(z,s)))
    if(len(z)<6):
        print(list(z),"file processing complete")
        break
input("Press Enter to exit")