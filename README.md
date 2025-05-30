# Simulador Termodinámico de Desalinizador Solar

![Versión](https://img.shields.io/badge/versión-1.0.0-blue.svg)
![Licencia](https://img.shields.io/badge/licencia-MIT-green.svg)

## Descripción General

Este proyecto implementa un modelo termodinámico avanzado para la simulación de un desalinizador solar, permitiendo estudiar su comportamiento bajo diferentes condiciones climáticas a lo largo del año. El simulador incorpora principios termodinámicos como transferencia de calor por conducción, convección y radiación, evaporación, condensación y eficiencia energética.

Este software está diseñado para investigadores, estudiantes y profesionales interesados en tecnologías de desalinización solar y energías renovables.

![Desalinizador Solar](https://via.placeholder.com/800x400?text=Modelo+de+Desalinizador+Solar)

## 🚀 Inicio Rápido

Para comenzar a utilizar el simulador inmediatamente:

1. **Instalación**:
   ```bash
   # Clonar el repositorio
   git clone https://github.com/usuario/simulador-desalinizador-solar.git
   cd simulador-desalinizador-solar
   
   # Instalar dependencias
   pip install -r requirements.txt
   ```

2. **Ejecutar Simulación Estándar**:
   ```bash
   python script_ejecutar_todo.py
   ```

3. **Ver Resultados**:
   - Abra el archivo `reporte_anual_desalinizador.html` en su navegador
   - Examine el informe ejecutivo en `informe_ejecutivo.md`
   - Explore los gráficos generados en la carpeta `resultados/`

## 🔍 Características Principales

- **Modelo Físico Completo**: Simulación basada en principios termodinámicos reales
- **Variación Estacional**: Análisis de rendimiento considerando cambios climáticos a lo largo del año
- **Visualización Avanzada**: Generación de gráficas detalladas del comportamiento del sistema
- **Reporte Web Interactivo**: Interfaz HTML para examinar resultados de forma visual
- **Informes Ejecutivos**: Generación automática de reportes en formato Markdown
- **Personalizable**: Arquitectura modular que permite modificar parámetros y componentes

## 📋 Estructura del Proyecto

```
.
├── simulacion_desalinizador_modificable.py   # Modelo termodinámico principal
├── parametros_configurables.py               # Configuración de parámetros físicos
├── actualizar_datos_reporte.py               # Integrador de datos para reportes
├── reporte_anual_desalinizador.html          # Interfaz web para visualización
├── script_ejecutar_todo.py                   # Script principal de ejecución
├── resultados/                               # Carpeta con gráficos generados
│   ├── simulacion_YYYYMM_anual.png          
│   ├── simulacion_YYYYMM_mensual.png        
│   ├── simulacion_YYYYMM_estacional.png     
│   └── simulacion_YYYYMM_energia.png        
├── datos_desalinizador_anual.csv             # Datos diarios de la simulación
├── datos_desalinizador_mensual.csv           # Resumen mensual de resultados
├── datos_simulacion.js                       # Datos para el reporte web
├── informe_ejecutivo.md                      # Informe de resultados en Markdown
├── requirements.txt                          # Dependencias del proyecto
├── LICENSE                                   # Licencia MIT
└── README.md                                 # Esta documentación
```

## ⚙️ Requisitos del Sistema

### Dependencias

- Python 3.7+
- Bibliotecas:
  - numpy >= 1.20.0
  - pandas >= 1.3.0
  - matplotlib >= 3.4.0
  - scipy >= 1.7.0

### Instalación

1. Clone el repositorio:
   ```bash
   git clone https://github.com/usuario/simulador-desalinizador-solar.git
   cd simulador-desalinizador-solar
   ```

2. Instale las dependencias requeridas:
   ```bash
   pip install -r requirements.txt
   ```

## 📖 Guía de Uso

### Ejecución Básica

Para ejecutar la simulación completa con los parámetros predeterminados:

```bash
python script_ejecutar_todo.py
```

Este comando realizará el proceso completo:
1. Ejecutará la simulación termodinámica
2. Generará todos los gráficos en la carpeta `resultados/`
3. Actualizará el reporte web
4. Creará un informe ejecutivo en `informe_ejecutivo.md`

Al finalizar la ejecución, se le preguntará si desea abrir el reporte en su navegador web. Responda `s` para verlo inmediatamente.

### Opciones de Ejecución Avanzada

El simulador principal (`simulacion_desalinizador_modificable.py`) acepta los siguientes argumentos:

```bash
python simulacion_desalinizador_modificable.py [opciones]

Opciones:
  -c, --config ARCHIVO    Ruta al archivo de configuración JSON
  -v, --visualizar        Mostrar gráficas durante la ejecución
  -g, --guardar           Guardar configuración actual como archivo JSON
  -p, --parametros        Mostrar parámetros actuales y salir
  -i, --informe           Generar informe ejecutivo en formato markdown
```

#### Ejemplos de uso

1. **Mostrar parámetros actuales**:
   ```bash
   python simulacion_desalinizador_modificable.py --parametros
   ```

2. **Usar configuración personalizada**:
   ```bash
   python simulacion_desalinizador_modificable.py --config mi_configuracion.json --visualizar
   ```

3. **Generar informe y guardar configuración**:
   ```bash
   python simulacion_desalinizador_modificable.py --informe --guardar
   ```

## 🔧 Personalización del Modelo

### Modificación de Parámetros Básicos

Para personalizar el comportamiento del desalinizador, edite el archivo `parametros_configurables.py`. Las principales categorías de parámetros son:

1. **Dimensiones físicas**: Tamaño, área de captación, volumen
2. **Propiedades térmicas**: Absorptividad, emisividad, ángulo de incidencia
3. **Materiales**: Tipo de material, conductividades térmicas, espesores
4. **Condiciones de operación**: Cantidad de agua, ubicación geográfica
5. **Parámetros de simulación**: Radiación base, variabilidad climática

#### Ejemplo de modificación:

```python
# En parametros_configurables.py
DIMENSIONES = {
    'largo': 0.5,      # Aumentar el largo a 50 cm
    'ancho': 0.3,      # Aumentar el ancho a 30 cm
    'altura': 0.15     # Aumentar la altura a 15 cm
}

PROPIEDADES_TERMICAS = {
    'absorptividad': 0.95,  # Mayor absorptividad (material más oscuro)
    'angulo_incidencia': 25  # Mejor ángulo de incidencia
}

# Cambiar la ubicación geográfica
CONDICIONES_OPERACION = {
    'masa_agua': 1.0,            # kg
    'horas_radiacion_util': 6,   # horas
    'hemisferio': 'norte',       # 'norte' o 'sur'
    'ubicacion_latitud': 40.5    # latitud en grados (Madrid: ~40.5)
}
```

### Creación de Configuraciones Personalizadas

También puede crear archivos JSON de configuración completa y cargarlos con el parámetro `--config`:

```json
{
  "dimensiones": {
    "largo": 0.5,
    "ancho": 0.3,
    "altura": 0.15
  },
  "propiedades_termicas": {
    "absorptividad": 0.95,
    "angulo_incidencia": 25,
    "material_caja": "aluminio"
  },
  "conductividades_termicas": {
    "aluminio": 205,
    "acero": 50.2,
    "cobre": 385
  },
  "condiciones_operacion": {
    "masa_agua": 1.5,
    "hemisferio": "norte",
    "ubicacion_latitud": 40.5
  },
  "parametros_simulacion": {
    "radiacion_base": 550,
    "amplitud_variacion": 350,
    "variabilidad_diaria": 150
  }
}
```

Para usar esta configuración:

```bash
python simulacion_desalinizador_modificable.py --config mi_configuracion.json
```

O con el script principal:

```bash
python script_ejecutar_todo.py --config mi_configuracion.json
```

### Simulación de Diferentes Condiciones Climáticas

Para simular diferentes condiciones climáticas, puede modificar los siguientes parámetros en `parametros_configurables.py` o en su archivo JSON:

```python
PARAMETROS_SIMULACION = {
    'radiacion_base': 550,         # Radiación solar media anual (W/m²)
    'amplitud_variacion': 350,     # Variación estacional (W/m²)
    'variabilidad_diaria': 150     # Variabilidad diaria (desv. estándar, W/m²)
}
```

#### Escenarios comunes:

1. **Clima ecuatorial**: Baja amplitud, alta radiación base
   ```python
   'radiacion_base': 700,
   'amplitud_variacion': 100,
   ```

2. **Clima nórdico**: Alta amplitud, baja radiación base
   ```python
   'radiacion_base': 350,
   'amplitud_variacion': 500,
   ```

3. **Clima desértico**: Alta radiación, alta variabilidad
   ```python
   'radiacion_base': 800,
   'amplitud_variacion': 200,
   'variabilidad_diaria': 250
   ```

## 📊 Interpretación de Resultados

### Archivos de Datos Generados

- **datos_desalinizador_anual.csv**: Contiene datos diarios detallados
  ```
  fecha,mes,dia,radiacion_Wm2,temp_ambiente_C,temp_agua_C,produccion_litros,GOR,...
  2024-01-01,1,1,342.5,5.2,37.8,0.02,0.0035,...
  ```

- **datos_desalinizador_mensual.csv**: Resumen de producción y rendimiento por mes
  ```
  mes,nombre_mes,produccion_litros,radiacion_Wm2,GOR,eficiencia_termica,...
  1,Enero,0.31,412.7,0.0125,0.212,...
  ```

- **informe_ejecutivo.md**: Análisis de resultados con hallazgos clave y recomendaciones

### Análisis de Gráficos

1. **simulacion_YYYYMM_anual.png**:
   - **Panel superior**: Muestra la producción diaria en litros
   - **Segundo panel**: Radiación solar diaria (W/m²)
   - **Tercer panel**: Temperaturas (ambiente, agua, vidrio)
   - **Cuarto panel**: Humedad relativa y velocidad del viento
   - **Quinto panel**: Eficiencia (GOR)
   - **Panel inferior**: Pérdidas térmicas

   **Interpretación**: Busque correlaciones entre los picos de radiación solar y producción. Observe cómo las temperaturas afectan la eficiencia.

2. **simulacion_YYYYMM_mensual.png**:
   - Producción mensual en barras
   - Temperaturas medias mensuales
   - Eficiencia mensual (GOR)
   
   **Interpretación**: Identifique los meses más productivos y su relación con las temperaturas medias.

3. **simulacion_YYYYMM_estacional.png**:
   - Distribución de producción por estación
   - Comparativa de temperatura y eficiencia por estación
   
   **Interpretación**: Analice qué estaciones son óptimas para la operación del sistema.

4. **simulacion_YYYYMM_energia.png**:
   - Balance energético mensual (energía solar, útil y evaporación)
   - Relación radiación-producción
   - Pérdidas térmicas vs producción

   **Interpretación**: Evalúe las pérdidas energéticas del sistema y dónde se podrían implementar mejoras.

### Reporte Web Interactivo

Para visualizar el reporte web, abra el archivo `reporte_anual_desalinizador.html` en cualquier navegador. Este reporte incluye:

- Resumen de estadísticas anuales (producción total, eficiencia)
- Distribución estacional de producción con indicadores de rendimiento
- Gráficos interactivos de producción mensual
- Análisis detallado de eficiencia energética
- Tabla completa de datos mensuales
- Recomendaciones basadas en los resultados de la simulación

**Consejo**: Use la función de zoom de su navegador para examinar en detalle las gráficas del reporte.

## 🔬 Extensión del Modelo

### Estructura de Clases

El simulador está organizado en tres clases principales:

1. **ParametrosDesalinizador**: Modelo físico y parámetros del sistema
   ```python
   # Ejemplo de acceso a parámetros
   params = ParametrosDesalinizador()
   area_captacion = params.area_captacion
   energia_requerida = params.energia_total_requerida
   ```

2. **ModeloClimatico**: Generación de datos climáticos realistas
   ```python
   # Ejemplo de generación de datos climáticos personalizados
   clima = ModeloClimatico(params)
   df_clima = clima.generar_datos_anuales()
   ```

3. **ModeloTermico**: Cálculos termodinámicos detallados
   ```python
   # Ejemplo de uso del modelo térmico
   modelo = ModeloTermico(params)
   df_temp = modelo.calcular_temperatura_sistema(df_clima)
   df_perdidas = modelo.calcular_perdidas_termicas(df_temp)
   ```

### Adición de Nuevos Modelos

Para implementar nuevos modelos, puede extender estas clases o crear nuevas en `simulacion_desalinizador_modificable.py`. Por ejemplo:

```python
class ModeloTermicoAvanzado(ModeloTermico):
    def __init__(self, params):
        super().__init__(params)
        self.parametros_adicionales = {
            'factor_turbulencia': 0.15,
            'coef_mejora_condensacion': 1.2
        }
        
    def calcular_temperatura_sistema(self, datos_climaticos):
        # Implementar modelo mejorado de cálculo de temperatura
        df = super().calcular_temperatura_sistema(datos_climaticos)
        
        # Agregar cálculos adicionales
        df['temp_mejorada'] = df['temp_agua_K'] * self.parametros_adicionales['coef_mejora_condensacion']
        
        return df
```

### Integración con Otros Sistemas

El simulador genera datos en formatos estándar (CSV, JSON) que pueden integrarse fácilmente con otros sistemas:

- **Modelos de optimización**: Evaluar diferentes configuraciones
  ```python
  import pandas as pd
  from simulacion_desalinizador_modificable import simular_desalinizador_anual
  
  # Ejecutar simulación con diferentes configuraciones
  resultados = []
  for angulo in range(20, 46, 5):
      # Modificar configuración
      config = {'propiedades_termicas': {'angulo_incidencia': angulo}}
      # Ejecutar simulación
      df = simular_desalinizador_anual(config)
      # Guardar resultado
      resultados.append({
          'angulo': angulo,
          'produccion_total': df['produccion_litros'].sum(),
          'eficiencia_media': df['eficiencia_termica'].mean()
      })
  
  # Analizar resultados
  df_resultados = pd.DataFrame(resultados)
  angulo_optimo = df_resultados.loc[df_resultados['produccion_total'].idxmax()]['angulo']
  print(f"Ángulo óptimo: {angulo_optimo}°")
  ```

- **Sistemas de control**: Simular estrategias de control adaptativo
- **Análisis económicos**: Calcular retorno de inversión

## ❓ Problemas Comunes y Soluciones

### Errores de instalación

**Problema**: Error al instalar dependencias
```
ERROR: Could not find a version that satisfies the requirement numpy>=1.20.0
```

**Solución**: Actualice pip e intente nuevamente
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### Errores durante la ejecución

**Problema**: Se muestra "Error: No se encontró el archivo 'parametros_configurables.py'"

**Solución**: Verifique que está ejecutando el script desde el directorio raíz del proyecto y que el nombre del archivo es correcto (verifique mayúsculas/minúsculas).

**Problema**: No se generan todos los gráficos esperados

**Solución**: Compruebe que tiene permisos de escritura en la carpeta `resultados/` y que todas las dependencias están correctamente instaladas.

**Problema**: El reporte HTML muestra "---" en lugar de valores numéricos

**Solución**: Verifique que se ha ejecutado correctamente `actualizar_datos_reporte.py` después de la simulación y que `datos_simulacion.js` se ha generado correctamente.

### Personalización

**Problema**: Cambios en `parametros_configurables.py` no tienen efecto

**Solución**: Asegúrese de guardar el archivo antes de ejecutar la simulación y verifique que esté editando el archivo correcto.

**Problema**: Los resultados parecen poco realistas

**Solución**: Revise los parámetros configurados. Para valores realistas:
- Radiación solar diaria: entre 200-900 W/m²
- Eficiencia térmica: normalmente entre 20-40%
- Temperatura del agua: no debe superar 95°C

## 🛠️ Contribuciones y Desarrollo Futuro

Áreas para mejorar el simulador:

- Implementación de modelos de condensación más sofisticados
- Integración con datos climáticos reales (APIs meteorológicas)
- Optimización automática de parámetros de diseño
- Interfaz gráfica para configuración y análisis

Para contribuir al proyecto:
1. Fork el repositorio
2. Cree una rama para su función (`git checkout -b feature/nueva-funcion`)
3. Commit sus cambios (`git commit -m 'Añadir nueva función'`)
4. Push a la rama (`git push origin feature/nueva-funcion`)
5. Abra un Pull Request

## 📜 Licencia

Este proyecto está licenciado bajo [MIT License](LICENSE).

## 📞 Contacto

Para consultas o contribuciones:
- Email: carlos06221@gmail.com
- Autor: Carlos Guillermo Porras
- GitHub: https://github.com/DD33KKY/Simulacion-de-Salinizadorr?tab=readme-ov-file

---

Desarrollado como parte del proyecto de modelado termodinámico de desalinizadores solares (2025). 
