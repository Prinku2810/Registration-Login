def login_sys():
      print('Choose 1 - LOGIN')
      print('Choose 2 - REGISTER')
      print('Choose 3 - FORGET PASSWORD')
      print('\n')
      option=int(input())

      if option==1:
        Login()
        
      elif option==2:
        Register()
       

      elif option==3:
        forgot_password()
       
        login_sys()
  
 
