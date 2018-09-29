
"###########################################################"
"#####                   NOMENCLATURA                   ###"
" TIPO DE CONTROL + NOMBRE DEL OBJETO + SELENIUM ELEMENT"
"########################################################"
# Label = lbl
# text = txt
# dropdown = dpd
# boton = btn
# checkbox= chk
# option buton = opt


class MenuLateral:
    ##############################
    ##########  Procesos #########
    ##############################
    lbl_procesos_xpath =  "//*[contains(@class, 'sidebar ng-scope')]//*[contains(text(),'Procesos')]"
    
    ##############################
    ##### Ductos E Instalaciones #
    ##############################

    lbl_DuctosEinstalaciones_xpath = "//*[contains(@class, 'sidebar ng-scope')]//*[contains(text(),'Ductos e instalaciones')]"
    
    ### Sub Menu
    
    lbl_Punto_de_ingreso =  "//*[contains(@class, 'sidebar ng-scope')]//*[contains(text(),'Puntos de Ingreso')]"

    lbl_Punto_de_ingreso =  "//*[contains(@class, 'sidebar ng-scope')]//*[contains(text(),'Puntos de Egreso')]"


#//*[contains(@class, 'sidebar ng-scope')]//*[contains(text(),'Empresas y')]

#//*[contains(@class, 'sidebar ng-scope')]//*[contains(text(),'metros')]

#//*[contains(@class, 'sidebar ng-scope')]//*[contains(text(),'Administraci')]