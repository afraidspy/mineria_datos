from sklearn.datasets import fetch_california_housing
import pandas as pd


class CargadorDatos:
    

    def cargar_datos(self) -> pd.DataFrame:
        """Carga el dataset y lo devuelve como un DataFrame de pandas."""
        datos = fetch_california_housing(as_frame=True)
        return datos.frame
