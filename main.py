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

    # Establecer la ruta de la solicitud de taxi
    address_from = data.address_from
    address_to = data.address_to
    routes_page.set_route(address_from, address_to)
    print(f"Ruta desde {routes_page.get_from()} hasta {routes_page.get_to()} configurada correctamente.")

    # Configuración de teléfono y código de confirmación
    routes_page.set_phone()
    routes_page.the_next_button()
    routes_page.code_number()
    routes_page.send_cell_info()

    # Añadir tarjeta y pagar
    routes_page.add_card()

    # Escribir mensaje para el conductor
    message = data.message_for_driver
    routes_page.write_drive_message(message)

    # Solicitar manta y pañuelos
    routes_page.request_blanket_and_tissues()

    # Solicitar helado
    routes_page.request_ice_cream()

    # Buscar taxi y esperar por la información del conductor
    routes_page.search_taxi()
    routes_page.wait_for_driver_info()

    # Cerrar el navegador
    driver.quit()

if __name__ == "__main__":
    main()
