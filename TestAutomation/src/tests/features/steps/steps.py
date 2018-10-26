from behave import *


@given(u'Start web server')
def step_impl(context):
    print ('background - Web browser started')

@step('Ingresa a la aplicacion olderval')
def Login(context):
    pass


