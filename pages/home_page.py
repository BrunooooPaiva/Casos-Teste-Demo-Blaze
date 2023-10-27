import conftest
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class HomePage (BasePage):

    def __init__(self):
        self.driver = conftest.driver
        self.product_store_title = (By.XPATH, "//a[@id='nava']")

    
    def verificar_se_esta_na_pagina_inicial(self):
        self.encontrar_elemento(self.product_store_title)