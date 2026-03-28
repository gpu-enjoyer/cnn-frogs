
# 1) request.json -> get_links.py -> links.json 


import requests
import time
import json
import random
from   pathlib import Path


# params <- request.json

this_dir = Path(__file__).resolve().parent

with open(this_dir/"json"/"request.json", 'r') as file:
    request_json = json.load(file)

depth = request_json.get("depth", 0)
names = request_json.get("names", [])

print(names)    

base_url = "https://api.inaturalist.org/v1/observations"


params = {
    "quality_grade": "research", # качественные
    "media_type":    "photo",    #  изображения
    "per_page":      200,        # api maximum
    "taxon_name":    "",         # incr
    "page":          1,          # incr
    "order_by":      "votes",    # сортировка по качеству
    "order":         "desc"      #  в порядке убывания
}


# all_links -> links.json

all_links = {
    name: []
    for name in names
}

total_requests = 0
start_time     = time.time()


for name in names:

    params["page"] = 1  
    params["taxon_name"] = name
    links = []
    d = 0

    print(f"get links: {name}")

    while (d < depth):

        try:
            response = requests.get(base_url, params=params, timeout=10)
            total_requests += 1
            if response.status_code != 200:
                print("    error: http: ", response.status_code)
                break
            data = response.json()  # json -> dict
            observations = data.get("results", [])
            if not observations:
                print(f"    data ends on page: {params['page']}")
                break
            for obs in observations:
                if d >= depth: break
                photos = obs.get("photos", [])
                for photo in photos:
                    if (d >= depth): break
                    url = photo.get("url")
                    if url:
                        # url = url.replace("square", "original")
                        links.append(url)
                        d += 1
                        if d % 500 == 0:
                            print(f"    recieved: [{d}/{depth}]")
            params["page"] += 1
            time.sleep(0.2 + random.uniform(0, 0.3))

        except Exception as e:
            print(f"error: {e}")
            time.sleep(2)

    all_links[name] = links.copy()

    elapsed = time.time() - start_time
    rate = total_requests / elapsed if elapsed > 0 else 0
    print(f"  [{len(links)}] links ")
    print(f"  [{rate:.1f}] requests/sec")


with open(this_dir/"json"/"links.json", 'w') as file:
    json.dump(all_links, file, indent=4)

elapsed = time.time() - start_time
links_num = sum(len(v) for v in all_links.values())
print("get_links.py done")
print(f"[{links_num}] links for [{(elapsed/60):.1f}] min")

