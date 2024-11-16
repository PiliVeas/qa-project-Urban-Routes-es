# pages.py

from selenium.webdriver.common.by import By
from helpers import retrieve_phone_code  

class UrbanRoutesPage:
    # Localizadores
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    taxi_button = (By.CLASS_NAME, "button round")
    code = (By.ID, 'code')
    next_button = (By.XPATH, '//*[text()="Siguiente"]')
    # Agrega el resto de los localizadores aquí...

    def __init__(self, driver):
        self.driver = driver

    # Métodos relacionados con las páginas
    def set_from(self, from_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def set_route(self, from_address, to_address):
        self.set_from(from_address)
        self.set_to(to_address)

    def code_number(self):
        """Solicita el código de confirmación y lo ingresa en el campo correspondiente."""
        phone_code = retrieve_phone_code(driver=self.driver)
        self.driver.find_element(*self.code).send_keys(phone_code)

    def click_next(self):
        self.driver.find_element(*self.next_button).click()

    
