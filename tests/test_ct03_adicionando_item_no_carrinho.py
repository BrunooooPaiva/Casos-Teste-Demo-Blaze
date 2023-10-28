import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup_teardown")
class TestCT03:

    def test_ct03_adicionando_item_no_carrinho(self):
        
        home_page = HomePage()
        login_page = LoginPage()

        # Entrando no site pela primeira vez e confirmando se está na tela inicial
        home_page.verificar_se_esta_na_pagina_inicial()

        # Log in de usuário
        home_page.clicar_no_bota_log_in()

        # Verificando se está na tela de log in
        login_page.verificar_se_esta_na_tela_de_login()
        
        # Preenchendo os campos e fazendo log in
        login_page.preencher_campos_usuario_senha_e_clicar("teste1234567", "teste")

        # Verificando para ver se realmente foi feito o log in
        home_page.verificar_se_foi_logado_corretamente()

        home_page.encontrando_item_pelo_nome('Samsung galaxy s6')

