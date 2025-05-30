# Simulador Termodinámico de Desalinizador Solar

## Descripción General

Este proyecto implementa un modelo termodinámico avanzado para la simulación de un desalinizador solar, permitiendo estudiar su comportamiento bajo diferentes condiciones climáticas a lo largo del año. El simulador incorpora principios termodinámicos como transferencia de calor por conducción, convección y radiación, evaporación, condensación y eficiencia energética.

![Desalinizador Solar](https://via.placeholder.com/800x400?text=Modelo+de+Desalinizador+Solar)

## Características Principales

- **Modelo Físico Completo**: Simulación basada en principios termodinámicos reales
- **Variación Estacional**: Análisis de rendimiento considerando cambios climáticos a lo largo del año
- **Visualización Avanzada**: Generación de gráficas detalladas del comportamiento del sistema
- **Reporte Web Interactivo**: Interfaz HTML para examinar resultados de forma visual
- **Informes Ejecutivos**: Generación automática de reportes en formato Markdown
- **Personalizable**: Arquitectura modular que permite modificar parámetros y componentes

## Estructura del Proyecto

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
└── README.md                                 # Esta documentación
```

## Requisitos del Sistema

### Dependencias

- Python 3.7+
- Bibliotecas:
  - numpy
  - pandas
  - matplotlib
  - scipy

### Instalación

1. Clone el repositorio:
   ```
   git clone https://github.com/usuario/simulador-desalinizador-solar.git
   cd simulador-desalinizador-solar
   ```

2. Instale las dependencias requeridas:
   ```
   pip install numpy pandas matplotlib scipy
   ```

## Uso del Simulador

### Ejecución Básica

Para ejecutar la simulación completa con los parámetros predeterminados:

```bash
python script_ejecutar_todo.py
```

Este comando:
1. Ejecutará la simulación termodinámica
2. Generará todos los gráficos en la carpeta `resultados/`
3. Actualizará el reporte web
4. Creará un informe ejecutivo en `informe_ejecutivo.md`

### Opciones de Ejecución

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

## Personalización del Modelo

### Modificación de Parámetros

Para personalizar el comportamiento del desalinizador, edite el archivo `parametros_configurables.py`. Las principales categorías de parámetros son:

1. **Dimensiones físicas**: Tamaño, área de captación, volumen
2. **Propiedades térmicas**: Absorptividad, emisividad, ángulo de incidencia
3. **Materiales**: Tipo de material, conductividades térmicas, espesores
4. **Condiciones de operación**: Cantidad de agua, ubicación geográfica
5. **Parámetros de simulación**: Radiación base, variabilidad climática

Ejemplo de modificación:

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
```

### Creación de Configuraciones Personalizadas

También puede crear archivos JSON de configuración y cargarlos con el parámetro `--config`:

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

## Interpretación de Resultados

### Archivos de Datos

- **datos_desalinizador_anual.csv**: Contiene datos diarios detallados (producción, radiación, temperatura, etc.)
- **datos_desalinizador_mensual.csv**: Resumen de producción y rendimiento por mes
- **informe_ejecutivo.md**: Análisis de resultados con hallazgos clave y recomendaciones

### Gráficos Generados

1. **simulacion_YYYYMM_anual.png**: Evolución de todos los parámetros a lo largo del año
2. **simulacion_YYYYMM_mensual.png**: Comparativa de producción y eficiencia por mes
3. **simulacion_YYYYMM_estacional.png**: Análisis estacional del rendimiento
4. **simulacion_YYYYMM_energia.png**: Balance energético detallado

### Reporte Web Interactivo

Para visualizar el reporte web, abra el archivo `reporte_anual_desalinizador.html` en cualquier navegador. Este reporte incluye:

- Resumen de estadísticas anuales
- Distribución estacional de producción
- Gráficos interactivos
- Análisis de eficiencia energética
- Recomendaciones basadas en los resultados

## Extensión del Modelo

### Estructura de Clases

El simulador está organizado en tres clases principales:

1. **ParametrosDesalinizador**: Modelo físico y parámetros del sistema
2. **ModeloClimatico**: Generación de datos climáticos realistas
3. **ModeloTermico**: Cálculos termodinámicos detallados

### Adición de Nuevos Modelos

Para implementar nuevos modelos, puede extender estas clases o crear nuevas en `simulacion_desalinizador_modificable.py`. Por ejemplo:

```python
class ModeloTermicoAvanzado(ModeloTermico):
    def __init__(self, params):
        super().__init__(params)
        self.parametros_adicionales = {...}
        
    def calcular_temperatura_sistema(self, datos_climaticos):
        # Implementar modelo mejorado de cálculo de temperatura
        ...
```

### Integración con Otros Sistemas

El simulador genera datos en formatos estándar (CSV, JSON) que pueden integrarse fácilmente con otros sistemas:

- **Modelos de optimización**: Evaluar diferentes configuraciones
- **Sistemas de control**: Simular estrategias de control adaptativo
- **Análisis económicos**: Calcular retorno de inversión

## Limitaciones Conocidas

- El modelo asume condiciones simplificadas de condensación
- No considera efectos de ensuciamiento o degradación de materiales
- Simplifica algunos aspectos de la transferencia de masa entre agua y vapor

## Contribuciones y Desarrollo Futuro

Áreas para mejorar el simulador:

- Implementación de modelos de condensación más sofisticados
- Integración con datos climáticos reales (APIs meteorológicas)
- Optimización automática de parámetros de diseño
- Interfaz gráfica para configuración y análisis

## Licencia

Este proyecto está licenciado bajo [MIT License](LICENSE).

## Contacto

Para consultas o contribuciones:
- Email: carlos06221@gmail.com
- Autor: Carlos Guillermo Porras
- GitHub: [[usuario/simulador-desalinizador-solar](https://github.com/usuario/simulador-desalinizador-solar)](https://github.com/DD33KKY/Simulacion-de-Salinizadorr?tab=readme-ov-file)

---

Desarrollado como parte del proyecto de modelado termodinámico de desalinizadores solares (2024). 
