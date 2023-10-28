import conftest


class BasePage:

    def __init__(self):
        self.driver = conftest.driver


    def encontrar_elemento(self, locator):
        return self.driver.find_element(*locator)

    def encontrar_elementos(self, locator):
        return self.driver.find_elements(*locator)
    
    def clicar_no_elemento(self, locator):
        self.encontrar_elemento(locator).click()

    def preencher_campo(self, locator, text):
        self.encontrar_elemento(locator).send_keys(text)
    
    def encontrar_elemento_texto(self, locator):
        self.driver.find_elements_by_xpath(locator)