"""
GENERADOR DE REPORTES HTML - Actualizado para 6 pruebas
"""
import os
from datetime import datetime

def generar_reporte_html(resultados):
    """Genera un reporte HTML con los resultados de las pruebas"""
    
    # Crear carpeta de reportes si no existe
    if not os.path.exists("reportes"):
        os.makedirs("reportes")
    
    # Calcular estadísticas
    total_pruebas = len(resultados)
    exitosas = sum(1 for r in resultados if r['estado'] == 'PASSED')
    fallidas = total_pruebas - exitosas
    
    # Calcular capturas totales
    capturas_totales = sum(r.get('capturas', 0) for r in resultados)
    
    # Generar nombre de archivo único
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    nombre_archivo = f"reporte_pruebas_{timestamp}.html"
    ruta_completa = os.path.join("reportes", nombre_archivo)
    
    # Crear el HTML
    html = f'''
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Reporte de Pruebas Automatizadas</title>
        <style>
            * {{
                margin: 0;
                padding: 0;
                box-sizing: border-box;
                font-family: 'Segoe UI', Arial, sans-serif;
            }}
            
            body {{
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                padding: 20px;
                min-height: 100vh;
            }}
            
            .container {{
                max-width: 1200px;
                margin: 0 auto;
                background: white;
                border-radius: 15px;
                box-shadow: 0 10px 30px rgba(0,0,0,0.3);
                overflow: hidden;
            }}
            
            .header {{
                background: linear-gradient(to right, #4A90E2, #9013FE);
                color: white;
                padding: 40px;
                text-align: center;
                position: relative;
                overflow: hidden;
            }}
            
            .header::before {{
                content: "🔧";
                font-size: 120px;
                position: absolute;
                opacity: 0.1;
                right: 20px;
                top: 20px;
            }}
            
            .header h1 {{
                font-size: 2.5em;
                margin-bottom: 10px;
            }}
            
            .stats-bar {{
                display: grid;
                grid-template-columns: repeat(4, 1fr);
                background: #f8f9fa;
                padding: 20px;
                border-bottom: 2px solid #e9ecef;
                gap: 15px;
            }}
            
            .stat-box {{
                text-align: center;
                padding: 15px;
                background: white;
                border-radius: 10px;
                box-shadow: 0 2px 5px rgba(0,0,0,0.1);
                transition: transform 0.3s;
            }}
            
            .stat-box:hover {{
                transform: translateY(-5px);
                box-shadow: 0 5px 15px rgba(0,0,0,0.2);
            }}
            
            .stat-number {{
                font-size: 2.5em;
                font-weight: bold;
                display: block;
            }}
            
            .stat-total {{ color: #4A90E2; }}
            .stat-passed {{ color: #28a745; }}
            .stat-failed {{ color: #dc3545; }}
            .stat-screenshots {{ color: #FF9900; }}
            
            .test-results {{
                padding: 30px;
            }}
            
            .phase-timeline {{
                display: flex;
                justify-content: space-between;
                margin: 30px 0;
                position: relative;
            }}
            
            .phase-timeline::before {{
                content: '';
                position: absolute;
                top: 50%;
                left: 10%;
                right: 10%;
                height: 3px;
                background: #e9ecef;
                z-index: 1;
            }}
            
            .phase {{
                text-align: center;
                z-index: 2;
                background: white;
                padding: 0 10px;
            }}
            
            .phase-icon {{
                font-size: 24px;
                margin-bottom: 5px;
            }}
            
            .test-card {{
                border: 1px solid #e9ecef;
                border-radius: 10px;
                padding: 25px;
                margin-bottom: 20px;
                background: #f8f9fa;
                transition: all 0.3s;
                position: relative;
                overflow: hidden;
            }}
            
            .test-card::before {{
                content: '';
                position: absolute;
                left: 0;
                top: 0;
                bottom: 0;
                width: 5px;
            }}
            
            .test-card.passed::before {{ background: #28a745; }}
            .test-card.failed::before {{ background: #dc3545; }}
            
            .test-card:hover {{
                box-shadow: 0 5px 15px rgba(0,0,0,0.1);
                transform: translateY(-2px);
            }}
            
            .test-title {{
                font-size: 1.3em;
                font-weight: bold;
                margin-bottom: 10px;
                display: flex;
                align-items: center;
                gap: 10px;
            }}
            
            .test-details {{
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
                gap: 15px;
                margin-top: 15px;
            }}
            
            .detail-item {{
                background: white;
                padding: 10px;
                border-radius: 5px;
                border-left: 3px solid #4A90E2;
            }}
            
            .detail-label {{
                font-size: 0.9em;
                color: #6c757d;
                display: block;
            }}
            
            .detail-value {{
                font-weight: bold;
                color: #333;
            }}
            
            .footer {{
                text-align: center;
                padding: 25px;
                background: #343a40;
                color: white;
                border-bottom-left-radius: 15px;
                border-bottom-right-radius: 15px;
            }}
            
            .flujo-completo {{
                background: linear-gradient(to right, #667eea, #764ba2);
                color: white;
                border: none;
            }}
            
            .flujo-completo .test-title {{
                color: white;
            }}
            
            .flujo-completo .detail-item {{
                background: rgba(255,255,255,0.1);
                color: white;
            }}
            
            .flujo-completo .detail-label {{
                color: rgba(255,255,255,0.8);
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>📋 Reporte de Pruebas Automatizadas</h1>
                <p>Sistema CRUD - Pruebas de Login y Operaciones CRUD</p>
                <p>Fecha de ejecución: {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}</p>
            </div>
            
            <div class="stats-bar">
                <div class="stat-box">
                    <span class="stat-number stat-total">{total_pruebas}</span>
                    <span>Total Pruebas</span>
                </div>
                <div class="stat-box">
                    <span class="stat-number stat-passed">{exitosas}</span>
                    <span>Pruebas Exitosas</span>
                </div>
                <div class="stat-box">
                    <span class="stat-number stat-failed">{fallidas}</span>
                    <span>Pruebas Fallidas</span>
                </div>
                <div class="stat-box">
                    <span class="stat-number stat-screenshots">{capturas_totales}</span>
                    <span>Capturas Tomadas</span>
                </div>
            </div>
            
            <div class="test-results">
                <h2 style="margin-bottom: 20px;">🧪 Resultados de las Pruebas</h2>
                
                <!-- Timeline del flujo completo -->
                <div class="phase-timeline">
                    <div class="phase">
                        <div class="phase-icon">📝</div>
                        <div>CREATE</div>
                    </div>
                    <div class="phase">
                        <div class="phase-icon">🔐</div>
                        <div>LOGIN</div>
                    </div>
                    <div class="phase">
                        <div class="phase-icon">✏️</div>
                        <div>UPDATE</div>
                    </div>
                    <div class="phase">
                        <div class="phase-icon">🗑️</div>
                        <div>DELETE</div>
                    </div>
                </div>
    '''
    
    # Agregar cada resultado de prueba
    for resultado in resultados:
        clase_css = "passed" if resultado['estado'] == 'PASSED' else "failed"
        
        # Clase especial para el flujo completo
        clase_extra = "flujo-completo" if "006" in resultado['nombre'] else ""
        
        html += f'''
                <div class="test-card {clase_css} {clase_extra}">
                    <div class="test-title">
                        {"✅" if resultado['estado'] == 'PASSED' else "❌"} 
                        {resultado['nombre']}
                    </div>
                    <div class="test-desc">{resultado.get('descripcion', '')}</div>
                    <div class="test-details">
                        <div class="detail-item">
                            <span class="detail-label">Estado</span>
                            <span class="detail-value">{resultado['estado']}</span>
                        </div>
                        <div class="detail-item">
                            <span class="detail-label">Duración</span>
                            <span class="detail-value">{resultado.get('duracion', 'N/A')} segundos</span>
                        </div>
                        <div class="detail-item">
                            <span class="detail-label">Capturas</span>
                            <span class="detail-value">{resultado.get('capturas', 0)}</span>
                        </div>
                        <div class="detail-item">
                            <span class="detail-label">Ejecutada</span>
                            <span class="detail-value">{resultado.get('timestamp', 'N/A')}</span>
                        </div>
                    </div>
                </div>
        '''
    
    # Cerrar HTML
    html += '''
            </div>
            
            <div class="footer">
                <p>🛠️ Pruebas ejecutadas con Selenium WebDriver + Python</p>
                <p>📁 Capturas guardadas en: carpeta 'capturas/'</p>
                <p>🌐 Sitio probado: https://brayant000.github.io/Brayant000Web.github.io/</p>
                <p style="margin-top: 15px; font-size: 0.9em; opacity: 0.8;">
                    Reporte generado automáticamente - Sistema de Pruebas Automatizadas
                </p>
            </div>
        </div>
        
        <script>
            // Efecto de resaltado al pasar el mouse
            document.querySelectorAll('.test-card').forEach(card => {
                card.addEventListener('mouseenter', () => {
                    card.style.boxShadow = '0 8px 25px rgba(0,0,0,0.15)';
                });
                card.addEventListener('mouseleave', () => {
                    card.style.boxShadow = '0 5px 15px rgba(0,0,0,0.1)';
                });
            });
            
            // Mostrar mensaje de carga
            console.log('Reporte cargado exitosamente');
        </script>
    </body>
    </html>
    '''
    
    # Escribir archivo
    with open(ruta_completa, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"📄 Reporte HTML generado: {ruta_completa}")
    return ruta_completa