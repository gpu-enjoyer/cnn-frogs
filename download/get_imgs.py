
import requests
import json
from   pathlib import Path

this_dir = Path(__file__).resolve().parent
dataset_path = this_dir / "dataset"

with open(this_dir / "json" / "links.json", "r") as file:
    links_json = json.load(file)

for class_name, class_links in links_json.items():
    class_path = dataset_path / class_name
    class_path.mkdir(parents=True, exist_ok=True)

    for i, url in enumerate(class_links):
        try:
            response = requests.get(url, timeout=7)
            response.raise_for_status()
            suffix = Path(url).suffix
            if not suffix:
                suffix = ".jpg"
            img_path = Path(class_path / f"{i}{suffix}")
            with open(img_path, "wb") as file:
                file.write(response.content)
            # print(f"saved: {img_path}")
            # time.sleep(1)
        except Exception as e:
            print(f"error: {url} -> {e}")

print("download.py done")
