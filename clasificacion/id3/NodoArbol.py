class NodoArbol:
    """
    Representa un nodo del árbol de decisión.

    Un nodo puede ser:
    - un nodo interno, que contiene un atributo para dividir
    - una hoja, que contiene una clase final
    """

    def __init__(self, atributo=None, clase=None):
        self.atributo = atributo
        self.clase = clase
        self.hijos = {}

    def es_hoja(self):
        """
        Indica si el nodo es una hoja.
        """
        return self.clase is not None