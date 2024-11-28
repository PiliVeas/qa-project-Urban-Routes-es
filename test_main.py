import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages import UrbanRoutesPage
import data

# Configuración automática del navegador
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(data.urban_routes_url)
    yield driver  # Devuelve el navegador para las pruebas
    driver.quit()  # Cierra el navegador al finalizar

# Página de rutas urbanas
@pytest.fixture
def routes_page(driver):
    return UrbanRoutesPage(driver)

# Prueba 1: Configura la dirección
def test_set_route(routes_page):
    address_from = data.address_from
    address_to = data.address_to
    routes_page.set_route(address_from, address_to)

    # Verifica que las direcciones se configuren correctamente
    assert routes_page.get_from() == address_from
    assert routes_page.get_to() == address_to
    print("¡Ruta configurada correctamente!")

# Prueba 2: Selecciona la tarifa "Comfort"
def test_select_comfort_tariff(routes_page):
    routes_page.set_route(data.address_from, data.address_to)
    routes_page.click_on_request_taxi()
    routes_page.click_on_comfort_tariff()
    assert routes_page.get_selected_tariff() == "Comfort"
    print("¡Tarifa Comfort seleccionada!")

# Prueba 3: Configura el número de teléfono
def test_set_phone(routes_page):
    routes_page.set_route(data.address_from, data.address_to)
    routes_page.click_on_request_taxi()
    routes_page.click_on_comfort_tariff()
    routes_page.click_to_open_phone_modal()
    routes_page.set_phone_number(data.phone_number)
    assert routes_page.get_phone_number() == data.phone_number
    print("¡Teléfono configurado correctamente!")

# Prueba 4: Agregar una tarjeta de crédito
def test_add_card(routes_page):
    routes_page.set_route(data.address_from, data.address_to)
    routes_page.click_on_request_taxi()
    routes_page.click_on_comfort_tariff()
    routes_page.add_card(data.card_info)
    assert routes_page.card_is_added()
    print("¡Tarjeta de crédito añadida!")

# Prueba 5: Escribir un mensaje para el conductor
def test_write_message_to_driver(routes_page):
    routes_page.set_route(data.address_from, data.address_to)
    routes_page.click_on_request_taxi()
    routes_page.click_on_comfort_tariff()
    message = data.message_for_driver
    routes_page.write_message_to_driver(message)
    assert routes_page.get_driver_message() == message
    print("¡Mensaje enviado!")

# Prueba 6: Pedir una manta y pañuelos
def test_request_blanket_and_tissues(routes_page):
    routes_page.set_route(data.address_from, data.address_to)
    routes_page.click_on_request_taxi()
    routes_page.click_on_comfort_tariff()
    routes_page.toggle_blanket_and_tissues()
    assert routes_page.is_blanket_and_tissues_requested(), "El toggle de manta y pañuelos no está activado."
    print("¡Manta y pañuelos solicitados!")

# Prueba 7: Pedir helados
def test_request_ice_cream(routes_page):
    routes_page.set_route(data.address_from, data.address_to)
    routes_page.click_on_request_taxi()
    routes_page.click_on_comfort_tariff()
    routes_page.request_ice_cream(2)
    assert routes_page.get_ice_cream_quantity() == 2
    print("¡Helados solicitados correctamente!")

# Prueba 8: Buscar un taxi
def test_search_taxi_modal(routes_page):
    routes_page.set_route(data.address_from, data.address_to)
    routes_page.click_on_request_taxi()
    routes_page.search_taxi()
    assert routes_page.search_modal_is_displayed()
    print("¡Modal de búsqueda de taxi mostrado!")


