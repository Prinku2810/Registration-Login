import re
import pickle
import Register
def Login():
    flag=0
    user_name=input("Enter Username  :")
    pass_word=input("Enter Password  :")

    with open("Register.txt",'rb') as log:
            user_n=log.read()
            user_check=pickle.loads(user_n)

            if(user_name not in user_check.keys()):
              print("Username doesn\'t exist\'s")
              flag=1
              
    with open("Register.txt",'rb') as l:
            pas_n=l.read()
            pass_check=pickle.loads(pas_n)
            
            if(pass_word not in pass_check.values()):
              print("Entered password is incorrect")
            
            else:
              print("Logged in Successfully")
              print("\n")
            
    if flag==1:
        print("Kindly register to log in")
        login_sys()
      
