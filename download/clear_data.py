
# Use with caution

from   pathlib import Path
import json
import shutil     # rm -rf
import subprocess


this_dir         = Path(__file__).resolve().parent

request_json_path = this_dir / "json" / "request.json"

links_json_path   = this_dir / "json" / "links.json"
dataset_path      = this_dir / "dataset"

dvc_lock_path     = this_dir / ".." / "dvc.lock"


with open(request_json_path, "r") as file:
    request_json = json.load(file)

clear_data = request_json.get("clear_data", True)

if not clear_data:
    exit


# rm -f  links.json
if links_json_path.exists():
    links_json_path.unlink()
    print(f"removed: {links_json_path}")

# rm -rf dataset/
if dataset_path.exists():
    shutil.rmtree(dataset_path)
    print(f"removed: {dataset_path}")

# clear dvc cache
subprocess.run(['dvc', 'gc', '--workspace', '-f'])

# rm -f  dvc.lock
if dvc_lock_path.exists():
    dvc_lock_path.unlink()
    print(f"removed: {dvc_lock_path}")
