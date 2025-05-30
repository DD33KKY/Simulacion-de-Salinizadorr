
// Archivo generado automáticamente por actualizar_datos_reporte.py
// Contiene los datos de la simulación del desalinizador solar

// Función para cargar los datos de simulación
function cargarDatosSimulacion() {
    console.log("Cargando datos de simulación...");
    
    // Datos generados por la simulación en Python
    datosSimulacion.produccion_total = 3.64;
    datosSimulacion.produccion_media = 0.01;
    datosSimulacion.radiacion_media = 502.15;
    datosSimulacion.gor_medio = 0.0498;
    datosSimulacion.dias_alta_produccion = 150;
    datosSimulacion.dias_baja_produccion = 185;
    
    datosSimulacion.datos_mensuales = [{"mes": "Enero", "produccion": 0.0, "radiacion": 185.8572204631529, "gor": 0.0004011204068186, "temp_agua_C": 40.708462472094055}, {"mes": "Febrero", "produccion": 0.0333547679517367, "radiacion": 314.54080173631434, "gor": 0.0176794632298636, "temp_agua_C": 46.70450879165794}, {"mes": "Marzo", "produccion": 0.2824969597408939, "radiacion": 501.5600668500476, "gor": 0.0817675738894765, "temp_agua_C": 54.36826611657093}, {"mes": "Abril", "produccion": 0.598035700347264, "radiacion": 675.2880186701308, "gor": 0.1057493104196986, "temp_agua_C": 62.7874775199475}, {"mes": "Mayo", "produccion": 0.7533357488237482, "radiacion": 790.7043680642928, "gor": 0.0962655428533991, "temp_agua_C": 67.71708391116493}, {"mes": "Junio", "produccion": 0.8061345195804375, "radiacion": 861.4676702111415, "gor": 0.0946808937373196, "temp_agua_C": 70.83028987213638}, {"mes": "Julio", "produccion": 0.669130844024418, "radiacion": 811.0956567385148, "gor": 0.0813176593281791, "temp_agua_C": 69.47198556998889}, {"mes": "Agosto", "produccion": 0.3711494167308611, "radiacion": 672.5616585674858, "gor": 0.0679756947336736, "temp_agua_C": 62.97511601403227}, {"mes": "Septiembre", "produccion": 0.1152160797572431, "radiacion": 488.04122055479127, "gor": 0.0406038525349462, "temp_agua_C": 54.60140065663317}, {"mes": "Octubre", "produccion": 0.0116715603229438, "radiacion": 331.399168160185, "gor": 0.009048011145934, "temp_agua_C": 47.23454948769632}, {"mes": "Noviembre", "produccion": 0.0, "radiacion": 224.40956585302737, "gor": 0.0001868954516122, "temp_agua_C": 43.259222468755965}, {"mes": "Diciembre", "produccion": 0.0, "radiacion": 153.32134313218188, "gor": 0.0, "temp_agua_C": 38.811453381117225}];
    datosSimulacion.datos_estacionales = {"Invierno": {"produccion": 0.0333547679517367, "gor": 0.0060268612122274, "porcentaje": 0.9162074832453256}, "Primavera": {"produccion": 1.6338684089119062, "gor": 0.09459414238752473, "porcentaje": 44.88001430707837}, "Verano": {"produccion": 1.8464147803357165, "gor": 0.08132474926639076, "porcentaje": 50.71835730850213}, "Oto\u00f1o": {"produccion": 0.1268876400801869, "gor": 0.0166129197108308, "porcentaje": 3.4854209011744492}};
    
    // Datos de análisis energético
    datosSimulacion.energia_solar = 1220.23;
    datosSimulacion.perdidas_termicas = 40.62;
    datosSimulacion.eficiencia_termica = 28.10;
    datosSimulacion.area_captacion = 0.1125;
    datosSimulacion.correlacion_rad_prod = 0.8378;
    
    // Actualizar la interfaz con los datos cargados
    actualizarInterfaz();
}
