
with open("raw_subs.srt", "r", encoding="utf-8") as f:
    lines = f.readlines()

clean = []

for line in lines:
    line = line.strip()

    # пропускаем служебные строки
    if not line:
        continue
    if line.isdigit():
        continue
    if "-->" in line:
        continue

    clean.append(line)

# удаляем инкрементальные версии
result = []

for line in clean:
    if not result:
        result.append(line)
        continue

    # если предыдущая строка является началом текущей
    if line.startswith(result[-1]):
        result[-1] = line   # заменяем на более длинную
    else:
        result.append(line)

with open("final.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(result))
