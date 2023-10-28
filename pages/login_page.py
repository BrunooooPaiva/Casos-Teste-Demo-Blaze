import conftest
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage (BasePage):

    def __init__(self):
        self.driver = conftest.driver
        self.titulo_log_in = (By.ID, "logInModalLabel")
        self.log_in_campo_usuario = (By.ID, "loginusername")
        self.log_in_campo_senha = (By.ID, "loginpassword")
        self.botao_log_in = (By.XPATH, "//button[text()='Log in']")

    def verificar_se_esta_na_tela_de_login(self):
        self.encontrar_elemento(self.titulo_log_in)

    def preencher_campos_usuario_senha_e_clicar(self, usuario, senha):
        self.preencher_campo(self.log_in_campo_usuario, usuario)
        self.preencher_campo(self.log_in_campo_senha, senha)
        self.clicar_no_elemento(self.botao_log_in)
        