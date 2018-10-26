# -*- coding: utf-8 -*-

'''
Created on 29 sept. 2018


'''
from src.functions.Functions import Functions as Selenium
from src.pages.Login_oldelval import Login_oldelval
from src.pages.Menu_oldelval import MenuLateral
import pytest


class Menu(Selenium):

    def Menu_DuctosEInstalaciones_PuntoDeIngreso(self):
        # Ductos E ingresos ------> Punto de Ingreso
        
        print ("Ductos E ingresos ------> Punto de Ingreso")
        
        self.esperar_Xpath(MenuLateral.lbl_DuctosEinstalaciones_xpath)
        
        #self.Xpath_Elements(MenuLateral.lbl_DuctosEinstalaciones_xpath).click()
        #elf.Xpath_Elements(MenuLateral.lbl_Punto_de_ingreso).click()
        
        self.JS_Click_Xpath(MenuLateral.lbl_Punto_de_ingreso)
        
        self.waitStopLoad(8)
        
        self.get_image("Login Results")

        