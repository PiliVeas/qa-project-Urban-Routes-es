from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  # Importar WebDriverWait
from selenium.webdriver.support import expected_conditions as EC  # Importar expected_conditions
from helpers import wait_for_element, wait_for_clickable
from selenium.webdriver.common.keys import Keys  # Para manejar teclas como BACKSPACE

class UrbanRoutesPage:
    def __init__(self, driver):
        self.driver = driver
        
    # Selectores
    from_input = (By.CSS_SELECTOR, "#from.input")
    to_input = (By.CSS_SELECTOR, "#to.input")
    request_taxi_button = (By.XPATH, "//button[text()='Pedir un taxi']")
    comfort_tariff_button = (By.XPATH, "//button[text()='Comfort']")
    phone_modal_button = (By.XPATH, "//div[contains(text(), 'Número de teléfono')]")  # Div que abre el modal
    phone_input = (By.CSS_SELECTOR, "#phone")  # Campo de entrada de teléfono
    next_button = (By.XPATH, "//button[text()='Siguiente']")  # Botón "Siguiente" en el modal
    credit_card_form = (By.CSS_SELECTOR, "#credit-card-form")
    message_input = (By.CSS_SELECTOR, "#driver-message")
    driver_info = (By.CSS_SELECTOR, "#driver-info")
    blanket_and_tissues_toggle = (By.CSS_SELECTOR, "#request-blanket-and-tissues-toggle") 
    ice_cream_counter_label = (By.CSS_SELECTOR, ".r-counter-label")
    ice_cream_counter_plus = (By.CSS_SELECTOR, ".counter-plus")
    search_modal = (By.CSS_SELECTOR, "#search-modal")


    # Métodos
    def set_route(self, address_from, address_to):
        wait_for_element(self.driver, *self.from_input).send_keys(address_from)
        wait_for_element(self.driver, *self.to_input).send_keys(address_to)

    def get_from(self):
        return self.driver.find_element(*self.from_input).get_attribute("value")

    def get_to(self):
        return self.driver.find_element(*self.to_input).get_attribute("value")

    def click_on_request_taxi(self):
        wait_for_clickable(self.driver, *self.request_taxi_button).click()
def click_on_comfort_tariff(self):
        comfort_tariff_button = "//div[contains(text(), 'Comfort')]"
        wait_for_clickable(self.driver, By.XPATH, comfort_tariff_button).click()

    def get_selected_tariff(self):
        tariff_element = self.driver.find_element(By.XPATH, "//div[contains(text(), 'Comfort')]")
        return tariff_element.text

    def click_to_open_phone_modal(self):
        open_phone_modal_xpath = "//div[contains(@class, 'np-text') and text()='Número de teléfono']"
        open_phone_modal = wait_for_element(self.driver, By.XPATH, open_phone_modal_xpath)
        open_phone_modal.click()

    def set_phone_number(self, phone_number):
        phone_input_xpath = "//input[@id='phone']"
        phone_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, phone_input_xpath)),
            message="El campo de entrada para el número de teléfono no es visible"
        )
        phone_input.clear()
        phone_input.send_keys(phone_number)

    def get_phone_number(self):
        return self.driver.find_element(By.CSS_SELECTOR, "#phone").get_attribute("value")

    def add_card(self, card_info):
        payment_method_button_xpath = "//div[@class='pp-text' and text()='Método de pago']"
        payment_button = wait_for_clickable(self.driver, By.XPATH, payment_method_button_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", payment_button)
        payment_button.click()
        add_card_button_xpath = "//div[contains(@class, 'pp-title') and text()='Agregar tarjeta']"
        add_card_button = wait_for_clickable(self.driver, By.XPATH, add_card_button_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", add_card_button)
        add_card_button.click()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='modal']")),
            message="La ventana emergente no es visible"
        )
        card_number_input_xpath = "//input[@id='number']"
        card_number_input = wait_for_element(self.driver, By.XPATH, card_number_input_xpath)
        card_number_input.clear()
        card_number_input.send_keys(Keys.BACKSPACE * len(card_number_input.get_attribute("value")))
        card_number_input.send_keys(card_info["number"].replace(" ", ""))
        card_code_input_xpath = "//input[@id='code']"
        card_code_input = wait_for_element(self.driver, By.XPATH, card_code_input_xpath)
        card_code_input.clear()
        card_code_input.send_keys(Keys.BACKSPACE * len(card_code_input.get_attribute("value")))
        card_code_input.send_keys(card_info["cvv"])
        add_button_xpath = "//button[contains(@class, 'button full') and text()='Agregar']"
        add_button = wait_for_clickable(self.driver, By.XPATH, add_button_xpath)
        add_button.click()

def card_is_added(self):
        success_message_xpath = "//div[contains(text(), 'Tarjeta añadida con éxito')]"
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, success_message_xpath))
        )

    def write_message_to_driver(self, message):
        message_input_xpath = "//textarea[@id='comment']"
        message_input = wait_for_element(self.driver, By.XPATH, message_input_xpath, timeout=10)
        message_input.clear()
        message_input.send_keys(message)

    def get_driver_message(self):
        return self.driver.find_element(*self.message_input).get_attribute("value")


    def toggle_blanket_and_tissues(self):
        toggle_element = wait_for_element(self.driver, *self.blanket_and_tissues_toggle)
        if "checked" not in toggle_element.get_attribute("outerHTML"):
            toggle_element.click()

   
    def is_blanket_and_tissues_requested(self):
        toggle_element = wait_for_element(self.driver, *self.blanket_and_tissues_toggle)
        return "checked" in toggle_element.get_attribute("outerHTML")
    

    def request_ice_cream(self, quantity):
        for _ in range(quantity):
            wait_for_clickable(self.driver, *self.ice_cream_counter_plus).click()
            
    def get_ice_cream_quantity(self):
        ice_cream_count_element = wait_for_element(self.driver, *self.ice_cream_counter_label)
        return int(ice_cream_count_element.text)  


    def search_taxi(self):
        wait_for_clickable(self.driver, *self.search_modal).click()

    def search_modal_is_displayed(self):
        return self.driver.find_element(*self.search_modal).is_displayed()



