# -*- coding: utf-8 -*-
import unittest

from src.functions.Functions import Functions
from src.functions.Inicializar import Inicializar
from src.pages.Login import Login
  
class tst_005(unittest.TestCase, Functions):

    def setUp(self):
        self.driver = self.abrir_Navegador()
        self.driver.get(Inicializar.URL2)

    def test_005(self):
        TEXT = self.driver.find_element_by_xpath(Login.lbl_Titulo_xpath).text

    
    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
