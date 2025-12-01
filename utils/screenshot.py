"""
UTILIDADES PARA CAPTURAS DE PANTALLA
"""
import os
from datetime import datetime

def tomar_captura(driver, nombre_prueba, carpeta="capturas"):
    """Toma una captura de pantalla y la guarda"""
    
    # Crear carpeta si no existe
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)
    
    # Generar nombre de archivo único
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    nombre_archivo = f"{nombre_prueba}_{timestamp}.png"
    ruta_completa = os.path.join(carpeta, nombre_archivo)
    
    try:
        # Tomar captura
        driver.save_screenshot(ruta_completa)
        print(f"📸 Captura guardada: {ruta_completa}")
        return ruta_completa
    except Exception as e:
        print(f"❌ Error tomando captura: {e}")
        return None

def tomar_captura_emergencia(driver, error, carpeta="capturas"):
    """Toma captura de emergencia cuando hay error"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    nombre_archivo = f"error_{timestamp}.png"
    ruta_completa = os.path.join(carpeta, nombre_archivo)
    
    try:
        # Intentar capturar URL y error en la imagen
        url = driver.current_url if driver else "No disponible"
        print(f"🚨 ERROR CAPTURADO - URL: {url}")
        print(f"🚨 Error: {error}")
        
        if driver:
            driver.save_screenshot(ruta_completa)
            print(f"📸 Captura de error guardada: {ruta_completa}")
            
        return ruta_completa
    except Exception as e:
        print(f"❌ Error crítico tomando captura: {e}")
        return None