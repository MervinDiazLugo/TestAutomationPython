# -*- coding: utf-8 -*-
import unittest
from src.functions.Functions import Functions
from src.pages.Login import Login
 
  
class tst_001(unittest.TestCase, Functions):

    def setUp(self):
        self.driver = self.abrir_Navegador()

    def test_001(self):
        TEXT = self.Xpath_Elements(Login.lbl_Titulo_xpath).text
        print (TEXT)
        
        if (self.dir_navegador == "FIREFOX"):
            self.assertEqual(u"Log in to Trello", TEXT)
        
        else:
            self.assertEqual(u"Iniciar sesión en Trello", TEXT)

        self.Xpath_Elements(Login.txt_email_xpath).send_keys("mediaz@cdainfo.com")
        
        self.Xpath_Elements(Login.txt_password_xpath).send_keys("Mm111213")
        
        self.Xpath_Elements(Login.btn_login_xpath).click()
        
        self.esperar_Xpath(Login.img_AvatarUsuario_xpath)
        
        self.Xpath_Elements(Login.img_AvatarUsuario_xpath).click()
        
        TEXT = self.Xpath_Elements(Login.lbl_UsuarioLogueado_xpath).text
        print (TEXT)
        self.assertEqual(u"Mervin Diaz (diazmervin)", TEXT)
        
        
        self.capturar_Pantalla()


    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
