from abc import ABC, abstractmethod

from sklearn.ensemble import GradientBoostingRegressor, RandomForestRegressor
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


class EstrategiaRegresion(ABC):
    """
    Clase abstracta que define el contrato para cualquier estrategia de regresión.
    """

    @abstractmethod
    def crear_modelo(self):
        """
        Crea y retorna un modelo de regresión.
        """
        pass


class EstrategiaRegresionLineal(EstrategiaRegresion):
    """
    Estrategia para regresión lineal.
    """

    def crear_modelo(self):
        return Pipeline([
            ("escalador", StandardScaler()),
            ("modelo", LinearRegression())
        ])


class EstrategiaRidge(EstrategiaRegresion):
    """
    Estrategia para regresión Ridge.
    """
    

    def crear_modelo(self):
        return Pipeline([
            ("escalador", StandardScaler()),
            ("modelo", Ridge(alpha=1.0))
        ])


class EstrategiaBosqueAleatorio(EstrategiaRegresion):
    """
    Estrategia para Random Forest Regressor.
    """

    def crear_modelo(self):
        return RandomForestRegressor(
            n_estimators=100,
            random_state=42
        )


class EstrategiaGradientBoosting(EstrategiaRegresion):
    """
    Estrategia para Gradient Boosting Regressor.
    """

    def crear_modelo(self):
        return GradientBoostingRegressor(
            n_estimators=100,
            learning_rate=0.1,
            random_state=42
        )