import re
import pickle
import Data
import Loginsys
#Register
def register_data():
      username=input("Enter Email id  :")
      password=input("Enter Password  :")

      username_check=r"([^0-9_.+-][][a-z0-9A-Z._+-a]+@[a-zA-Z0-9.-]+\.[a-z])"
      match_username=re.match(username_check,username)

      if match_username==None:
        print("Entered username is not valid")

      password_check="^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*_+-])[a-zA-Z\d!@#$%^&*_+-]{5,16}$"
      match_password=re.match(password_check,password)

      if match_password==None:
        print("Password entered is not valid")
     
      Data.user_pswd.update({username:password})
     
      with open("Register.txt",'wb') as regis:
        pickle.dump(Data.user_pswd,regis)
      print("kindly log in")
      Loginsys.login_sys()
        
