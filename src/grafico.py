import csv
from pathlib import Path

import matplotlib.pyplot as plt


def leer_resultados(ruta):
    resultados = []
    with ruta.open("r", newline="", encoding="utf-8") as archivo:
        for fila in csv.DictReader(archivo):
            resultados.append({
                "tamano": int(fila["tamano"]),
                "tiempo_mimatmul_s": float(fila["tiempo_mimatmul_s"]),
                "tiempo_numpy_s": float(fila["tiempo_numpy_s"]),
            })
    return resultados


def generar_grafico(resultados, salida):
    tamanos = [r["tamano"] for r in resultados]
    tiempos_mimatmul = [r["tiempo_mimatmul_s"] for r in resultados]
    tiempos_numpy = [r["tiempo_numpy_s"] for r in resultados]

    plt.figure(figsize=(8, 5))
    plt.plot(tamanos, tiempos_mimatmul, marker="o", label="mimatmul")
    plt.plot(tamanos, tiempos_numpy, marker="s", label="NumPy (matmul)")
    plt.xlabel("Tamaño de la matriz (n×n)")
    plt.ylabel("Tiempo (segundos)")
    plt.title("Rendimiento: mimatmul vs NumPy")
    plt.yscale("log")
    plt.legend()
    plt.grid(True, which="both", linestyle="--", alpha=0.6)

    salida.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(salida, dpi=150)
    print(f"Gráfico guardado en {salida}")


def main():
    raiz = Path(__file__).resolve().parent.parent
    ruta_csv = raiz / "data" / "benchmark.csv"
    salida = raiz / "data" / "grafico_rendimiento.png"
    resultados = leer_resultados(ruta_csv)
    generar_grafico(resultados, salida)


if __name__ == "__main__":
    main()
