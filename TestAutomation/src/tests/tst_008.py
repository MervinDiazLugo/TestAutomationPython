# -*- coding: utf-8 -*-
import unittest
from src.functions.Functions import Functions
from src.parts.Login import Login 
from src.parts.Menu import Menu

import allure


@allure.feature(u'Login Oldelval')
@allure.story(u'008: Loguearse exitosamente en la aplicación')
@allure.testcase(u"Caso de Prueba 008", u'http://my.tms.org/browse/TESTCASE-39')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(u"""El Usuario se loguea en la aplicación:</br>
-- Ingresa a pantralla de inicio. </br>
-- Ingresa un usuario valido. </br>
-- Ingresa una contraseña correcta. </br>
""")
class tst_008(unittest.TestCase,Login, Menu, Functions):

    def setUp(self):
        with allure.step(u'Ingresar a la aplicación'):
            self.driver = self.abrir_Navegador("http://oldelval.practia.global/")
            self.User = self.LeerCelda('A1')
            self.Password = self.LeerCelda('B1')

    def test_008(self):
        with allure.step(u"Se loguea en la aplicacion"):
            self.Login_app()
            
        with allure.step(u"Ductos E ingresos ------> Punto de Ingreso"):
            self.Menu_DuctosEInstalaciones_PuntoDeIngreso()
            
    
    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
