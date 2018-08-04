# -*- coding: utf-8 -*-
import unittest
import allure
import pytest
from src.functions.Functions import Functions
from src.functions.Inicializar import Inicializar
from src.pages.Mercadolibre import Mercadolibre
  
@allure.feature(u' Mercado libre productos Damas, Descargar App para Android')
@allure.story(u' VER PRODUCTOS DE DAMAS, DESCARGA DE APP')
@allure.testcase(u'')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(u"""
  --TEST 1 </br> 
  - Abrir Mercdolibre.com </br>
  --Desplegar Lista de Categoria </br>
  --Seleccionar Categoria Moda </br>
  --Ver en Pantalla Productos de Damas </br>
  --TEST 2 </br>
  --Seleccionar Boton Descarga Aplicacion </br>
  --Ir a la pantalla para Descargar APP </br>
  
  """)
class tst_005(unittest.TestCase, Functions):

    def setUp(self):
        with allure.step(u'VER PRODUCTOS DE DAMAS, DESCARGA DE APP')
        self.driver = self.abrir_Navegador()
        self.driver.get(Inicializar.URL2)

    def test_005_A(self):
        with allure.step(u'Ver en Pantalla Productos de Damas')
            self.waitStopLoad(5)
            self.esperar_Xpath(Mercadolibre.btn_DescargaAplicacion_xpath)
        
            self.mouse_over_xpath(Mercadolibre.lbl_Categoria_xpath)
        
            self.JS_Click_Xpath(Mercadolibre.lbl_Moda_xpath)
        
            self.waitStopLoad(3)
            self.esperar_Xpath(Mercadolibre.lbl_Mujers_xpath)
        
            self.capturar_Pantalla()
        


    def test_005_B(self):
        with allure.step(u'Ir a la pantalla para Descargar APP')
            self.esperar_Xpath(Mercadolibre.btn_DescargaAplicacion_xpath)
        
            self.JS_Click_Xpath(Mercadolibre.btn_DescargaAplicacion_xpath)
            self.waitStopLoad(5)
            self.esperar_Xpath(Mercadolibre.btn_Android_xpath)
        
            self.capturar_Pantalla()
    

    
    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
