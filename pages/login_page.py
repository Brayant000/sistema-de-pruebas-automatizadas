"""
PÁGINA DE LOGIN - ACTUALIZADO para tu sistema real
"""
from .base_page import BasePage
from selenium.webdriver.common.by import By
import time

class LoginPage(BasePage):
    # Locators actualizados según tu HTML
    EMAIL_INPUT = "loginEmail"
    PASSWORD_INPUT = "loginPassword"
    SUBMIT_BUTTON = "//button[contains(text(), 'Iniciar Sesión') or @type='submit']"
    ERROR_MESSAGE = "//div[contains(@class, 'alert') or contains(@class, 'error')]"
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def navigate_to_login(self):
        """Navega a la página de login"""
        self.driver.get("https://brayant000.github.io/Brayant000Web.github.io/login.html")
        time.sleep(2)
    
    def login(self, email, password):
        """Realiza login con credenciales"""
        try:
            self.send_keys(self.EMAIL_INPUT, email)
            self.send_keys(self.PASSWORD_INPUT, password)
            self.click(self.SUBMIT_BUTTON, By.XPATH)
            time.sleep(3)
            return True
        except Exception as e:
            print(f"⚠️ Error en login: {e}")
            return False
    
    def is_login_successful(self):
        """Verifica si el login fue exitoso"""
        time.sleep(2)
        current_url = self.driver.current_url
        page_source = self.driver.page_source.lower()
        
        # Verificar múltiples indicadores de éxito
        success_indicators = [
            "dashboard" in current_url,
            "bienvenido" in page_source,
            "sesión iniciada" in page_source,
            "welcome" in page_source
        ]
        
        return any(success_indicators)
    
    def get_error_message(self):
        """Obtiene mensaje de error del login"""
        try:
            # Buscar en diferentes lugares
            error_selectors = [
                (By.ID, "loginMessage"),
                (By.CLASS_NAME, "alert-danger"),
                (By.CLASS_NAME, "error-message"),
                (By.XPATH, "//div[contains(text(), 'incorrecta') or contains(text(), 'error')]")
            ]
            
            for by, selector in error_selectors:
                try:
                    element = self.driver.find_element(by, selector)
                    text = element.text.strip()
                    if text:
                        return text
                except:
                    continue
            
            # Buscar en texto de página
            page_text = self.driver.find_element(By.TAG_NAME, 'body').text
            error_keywords = ['incorrecta', 'inválida', 'error', 'falló', 'no existe']
            
            for keyword in error_keywords:
                if keyword in page_text.lower():
                    lines = page_text.split('\n')
                    for line in lines:
                        if keyword in line.lower():
                            return line.strip()
            
            return ""
            
        except Exception as e:
            print(f"⚠️ Error obteniendo mensaje: {e}")
            return ""
    
    def handle_alert(self, accept=True):
        """Maneja alertas del navegador"""
        try:
            alert = self.driver.switch_to.alert
            text = alert.text
            print(f"🔔 Alerta detectada: {text}")
            if accept:
                alert.accept()
            else:
                alert.dismiss()
            time.sleep(1)
            return text
        except:
            return None
    
    def logout(self):
        """Cierra sesión desde el dashboard"""
        try:
            if "dashboard" in self.driver.current_url:
                # Buscar botón de logout
                logout_selectors = [
                    (By.ID, "logoutBtn"),
                    (By.XPATH, "//a[contains(text(), 'Cerrar')]"),
                    (By.XPATH, "//button[contains(text(), 'Salir')]"),
                    (By.CLASS_NAME, "logout-button")
                ]
                
                for by, selector in logout_selectors:
                    try:
                        self.click(selector, by)
                        time.sleep(2)
                        print("✅ Sesión cerrada exitosamente")
                        return True
                    except:
                        continue
        except Exception as e:
            print(f"⚠️ Error en logout: {e}")
        
        return False
    
    def wait_for_element_visible(self, locator, by=By.ID, timeout=10):
        """Espera a que un elemento sea visible"""
        import time
        start_time = time.time()
        
        while time.time() - start_time < timeout:
            try:
                element = self.driver.find_element(by, locator)
                if element.is_displayed():
                    return element
            except:
                pass
            time.sleep(0.5)
        
        return None