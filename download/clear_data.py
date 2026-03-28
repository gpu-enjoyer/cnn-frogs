
from   pathlib import Path
import json
import shutil # rm -rf


this_dir         = Path(__file__).resolve().parent

request_json_path = this_dir / "json" / "request.json"
links_json_path   = this_dir / "json" / "links.json"
dataset_path      = this_dir / "dataset"


with open(request_json_path, "r") as file:
    request_json = json.load(file)

clear_data = request_json.get("clear_data", True)

if not clear_data:
    exit


if links_json_path.exists():
    links_json_path.unlink()
    print(f"removed: {links_json_path}")

if dataset_path.exists():
    shutil.rmtree(dataset_path)
    print(f"removed: {dataset_path}")
