import pytest
from pages.home_page import HomePage
from pages.formulario_registro import FormularioRegistro


@pytest.mark.usefixtures("setup_teardown")
class TestCT01:

    def test_ct01_fazendo_registro(self):

        home_page = HomePage()
        formulario_registro = FormularioRegistro()


        # Entrando no site pela primeira vez e confirmando se está na tela inicial
        home_page.verificar_se_esta_na_pagina_inicial()

        # Cadastro de usuário
        home_page.clicar_no_botao_sign_up()

        # Preenchendo os campos do formulário de registro 
        formulario_registro.verificar_se_esta_na_pagina_de_registro()
        formulario_registro.preencher_campo_usuario_senha_e_clicar("teste1234567", "teste")

        # Verificando se deu certo o registro ao voltar para a tela inicial novamente
        home_page.verificar_se_esta_na_pagina_inicial()