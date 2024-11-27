# pages.py

from selenium.webdriver.common.by import By
from helpers import wait_for_element, wait_for_clickable

class UrbanRoutesPage:
    def __init__(self, driver):
        self.driver = driver

    # Selectores
    from_input = (By.CSS_SELECTOR, "#from-input")
    to_input = (By.CSS_SELECTOR, "#to-input")
    request_taxi_button = (By.CSS_SELECTOR, "#request-taxi")
    comfort_tariff_button = (By.CSS_SELECTOR, ".comfort-tariff")
    phone_input = (By.CSS_SELECTOR, "#phone-input")
    credit_card_form = (By.CSS_SELECTOR, "#credit-card-form")
    confirmation_code_input = (By.CSS_SELECTOR, "#confirmation-code")
    message_input = (By.CSS_SELECTOR, "#driver-message")
    search_modal = (By.CSS_SELECTOR, "#search-modal")
    driver_info = (By.CSS_SELECTOR, "#driver-info")

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
        wait_for_clickable(self.driver, *self.comfort_tariff_button).click()

    def set_phone(self, phone_number):
        wait_for_element(self.driver, *self.phone_input).send_keys(phone_number)

    def phone_is_set(self):
        return self.driver.find_element(*self.phone_input).get_attribute("value") != ""

    def add_card(self, card_info):
        form = wait_for_element(self.driver, *self.credit_card_form)
        form.find_element(By.CSS_SELECTOR, "#card-number").send_keys(card_info["number"])
        form.find_element(By.CSS_SELECTOR, "#expiry-date").send_keys(card_info["expiry_date"])
        form.find_element(By.CSS_SELECTOR, "#cardholder-name").send_keys(card_info["cardholder_name"])
        form.find_element(By.CSS_SELECTOR, "#cvv").send_keys(card_info["cvv"])

    def card_is_added(self):
        return "Card added successfully" in self.driver.page_source

    def enter_confirmation_code(self, confirmation_code):
        wait_for_element(self.driver, *self.confirmation_code_input).send_keys(confirmation_code)

    def confirmation_is_valid(self):
        return "Code confirmed" in self.driver.page_source

    def write_drive_message(self, message):
        wait_for_element(self.driver, *self.message_input).send_keys(message)

    def get_driver_message(self):
        return self.driver.find_element(*self.message_input).get_attribute("value")

    def search_taxi(self):
        wait_for_clickable(self.driver, *self.search_modal).click()

    def search_modal_is_displayed(self):
        return self.driver.find_element(*self.search_modal).is_displayed()

    def wait_for_driver_info(self):
        return wait_for_element(self.driver, *self.driver_info).text
