from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split


class CargadorDatasetCasas:
    """
    Clase encargada de cargar y dividir el dataset.
    """

    def cargar_datos(self):
        """
        Carga el dataset California Housing.
        """
        dataset = fetch_california_housing(as_frame=True)

        X = dataset.data
        y = dataset.target

        return X, y

    def dividir_datos(
        self,
        X,
        y,
        porcentaje_prueba=0.2,
        semilla=42
    ):
        """
        Divide los datos en entrenamiento y prueba.
        """
        return train_test_split(
            X,
            y,
            test_size=porcentaje_prueba,
            random_state=semilla
        )