import re
import pickle
import Loginsys

def forgot_password():
  user=input("Enter Username   :")

  with open("Register.txt",'rb') as file:
    data=file.read()
    d=pickle.loads(data)
  if (d.get(user)==None):
    print("Username doesnot exists, kindly register again")
    Loginsys.login_sys()
  else:  
    print("your password is  :",d.get(user))
