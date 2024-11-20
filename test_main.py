# test_main.py

import time
from selenium import webdriver
from pages import UrbanRoutesPage
import data

class TestUrbanRoutes:
    def setup_method(self):
        """Configura el entorno antes de cada prueba."""
        self.driver = webdriver.Chrome()
        self.driver.get(data.urban_routes_url)
        self.routes_page = UrbanRoutesPage(self.driver)

    def teardown_method(self):
        """Cierra el navegador después de cada prueba."""
        self.driver.quit()

    # Prueba 1 - Configurar la dirección
    def test_set_route(self):
        address_from = data.address_from
        address_to = data.address_to
        self.routes_page.set_route(address_from, address_to)
        assert self.routes_page.get_from() == address_from
        assert self.routes_page.get_to() == address_to

    # Prueba 2 - Seleccionar la tarifa Comfort
    def test_select_comfort_tariff(self):
        self.test_set_route()
        self.routes_page.click_on_request_taxi()
        self.routes_page.click_on_comfort_tariff()
        time.sleep(3)  # Para simular la espera de la selección de tarifa
        assert self.routes_page.get_selected_tariff() == "Comfort"

    # Prueba 3 - Rellenar el número de teléfono
    def test_set_phone(self):
        self.test_set_route()
        self.routes_page.set_phone()
        time.sleep(1)  # Simula el tiempo para completar la acción
        assert self.routes_page.phone_is_set()  # Método que verifica si el teléfono fue configurado

    # Prueba 4 - Agregar una tarjeta de crédito
    def test_add_card(self):
        self.test_set_route()
        self.routes_page.add_card()
        assert self.routes_page.card_is_added()  # Verifica que la tarjeta fue añadida correctamente

    # Prueba 5 - Código de confirmación para agregar tarjeta
    def test_card_confirmation_code(self):
        self.test_add_card()
        self.routes_page.enter_confirmation_code()
        assert self.routes_page.confirmation_is_valid()  # Verifica si el código es aceptado

    # Prueba 6 - Escribir un mensaje para el conductor
    def test_write_message_to_driver(self):
        self.test_set_route()
        message = data.message_for_driver
        self.routes_page.write_drive_message(message)
        assert self.routes_page.get_driver_message() == message

    # Prueba 7 - Pedir una manta y pañuelos
    def test_request_blanket_and_tissues(self):
        self.test_set_route()
        self.routes_page.request_blanket_and_tissues()
        assert self.routes_page.blanket_and_tissues_requested()  # Verifica que se realizó la solicitud

    # Prueba 8 - Pedir 2 helados
    def test_request_ice_cream(self):
        self.test_set_route()
        self.routes_page.request_ice_cream(quantity=2)
        assert self.routes_page.get_ice_cream_quantity() == 2

    # Prueba 9 - Aparece el modal para buscar un taxi
    def test_search_taxi_modal(self):
        self.test_set_route()
        self.routes_page.search_taxi()
        assert self.routes_page.search_modal_is_displayed()  # Verifica que el modal aparece

    # Prueba 10 - Esperar información del conductor
    def test_wait_for_driver_info(self):
        self.test_search_taxi_modal()
        driver_info = self.routes_page.wait_for_driver_info()
        assert driver_info is not None  # Verifica que se recibe la información del conductor
