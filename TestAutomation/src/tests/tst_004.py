# -*- coding: utf-8 -*-
import unittest

from src.functions.Functions import Functions
from src.pages.Login import Login

import allure
import pytest

  
@allure.feature(u'Login a Trello')
@allure.story(u'001: probar el acceso de usuario a trello')
@allure.testcase(u"caso de prueba 00001",u'http://www.trello.com')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(u"""conectar a trello con exito:</br>
  -- escibir la url de trello </br>
  -- ir a login </br>
  -- esribir usuario y contraseña </br>
  -- presionar Enter </br>
  -- el navegador abre trello y nos muestra la imagen a la derecha </br>""")
  
class tst_004(unittest.TestCase, Functions):
    
    def setUp(self):
        with allure.step(u'conectar a trello con exito'):
        
            self.driver = self.abrir_Navegador()

    def test_004(self):
        with allure.step(u'escibir la url de trello'):
            TEXT = self.driver.find_element_by_xpath(Login.lbl_Titulo_xpath).text
            print (TEXT)

        self.assertEqual(u"Iniciar sesión en Trello", TEXT)
    
    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
