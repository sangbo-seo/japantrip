"""scripts/courses/*.html 조각으로 글 본문을 교체합니다.

파일 이름: <메뉴>__<슬러그>.html  (예: itineraries__osaka-3n4d-family.html)
첫 줄 주석으로 제목과 요약문을 바꿀 수 있습니다.
    <!-- title: 새 제목 | lead: 새 요약문 -->

본문은 대표 사진(없으면 글 머리) 뒤의 내용을 모두 대체합니다.
실행 후 scripts/polish_site.py 를 실행하세요.
"""
import re
from pathlib import Path

from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parent.parent / "06-site"
COURSES = Path(__file__).resolve().parent / "courses"
SITE = "일본 여행 가이드"


def main():
    renames = {}
    for frag in sorted(COURSES.glob("*.html")):
        section, slug = frag.stem.split("__")
        page = ROOT / section / slug / "index.html"
        text = frag.read_text(encoding="utf-8")
        meta = {}
        m = re.match(r"\s*<!--(.*?)-->", text, re.S)
        if m:
            for part in m.group(1).split("|"):
                k, _, v = part.partition(":")
                meta[k.strip()] = v.strip()
            text = text[m.end():]
        soup = BeautifulSoup(page.read_text(encoding="utf-8"), "html.parser")
        article = soup.find("article")
        anchor = article.find("figure", class_="hero") or article.find("header", class_="post-head")
        for sib in list(anchor.next_siblings):
            sib.extract()
        anchor.insert_after(BeautifulSoup(text, "html.parser"))

        if meta.get("lead"):
            lead = article.find("p", class_="lead")
            if lead:
                lead.string = meta["lead"]
        if meta.get("title"):
            h1 = article.find("h1")
            old = h1.get_text(strip=True)
            new = meta["title"]
            if old != new:
                renames[old] = new
                h1.string = new
                soup.title.string = f"{new} | {SITE}"
        page.write_text(str(soup), encoding="utf-8", newline="\n")
        print("updated", page.relative_to(ROOT))

    # 바뀐 제목을 사이드바·목록 링크에도 반영
    if renames:
        for p in ROOT.rglob("index.html"):
            s = p.read_text(encoding="utf-8")
            t = s
            for old, new in renames.items():
                t = t.replace(f">{old}<", f">{new}<")
            if t != s:
                p.write_text(t, encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
