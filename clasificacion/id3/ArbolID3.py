import math
from collections import Counter
from NodoArbol import NodoArbol

class ArbolID3:
    """
    Implementación manual del algoritmo ID3 para datos categóricos.
    """

    def __init__(self):
        self.raiz = None
        self.columna_objetivo = None
        self.clase_por_defecto = None

    def calcular_entropia(self, etiquetas):
        """
        Calcula la entropía de una lista de etiquetas.
        """
        total = len(etiquetas)
        conteos = Counter(etiquetas)

        entropia = 0.0
        for cantidad in conteos.values():
            probabilidad = cantidad / total
            entropia -= probabilidad * math.log2(probabilidad)

        return entropia

    def calcular_ganancia_informacion(self, datos, atributo):
        """
        Calcula la ganancia de información de un atributo.
        """
        etiquetas_totales = [fila[self.columna_objetivo] for fila in datos]
        entropia_total = self.calcular_entropia(etiquetas_totales)

        valores_atributo = set(fila[atributo] for fila in datos)
        entropia_ponderada = 0.0

        for valor in valores_atributo:
            subconjunto = [fila for fila in datos if fila[atributo] == valor]
            etiquetas_subconjunto = [fila[self.columna_objetivo] for fila in subconjunto]

            peso = len(subconjunto) / len(datos)
            entropia_subconjunto = self.calcular_entropia(etiquetas_subconjunto)

            entropia_ponderada += peso * entropia_subconjunto

        ganancia = entropia_total - entropia_ponderada
        return ganancia

    def obtener_clase_mayoritaria(self, datos):
        """
        Devuelve la clase más frecuente en el conjunto de datos.
        """
        etiquetas = [fila[self.columna_objetivo] for fila in datos]
        return Counter(etiquetas).most_common(1)[0][0]

    def todas_las_etiquetas_iguales(self, datos):
        """
        Verifica si todas las filas tienen la misma clase.
        """
        etiquetas = [fila[self.columna_objetivo] for fila in datos]
        return len(set(etiquetas)) == 1

    def construir_arbol(self, datos, atributos_disponibles):
        """
        Construye el árbol de decisión de forma recursiva.
        """
        etiquetas = [fila[self.columna_objetivo] for fila in datos]

        if self.todas_las_etiquetas_iguales(datos):
            return NodoArbol(clase=etiquetas[0])

        if not atributos_disponibles:
            return NodoArbol(clase=self.obtener_clase_mayoritaria(datos))

        ganancias = {}
        for atributo in atributos_disponibles:
            ganancias[atributo] = self.calcular_ganancia_informacion(datos, atributo)

        mejor_atributo = max(ganancias, key=ganancias.get)
        nodo = NodoArbol(atributo=mejor_atributo)

        valores_mejor_atributo = set(fila[mejor_atributo] for fila in datos)

        for valor in valores_mejor_atributo:
            subconjunto = [fila for fila in datos if fila[mejor_atributo] == valor]

            if not subconjunto:
                nodo.hijos[valor] = NodoArbol(clase=self.obtener_clase_mayoritaria(datos))
            else:
                nuevos_atributos = [a for a in atributos_disponibles if a != mejor_atributo]
                nodo.hijos[valor] = self.construir_arbol(subconjunto, nuevos_atributos)

        return nodo

    def ajustar(self, datos, columna_objetivo):
        """
        Entrena el árbol ID3.
        """
        self.columna_objetivo = columna_objetivo
        self.clase_por_defecto = self.obtener_clase_mayoritaria(datos)
        atributos = [columna for columna in datos[0].keys() if columna != columna_objetivo]
        self.raiz = self.construir_arbol(datos, atributos)

    def predecir_una(self, muestra):
        """
        Predice la clase de una sola muestra.
        """
        nodo_actual = self.raiz

        while not nodo_actual.es_hoja():
            valor = muestra.get(nodo_actual.atributo)

            if valor not in nodo_actual.hijos:
                return self.clase_por_defecto

            nodo_actual = nodo_actual.hijos[valor]

        return nodo_actual.clase

    def predecir_varias(self, muestras):
        """
        Predice la clase de varias muestras.
        """
        return [self.predecir_una(muestra) for muestra in muestras]

    def imprimir_arbol(self, nodo=None, sangria=""):
        """
        Imprime el árbol de forma legible.
        """
        if nodo is None:
            nodo = self.raiz

        if nodo.es_hoja():
            print(sangria + "----- " + str(nodo.clase))
            return

        for valor, hijo in nodo.hijos.items():
            print(f"{sangria}{nodo.atributo} = {valor}")
            self.imprimir_arbol(hijo, sangria + "    ")

    def imprimir_ganancias(self, datos):
        """
        Imprime la ganancia de información de cada atributo.
        """
        atributos = [columna for columna in datos[0].keys() if columna != self.columna_objetivo]

        print("Ganancias de información:")
        for atributo in atributos:
            ganancia = self.calcular_ganancia_informacion(datos, atributo)
            print(f"{atributo}: {ganancia:.4f}")