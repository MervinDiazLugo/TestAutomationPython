# -*- coding: utf-8 -*-
import unittest

from src.functions.Functions import Functions
from src.pages.Login import Login
import allure  # a los allure se los llama decoradores.
import pytest

@allure.feature(u'login Trello')
@allure.story(u'El usuario se loguea en Trello')
@allure.testcase(u"Caso de Prueba 00001", u'https://my.tms.org/browse/TESTCASE-39')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(U"""El Usuario se loguea en Trello y se busca el que se valide el nombre de Usuario :</br>
-- Abrir el navegador. </br>
-- Buscar Trello.</br>""")
#-- Entrar a la pagina de Inicio de Trello. </br>
#-- Escribir Usuario y Contraseña. </br>
#-- Hacer Click en boton de Iniciar Sesion. </br>
#-- Ir a la etiqueta Login. </br>
#-- Validar el nombre que debe corresponder.</br>""")

  
class tst_003(unittest.TestCase, Functions):

    def setUp(self):
        with allure.step(u'Abrir el navegador'):
            self.driver = self.abrir_Navegador("https://trello.com/login")

    def test_003(self):
        with allure.step(u'Buscar Trello'):
            TEXT = self.driver.find_element_by_xpath(Login.lbl_Titulo_xpath).text
            print (TEXT)

        self.assertEqual(u"Iniciar sesión en Trello", TEXT)
    
    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
