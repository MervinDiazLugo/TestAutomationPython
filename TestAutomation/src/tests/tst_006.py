# -*- coding: utf-8 -*-
import unittest
from src.functions.Functions import Functions
from src.functions.Inicializar import Inicializar
from src.pages.Mercadolibre import Mercadolibre

import allure


@allure.feature(u'Google Play')
@allure.story(u'001: verify query results for RAET in google')
@allure.testcase(u"Caso de Prueba 00001", u'http://my.tms.org/browse/TESTCASE-39')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(u"""The PO gives us the following specification:</br>
-- Abrir trello. </br>
-- Abrir trello. </br>
-- Abrir trello. </br>
""")
class tst_006(unittest.TestCase, Functions):

    def setUp(self):
        with allure.step(u'Ingresar a la aplicación'):
            self.driver = self.abrir_Navegador()
            self.driver.get(Inicializar.URL2)
    

    def test_006_B(self):
        with allure.step(u'Clicquear en el boton de descarga de aplicacion Google play'):
            self.esperar_Xpath(Mercadolibre.btn_DescargaAplicacion_xpath)
            
            self.JS_Click_Xpath(Mercadolibre.btn_DescargaAplicacion_xpath)
            
            self.waitStopLoad(5)
            self.esperar_Xpath(Mercadolibre.btn_Android_xpath)
            
            
        with allure.step(u'Verificar que se muestre el boton'):   
            VERIFICAR = self.verificar_xpath(Mercadolibre.btn_Android_xpath)
            
            print ("El elemento esta presente: " + str(VERIFICAR))
            
            self.assertTrue(VERIFICAR)
     
            self.capturar_Pantalla()
        

    
    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
