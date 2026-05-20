from src.comparador_modelos import ComparadorModelos
from src.configuracion import crear_directorios_proyecto


def main():
    print("=" * 60)
    print("PREDICCIÓN DE PRECIOS DE CASAS")
    print("=" * 60)

    crear_directorios_proyecto()

    comparador = ComparadorModelos()

    resultados = comparador.ejecutar_comparacion()

    print("\nResumen final de resultados:")
    print(resultados)


if __name__ == "__main__":
    main()