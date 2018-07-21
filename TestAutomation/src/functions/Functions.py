# -*- coding: utf-8 -*-
'''
Created on 1 jul. 2018

@author: MMLPQTP
'''
import time, os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as Chrome_Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from src.functions.Inicializar import Inicializar
<<<<<<< HEAD
     ####branch temp
=======
from selenium.webdriver.common.action_chains import ActionChains

>>>>>>> branch 'master' of https://github.com/MervinDiazLugo/TestAutomationPython.git

class Functions():

    def Xpath_Elements(self, XPATH):
        elements = self.driver.find_element_by_xpath(XPATH)
        print ("Xpath_Elements: Se interactuo con el elemento " + XPATH)
        return elements
        
    def ID_Elements(self, ID):
        elements = self.driver.find_element_by_id(ID)
        print ("Xpath_Elements: Se interactuo con el elemento " + ID)
        return elements

    def esperar_Xpath(self, XPATH): #Esperar que un elemento sea visible 
        try:
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.visibility_of_element_located((By.XPATH, XPATH)))

        except TimeoutException:
            print (u"esperar_Xpath: No presente " + XPATH)
            return False
        
        print (u"esperar_Xpath: Se mostró el elemento " + XPATH)
        return True
    
    def esperar_CSS(self, CSS):
        try:
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, CSS)))

        except TimeoutException:
            print (u"esperar_CSS: No presente " + CSS)
            return False
        
        print (u"esperar_CSS: Se mostró el elemento " + CSS)
        return True
            
    ##############   -=_CAPTURA DE PANTALLA_=-   #############################
    ##########################################################################        
    def capturar_Pantalla(self):  
        def hora_Actual():
            hora = time.strftime("%H%M%S")  # formato 24 houras
            return hora
        
        dia = time.strftime("%d-%m-%Y")  # formato aaaa/mm/dd
        
        GeneralPath = Inicializar.Path_Evidencias
        DriverTest = Inicializar.NAVEGADOR
        TestCase = self.__class__.__name__
        horaAct = str(hora_Actual())
        
        path = GeneralPath + dia + "\\" + TestCase + "\\" + DriverTest + "\\" +  horaAct + "\\"
 
        if not os.path.exists(path): # si no existe el directorio lo crea
 
            os.makedirs(path)
 
        img = path + TestCase + "_(" + str(hora_Actual()) + ")" + ".png"
         
        self.driver.get_screenshot_as_file(img)
        
        print (img)
         
        return img  
    
    
    ##########################################################################
    ##############   -=_INICIALIZAR DRIVERS_=-   #############################
    ##########################################################################

    def abrir_Navegador(self):
        navegador = Inicializar.NAVEGADOR
        print ("----------------")
        print (navegador)
        print ("---------------")
        
        if navegador == ("CHROME"):
            
            options = Chrome_Options()
            options.add_argument('--start-maximized')
            self.driver = webdriver.Chrome(chrome_options=options)
            self.driver.implicitly_wait(10)
            self.dir_navegador = "CHROME"
            self.driver.get( Inicializar.URL)
            return self.driver
        
        if navegador == ("CHROME_headless"):
            
            options = Chrome_Options()
            options.add_argument('headless')
            options.add_argument('--start-maximized')
            options.add_argument('--lang=es')
            self.driver = webdriver.Chrome(chrome_options=options)
            self.driver.implicitly_wait(10)
            self.dir_navegador = "CHROME Headless"
            self.driver.get( Inicializar.URL)
            return self.driver
        
        if navegador == ("FIREFOX"):
            opts = FirefoxOptions()
            opts.set_preference("intl.accept_languages", "es") 

            self.driver = webdriver.Firefox()

            self.driver.implicitly_wait(10)
            self.dir_navegador = "FIREFOX"
            self.driver.get( Inicializar.URL)
            return self.driver 
        
        elif navegador != ("CHROME_headless") and  navegador != ("CHROME") and navegador != ("FIREFOX") :
            print ("----------------")
            print ("Define bien el DRIVER")
            print ("----------------")
            
        ################## codigo negro #######################
         
         
    def JS_Click_Xpath(self, xpath):
        localizador = self.driver.find_element_by_xpath(xpath)
        self.driver.execute_script("arguments[0].click();", localizador)
    
    def JS_Click_CSS(self, css):
        localizador = self.driver.find_element_by_css_selector(css)
        self.driver.execute_script("arguments[0].click();", localizador)
        
        ####################################
    