# -*- coding: utf-8 -*-
import unittest

from src.functions.Functions import Functions
from src.pages.Login import Login
  
class tst_003(unittest.TestCase, Functions):

    def setUp(self):
        self.driver = self.abrir_Navegador()

    def test_003(self):
        TEXT = self.driver.find_element_by_xpath(Login.lbl_Titulo_xpath).text
        print (TEXT)

        self.assertEqual(u"Iniciar sesión en Trello", TEXT)
    
    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
