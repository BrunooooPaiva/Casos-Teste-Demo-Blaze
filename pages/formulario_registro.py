import conftest
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class FormularioRegistro (BasePage):

    def __init__(self):
        self.driver = conftest.driver
        self.titulo_sign_up = (By.ID, "signInModalLabel")
        self.registro_campo_usuario = (By.ID, "sign-username")
        self.registro_campo_senha = (By.ID, "sign-password")
        self.botao_registro = (By.XPATH, "//button[text()='Sign up']")

    def verificar_se_esta_na_pagina_de_registro(self):
        self.encontrar_elemento(self.titulo_sign_up)

    def preencher_campo_usuario_senha_e_clicar(self, usuario, senha):
        self.preencher_campo(self.registro_campo_usuario, usuario)
        self.preencher_campo(self.registro_campo_senha, senha)
        self.clicar_no_elemento(self.botao_registro)
    