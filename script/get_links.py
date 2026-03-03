
# imports

import requests
import time
import json
from   pathlib import Path


# params <- request.json

root_path = Path(__file__).resolve().parent.parent

with open(root_path/"json_to_json"/"request.json", 'r') as file:
    request_json = json.load(file)

depth = request_json.get("depth", 0)
names = request_json.get("names", [])

print(names)

base_url = "https://api.inaturalist.org/v1/observations"

params = {
    "quality_grade": "research",
    "media_type":    "photo",
    "per_page":      10,
    "taxon_name":    "",   # incr.
    "page":          1     # incr.
}


# all_links -> links.json

all_links = {
    f"class{i}": [] 
    for i in range(1, len(names) + 1)
}

for j, name in enumerate(names, start=1):
    params["page"] = 1
    params["taxon_name"] = name
    links = []
    d = 0

    print(name, j)

    while (d < depth):
        response = requests.get(base_url, params=params)
        if response.status_code != 200:
            print("response: error: ", response.status_code)
            break
        data = response.json()  # json -> dict
        observations = data["results"]
        if not observations:
            break

        for obs in observations:
            photos = obs.get("photos", [])
            for photo in photos:
                if (d >= depth):
                    break
                url = photo.get("url")
                if url:
                    d += 1
                    url = url.replace("square", "original")
                    links.append(url)
      
        params["page"] += 1
        time.sleep(1)

    all_links[f"class{j}"] = links.copy()


with open(root_path/"json_to_json"/"links.json", 'w') as file:
    json.dump(all_links, file, indent=4)

print("get_links.py done")
