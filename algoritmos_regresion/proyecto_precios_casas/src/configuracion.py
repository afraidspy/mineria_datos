from pathlib import Path


RUTA_BASE = Path(__file__).resolve().parent.parent

RUTA_MODELOS = RUTA_BASE / "modelos_guardados"
RUTA_RESULTADOS = RUTA_BASE / "resultados"
RUTA_GRAFICAS = RUTA_RESULTADOS / "graficas"
RUTA_METRICAS = RUTA_RESULTADOS / "metricas"

RUTA_MEJOR_MODELO = RUTA_MODELOS / "mejor_modelo_precios_casas.pkl"
RUTA_RESULTADOS_MODELOS = RUTA_METRICAS / "resultados_modelos.csv"


def crear_directorios_proyecto():
    """
    Crea los directorios de salida del proyecto si no existen.
    """
    RUTA_MODELOS.mkdir(parents=True, exist_ok=True)
    RUTA_GRAFICAS.mkdir(parents=True, exist_ok=True)
    RUTA_METRICAS.mkdir(parents=True, exist_ok=True)