import subprocess
import os

script = "/workspaces/server/servidor_minecraft/run.sh"

if not os.path.isfile(script):
    print(f"No se encontró el archivo: {script}")
    exit(1)

# Dar permisos de ejecución por si acaso
subprocess.run(["chmod", "+x", script], check=True)

# Ejecutar el script
subprocess.run([script], check=True)