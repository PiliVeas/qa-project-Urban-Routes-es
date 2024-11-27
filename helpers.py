# helpers.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Espera a que un elemento esté visible
def wait_for_element(driver, by, value, timeout=10):
    return WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located((by, value))  # Cambio aquí de presence a visibility
    )

# Espera a que un elemento sea clicable
def wait_for_clickable(driver, by, value, timeout=10):
    return WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable((by, value))
    )

# Verifica si un elemento está presente
def is_element_present(driver, by, value):
    try:
        driver.find_element(by, value)
        return True
    except:
        return False

