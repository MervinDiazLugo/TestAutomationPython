# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException 
import time, os, allure
from builtins import str


@allure.feature(u'Google')
@allure.story(u'001: Verificar  RAET in google')
@allure.testcase(u'Caso de Prueba tst_01')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(u"""The PO gives us the following specification:</br>
El resultado de buqueda sea mayor a 10000  </br>

1- Ingresar a https://www.google.com. </br>
2- Ingresar RAET el la barra de busqueda y tomar capturas</br>
3- Verficar los resultados  </br>
4- Cerrar Navegador </br>
 </br></br>""")
  
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
        
        GeneralPath = "C:\\Evidencias\\Python\\" #Directorio de las Capturas#
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
        with allure.step(u'Paso 2 Ingresar RAET el la barra de busqueda"'):
            driver = self.driver
            driver.get("https://www.google.com/")
            
        ################### XPATH A UTLIZAR ############################
        
            txt_busqueda_xpath  =  "//*[@id='lst-ib']"
            txt_resultado_xpath = "//*[@id='resultStats']"
                      
            driver.find_element_by_xpath(txt_busqueda_xpath).send_keys("RAET")
            self.capturar_Pantalla()
            driver.find_element_by_xpath(txt_busqueda_xpath).send_keys(Keys.ENTER)
            self.esperar_elemento(txt_resultado_xpath)
            self.capturar_Pantalla()
            
        with allure.step(u'PASO 3: Verificar los resultados de busqueda'): 
               
            Resultado = driver.find_element_by_xpath(txt_resultado_xpath).text
            print (Resultado)
            RAET = Resultado.split(" ")[2]
            print ("RAET obtuvo: " + str(RAET) + " Resultados de busqueda")
            
            
    def tearDown(self):
        with allure.step(u'PASO 4: Cerrar Navegador'):
            self.driver.quit()


if __name__ == "__main__":
    unittest.main()
            
    
