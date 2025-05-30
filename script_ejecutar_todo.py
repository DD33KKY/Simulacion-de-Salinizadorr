#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Script para ejecutar la simulación completa del prototipo de desalinización solar.
Este script ejecuta todas las partes del proceso de simulación:
1. Simulación termodinámica avanzada del prototipo durante un año
2. Generación de gráficas detalladas y datos de rendimiento
3. Actualización del reporte HTML con los datos generados
4. Análisis avanzado de rendimiento por estación y balance energético
"""

import os
import sys
import time
from datetime import datetime
import importlib.util
import shutil

def verificar_dependencias():
    """Verifica que todas las dependencias necesarias estén instaladas"""
    dependencias = ['numpy', 'pandas', 'matplotlib', 'scipy']
    faltantes = []
    
    for dep in dependencias:
        if importlib.util.find_spec(dep) is None:
            faltantes.append(dep)
    
    if faltantes:
        print("\n⚠️  ADVERTENCIA: Faltan algunas dependencias necesarias.")
        print("Por favor, instale las siguientes bibliotecas con pip:")
        print(f"    pip install {' '.join(faltantes)}")
        return False
    
    return True

def ejecutar_simulacion_avanzada():
    """Ejecuta el script de simulación termodinámica avanzada"""
    print("\n🔄 Iniciando simulación termodinámica avanzada del desalinizador solar...")
    start_time = time.time()
    
    try:
        # Importar y ejecutar el módulo de simulación avanzada
        spec = importlib.util.spec_from_file_location(
            "simulacion_desalinizador_modificable", 
            "simulacion_desalinizador_modificable.py"
        )
        simulacion = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(simulacion)
        
        # La simulación ya se ejecuta al importar el módulo debido a la estructura del script
        
        # Forzar la generación del informe ejecutivo si hay una función disponible para ello
        if hasattr(simulacion, 'generar_informe_ejecutivo') and hasattr(simulacion, 'simular_desalinizador_anual'):
            try:
                # Intentar ejecutar con acceso a las variables globales del módulo
                if hasattr(simulacion, 'df_resultados') and hasattr(simulacion, 'df_mensual') and hasattr(simulacion, 'df_estacional'):
                    simulacion.generar_informe_ejecutivo(simulacion.df_resultados, simulacion.df_mensual, simulacion.df_estacional)
                    print("\n✅ Informe ejecutivo generado correctamente.")
            except Exception as e:
                print(f"\n⚠️ No se pudo generar automáticamente el informe ejecutivo: {str(e)}")
                print("El informe ejecutivo depende de la ejecución previa de la simulación.")
        
        elapsed_time = time.time() - start_time
        print(f"\n✅ Simulación termodinámica avanzada completada en {elapsed_time:.2f} segundos.")
        return True
    
    except Exception as e:
        print(f"\n❌ Error al ejecutar la simulación avanzada: {str(e)}")
        return False

def actualizar_reporte():
    """Actualiza el reporte web con los datos de simulación"""
    print("\n🔄 Actualizando reporte web con datos de simulación termodinámica...")
    
    try:
        # Importar y ejecutar el módulo de actualización de reporte
        spec = importlib.util.spec_from_file_location("actualizar_datos_reporte", "actualizar_datos_reporte.py")
        actualizar = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(actualizar)
        
        # Ejecutar la función principal del módulo
        actualizar.actualizar_datos_reporte()
        
        print("\n✅ Reporte web actualizado correctamente.")
        return True
    
    except Exception as e:
        print(f"\n❌ Error al actualizar el reporte web: {str(e)}")
        return False

def mover_archivos_a_resultados():
    """Mueve los archivos de gráficos a la carpeta de resultados"""
    archivos_a_mover = [
        'resultados_desalinizador_anual.png',
        'produccion_mensual_desalinizador.png',
    ]
    
    # Crear carpeta de resultados si no existe
    if not os.path.exists('resultados'):
        os.makedirs('resultados')
        print("Se creó el directorio 'resultados' para almacenar las gráficas")
    
    # Generar nombre para el mes actual
    fecha_actual = datetime.now()
    mes_actual = fecha_actual.strftime('%Y%m')
    timestamp = fecha_actual.strftime('%Y%m%d_%H%M')
    
    # Mover y renombrar los archivos
    archivos_movidos = []
    for archivo in archivos_a_mover:
        if os.path.exists(archivo):
            # Determinar nuevos nombres (con timestamp y sin timestamp)
            nuevo_nombre_timestamp = f"simulacion_{timestamp}_" + archivo.split('_')[-1]
            nuevo_nombre_simple = f"simulacion_{mes_actual}_" + archivo.split('_')[-1]
            
            destino_timestamp = os.path.join('resultados', nuevo_nombre_timestamp)
            destino_simple = os.path.join('resultados', nuevo_nombre_simple)
            
            # Si ya existe un archivo con ese nombre, eliminarlo
            if os.path.exists(destino_timestamp):
                os.remove(destino_timestamp)
            if os.path.exists(destino_simple):
                os.remove(destino_simple)
                
            # Mover archivo con timestamp
            shutil.move(archivo, destino_timestamp)
            # Crear copia con nombre simple para el HTML
            shutil.copy2(destino_timestamp, destino_simple)
            archivos_movidos.append((archivo, destino_simple))
    
    # Crear un gráfico de análisis energético si no existe
    archivo_energia = f"simulacion_{mes_actual}_energia.png"
    destino_energia = os.path.join('resultados', archivo_energia)
    
    # Buscar archivos de energía recientes
    archivos_energia = [f for f in os.listdir('resultados') if f.endswith('_energia.png')]
    if archivos_energia:
        # Ordenar por fecha de modificación (más reciente primero)
        archivos_energia.sort(key=lambda x: os.path.getmtime(os.path.join('resultados', x)), reverse=True)
        # Copiar el más reciente con el nombre simple
        shutil.copy2(os.path.join('resultados', archivos_energia[0]), destino_energia)
        print(f"✅ Copiado archivo de análisis energético como: {destino_energia}")
    else:
        # Si no encontramos archivos existentes, intentar generarlos
        try:
            # Si existe una función para generar el gráfico, importarla y ejecutarla
            spec = importlib.util.spec_from_file_location("simulacion_desalinizador_modificable", "simulacion_desalinizador_modificable.py")
            simulacion = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(simulacion)
            
            # Verificar si existe la función para generar el gráfico de energía
            if hasattr(simulacion, "generar_grafico_energia"):
                simulacion.generar_grafico_energia(destino_energia)
                print(f"✅ Generado gráfico de análisis energético: {destino_energia}")
        except Exception as e:
            print(f"⚠️ No se pudo generar el gráfico de energía: {str(e)}")
    
    # Buscar archivo estacional y copiarlo con nombre simple si existe
    archivo_estacional = f"simulacion_{mes_actual}_estacional.png"
    destino_estacional = os.path.join('resultados', archivo_estacional)
    archivos_estacional = [f for f in os.listdir('resultados') if f.endswith('_estacional.png')]
    if archivos_estacional:
        # Ordenar por fecha de modificación (más reciente primero)
        archivos_estacional.sort(key=lambda x: os.path.getmtime(os.path.join('resultados', x)), reverse=True)
        # Copiar el más reciente con el nombre simple
        shutil.copy2(os.path.join('resultados', archivos_estacional[0]), destino_estacional)
        print(f"✅ Copiado archivo de análisis estacional como: {destino_estacional}")
    
    if archivos_movidos:
        print("\n✅ Archivos procesados para el reporte web:")
        for origen, destino in archivos_movidos:
            print(f"    {origen} → {destino}")
    
    return True

def verificar_archivos_generados():
    """Verifica que todos los archivos necesarios hayan sido generados"""
    archivos_esperados = [
        'datos_desalinizador_anual.csv',
        'datos_desalinizador_mensual.csv',
        'datos_simulacion.js',
        'reporte_anual_desalinizador.html'
    ]
    
    # Fecha actual para verificar archivos en la carpeta resultados
    fecha_actual = datetime.now()
    mes_actual = fecha_actual.strftime('%Y%m')
    
    archivos_resultados = [
        os.path.join('resultados', f'simulacion_{mes_actual}_anual.png'),
        os.path.join('resultados', f'simulacion_{mes_actual}_mensual.png')
    ]
    
    archivos_esperados.extend(archivos_resultados)
    
    archivos_faltantes = [archivo for archivo in archivos_esperados if not os.path.exists(archivo)]
    
    if archivos_faltantes:
        print("\n⚠️  ADVERTENCIA: No se han generado todos los archivos esperados.")
        print("Faltan los siguientes archivos:")
        for archivo in archivos_faltantes:
            print(f"    - {archivo}")
        return False
    
    return True

def mostrar_instrucciones():
    """Muestra instrucciones para visualizar los resultados"""
    fecha_actual = datetime.now()
    mes_actual = fecha_actual.strftime('%Y%m')
    
    print("\n📊 RESULTADOS DE LA SIMULACIÓN TERMODINÁMICA AVANZADA")
    print("=" * 60)
    print("Para visualizar los resultados completos:")
    print(f"1. Abra el archivo 'reporte_anual_desalinizador.html' en su navegador web")
    print(f"   Ruta completa: {os.path.abspath('reporte_anual_desalinizador.html')}")
    print("\n2. Revise los siguientes archivos para análisis detallado:")
    print("   - datos_desalinizador_anual.csv (datos diarios)")
    print("   - datos_desalinizador_mensual.csv (resumen mensual)")
    print(f"   - resultados/simulacion_{mes_actual}_anual.png (gráficas de evolución anual)")
    print(f"   - resultados/simulacion_{mes_actual}_mensual.png (producción mensual)")
    print(f"   - resultados/simulacion_{mes_actual}_energia.png (balance energético)")

def abrir_reporte():
    """Intenta abrir automáticamente el reporte HTML"""
    reporte_path = os.path.abspath('reporte_anual_desalinizador.html')
    
    if sys.platform == 'win32':
        os.startfile(reporte_path)
    elif sys.platform == 'darwin':  # macOS
        os.system(f'open "{reporte_path}"')
    else:  # Linux y otros
        os.system(f'xdg-open "{reporte_path}"')
    
    print(f"\n✅ Abriendo reporte en su navegador predeterminado...")

def main():
    """Función principal que coordina todo el proceso"""
    print("\n" + "=" * 60)
    print("🌞 SIMULADOR TERMODINÁMICO DE DESALINIZACIÓN SOLAR")
    print("   Modelo físico avanzado con análisis estacional")
    print("=" * 60)
    
    # Verificar dependencias
    if not verificar_dependencias():
        print("\n❌ Por favor, instale las dependencias faltantes e intente de nuevo.")
        return
    
    # Ejecutar simulación
    if not ejecutar_simulacion_avanzada():
        print("\n❌ La simulación avanzada no se ha completado correctamente.")
        return
    
    # Mover archivos de gráficos a la carpeta de resultados
    mover_archivos_a_resultados()
    
    # Actualizar reporte web
    if not actualizar_reporte():
        print("\n❌ No se ha podido actualizar el reporte web.")
    
    # Verificar archivos generados
    verificar_archivos_generados()
    
    # Mostrar instrucciones
    mostrar_instrucciones()
    
    # Preguntar si desea abrir el reporte automáticamente
    respuesta = input("\n¿Desea abrir el reporte en su navegador web? (s/n): ")
    if respuesta.lower() == 's':
        abrir_reporte()
    
    print("\n✨ Proceso completado. ¡Gracias por utilizar el simulador termodinámico de desalinización solar!")
    print("=" * 60)

if __name__ == "__main__":
    main() 