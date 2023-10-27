import conftest


class BasePage:

    def __init__(self):
        self.driver = conftest.driver


    def encontrar_elemento(self, locator):
        return self.driver.find_element(*locator)

    def encontrar_elementos(self, locator):
        return self.driver.find_elements(*locator)