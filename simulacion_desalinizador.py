import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Parámetros del sistema
class ParametrosDesalinizador:
    def __init__(self):
        # Dimensiones
        self.largo = 0.45  # m
        self.ancho = 0.25  # m
        self.altura = 0.30  # m
        self.area_captacion = self.largo * self.ancho  # m²
        self.volumen = self.largo * self.ancho * self.altura  # m³
        self.volumen_litros = self.volumen * 1000  # litros
        
        # Propiedades térmicas
        self.absorptividad = 0.9  # adimensional
        self.angulo_incidencia = 30  # grados
        self.cos_angulo = np.cos(np.radians(self.angulo_incidencia))
        
        # Propiedades del agua
        self.cp_agua = 4186  # J/(kg·K)
        self.calor_latente_vaporizacion = 2.26e6  # J/kg
        self.temp_inicial = 293  # K (20°C)
        self.temp_ebullicion = 368  # K (95°C)
        self.delta_T = self.temp_ebullicion - self.temp_inicial  # K
        
        # Energía requerida para 2 kg de agua
        self.energia_calentamiento = 2 * self.cp_agua * self.delta_T  # J
        self.energia_evaporacion = 2 * self.calor_latente_vaporizacion  # J
        self.energia_total_requerida = self.energia_calentamiento + self.energia_evaporacion  # J
        self.energia_por_kg = self.energia_total_requerida / 2  # J/kg
        
        # Tiempo de operación
        self.horas_radiacion_util = 6  # horas
        self.segundos_radiacion_util = self.horas_radiacion_util * 3600  # segundos

# Función para simular radiación solar diaria durante un año
def generar_radiacion_solar_anual():
    # Generar fechas para un año
    fecha_inicio = datetime(2024, 1, 1)
    fechas = [fecha_inicio + timedelta(days=i) for i in range(365)]
    
    # Modelo de radiación solar basado en la época del año
    # Variación sinusoidal con máximo en verano y mínimo en invierno
    mes = np.array([fecha.month for fecha in fechas])
    
    # Para hemisferio norte (ajustar según ubicación)
    radiacion_base = 500  # W/m²
    amplitud = 350  # W/m²
    fase = (mes - 6) * (2 * np.pi / 12)  # Máximo en junio/julio (mes 6-7)
    radiacion_media = radiacion_base + amplitud * np.cos(fase)
    
    # Añadir variabilidad diaria (clima, nubes, etc.)
    variabilidad = np.random.normal(0, 100, len(fechas))
    radiacion = radiacion_media + variabilidad
    
    # Asegurar que la radiación esté en el rango realista (100-950 W/m²)
    radiacion = np.clip(radiacion, 100, 950)
    
    return pd.DataFrame({
        'fecha': fechas,
        'radiacion_Wm2': radiacion,
        'mes': mes,
        'dia': [fecha.day for fecha in fechas]
    })

# Función para calcular la producción de agua diaria
def calcular_produccion_agua(radiacion, parametros):
    # Energía solar útil captada
    energia_solar_util = (radiacion * 
                         parametros.absorptividad * 
                         parametros.cos_angulo * 
                         parametros.area_captacion * 
                         parametros.segundos_radiacion_util)  # J
    
    # Producción de agua (kg) limitada por la energía disponible
    produccion_maxima = energia_solar_util / parametros.energia_por_kg
    
    # Factor de eficiencia del sistema (condiciones ideales pero realistas)
    # Consideramos pérdidas por conducción, convección y radiación
    eficiencia_sistema = np.where(radiacion >= 800, 0.80,
                        np.where(radiacion >= 600, 0.70,
                        np.where(radiacion >= 400, 0.55, 0.35)))
    
    # Producción real considerando la eficiencia
    produccion_real_kg = produccion_maxima * eficiencia_sistema
    
    # Convertir a litros (1 kg de agua = 1 litro aproximadamente)
    produccion_real_litros = produccion_real_kg
    
    return produccion_real_litros

# Simular el sistema durante un año
def simular_desalinizador_anual():
    # Inicializar parámetros
    params = ParametrosDesalinizador()
    
    # Generar datos de radiación solar
    df_radiacion = generar_radiacion_solar_anual()
    
    # Calcular producción diaria
    df_radiacion['produccion_litros'] = calcular_produccion_agua(
        df_radiacion['radiacion_Wm2'], params)
    
    # Calcular GOR (Gain Output Ratio)
    # GOR = Energía de evaporación / Energía solar total incidente
    df_radiacion['energia_evaporacion'] = df_radiacion['produccion_litros'] * params.calor_latente_vaporizacion
    df_radiacion['energia_solar_total'] = (df_radiacion['radiacion_Wm2'] * 
                                          params.area_captacion * 
                                          params.segundos_radiacion_util)
    df_radiacion['GOR'] = df_radiacion['energia_evaporacion'] / df_radiacion['energia_solar_total']
    
    return df_radiacion

