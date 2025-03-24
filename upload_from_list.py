import os
import subprocess

databricks_folder = "/Shared/DataOps3"
deploy_file = "deploy_list.txt"

with open(deploy_file, "r") as f:
    notebooks = [line.strip() for line in f if line.strip()]

for nb in notebooks:
    target_path = f"{databricks_folder}/{os.path.basename(nb)}"
    print(f"Uploading {nb} to {target_path}")
    subprocess.run(["databricks", "workspace", "import", nb, target_path, "--overwrite"], check=True)
