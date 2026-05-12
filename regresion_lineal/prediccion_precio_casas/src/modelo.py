from sklearn.linear_model import LinearRegression


class ModeloRegresionViviendas:
    """Clase para el modelo de  regresión lineal múltiple."""

    def __init__(self):
        self.modelo = LinearRegression()

    def entrenar(self, x_entrenamiento, y_entrenamiento):
        """Entrena el modelo con los datos de entrenamiento."""
        self.modelo.fit(x_entrenamiento, y_entrenamiento)

    def predecir(self, x_prueba):
        """Genera predicciones usando los datos de prueba."""
        return self.modelo.predict(x_prueba)

    def obtener_intercepto(self):
        """Devuelve el intercepto del modelo."""
        return self.modelo.intercept_

    def obtener_coeficientes(self):
        """Devuelve los coeficientes del modelo."""
        return self.modelo.coef_
