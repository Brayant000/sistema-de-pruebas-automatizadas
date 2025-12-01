"""
CONFIGURACIÓN DEL PROYECTO
"""
BASE_URL = "https://brayant000.github.io/Brayant000Web.github.io/"
LOGIN_URL = BASE_URL + "login.html"
REGISTER_URL = BASE_URL

# Configuración del navegador
HEADLESS = False
WAIT_TIME = 10
SCREENSHOT_DIR = "capturas"
REPORT_DIR = "reportes"

# Credenciales de prueba
TEST_USER = {
    "name": "Usuario Test",
    "email": "test@example.com",
    "phone": "+1234567890"
}