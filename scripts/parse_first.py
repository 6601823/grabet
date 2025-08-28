import pathlib, requests
from bs4 import BeautifulSoup

lists_dir = pathlib.Path("lists")
data_dir = pathlib.Path("data")
data_dir.mkdir(exist_ok=True)

# Берём первый список и первый URL
first_list = next(lists_dir.glob("*.txt"))
first_url = first_list.read_text(encoding="utf-8").splitlines()[0].strip()

print(f"Парсим: {first_url}")

# Скачиваем HTML
resp = requests.get(first_url, timeout=20)
resp.raise_for_status()

# Чистим HTML → текст
soup = BeautifulSoup(resp.text, "html.parser")
for bad in soup(["script", "style", "noscript"]):
    bad.decompose()
text = soup.get_text(" ", strip=True)

# Сохраняем результат
out_file = data_dir / "result.txt"
out_file.write_text(text[:5000], encoding="utf-8")  # ограничим первые 5000 символов

print(f"Сохранено в {out_file}")
