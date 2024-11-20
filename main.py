# main.py

from selenium import webdriver
from pages import UrbanRoutesPage
import data

def main():
    # Configuración inicial del navegador
    driver = webdriver.Chrome()

    # Navegar a la URL principal
    driver.get(data.urban_routes_url)

    # Crear una instancia de la página
    routes_page = UrbanRoutesPage(driver)


 class TestUrbanRoutes:
    def setup_method(self):
        # Configura el entorno antes de cada prueba
        self.driver = webdriver.Chrome()
        self.driver.get(data.urban_routes_url)
        self.routes_page = UrbanRoutesPage(self.driver)

    def teardown_method(self):
        # Cierra el navegador después de cada prueba
        self.driver.quit()



# Prueba 1 - Configura la dirección
def test_set_route(self):
    self.driver.get(data.urban_routes_url) 
    self.routes_page = UrbanRoutesPage(self.driver)
    address_from = data.addres_from
    address_to = data.address_to
    self.routes_page.set_route(address_from, address_to)
    assert self.routes_page.get_from() == address_from
    assert self.routes_page.get_to() == address_to

# Prueba 2 - Selecciona la tarifa comfort y pide un taxi
def test_select_comfort_tariff(self):
    self.test_set_route() 
    self.routes_page.click_on_request_taxi()
    self.routes_page.click_on_comfort_tariff()
    time.sleep(3)
    assert self.routes_page.get_selected_tariff() == "Comfort"

# Prueba 3 - Rellenar el número de teléfono
def test_set_phone(self):
    self.test_select_comfort_tariff()  # Hereda configuración previa
    self.routes_page.set_phone()
    time.sleep(1)  # Simula el tiempo para completar la acción
    assert self.routes_page.phone_is_set()  # Método que verifica si el teléfono fue configurado

# Prueba 4 - Agregar una tarjeta de crédito
def test_add_card(self):
    self.test_set_phone()  # Hereda configuración previa
    self.routes_page.add_card()
    assert self.routes_page.card_is_added()  # Verifica que la tarjeta fue añadida correctamente

# Prueba 5 - Código de confirmación para agregar tarjeta
def test_card_confirmation_code(self):
    self.test_add_card()  # Hereda configuración previa
    self.routes_page.enter_confirmation_code()
    assert self.routes_page.confirmation_is_valid()  # Verifica si el código es aceptado

# Prueba 6 - Escribir un mensaje para el conductor
def test_write_message_to_driver(self):
    self.test_card_confirmation_code()  # Hereda configuración previa
    message = data.message_Ffor_driver
    self.routes_page.write_drive_message(message)
    assert self.routes_page.get_driver_message() == message

# Prueba 7 - Pedir una manta y pañuelos
def test_request_blanket_and_tissues(self):
    self.test_write_message_to_driver()  # Hereda configuración previa
    self.routes_page.request_blanket_and_tissues()
    assert self.routes_page.blanket_and_tissues_requested()  # Verifica que se realizó la solicitud

# Prueba 8 - Pedir 2 helados
def test_request_ice_cream(self):
    self.test_request_blanket_and_tissues()  # Hereda configuración previa
    self.routes_page.request_ice_cream(quantity=2)
    assert self.routes_page.get_ice_cream_quantity() == 2

# Prueba 9 - Aparece el modal para buscar un taxi
def test_search_taxi_modal(self):
    self.test_request_ice_cream()  # Hereda configuración previa
    self.routes_page.search_taxi()
    assert self.routes_page.search_modal_is_displayed()  # Verifica que el modal aparece

# Prueba 10 - Esperar información del conductor
def test_wait_for_driver_info(self):
    self.test_search_taxi_modal()  # Hereda configuración previa
    driver_info = self.routes_page.wait_for_driver_info()
    assert driver_info is not None  # Verifica que se recibe la información del conductor








     
    # Cerrar el navegador
    driver.quit()

if __name__ == "__main__":
    main()
