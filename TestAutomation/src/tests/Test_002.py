# -*- coding: utf-8 -*-
from selenium import webdriver as selenium
from selenium.webdriver.support.ui import Select  
import unittest, time


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = selenium.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.migraciones.gov.ar/turnos/verificar_jurisdiccion.php"
        self.driver.get(self.base_url)
    
    def test_untitled_test_case(self):
        
        Selec= Select(self.driver.find_element_by_xpath("//*[@id='tipo_turno']"))
        
        Selec.select_by_index(1)
        
        time.sleep(3)
        
        Selec.select_by_value("998")
        
        time.sleep(3)
        
        Selec.select_by_visible_text("PRORROGA DE RESIDENCIA")
        
        time.sleep(3)
        
        self.driver.find_element_by_xpath("//*[@id='tipo_turno']").click()
        self.driver.find_element_by_xpath("//*[@id='tipo_turno']/option[3]").click()
        
        time.sleep(3)
        
#         texto = self.driver.find_element_by_xpath("(//*[contains(@id,'mega-bottombar')])").text
#         print (texto)
#         
#         texto = self.driver.find_element_by_xpath("(//*[contains(@id,'mega-bottombar')])").text
#         
#         self.driver.find_element_by_id("uh-search-box").click()
#         self.driver.find_element_by_id("uh-search-box").clear()
#         self.driver.find_element_by_id("uh-search-box").send_keys("messí")
#         time.sleep(5)
#         print ("MESSI NO MARCÓ")
        
#         driver.find_element_by_id("yui_3_18_0_3_1529178871710_1706").click()
#         driver.find_element_by_id("yui_3_10_0_1_1529179287859_800").click()
#         try: self.assertEqual("Lionel Messi", driver.find_element_by_id("yui_3_10_0_1_1529179287859_915").text)
#         except AssertionError as e: self.verificationErrors.append(str(e))
    

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()