#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Archivo de configuración para el simulador de desalinización solar.
Contiene los parámetros configurables que pueden ajustarse para simular
diferentes condiciones y diseños del prototipo.
"""

# Parámetros del prototipo
DIMENSIONES = {
    'largo': 0.45,    # Largo de la caja (m)
    'ancho': 0.25,    # Ancho de la caja (m)
    'altura': 0.30,   # Altura de la caja (m)
}

# Propiedades térmicas
PROPIEDADES_TERMICAS = {
    'absorptividad': 0.9,         # Absorptividad del material (adimensional)
    'angulo_incidencia': 30,      # Ángulo de incidencia solar (grados)
    'material_caja': 'aluminio',  # Material de la caja ('acero', 'aluminio' o 'pvc')
}

# Propiedades del agua
PROPIEDADES_AGUA = {
    'cp_agua': 4186,                    # Capacidad calorífica específica (J/(kg·K))
    'calor_latente_vaporizacion': 2.26e6,  # Calor latente de vaporización (J/kg)
    'temp_inicial': 293,                # Temperatura inicial del agua (K) (20°C)
    'temp_ebullicion': 368,             # Temperatura de ebullición (K) (95°C)
}

# Conductividades térmicas de los materiales (W/(m·K))
CONDUCTIVIDADES_TERMICAS = {
    'acero': 50,       # Acero
    'aluminio': 205,   # Aluminio
    'pvc': 0.19,       # PVC
}

# Condiciones de operación
CONDICIONES_OPERACION = {
    'horas_radiacion_util': 6,      # Horas de radiación solar útil por día
    'masa_agua': 2,                 # Masa de agua en la caja (kg)
    'hemisferio': 'norte',          # Hemisferio ('norte' o 'sur')
    'ubicacion_latitud': 40.0,      # Latitud de la ubicación (grados)
}

# Parámetros de la simulación
PARAMETROS_SIMULACION = {
    'radiacion_base': 500,          # Radiación solar base media (W/m²)
    'amplitud_variacion': 350,      # Amplitud de variación estacional (W/m²)
    'variabilidad_diaria': 100,     # Desviación estándar de variabilidad diaria (W/m²)
    'factor_eficiencia_alta': 0.80, # Factor de eficiencia con radiación alta (>800 W/m²)
    'factor_eficiencia_media': 0.70, # Factor de eficiencia con radiación media (600-800 W/m²)
    'factor_eficiencia_baja': 0.55, # Factor de eficiencia con radiación baja (400-600 W/m²)
    'factor_eficiencia_minima': 0.35, # Factor de eficiencia con radiación mínima (<400 W/m²)
}

# Opciones de visualización
OPCIONES_VISUALIZACION = {
    'dpi_graficas': 300,            # DPI para guardar las gráficas
    'mostrar_graficas': False,      # Mostrar gráficas durante la ejecución
    'tema_graficas': 'seaborn-v0_8-darkgrid', # Tema de las gráficas
}

def cargar_parametros():
    """
    Carga los parámetros configurables desde este archivo.
    Retorna un diccionario con todos los parámetros.
    """
    return {
        'dimensiones': DIMENSIONES,
        'propiedades_termicas': PROPIEDADES_TERMICAS,
        'propiedades_agua': PROPIEDADES_AGUA,
        'conductividades_termicas': CONDUCTIVIDADES_TERMICAS,
        'condiciones_operacion': CONDICIONES_OPERACION,
        'parametros_simulacion': PARAMETROS_SIMULACION,
        'opciones_visualizacion': OPCIONES_VISUALIZACION
    }

def guardar_parametros_actuales():
    """
    Guarda los parámetros actuales en un archivo JSON para referencia futura.
    Útil para mantener un registro de configuraciones de simulación específicas.
    """
    import json
    import os
    from datetime import datetime
    
    parametros = cargar_parametros()
    
    # Crear directorio para configuraciones si no existe
    if not os.path.exists('configuraciones'):
        os.makedirs('configuraciones')
    
    # Generar nombre de archivo con marca de tiempo
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"configuraciones/parametros_{timestamp}.json"
    
    # Guardar en formato JSON
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(parametros, f, indent=2)
    
    print(f"Parámetros guardados en: {filename}")
    return filename

def cargar_parametros_desde_archivo(ruta_archivo):
    """
    Carga parámetros desde un archivo JSON previamente guardado.
    
    Args:
        ruta_archivo: Ruta al archivo JSON con parámetros
        
    Returns:
        Diccionario con los parámetros cargados
    """
    import json
    
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as f:
            parametros = json.load(f)
        print(f"Parámetros cargados desde: {ruta_archivo}")
        return parametros
    except Exception as e:
        print(f"Error al cargar parámetros: {str(e)}")
        return None

def mostrar_parametros_actuales():
    """
    Muestra en consola los parámetros actuales de configuración.
    """
    parametros = cargar_parametros()
    
    print("\n======== CONFIGURACIÓN ACTUAL DEL SIMULADOR ========")
    
    print("\n----- DIMENSIONES DEL PROTOTIPO -----")
    print(f"Largo: {parametros['dimensiones']['largo']} m")
    print(f"Ancho: {parametros['dimensiones']['ancho']} m")
    print(f"Altura: {parametros['dimensiones']['altura']} m")
    
    area = parametros['dimensiones']['largo'] * parametros['dimensiones']['ancho']
    volumen = area * parametros['dimensiones']['altura']
    print(f"Área de captación: {area:.4f} m²")
    print(f"Volumen: {volumen:.4f} m³ ({volumen*1000:.2f} litros)")
    
    print("\n----- PROPIEDADES TÉRMICAS -----")
    print(f"Absorptividad: {parametros['propiedades_termicas']['absorptividad']}")
    print(f"Ángulo de incidencia: {parametros['propiedades_termicas']['angulo_incidencia']}°")
    print(f"Material de la caja: {parametros['propiedades_termicas']['material_caja']}")
    
    print("\n----- CONDICIONES DE OPERACIÓN -----")
    print(f"Horas de radiación útil: {parametros['condiciones_operacion']['horas_radiacion_util']} horas/día")
    print(f"Masa de agua: {parametros['condiciones_operacion']['masa_agua']} kg")
    print(f"Hemisferio: {parametros['condiciones_operacion']['hemisferio']}")
    
    print("\n----- PARÁMETROS DE SIMULACIÓN -----")
    print(f"Radiación base: {parametros['parametros_simulacion']['radiacion_base']} W/m²")
    print(f"Amplitud de variación estacional: {parametros['parametros_simulacion']['amplitud_variacion']} W/m²")
    
    print("\n----- FACTORES DE EFICIENCIA -----")
    print(f"Alta radiación (>800 W/m²): {parametros['parametros_simulacion']['factor_eficiencia_alta']*100:.1f}%")
    print(f"Media radiación (600-800 W/m²): {parametros['parametros_simulacion']['factor_eficiencia_media']*100:.1f}%")
    print(f"Baja radiación (400-600 W/m²): {parametros['parametros_simulacion']['factor_eficiencia_baja']*100:.1f}%")
    print(f"Mínima radiación (<400 W/m²): {parametros['parametros_simulacion']['factor_eficiencia_minima']*100:.1f}%")
    
    print("\n========================================================")

if __name__ == "__main__":
    mostrar_parametros_actuales()
    opcion = input("\n¿Desea guardar esta configuración? (s/n): ")
    if opcion.lower() == 's':
        archivo = guardar_parametros_actuales()
        print(f"Configuración guardada en: {archivo}")
    print("\nPara utilizar estos parámetros en la simulación, ejecute:")
    print("    python simulacion_desalinizador.py") 