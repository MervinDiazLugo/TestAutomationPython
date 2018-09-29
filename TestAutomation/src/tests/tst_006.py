# -*- coding: utf-8 -*-
import unittest, time
from src.functions.Functions import Functions

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
            self.driver = self.abrir_Navegador("http://oldelval.practia.global/")
    

    def test_006_B(self):

            
        arreglo = self.driver.find_elements_by_xpath("(//div[contains(@class, 'login-box')]//*[contains(@id,'txt')])")
        datos = ["User1" , "123456"]
        i = 0
        for txts in arreglo:
            txts.send_keys(datos[i])
            i = ++1
        
        self.Xpath_Elements("(//div[contains(@class, 'login-box')]//*[contains(text(),'Ingresar')])").click()
        
        self.get_image("HOLA")
        time.sleep(5)
            

    
    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
