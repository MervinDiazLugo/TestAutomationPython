# -*- coding: utf-8 -*-
import unittest, time

from src.functions.Functions import Functions
from src.functions.Inicializar import Inicializar
from src.pages.Mercadolibre import Mercadolibre
  
class tst_005(unittest.TestCase, Functions):

    def setUp(self):
        self.driver = self.abrir_Navegador()
        self.driver.get(Inicializar.URL2)

    def test_005_A(self):
        self.waitStopLoad(5)
        self.esperar_Xpath(Mercadolibre.btn_DescargaAplicacion_xpath)
        
        self.mouse_over_xpath(Mercadolibre.lbl_Categoria_xpath)
        
        self.JS_Click_Xpath(Mercadolibre.lbl_Moda_xpath)
        
        self.waitStopLoad(3)
        self.esperar_Xpath(Mercadolibre.lbl_Mujers_xpath)
        
        self.capturar_Pantalla()
        


    def test_005_B(self):
        self.esperar_Xpath(Mercadolibre.btn_DescargaAplicacion_xpath)
        
        self.JS_Click_Xpath(Mercadolibre.btn_DescargaAplicacion_xpath)
        
        self.waitStopLoad(5)
        self.esperar_Xpath(Mercadolibre.btn_Android_xpath)
        
        self.capturar_Pantalla()
    

    
    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
