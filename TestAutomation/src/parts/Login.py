# -*- coding: utf-8 -*-

'''
Created on 29 sept. 2018


'''
from src.functions.Functions import Functions as Selenium
from src.pages.Login_oldelval import Login_oldelval
import pytest


class Login(Selenium):

    def Login_app(self):
        
        self.esperar_Xpath(Login_oldelval.lbl_Titulo_xpath)
        
        self.Xpath_Elements(Login_oldelval.txt_user_xpath).send_keys(self.User)
        
        self.Xpath_Elements(Login_oldelval.txt_pass_xpath).send_keys(self.Password)
        
        self.get_image("Usuario y pass")
        
        self.Xpath_Elements(Login_oldelval.btn_ingresar_xpath).click()
        
        self.waitStopLoad(8)
        
        self.get_image("Login Results")
        
        NoLogin = self.verificar_xpath(Login_oldelval.msj_NoLogin_xpath)
        print (str(NoLogin))
        
        if NoLogin == False:
            pass
        
        else:
            msj_Error_Login = self.Xpath_Elements(Login_oldelval.msj_NoLogin_xpath).text
            
            if msj_Error_Login == "Usuario bloqueado.":
                
                print (msj_Error_Login)
                pytest.skip(msj_Error_Login)
                
            if msj_Error_Login == "Usuario o Contraseña inválidos.":
                
                print (msj_Error_Login)
                pytest.skip(msj_Error_Login)
        
            if msj_Error_Login == "Usuario o password incorrecto.":
                print (msj_Error_Login)
                pytest.skip(msj_Error_Login)
        
        
        