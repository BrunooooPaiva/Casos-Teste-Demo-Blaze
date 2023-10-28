from asyncio import wait
import conftest
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class HomePage (BasePage):

    def __init__(self):
        self.driver = conftest.driver
        self.product_store_titulo = (By.XPATH, "//a[@id='nava']")
        self.botao_sign_up = (By.ID, "signin2")
        self.botao_log_in = (By.ID, "login2")
        self.nome_user = (By.ID, "nameofuser")

    
    def verificar_se_esta_na_pagina_inicial(self):
        self.encontrar_elemento(self.product_store_titulo)

    def clicar_no_botao_sign_up(self):
        self.clicar_no_elemento(self.botao_sign_up)

    def clicar_no_bota_log_in(self):
        self.clicar_no_elemento(self.botao_log_in)

    def verificar_se_foi_logado_corretamente(self):
        self.encontrar_elemento(self.nome_user)

    def encontrando_item_pelo_nome(self, text):
        self.item = "//*[@class='hrefch' and text()='"+text+"']"
        self.encontrando_item_pelo_nome(self.item)
    
