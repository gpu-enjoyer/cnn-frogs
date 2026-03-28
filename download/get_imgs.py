
# 2) links.json -> get_imgs.py -> dataset/

import requests
import time
import json
import random

from   pathlib             import Path
from   concurrent.futures  import ThreadPoolExecutor, as_completed
from   threading           import Lock
from   collections         import Counter

# PARAMS
MAX_WORKERS = 50
TIMEOUT = 15
RETRY_ATTEMPTS = 3
RETRY_DELAY = 2


this_dir = Path(__file__).resolve().parent
dataset_path = this_dir / "dataset"

with open(this_dir / "json" / "links.json", "r") as file:
    links_json = json.load(file)


stats = {
    "success": 0,
    "failed": 0,
    "errors": Counter()
}
stats_lock = Lock()


def get_suffix_from_url(url: str) -> str:
    """Получить расширение изображения"""
    suffix = Path(url).suffix.lower()
    if suffix in ['.jpg', '.jpeg', '.png', '.webp']:
        return suffix
    return ".jpg"


def download_single_image(args):
    """Загрузка изображения в несколько попыток"""
    url, class_name, idx, total = args

    for attempt in range(RETRY_ATTEMPTS):
        try:
            response = requests.get(url, timeout=TIMEOUT)
            response.raise_for_status()

            suffix = get_suffix_from_url(url)
            file_name = f"{idx:07d}{suffix}"  # 0000001.jpg
            filepath = dataset_path / class_name / file_name

            with open(filepath, "wb") as f:
                f.write(response.content)

            with stats_lock:
                stats["success"] += 1

            # success, url, error
            return True, url, None

        except Exception as e:
            if attempt < RETRY_ATTEMPTS - 1:
                # increase time for sleep
                time.sleep(RETRY_DELAY * (attempt + 1) + random.uniform(0, 1))
            else:
                with stats_lock:
                    stats["failed"] += 1
                    error_type = type(e).__name__
                    stats["errors"][error_type] += 1
                # success, url, error
                return False, url, str(e)

    # success, url, error
    return False, url, "max retries exceeded"


def print_progress(current, total, start_time, class_name=""):
    """Статус загрузки"""
    elapsed = time.time() - start_time
    speed = current / elapsed if elapsed > 0 else 0
    remaining = (total - current) / speed if speed > 0 else 0

    bar_len = 30
    filled = int(bar_len * current / total) if total > 0 else 0
    bar = "█" * filled + "░" * (bar_len - filled)

    print(f"\r[{bar}] {current}/{total} ({current*100//total}%) "
          f"| {speed:.1f} img/s | {remaining:.0f}s осталось | {class_name}   ",
          end="", flush=True)




print("=" * 50)
start_time = time.time()

all_tasks     = []
task_metadata = []  # (url, class_name, idx, total_for_class)

for class_name, links in links_json.items():
    class_path = dataset_path / class_name.replace(" ", "_")
    class_path.mkdir(parents=True, exist_ok=True)

    for idx, url in enumerate(links):
        all_tasks.append((url, class_name.replace(" ", "_"), idx, len(links)))

total_tasks = len(all_tasks)
print(f"К загрузке: {total_tasks} изображений")
print("=" * 50)


completed = 0

with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
    futures = {executor.submit(download_single_image, task): task for task in all_tasks}

    for future in as_completed(futures):
        success, url, error = future.result()
        completed += 1

        if completed % 100 == 0 or completed == total_tasks:
            print_progress(completed, total_tasks, start_time)


elapsed = time.time() - start_time
total_speed = total_tasks / elapsed if elapsed > 0 else 0

print("\n")
print("=" * 50)
print("Загрузка завершена")
print(f"  Время: {elapsed:.1f} сек ({elapsed/60:.1f} min)")
print(f"  Скорость: {total_speed:.1f} imgs/sec")
print(f"  Успешно: {stats['success']}")
print(f"  Ошибок: {stats['failed']}")
print("=" * 50)

if stats['errors']:
    print("Основные ошибки: ")
    for error_type, count in stats['errors'].most_common(5):
        print(f"  - {error_type}: {count}")

