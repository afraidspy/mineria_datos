
from ArbolID3 import ArbolID3

datos = [
    {"Pronóstico": "Soleado", "Temperatura": "Caluroso", "Humedad": "Alta", "Viento": "Débil", "¿Se juega?": "No"},
    {"Pronóstico": "Soleado", "Temperatura": "Caluroso", "Humedad": "Alta", "Viento": "Fuerte", "¿Se juega?": "No"},
    {"Pronóstico": "Nublado", "Temperatura": "Caluroso", "Humedad": "Alta", "Viento": "Débil", "¿Se juega?": "Sí"},
    {"Pronóstico": "Lluvia", "Temperatura": "Templado", "Humedad": "Alta", "Viento": "Débil", "¿Se juega?": "Sí"},
    {"Pronóstico": "Lluvia", "Temperatura": "Fresco", "Humedad": "Normal", "Viento": "Débil", "¿Se juega?": "Sí"},
    {"Pronóstico": "Lluvia", "Temperatura": "Fresco", "Humedad": "Normal", "Viento": "Fuerte", "¿Se juega?": "No"},
    {"Pronóstico": "Nublado", "Temperatura": "Fresco", "Humedad": "Normal", "Viento": "Fuerte", "¿Se juega?": "Sí"},
    {"Pronóstico": "Soleado", "Temperatura": "Templado", "Humedad": "Alta", "Viento": "Fuerte", "¿Se juega?": "No"},
    {"Pronóstico": "Soleado", "Temperatura": "Fresco", "Humedad": "Normal", "Viento": "Débil", "¿Se juega?": "Sí"},
    {"Pronóstico": "Lluvia", "Temperatura": "Templado", "Humedad": "Normal", "Viento": "Débil", "¿Se juega?": "Sí"},
    {"Pronóstico": "Soleado", "Temperatura": "Templado", "Humedad": "Normal", "Viento": "Débil", "¿Se juega?": "Sí"},
    {"Pronóstico": "Nublado", "Temperatura": "Templado", "Humedad": "Alta", "Viento": "Fuerte", "¿Se juega?": "Sí"},
    {"Pronóstico": "Nublado", "Temperatura": "Caluroso", "Humedad": "Normal", "Viento": "Débil", "¿Se juega?": "Sí"},
    {"Pronóstico": "Lluvia", "Temperatura": "Templado", "Humedad": "Alta", "Viento": "Fuerte", "¿Se juega?": "No"},
]

arbol = ArbolID3()
arbol.ajustar(datos, "¿Se juega?")
arbol.imprimir_ganancias(datos)
print()
print("Árbol generado:")
arbol.imprimir_arbol()