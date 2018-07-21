# -*- coding: utf-8 -*-
import unittest

from src.functions.Functions import Functions
from src.functions.Inicializar import Inicializar
from src.pages.Mercadolibre import Mercadolibre
  
class tst_006(unittest.TestCase, Functions):

    def setUp(self):
        self.driver = self.abrir_Navegador()
        self.driver.get(Inicializar.URL2)


    def test_006_B(self):
        self.esperar_Xpath(Mercadolibre.btn_DescargaAplicacion_xpath)
        
        self.JS_Click_Xpath(Mercadolibre.btn_DescargaAplicacion_xpath)
        
        self.waitStopLoad(5)
        self.esperar_Xpath(Mercadolibre.btn_Android_xpath)
        
        VERIFICAR = self.verificar_xpath(Mercadolibre.btn_Android_xpath)
        
        print ("El elemento esta presente: " + str(VERIFICAR))
        
        self.assertTrue(VERIFICAR)
 
        
        self.capturar_Pantalla()
    

    
    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
