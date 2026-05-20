import joblib
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

from src.configuracion import RUTA_GRAFICAS


class PredictorPreciosCasas:
    """
    Clase contexto que utiliza una estrategia de regresión.
    """

    def __init__(self, estrategia):
        self.estrategia = estrategia
        self.modelo = self.estrategia.crear_modelo()

    def entrenar(self, X_entrenamiento, y_entrenamiento):
        """
        Entrena el modelo seleccionado.
        """
        self.modelo.fit(X_entrenamiento, y_entrenamiento)

    def predecir(self, X_prueba):
        """
        Realiza predicciones.
        """
        return self.modelo.predict(X_prueba)

    def evaluar(self, X_prueba, y_prueba):
        """
        Evalúa el desempeño del modelo.
        """
        predicciones = self.predecir(X_prueba)

        return {
            "MAE": mean_absolute_error(y_prueba, predicciones),
            "MSE": mean_squared_error(y_prueba, predicciones),
            "RMSE": mean_squared_error(y_prueba, predicciones) ** 0.5,
            "R2": r2_score(y_prueba, predicciones)
        }

    def guardar_modelo(self, ruta_archivo):
        """
        Guarda el modelo entrenado.
        """
        joblib.dump(self.modelo, ruta_archivo)

    def cargar_modelo(self, ruta_archivo):
        """
        Carga un modelo previamente entrenado.
        """
        self.modelo = joblib.load(ruta_archivo)

    def obtener_importancia_variables(self, nombres_variables):
        """
        Obtiene importancia de variables o coeficientes.
        """
        modelo_real = self.modelo

        if hasattr(self.modelo, "named_steps"):
            modelo_real = self.modelo.named_steps["modelo"]

        if hasattr(modelo_real, "feature_importances_"):
            importancias = modelo_real.feature_importances_

        elif hasattr(modelo_real, "coef_"):
            importancias = abs(modelo_real.coef_)

        else:
            return None

        df_importancia = pd.DataFrame({
            "Variable": nombres_variables,
            "Importancia": importancias
        })

        return df_importancia.sort_values(
            by="Importancia",
            ascending=False
        )

    def graficar_importancia_variables(
        self,
        nombres_variables,
        nombre_modelo
    ):
        """
        Genera y guarda gráfica de importancia de variables.
        """
        importancia = self.obtener_importancia_variables(
            nombres_variables
        )

        if importancia is None:
            print(
                f"El modelo {nombre_modelo} no soporta importancia de variables."
            )
            return

        importancia = importancia.head(10)

        plt.figure(figsize=(10, 6))

        plt.barh(
            importancia["Variable"],
            importancia["Importancia"]
        )

        plt.xlabel("Importancia")
        plt.ylabel("Variable")
        plt.title(
            f"Importancia de variables - {nombre_modelo}"
        )

        plt.gca().invert_yaxis()
        plt.tight_layout()

        nombre_archivo = (
            f"importancia_{nombre_modelo.replace(' ', '_')}.png"
        )

        ruta_archivo = RUTA_GRAFICAS / nombre_archivo

        plt.savefig(ruta_archivo, dpi=300)
        plt.show()