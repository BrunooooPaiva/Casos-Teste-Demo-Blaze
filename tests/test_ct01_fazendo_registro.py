import pytest
from pages.home_page import HomePage


@pytest.mark.usefixtures("setup_teardown")
class TestCT01:

    def test_ct01_fazendo_registro(self):

        home_page = HomePage()


        home_page.verificar_se_esta_na_pagina_inicial()