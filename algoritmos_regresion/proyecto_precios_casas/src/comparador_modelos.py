import pandas as pd

from src.cargador_datos import CargadorDatasetCasas
from src.configuracion import (
    RUTA_MEJOR_MODELO,
    RUTA_METRICAS,
    RUTA_RESULTADOS_MODELOS
)
from src.estrategias_modelos import (
    EstrategiaBosqueAleatorio,
    EstrategiaGradientBoosting,
    EstrategiaRegresionLineal,
    EstrategiaRidge
)
from src.predictor import PredictorPreciosCasas


class ComparadorModelos:
    """
    Clase encargada de entrenar, evaluar y comparar modelos.
    """

    def __init__(self):
        self.estrategias = {
            "Regresion_Lineal": EstrategiaRegresionLineal(),
            "Ridge": EstrategiaRidge(),
            "Random_Forest": EstrategiaBosqueAleatorio(),
            "Gradient_Boosting": EstrategiaGradientBoosting()
        }

    def ejecutar_comparacion(self):
        """
        Ejecuta el flujo completo de comparación de modelos.
        """
        cargador = CargadorDatasetCasas()

        X, y = cargador.cargar_datos()

        X_entrenamiento, X_prueba, y_entrenamiento, y_prueba = (
            cargador.dividir_datos(X, y)
        )

        resultados = []

        mejor_predictor = None
        mejor_r2 = float("-inf")
        mejor_nombre = None

        for nombre_modelo, estrategia in self.estrategias.items():
            print(f"\nEntrenando modelo: {nombre_modelo}")

            predictor = PredictorPreciosCasas(estrategia)

            predictor.entrenar(
                X_entrenamiento,
                y_entrenamiento
            )

            metricas = predictor.evaluar(
                X_prueba,
                y_prueba
            )

            metricas["Modelo"] = nombre_modelo

            resultados.append(metricas)

            importancia = predictor.obtener_importancia_variables(
                X.columns
            )

            if importancia is not None:
                ruta_csv = (
                    RUTA_METRICAS /
                    f"importancia_{nombre_modelo}.csv"
                )

                importancia.to_csv(
                    ruta_csv,
                    index=False
                )

                predictor.graficar_importancia_variables(
                    nombres_variables=X.columns,
                    nombre_modelo=nombre_modelo
                )

            if metricas["R2"] > mejor_r2:
                mejor_r2 = metricas["R2"]
                mejor_predictor = predictor
                mejor_nombre = nombre_modelo

        mejor_predictor.guardar_modelo(
            RUTA_MEJOR_MODELO
        )

        df_resultados = pd.DataFrame(resultados)

        df_resultados = df_resultados[
            ["Modelo", "MAE", "MSE", "RMSE", "R2"]
        ]

        df_resultados = df_resultados.sort_values(
            by="R2",
            ascending=False
        )

        df_resultados.to_csv(
            RUTA_RESULTADOS_MODELOS,
            index=False
        )

        print("\nMejor modelo encontrado:")
        print(mejor_nombre)
        print(f"R2: {mejor_r2:.4f}")
        print(f"Modelo guardado en: {RUTA_MEJOR_MODELO}")

        return df_resultados