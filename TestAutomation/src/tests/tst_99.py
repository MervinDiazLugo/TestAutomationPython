# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException 
from src.pages.Google import Home
import time, os, allure
from builtins import str


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

  
class tst_01(unittest.TestCase):

    def esperar_elemento(self, XPATH):
        try:
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.visibility_of_element_located((By.XPATH, XPATH)))
            print (u"esperar_Xpath: Se mostró el elemento " + XPATH)
            return True

        except TimeoutException:
            print (u"esperar_Xpath: No presente " + XPATH)
            return False
        
    def capturar_Pantalla(self):  
        def hora_Actual():
            hora = time.strftime("%H%M%S")
            return hora
        
        dia = time.strftime("%d-%m-%Y")
        
        GeneralPath = "C:\\Evidencias\\Python\\"
        DriverTest = "CHROME"
        TestCase = self.__class__.__name__
        horaAct = str(hora_Actual())
        
        path = GeneralPath + dia + "\\" + TestCase + "\\" + DriverTest + "\\" +  horaAct + "\\"
 
        if not os.path.exists(path): 
            os.makedirs(path)
 
        img = path + TestCase + "_(" + str(hora_Actual()) + ")" + ".png"
         
        self.driver.get_screenshot_as_file(img)
        
        print (img)
         
        return img  
    
    def setUp(self):
        with allure.step(u'Abrir el navegador'):  
            self.driver = webdriver.Chrome()
            self.driver.implicitly_wait(30)
                 
    def test_01(self):
        with allure.step(u'Paso 2 Buscar "RAET"'):
            driver = self.driver
            driver.get("https://www.google.com/")
            
        
            
            btn_Busque_apath = "//*[@id='tsf']/div[2]/div[3]/center/input[1]"
            
            txt_resultado_xpath = "//*[@id='resultStats']"
            
            driver.find_element_by_xpath("//*[@id='lst-ib']").send_keys("RAET")
            self.capturar_Pantalla()
            driver.find_element_by_xpath("//*[@id='lst-ib']").send_keys(Keys.ENTER)
            self.esperar_elemento(txt_resultado_xpath)
            self.capturar_Pantalla()
            
        with allure.step(u'PASO 3: Verificar los resultados de busqueda'): 
               
            Resultados = driver.find_element_by_xpath(txt_resultado_xpath).text
            print (Resultados)
            RAET = Resultados.split(" ")[2]
            print ("RAET obtuvo: " + str(RAET) + " Resultados de busqueda")
            
            if (RAET > 10000):
                print ("RAET obtuvo mucho")
    
            
    def tearDown(self):
        with allure.step(u'PASO 4: Cerrar Navegador'):
            self.driver.quit()


if __name__ == "__main__":
    unittest.main()
            
    
