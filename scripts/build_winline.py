#!/usr/bin/env python3
import json, pathlib
from jinja2 import Environment, FileSystemLoader, select_autoescape

ROOT = pathlib.Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "winline.json"
TPL_DIR = ROOT / "templates"
OUT = ROOT / "promo-winline.html"

def main():
    data = json.loads(DATA.read_text(encoding="utf-8"))
    env = Environment(loader=FileSystemLoader(str(TPL_DIR)),
                      autoescape=select_autoescape(["html","xml"]))
    OUT.write_text(env.get_template("promo-winline.html.j2").render(data=data), encoding="utf-8")
    print(f"Rendered: {OUT}")

if __name__ == "__main__":
    main()
