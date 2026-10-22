"""도시·권역 가이드에서 예산 중심 내용을 덜어 내는 일회성 정리 스크립트.

- '총예산 예시' 섹션 삭제
- 표에서 숙박·식비·총예산 금액 열과 '1인 총예산' 행 삭제 (교통·입장 요금은 유지)
- 숙박비·식비·총예산을 가리키는 문장 삭제
- 사라진 섹션을 가리키는 바로가기 링크 정리

여러 번 실행해도 결과가 같습니다. 실행 후 scripts/polish_site.py 를 실행하세요.
"""
import re
from pathlib import Path

from bs4 import BeautifulSoup, NavigableString

ROOT = Path(__file__).resolve().parent.parent / "06-site"

DROP_SECTIONS = {"총예산 예시"}
DROP_COLS = re.compile(r"가격대|^1인 총예산$|^금액|^3인 금액$|^1인 금액$|^예상 비용")
DROP_ROWS = re.compile(r"^(1인 총예산|예산|예산을 가장 세게 맞출 때|숙소 가격대)$")
DROP_SENTENCE = re.compile(
    r"총예산 예시|1박 가격|숙박세|식당별 가격|식당 가격|식비 계산|항공권 최저가|같은 날짜와 같은 인원|가격대는|가격대와 예약|같은 침대를 쓰면 면제|한 침대를 쓰면 면제")
SENTENCE = re.compile(r"[^.!?]*?(?:[.!?](?=\s|$)|$)")


def drop_section(article, name):
    for h2 in article.find_all("h2"):
        if h2.get_text(strip=True) != name:
            continue
        for sib in list(h2.find_next_siblings()):
            if sib.name == "h2" or (sib.name == "section"):
                break
            sib.decompose()
        h2.decompose()


def trim_tables(article):
    for table in article.find_all("table"):
        head = table.find("tr")
        if not head:
            continue
        cols = [i for i, th in enumerate(head.find_all(["th", "td"]))
                if th.name == "th" and DROP_COLS.search(th.get_text(strip=True))]
        if cols:
            for tr in table.find_all("tr"):
                cells = tr.find_all(["th", "td"], recursive=False)
                for i in sorted(cols, reverse=True):
                    if i < len(cells):
                        cells[i].decompose()
        for tr in table.find_all("tr"):
            td = tr.find("td")
            if td and DROP_ROWS.match(td.get_text(strip=True)):
                tr.decompose()


def trim_sentences(article):
    for s in list(article.find_all(string=DROP_SENTENCE)):
        if s.find_parent(["th", "td", "h2", "h3"]):
            continue
        kept = [m.group(0) for m in SENTENCE.finditer(str(s)) if m.group(0) and not DROP_SENTENCE.search(m.group(0))]
        s.replace_with("".join(kept).lstrip() if kept else "")
    for el in article.find_all(["p", "li"]):
        if not el.get_text(strip=True) and not el.find(["img", "a"]):
            el.decompose()


def fix_anchors(article):
    ids = {t["id"] for t in article.find_all(id=True)}
    for a in article.find_all("a", href=re.compile(r"^#")):
        if a["href"][1:] in ids:
            continue
        if a.find_parent(class_=["jump", "actions"]):
            a.decompose()
        else:
            a.unwrap()


def main():
    for page in sorted(ROOT.rglob("index.html")):
        rel = page.relative_to(ROOT).parts
        if rel[0] == "tools" or "flight-total-cost" in rel or "money" in rel:
            # 예산 도구와 비용 비교 글은 그대로 둠 (사라진 섹션 언급만 정리)
            soup = BeautifulSoup(page.read_text(encoding="utf-8"), "html.parser")
            article = soup.find("article")
            if article:
                for s in list(article.find_all(string=re.compile("총예산 예시"))):
                    if not s.find_parent(["th", "td"]):
                        kept = [m.group(0) for m in SENTENCE.finditer(str(s))
                                if m.group(0) and "총예산 예시" not in m.group(0)]
                        s.replace_with("".join(kept).lstrip())
                page.write_text(str(soup), encoding="utf-8", newline="\n")
            continue
        soup = BeautifulSoup(page.read_text(encoding="utf-8"), "html.parser")
        article = soup.find("article")
        if article is None:
            continue
        if rel[0] == "regions":
            for name in DROP_SECTIONS:
                drop_section(article, name)
            trim_tables(article)
        trim_sentences(article)
        fix_anchors(article)
        page.write_text(str(soup), encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
