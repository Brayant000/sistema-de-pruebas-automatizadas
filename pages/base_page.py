"""
PÁGINA BASE - Funciones comunes mejoradas
"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def find_element(self, locator, by=By.ID, timeout=10):
        """Encuentra un elemento"""
        try:
            wait = WebDriverWait(self.driver, timeout)
            return wait.until(EC.presence_of_element_located((by, locator)))
        except Exception as e:
            print(f"⚠️ No se encontró elemento {locator}: {e}")
            raise
    
    def find_elements(self, locator, by=By.ID, timeout=10):
        """Encuentra múltiples elementos"""
        try:
            wait = WebDriverWait(self.driver, timeout)
            return wait.until(EC.presence_of_all_elements_located((by, locator)))
        except Exception as e:
            print(f"⚠️ No se encontraron elementos {locator}: {e}")
            return []
    
    def click(self, locator, by=By.ID):
        """Hace click en un elemento"""
        try:
            element = self.find_element(locator, by)
            element.click()
            time.sleep(0.5)
            return True
        except Exception as e:
            print(f"⚠️ Error haciendo click en {locator}: {e}")
            # Intentar con JavaScript
            try:
                element = self.find_element(locator, by)
                self.driver.execute_script("arguments[0].click();", element)
                time.sleep(0.5)
                return True
            except:
                return False
    
    def send_keys(self, locator, text, by=By.ID):
        """Escribe texto en un campo"""
        try:
            element = self.find_element(locator, by)
            element.clear()
            element.send_keys(text)
            return True
        except Exception as e:
            print(f"⚠️ Error enviando texto a {locator}: {e}")
            return False
    
    def get_text(self, locator, by=By.ID):
        """Obtiene el texto de un elemento"""
        try:
            element = self.find_element(locator, by)
            return element.text.strip()
        except:
            return ""
    
    def is_element_present(self, locator, by=By.ID, timeout=5):
        """Verifica si un elemento está presente"""
        try:
            self.find_element(locator, by, timeout)
            return True
        except:
            return False
    
    def is_element_visible(self, locator, by=By.ID):
        """Verifica si un elemento es visible"""
        try:
            element = self.find_element(locator, by)
            return element.is_displayed()
        except:
            return False
    
    def wait_for_element_visible(self, locator, by=By.ID, timeout=10):
        """Espera a que un elemento sea visible"""
        try:
            wait = WebDriverWait(self.driver, timeout)
            return wait.until(EC.visibility_of_element_located((by, locator)))
        except:
            return None
    
    def take_screenshot(self, name):
        """Toma una captura de pantalla"""
        try:
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            filename = f"capturas/{name}_{timestamp}.png"
            self.driver.save_screenshot(filename)
            print(f"📸 Captura guardada: {filename}")
            return filename
        except Exception as e:
            print(f"⚠️ Error tomando captura: {e}")
            return None
    
    def execute_js(self, script, *args):
        """Ejecuta JavaScript"""
        try:
            return self.driver.execute_script(script, *args)
        except Exception as e:
            print(f"⚠️ Error ejecutando JS: {e}")
            return None