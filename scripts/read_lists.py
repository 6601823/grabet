import pathlib

lists_dir = pathlib.Path("lists")

for file in lists_dir.glob("*.txt"):
    print(f"\n=== Файл: {file.name} ===")
    urls = file.read_text(encoding="utf-8").splitlines()
    for url in urls:
        url = url.strip()
        if url:
            print(url)
