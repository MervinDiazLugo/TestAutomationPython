# -*- coding: utf-8 -*-
'''
Created on 1 jul. 2018

@author: MMLPQTP
'''
import time, os, shutil, io, allure
from PIL import Image
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as Chrome_Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from src.functions.Inicializar import Inicializar
from selenium.webdriver.common.action_chains import ActionChains
import pytest

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
            print (u"esperar_Xpath: Se mostró el elemento " + XPATH)
            return True

        except TimeoutException:
            print (u"esperar_Xpath: No presente " + XPATH)
            return False
        
        
    
    def esperar_CSS(self, CSS):
        try:
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, CSS)))

        except TimeoutException:
            print (u"esperar_CSS: No presente " + CSS)
            return False
        
        print (u"esperar_CSS: Se mostró el elemento " + CSS)
        return True
    
    ##########################################################################
    ##############       -=_JS     CLICKS _=-              ###################
    ##########################################################################
         
         
    def JS_Click_Xpath(self, xpath):
        try:
            localizador = self.driver.find_element_by_xpath(xpath)
            self.driver.execute_script("arguments[0].click();", localizador)
            print ("JS_Click_Xpath: Se hizo click en: " +  xpath)
            return True
        
        except NoSuchElementException:
            print ("JS_Click_Xpath: No se encontro " +  xpath)
            return False
            
    def JS_Click_CSS(self, css):
        localizador = self.driver.find_element_by_css_selector(css)
        self.driver.execute_script("arguments[0].click();", localizador)
        
    ##########################################################################
    ##############   -=_JS     IR     A _=-                ###################
    ##########################################################################
    def ir_a_xpath(self, elemento):
        try:
            localizador = self.driver.find_element(By.XPATH, elemento)  
            self.driver.execute_script("arguments[0].scrollIntoView();", localizador)
            
        except TimeoutException:
            
            print (u"ir_a_xpath: No presente " + elemento)
            return False
        
        print (u"ir_a_xpath: Se desplazó al elemento, " + elemento)
        return True
    
    ##########################################################################
    ##############    -=_ACTION CHAINS _=-                ###################
    ##########################################################################
    def mouse_over_xpath(self, xpath):
        element = self.driver.find_element_by_xpath(xpath)
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()
        
    def mouse_over_css(self, css):
        element = self.driver.find_element_by_css_selector(css)
        action = ActionChains(self.driver)
        action.move_to_element(element).perform() 
  
    def verificar_xpath(self, xpath): #devuelve true o false
        try:
            self.driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            print (u"Verificar: Elemento No presente " + xpath)
            return False
        print (u"Verificar: Se visualizo el elemento, "+ xpath)
        return True      
    
    
    def verificar_CSS(self, CSS): #devuelve true o false
        try:
            self.driver.find_element_by_css_selector(CSS)
        except NoSuchElementException:
            print (u"Verificar: Elemento No presente " + CSS)
            return False
        print (u"Verificar: Se visualizo el elemento, "+ CSS)
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
    
    def get_image(self, Descripcion):
        IMAGEN = self.capturar_Pantalla()
        CAPTURA = Image.open(IMAGEN, mode="r")
        ImageProcess = io.BytesIO()
        CAPTURA.save(ImageProcess, format= "PNG")
        ImageProcess = ImageProcess.getvalue()
        allure.attach(ImageProcess, Descripcion, attachment_type=allure.attachment_type.PNG)
    
    def waitStopLoad(self, timeLoad=8):
        print ("waitStopLoad: Inicia")
        try:
                totalWait = 0
                while (totalWait < timeLoad):
                    print("Cargando ... intento: " + str(totalWait))
                    time.sleep(1)
                    totalWait = totalWait + 1
        except: 
            print ("waitStopLoad: Carga Finalizada ... ")
            
    def Modificar_XML_Enviroments(self):

        print ("--------------------------------------")
        print ("Estableciendo Datos del Reporte...")
        JOB_NAME = os.environ['JOB_NAME']
        NODE_NAME = os.environ['NODE_NAME']
        NAVEGADOR = Inicializar.NAVEGADOR
        print (NODE_NAME)
        print (JOB_NAME)
        print (NAVEGADOR)
        print ("--------------------------------------")

        Enviroment = open('../data/environment.xml', 'w')
        Template = open('../data/environment_Template.xml', 'r')
        
        with Template as f:
            texto = f.read()
            
            texto = texto.replace("JOB_NAME", JOB_NAME)
            texto = texto.replace("NODE_NAME", NODE_NAME)
            texto = texto.replace("NAVEGADOR", NAVEGADOR)
        
        with Enviroment as f:
            f.write(texto)
             
        Enviroment.close()    
        Template.close()

        time.sleep(5) 
        
        shutil.rmtree("../allure-results")
        
        try:
            os.makedirs("../allure-results")
        except OSError:
            print ("No se pudo generar la carpeta ../allure-results")
        
        shutil.copy("../data/environment.xml","../allure-results")           


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
            self.driver.get(Inicializar.URL)
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
            pytest.skip("Define el DRIVER")
            exit



