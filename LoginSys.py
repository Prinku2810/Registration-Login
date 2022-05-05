import Register
import Login
import Forgotpswd
def login_sys():
      print('Choose 1 - LOGIN')
      print('Choose 2 - REGISTER')
      print('Choose 3 - FORGET PASSWORD')
      print('\n')
      option=int(input())

      if option==1:
        Login.login()
        
      elif option==2:
        Register.register_data()
       

      elif option==3:
        Forgotpswd.forgot_password()
       
        login_sys()
  
 
