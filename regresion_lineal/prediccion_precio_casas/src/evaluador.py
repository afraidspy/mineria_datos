import numpy as np
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


class EvaluadorModelo:
    """Clase responsable de evaluar el rendimiento del modelo."""

    def evaluar(self, y_real, y_predicho):
        """Calcula métricas de evaluación para un modelo de regresión."""
        mse = mean_squared_error(y_real, y_predicho)
        rmse = np.sqrt(mse)
        mae = mean_absolute_error(y_real, y_predicho)
        r2 = r2_score(y_real, y_predicho)

        return {
            "mse": mse,
            "rmse": rmse,
            "mae": mae,
            "r2": r2,
        }

    def crear_tabla_errores(self, y_real, y_predicho, max_filas=10):
        """Crea una tabla con valores reales, predichos, errores y errores cuadrados."""
        tabla = pd.DataFrame({
            "valor_real": y_real.reset_index(drop=True),
            "valor_predicho": y_predicho,
        })

        tabla["error"] = tabla["valor_real"] - tabla["valor_predicho"]
        tabla["error_absoluto"] = tabla["error"].abs()
        tabla["error_cuadrado"] = tabla["error"] ** 2

        return tabla.head(max_filas)
