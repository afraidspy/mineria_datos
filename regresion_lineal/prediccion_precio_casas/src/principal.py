from sklearn.model_selection import train_test_split

from cargador_datos import CargadorDatos
from modelo import ModeloRegresionViviendas
from evaluador import EvaluadorModelo


def main():
    # Cargar los datos
    cargador = CargadorDatos()
    df = cargador.cargar_datos()

    print("Primeras filas del conjunto de datos:")
    print(df.head())

    # Separar variables independientes y variable dependiente
    x = df.drop(columns=["MedHouseVal"])
    y = df["MedHouseVal"]

    # Dividir datos en entrenamiento y prueba
    x_entrenamiento, x_prueba, y_entrenamiento, y_prueba = train_test_split(
        x,
        y,
        test_size=0.2,
        random_state=42
    )

    # Crear y entrenar el modelo
    modelo = ModeloRegresionViviendas()
    modelo.entrenar(x_entrenamiento, y_entrenamiento)

    # Hacer predicciones
    y_predicho = modelo.predecir(x_prueba)

    # Evaluar el modelo
    evaluador = EvaluadorModelo()
    resultados = evaluador.evaluar(y_prueba, y_predicho)
    tabla_errores = evaluador.crear_tabla_errores(y_prueba, y_predicho)

    # Mostrar resultados
    print("\nIntercepto del modelo:")
    print(modelo.obtener_intercepto())

    print("\nCoeficientes del modelo:")
    for variable, coeficiente in zip(x.columns, modelo.obtener_coeficientes()):
        print(f"{variable}: {coeficiente:.6f}")

    print("\nMétricas de evaluación:")
    print(f"MSE  - Error cuadrático medio: {resultados['mse']:.6f}")
    print(f"RMSE - Raíz del error cuadrático medio: {resultados['rmse']:.6f}")
    print(f"MAE  - Error absoluto medio: {resultados['mae']:.6f}")
    print(f"R2   - Coeficiente de determinación: {resultados['r2']:.6f}")

    print("\nEjemplo de errores en predicciones:")
    print(tabla_errores.to_string(index=False))


if __name__ == "__main__":
    main()
