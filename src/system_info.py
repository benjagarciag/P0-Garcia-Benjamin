import json
import os
import platform
import subprocess
from pathlib import Path

import psutil


def obtener_nucleos_fisicos():
    if os.name == "nt":
        try:
            resultado = subprocess.run(
                ["powershell", "-NoProfile", "-Command",
                 "(Get-CimInstance Win32_Processor).NumberOfCores"],
                capture_output=True, text=True, check=True, timeout=15,
            )
            valor = resultado.stdout.strip()
            if valor:
                return int(valor)
        except Exception:
            pass
    return os.cpu_count()


def obtener_info_sistema():
    memoria_total_gb = round(psutil.virtual_memory().total / (1024**3), 2)
    return {
        "sistema_operativo": platform.system(),
        "version_sistema": platform.release(),
        "arquitectura": platform.machine(),
        "version_python": platform.python_version(),
        "procesador": platform.processor() or os.environ.get("PROCESSOR_IDENTIFIER", "No disponible"),
        "nucleos_fisicos": obtener_nucleos_fisicos(),
        "procesadores_logicos": os.cpu_count(),
        "memoria_ram_total_gb": memoria_total_gb,
    }


def main():
    info = obtener_info_sistema()
    salida = Path(__file__).resolve().parent.parent / "data" / "system_info.json"
    salida.parent.mkdir(parents=True, exist_ok=True)
    salida.write_text(json.dumps(info, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(info, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
