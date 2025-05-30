import pandas as pd
import json
import os
import numpy as np

def actualizar_datos_reporte():
    """
    Extrae datos de los archivos CSV generados por la simulación y
    crea un archivo JavaScript con los datos para el reporte HTML
    """
    print("Actualizando datos para el reporte web...")
    
    # Verificar si existen los archivos de datos
    if not os.path.exists('datos_desalinizador_anual.csv') or not os.path.exists('datos_desalinizador_mensual.csv'):
        print("Error: No se encontraron los archivos de datos. Ejecute primero la simulación.")
        return
    
    # Cargar datos
    df_anual = pd.read_csv('datos_desalinizador_anual.csv')
    df_mensual = pd.read_csv('datos_desalinizador_mensual.csv')
    
    # Calcular estadísticas anuales
    produccion_total = df_anual['produccion_litros'].sum()
    produccion_media = df_anual['produccion_litros'].mean()
    radiacion_media = df_anual['radiacion_Wm2'].mean()
    gor_medio = df_anual['GOR'].mean()
    
    # Días de alta y baja producción
    dias_alta_produccion = len(df_anual[df_anual['produccion_litros'] > produccion_media])
    dias_baja_produccion = len(df_anual[df_anual['produccion_litros'] < produccion_media/2])
    
    # Calcular correlación entre radiación y producción
    correlacion_rad_prod = df_anual['radiacion_Wm2'].corr(df_anual['produccion_litros'])
    
    # Análisis energético
    # Estos valores pueden ser extraídos del dataframe si están disponibles
    # o pueden ser calculados si se tienen los datos necesarios
    area_captacion = 0.1125  # m²
    energia_solar_media = df_anual['radiacion_Wm2'].mean() * area_captacion * 3600 * 6 / 1000  # kJ/día (6 horas efectivas)
    
    # Si están disponibles los datos de temperatura, recuperarlos
    if 'perdidas_termicas_W' in df_anual.columns:
        perdidas_termicas_media = df_anual['perdidas_termicas_W'].mean()
    else:
        # Valor estimado si no está disponible
        perdidas_termicas_media = 40.62  # W
    
    # Calcular eficiencia térmica aproximada
    eficiencia_termica = (1 - (perdidas_termicas_media * 3600 * 6) / (energia_solar_media * 1000)) * 100  # %
    
    # Calcular estadísticas estacionales
    # Asignar estación a cada mes
    estaciones = {
        'Invierno': [12, 1, 2],
        'Primavera': [3, 4, 5],
        'Verano': [6, 7, 8],
        'Otoño': [9, 10, 11]
    }
    
    # Crear un diccionario para almacenar los datos por estación
    datos_estacionales = {}
    
    for estacion, meses in estaciones.items():
        # Filtrar datos mensuales por estación
        datos_estacion = df_mensual[df_mensual['mes'].isin(meses)]
        
        # Calcular producción total de la estación
        produccion_estacion = datos_estacion['produccion_litros'].sum()
        
        # Calcular GOR medio de la estación
        gor_estacion = datos_estacion['GOR'].mean()
        
        # Calcular porcentaje de producción anual
        porcentaje_estacion = (produccion_estacion / produccion_total) * 100 if produccion_total > 0 else 0
        
        # Almacenar datos de la estación
        datos_estacionales[estacion] = {
            'produccion': float(produccion_estacion),
            'gor': float(gor_estacion),
            'porcentaje': float(porcentaje_estacion)
        }
    
    # Preparar datos mensuales para el reporte
    datos_mensuales = []
    for _, row in df_mensual.iterrows():
        datos_mes = {
            'mes': row['nombre_mes'],
            'produccion': float(row['produccion_litros']),
            'radiacion': float(row['radiacion_Wm2']),
            'gor': float(row['GOR'])
        }
        
        # Agregar temperatura del agua si está disponible
        if 'temp_agua_C' in df_mensual.columns:
            datos_mes['temp_agua_C'] = float(row['temp_agua_C'])
            
        datos_mensuales.append(datos_mes)
    
    # Crear un diccionario con todos los datos para el reporte
    datos_reporte = {
        'produccion_total': float(produccion_total),
        'produccion_media': float(produccion_media),
        'radiacion_media': float(radiacion_media),
        'gor_medio': float(gor_medio),
        'dias_alta_produccion': int(dias_alta_produccion),
        'dias_baja_produccion': int(dias_baja_produccion),
        'datos_mensuales': datos_mensuales,
        'datos_estacionales': datos_estacionales,
        'energia_solar': float(energia_solar_media),
        'perdidas_termicas': float(perdidas_termicas_media),
        'eficiencia_termica': float(eficiencia_termica),
        'area_captacion': float(area_captacion),
        'correlacion_rad_prod': float(correlacion_rad_prod)
    }
    
    # Convertir a JavaScript
    js_content = f"""
// Archivo generado automáticamente por actualizar_datos_reporte.py
// Contiene los datos de la simulación del desalinizador solar

// Función para cargar los datos de simulación
function cargarDatosSimulacion() {{
    console.log("Cargando datos de simulación...");
    
    // Datos generados por la simulación en Python
    datosSimulacion.produccion_total = {datos_reporte['produccion_total']:.2f};
    datosSimulacion.produccion_media = {datos_reporte['produccion_media']:.2f};
    datosSimulacion.radiacion_media = {datos_reporte['radiacion_media']:.2f};
    datosSimulacion.gor_medio = {datos_reporte['gor_medio']:.4f};
    datosSimulacion.dias_alta_produccion = {datos_reporte['dias_alta_produccion']};
    datosSimulacion.dias_baja_produccion = {datos_reporte['dias_baja_produccion']};
    
    datosSimulacion.datos_mensuales = {json.dumps(datos_mensuales)};
    datosSimulacion.datos_estacionales = {json.dumps(datos_estacionales)};
    
    // Datos de análisis energético
    datosSimulacion.energia_solar = {datos_reporte['energia_solar']:.2f};
    datosSimulacion.perdidas_termicas = {datos_reporte['perdidas_termicas']:.2f};
    datosSimulacion.eficiencia_termica = {datos_reporte['eficiencia_termica']:.2f};
    datosSimulacion.area_captacion = {datos_reporte['area_captacion']:.4f};
    datosSimulacion.correlacion_rad_prod = {datos_reporte['correlacion_rad_prod']:.4f};
    
    // Actualizar la interfaz con los datos cargados
    actualizarInterfaz();
}}
"""
    
    # Guardar como archivo JS
    with open('datos_simulacion.js', 'w', encoding='utf-8') as js_file:
        js_file.write(js_content)
    
    print(f"Datos actualizados correctamente. Se generó el archivo 'datos_simulacion.js'.")
    print(f"Producción total anual: {produccion_total:.2f} litros")
    print(f"Producción media diaria: {produccion_media:.2f} litros/día")
    print(f"Distribución estacional: Verano {datos_estacionales['Verano']['porcentaje']:.1f}%, "
          f"Primavera {datos_estacionales['Primavera']['porcentaje']:.1f}%, "
          f"Otoño {datos_estacionales['Otoño']['porcentaje']:.1f}%, "
          f"Invierno {datos_estacionales['Invierno']['porcentaje']:.1f}%")
    print(f"Eficiencia térmica: {eficiencia_termica:.2f}%")
    
    # Verificar si existe el informe ejecutivo
    if os.path.exists('informe_ejecutivo.md'):
        print("\n✅ Se encontró el informe ejecutivo detallado en 'informe_ejecutivo.md'")
        print("   El informe contiene un análisis termodinámico completo del sistema.")
    
    # Actualizar el archivo HTML para que cargue el JS generado
    actualizar_html_para_cargar_js()
    
    # Crear directorio de resultados si no existe
    if not os.path.exists('resultados'):
        os.makedirs('resultados')
        print("Se creó el directorio 'resultados' para almacenar las gráficas")
    
def actualizar_html_para_cargar_js():
    """
    Modifica el archivo HTML para que cargue el archivo JS generado
    """
    html_file = 'reporte_anual_desalinizador.html'
    
    if not os.path.exists(html_file):
        print(f"Error: No se encontró el archivo {html_file}")
        return
    
    with open(html_file, 'r', encoding='utf-8') as file:
        html_content = file.read()
    
    # Buscar la etiqueta </head> para insertar la referencia al script
    if '</head>' in html_content and 'datos_simulacion.js' not in html_content:
        # Insertar referencia al archivo JS antes de cerrar el head
        modified_content = html_content.replace(
            '</head>',
            '    <script src="datos_simulacion.js"></script>\n</head>'
        )
        
        # Guardar el HTML modificado
        with open(html_file, 'w', encoding='utf-8') as file:
            file.write(modified_content)
        
        print(f"Se actualizó {html_file} para cargar los datos de simulación.")
    else:
        print(f"No se pudo actualizar {html_file} o ya estaba actualizado.")

if __name__ == "__main__":
    actualizar_datos_reporte() 