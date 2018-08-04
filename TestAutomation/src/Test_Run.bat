cd C:\Framework\Workspace\TestAutomation\src\tests
SET PATH=%PATH%;%PYTHONPATH%;

@echo off 
echo. ##################### PRUEBAS #####################

C:\Framework\Python36\python.exe -m pytest tst_006.py --alluredir ..\allure-results

pause