# Función para visualizar los resultados
def visualizar_resultados(df_resultados):
    # Configurar estilo de gráficas
    plt.style.use('seaborn-v0_8-darkgrid')
    plt.figure(figsize=(14, 18))
    
    # 1. Producción diaria a lo largo del año
    plt.subplot(3, 1, 1)
    plt.plot(df_resultados['fecha'], df_resultados['produccion_litros'], color='blue', linewidth=1.5)
    plt.title('Producción Diaria de Agua Desalinizada', fontsize=16)
    plt.ylabel('Litros', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)
    
    # 2. Radiación solar a lo largo del año
    plt.subplot(3, 1, 2)
    plt.plot(df_resultados['fecha'], df_resultados['radiacion_Wm2'], color='orange', linewidth=1.5)
    plt.title('Radiación Solar Diaria', fontsize=16)
    plt.ylabel('W/m²', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)
    
    # 3. Eficiencia del sistema (GOR)
    plt.subplot(3, 1, 3)
    plt.plot(df_resultados['fecha'], df_resultados['GOR'], color='green', linewidth=1.5)
    plt.title('Gain Output Ratio (GOR)', fontsize=16)
    plt.ylabel('GOR', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)
    
    plt.tight_layout()
    plt.savefig('resultados_desalinizador_anual.png', dpi=300, bbox_inches='tight')
    
    # Estadísticas mensuales
    df_mensual = df_resultados.groupby('mes').agg({
        'produccion_litros': 'sum',
        'radiacion_Wm2': 'mean',
        'GOR': 'mean'
    }).reset_index()
    
    nombres_meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 
                     'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
    df_mensual['nombre_mes'] = df_mensual['mes'].apply(lambda x: nombres_meses[x-1])
    
    # Gráfica de producción mensual
    plt.figure(figsize=(14, 8))
    plt.bar(df_mensual['nombre_mes'], df_mensual['produccion_litros'], color='blue')
    plt.title('Producción Mensual de Agua Desalinizada (Litros)', fontsize=16)
    plt.ylabel('Litros', fontsize=12)
    plt.grid(True, axis='y', linestyle='--', alpha=0.7)
    plt.xticks(rotation=45)
    plt.savefig('produccion_mensual_desalinizador.png', dpi=300, bbox_inches='tight')
    
    # Guardar resultados en CSV
    df_resultados.to_csv('datos_desalinizador_anual.csv', index=False)
    df_mensual.to_csv('datos_desalinizador_mensual.csv', index=False)
    
    return df_mensual

# Ejecutar simulación
if __name__ == "__main__":
    print("Iniciando simulación del desalinizador solar...")
    df_resultados = simular_desalinizador_anual()
    df_mensual = visualizar_resultados(df_resultados)
    
    # Mostrar estadísticas anuales
    produccion_anual = df_resultados['produccion_litros'].sum()
    produccion_media_diaria = df_resultados['produccion_litros'].mean()
    radiacion_media = df_resultados['radiacion_Wm2'].mean()
    gor_medio = df_resultados['GOR'].mean()
    
    print(f"\nESTADÍSTICAS ANUALES DEL DESALINIZADOR SOLAR")
    print(f"============================================")
    print(f"Producción total anual: {produccion_anual:.2f} litros")
    print(f"Producción media diaria: {produccion_media_diaria:.2f} litros/día")
    print(f"Radiación solar media: {radiacion_media:.2f} W/m²")
    print(f"GOR (Gain Output Ratio) medio: {gor_medio:.4f}")
    
    # Días de alta y baja producción
    dias_alta_produccion = len(df_resultados[df_resultados['produccion_litros'] > produccion_media_diaria])
    dias_baja_produccion = len(df_resultados[df_resultados['produccion_litros'] < produccion_media_diaria/2])
    
    print(f"\nDías con producción superior a la media: {dias_alta_produccion}")
    print(f"Días con producción inferior a la mitad de la media: {dias_baja_produccion}")
    
    # Producción por estaciones
    print(f"\nPRODUCCIÓN POR MESES")
    print(f"===================")
    for _, row in df_mensual.iterrows():
        print(f"{row['nombre_mes']}: {row['produccion_litros']:.2f} litros") 