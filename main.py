# main.py

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
    routes_page.set_route(data.address_from, data.address_to)  # Configura la ruta
    routes_page.click_on_request_taxi()

    # Espera hasta que el botón de tarifa esté disponible
    WebDriverWait(routes_page.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".comfort-tariff"))
    )
    
    routes_page.click_on_comfort_tariff()
    assert routes_page.get_selected_tariff() == "Comfort"
    print("¡Tarifa Comfort seleccionada!")

# Prueba 3: Configura el número de teléfono
def test_set_phone(routes_page):
    routes_page.set_route(data.address_from, data.address_to)
    routes_page.click_on_request_taxi()
    routes_page.click_on_comfort_tariff()

    # Espera hasta que el campo de teléfono esté disponible
    WebDriverWait(routes_page.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#phone-input"))
    )
    routes_page.set_phone(data.phone_number)
    assert routes_page.phone_is_set()
    print("¡Teléfono configurado!")

# Prueba 4: Agregar una tarjeta de crédito
def test_add_card(routes_page):
    routes_page.set_route(data.address_from, data.address_to)
    routes_page.click_on_request_taxi()
    routes_page.click_on_comfort_tariff()

    # Espera hasta que el formulario de tarjeta esté disponible
    WebDriverWait(routes_page.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#credit-card-form"))
    )
    routes_page.add_card(data.card_info)
    assert routes_page.card_is_added()
    print("¡Tarjeta de crédito añadida!")

# Prueba 5: Confirmar código de tarjeta
def test_card_confirmation_code(routes_page):
    routes_page.set_route(data.address_from, data.address_to)
    routes_page.click_on_request_taxi()
    routes_page.click_on_comfort_tariff()
    routes_page.add_card(data.card_info)

    # Espera hasta que el campo de código de confirmación esté disponible
    WebDriverWait(routes_page.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#confirmation-code"))
    )
    routes_page.enter_confirmation_code(data.confirmation_code)
    assert routes_page.confirmation_is_valid()
    print("¡Código de tarjeta confirmado!")

# Prueba 6: Escribir un mensaje para el conductor
def test_write_message_to_driver(routes_page):
    routes_page.set_route(data.address_from, data.address_to)
    routes_page.click_on_request_taxi()
    routes_page.click_on_comfort_tariff()
    routes_page.add_card(data.card_info)
    message = data.message_for_driver
    routes_page.write_drive_message(message)
    assert routes_page.get_driver_message() == message
    print("¡Mensaje enviado!")

# Prueba 7: Pedir una manta y pañuelos
def test_request_blanket_and_tissues(routes_page):
    routes_page.set_route(data.address_from, data.address_to)
    routes_page.click_on_request_taxi()
    routes_page.click_on_comfort_tariff()
    WebDriverWait(routes_page.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#request-items"))
    )
    routes_page.request_blanket_and_tissues()
    assert routes_page.blanket_and_tissues_requested()
    print("Manta y pañuelos solicitados")

# Prueba 8: Pedir 2 helados
def test_request_ice_cream(routes_page):
    routes_page.set_route(data.address_from, data.address_to)
    routes_page.click_on_request_taxi()
    routes_page.click_on_comfort_tariff()
    WebDriverWait(routes_page.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#request-items"))
    )
    routes_page.request_ice_cream(quantity=2)
    assert routes_page.get_ice_cream_quantity() == 2
    print("Helados solicitados")

# Prueba 9: Aparece el modal para buscar un taxi
def test_search_taxi_modal(routes_page):
    routes_page.set_route(data.address_from, data.address_to)
    routes_page.click_on_request_taxi()
    WebDriverWait(routes_page.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#search-modal"))
    )
    routes_page.search_taxi()
    assert routes_page.search_modal_is_displayed()

# Prueba 10: Esperar información del conductor
def test_wait_for_driver_info(routes_page):
    routes_page.set_route(data.address_from, data.address_to)
    routes_page.click_on_request_taxi()
    routes_page.click_on_comfort_tariff()
    WebDriverWait(routes_page.driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#driver-info"))
    )
    driver_info = routes_page.wait_for_driver_info()
    assert driver_info is not None
    print("Información del conductor recibida")
