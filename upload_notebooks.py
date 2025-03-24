import os
import subprocess

# Configura tus rutas
local_notebooks_dir = "Databricks"
databricks_folder = "/Shared/DataOps2" 

# Crear la carpeta en Databricks si no existe
subprocess.run([
    "databricks", "workspace", "mkdirs", databricks_folder
], check=True)

# Subir todos los notebooks a la carpeta deseada
subprocess.run([
    "databricks", "workspace", "import_dir",
    local_notebooks_dir, databricks_folder, "-o"
], check=True)
