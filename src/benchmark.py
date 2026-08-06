import csv
import time
from pathlib import Path

import numpy as np

from src.mimatmul import mimatmul


def medir_tiempo(funcion):
    inicio = time.perf_counter()
    funcion()
    return time.perf_counter() - inicio


def ejecutar_benchmark(tamanos):
    resultados = []
    for n in tamanos:
        A = np.random.rand(n, n)
        B = np.random.rand(n, n)

        C_mimatmul = mimatmul(A.tolist(), B.tolist())
        C_numpy = np.matmul(A, B)
        if not np.allclose(C_mimatmul, C_numpy):
            raise ValueError(f"Los resultados no coinciden para el tamaño {n}")

        tiempo_mimatmul = medir_tiempo(lambda: mimatmul(A.tolist(), B.tolist()))
        tiempo_numpy = medir_tiempo(lambda: np.matmul(A, B))

        resultados.append({
            "tamano": n,
            "tiempo_mimatmul_s": tiempo_mimatmul,
            "tiempo_numpy_s": tiempo_numpy,
        })
    return resultados


def main():
    tamanos = [2, 4, 8, 16, 32, 64]
    resultados = ejecutar_benchmark(tamanos)

    salida = Path(__file__).resolve().parent.parent / "data" / "benchmark.csv"
    salida.parent.mkdir(parents=True, exist_ok=True)
    with salida.open("w", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=resultados[0].keys())
        escritor.writeheader()
        escritor.writerows(resultados)

    for fila in resultados:
        print(f"n={fila['tamano']:>3}  mimatmul={fila['tiempo_mimatmul_s']:.6f}s  numpy={fila['tiempo_numpy_s']:.6f}s")


if __name__ == "__main__":
    main()
