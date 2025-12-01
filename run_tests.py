"""
EJECUTOR PRINCIPAL - Corre todas las pruebas
"""
import time
from datetime import datetime
import webbrowser
import os

# Importar las pruebas
from tests.test_login import test_login_exitoso, test_login_invalido
from tests.test_crud import test_crud_create, test_crud_read_update, test_crud_delete
from tests.test_flujo_completo import test_flujo_completo_crud  # NUEVO IMPORT
from utils.report import generar_reporte_html

def ejecutar_todas_las_pruebas():
    """Ejecuta las 6 pruebas y genera reporte"""
    
    print("="*80)
    print("🚀 SISTEMA DE PRUEBAS AUTOMATIZADAS")
    print("="*80)
    print("📋 Ejecutando 6 pruebas (6 Historias de Usuario):")
    print("   1. HU-001: Login exitoso (Camino feliz)")
    print("   2. HU-002: Login inválido (Prueba negativa)")
    print("   3. HU-003: CRUD Create (Camino feliz)")
    print("   4. HU-004: CRUD Read/Update (Prueba límites)")
    print("   5. HU-005: CRUD Delete (Prueba negativa)")
    print("   6. HU-006: Flujo Completo CRUD (Integración)")  # NUEVA PRUEBA
    print("="*80)
    
    # Crear carpetas necesarias
    for carpeta in ["capturas", "reportes"]:
        if not os.path.exists(carpeta):
            os.makedirs(carpeta)
            print(f"📁 Carpeta creada: {carpeta}/")
    
    resultados = []
    
    # Lista de pruebas a ejecutar
    pruebas = [
        ("HU-001: Login exitoso", test_login_exitoso),
        ("HU-002: Login inválido", test_login_invalido),
        ("HU-003: CRUD Create", test_crud_create),
        ("HU-004: CRUD Read/Update", test_crud_read_update),
        ("HU-005: CRUD Delete", test_crud_delete),
        ("HU-006: Flujo Completo CRUD", test_flujo_completo_crud)  # NUEVA PRUEBA
    ]
    
    print("\n🎬 INICIANDO EJECUCIÓN DE PRUEBAS...")
    print("-"*80)
    
    # Ejecutar cada prueba
    for nombre_prueba, funcion_prueba in pruebas:
        print(f"\n▶️ Ejecutando: {nombre_prueba}")
        
        try:
            # Ejecutar prueba y obtener resultado
            resultado = funcion_prueba()
            resultado['timestamp'] = datetime.now().strftime("%H:%M:%S")
            resultados.append(resultado)
            
            print(f"   Estado: {resultado['estado']}")
            
        except Exception as e:
            print(f"❌ Error ejecutando {nombre_prueba}: {e}")
            resultados.append({
                'nombre': nombre_prueba,
                'descripcion': f'Error: {str(e)}',
                'estado': 'FAILED',
                'timestamp': datetime.now().strftime("%H:%M:%S")
            })
        
        # Pequeña pausa entre pruebas
        time.sleep(2)
    
    # Generar reporte HTML
    print("\n" + "="*80)
    print("📊 GENERANDO REPORTE...")
    print("="*80)
    
    reporte = generar_reporte_html(resultados)
    
    # Mostrar resumen
    print("\n📈 RESUMEN DE EJECUCIÓN:")
    print("-"*40)
    
    exitosas = sum(1 for r in resultados if r['estado'] == 'PASSED')
    total = len(resultados)
    
    for resultado in resultados:
        emoji = "✅" if resultado['estado'] == 'PASSED' else "❌"
        print(f"{emoji} {resultado['nombre']}")
    
    print(f"\n📊 Total: {exitosas}/{total} pruebas exitosas")
    print(f"📄 Reporte: {reporte}")
    
    # Preguntar si abrir reporte
    print("\n¿Abrir reporte en navegador? (S/N): ", end="")
    respuesta = input().strip().lower()
    
    if respuesta in ['s', 'si', 'sí', 'y', 'yes']:
        webbrowser.open(f"file://{os.path.abspath(reporte)}")
        print("🌐 Reporte abierto en navegador")
    
    print("\n" + "="*80)
    print("🏁 ¡PRUEBAS COMPLETADAS!")
    print("="*80)

if __name__ == "__main__":
    ejecutar_todas_las_pruebas()