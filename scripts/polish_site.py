"""06-site HTML을 사이트 공통 레이아웃으로 정리하는 스크립트.

여러 번 실행해도 결과가 같습니다. 콘텐츠를 다시 생성한 뒤에도 이 스크립트를 실행하면
헤더/푸터/메타 태그/섹션 정리가 다시 적용됩니다.

    python scripts/polish_site.py
"""
import html
import os
import re
import sys
from pathlib import Path

from bs4 import BeautifulSoup, Comment, NavigableString, Tag

try:
    from PIL import Image
except ImportError:  # 이미지 변환은 선택
    Image = None

ROOT = Path(__file__).resolve().parent.parent / "06-site"
BASE = "https://japantrip.haesis.com"
SITE = "일본 여행 가이드"
CHECKED = "2026-10-22"
FONT_CSS = "https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/variable/pretendardvariable-dynamic-subset.min.css"
CSS_VER = "3"

MENU = [
    ("prepare", "준비", "출국 전에 할 일: 항공권, 입국, 통신, 돈, 짐"),
    ("regions", "지역", "어디로 갈지: 도시와 권역 비교"),
    ("itineraries", "일정", "며칠을 어떻게 쓸지: 일수별 가족 일정"),
    ("transport", "이동", "공항과 도시 간 교통, 렌터카"),
    ("onsite", "현장", "도착 후 바로 쓰는 정보: 음식, 면세, 아이, 문제 대응"),
    ("tools", "도구", "예산, 환율, 면세 계산과 체크리스트"),
]
MENU_NAME = {k: v for k, v, _ in MENU}

# 도시 허브 템플릿의 블록 문자 -> 섹션 이름
HUB_BLOCKS = {
    "A": "개요", "B": "한눈에 보기", "C": "이 도시가 맞는 사람", "D": "바로가기",
    "E": "공항에서 시내까지", "F": "숙소 권역", "G": "추천 일정", "H": "아이 동반 코스",
    "I": "맛집 시간대", "J": "근교 당일치기", "K": "총예산 예시", "L": "현지 팁·주의",
    "M": "귀국 동선", "N": "FAQ", "O": "관련 글", "P": "다른 도시 비교",
}
FINEPRINT = {"확인 필요 항목", "확인 필요로 남긴 항목", "공식 출처", "업데이트 정보",
             "확인 방법과 출처", "확인 필요 항목, 공식 출처"}
DROP_SECTIONS = {"규칙", "이 글을 쓰는 순서"}
RENAME = {"푸터": "업데이트 정보", "하위 목록": "이 메뉴의 글", "이 폴더의 글": "이 주제의 글"}
UNWRAP_HEADINGS = {"본문"}

LOGO = ('<svg viewBox="0 0 32 32" aria-hidden="true"><rect width="32" height="32" rx="9" fill="#1d2a44"/>'
        '<circle cx="16" cy="16" r="7" fill="#e0483c"/></svg>')

ICONS = {
    "calendar": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/></svg>',
    "users": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87M16 3.13a4 4 0 0 1 0 7.75"/></svg>',
    "wallet": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 12V8H6a2 2 0 0 1 0-4h12v4"/><path d="M4 6v12a2 2 0 0 0 2 2h14v-4"/><path d="M18 12a2 2 0 0 0 0 4h4v-4Z"/></svg>',
    "heart": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20.8 4.6a5.5 5.5 0 0 0-7.8 0L12 5.7l-1-1.1a5.5 5.5 0 0 0-7.8 7.8l1 1.1L12 21l7.8-7.5 1-1.1a5.5 5.5 0 0 0 0-7.8Z"/></svg>',
}


def slug(text):
    t = text.strip().lower()
    t = re.sub(r"[^\w\s-]", "", t)
    return re.sub(r"\s+", "-", t).strip("-")


def clean_heading(text, level):
    t = text.strip()
    if level == 2:
        t = re.sub(r"^(?:[A-Z]|\d+)(?:-\d+)?\.\s+", "", t)
    else:
        t = re.sub(r"^[A-Z]-?\d*\.\s+", "", t)
    t = re.sub(r"\s*\(선택\)$", "", t)
    return t


def frag(markup):
    return BeautifulSoup(markup, "html.parser")


def section_nodes(h2):
    """h2 다음부터 다음 h2 전까지의 형제 노드."""
    nodes = []
    for sib in list(h2.next_siblings):
        if isinstance(sib, Tag) and (sib.name == "h2" or (sib.name == "section" and "fineprint" in sib.get("class", []))):
            break
        nodes.append(sib)
    return nodes


def text_of(nodes):
    return "".join(n.get_text() if isinstance(n, Tag) else str(n) for n in nodes).strip()


def img_variant(src, suffix):
    """img/foo.jpg -> img/foo{suffix}.webp, 파일을 만들 수 있을 때만."""
    m = re.match(r"^(.*?img/)([^/]+)\.(jpe?g|png)$", src)
    if not m or Image is None:
        return src
    name = m.group(2)
    srcfile = ROOT / "img" / f"{name}.{m.group(3)}"
    width = 640 if suffix == "-sm" else 1280
    out = ROOT / "img" / f"{name}{suffix}.webp"
    if srcfile.exists() and not out.exists():
        im = Image.open(srcfile).convert("RGB")
        if im.width > width:
            im = im.resize((width, round(im.height * width / im.width)), Image.LANCZOS)
        im.save(out, "WEBP", quality=80, method=6)
    return f"{m.group(1)}{name}{suffix}.webp" if out.exists() else src


def jpg_of(src):
    """webp로 바뀐 경로에서 원본 jpg 경로를 되찾는다."""
    m = re.match(r"^(.*?img/)([^/]+?)(?:-sm|-lg)?\.webp$", src)
    if m:
        for ext in ("jpg", "jpeg", "png"):
            if (ROOT / "img" / f"{m.group(2)}.{ext}").exists():
                return f"{m.group(1)}{m.group(2)}.{ext}"
    return src


def header_html(pre, section):
    links = "".join(
        f'<a href="{pre}{k}/index.html"{" class=\"on\"" if k == section else ""}>{v}</a>' for k, v, _ in MENU)
    return (f'<header class="site-header"><div class="wrap">'
            f'<a class="brand" href="{pre}index.html">{LOGO}<span><b>{SITE}</b><small>JAPAN TRIP GUIDE</small></span></a>'
            f'<nav class="gnav" aria-label="주 메뉴">{links}</nav></div></header>')


def footer_html(pre):
    links = "".join(f'<a href="{pre}{k}/index.html">{v}</a>' for k, v, _ in MENU)
    return (f'<footer class="site-footer"><div class="wrap"><div class="cols">'
            f'<div><a class="brand" href="{pre}index.html">{LOGO}<span><b>{SITE}</b><small>JAPAN TRIP GUIDE</small></span></a>'
            f'<p>한국인 가족 여행자를 위한 일본 여행 정리. 공식 자료를 바탕으로 작성했으며, 요금·운행 시각·제도는 수시로 바뀌니 예약 전 공식 안내를 꼭 확인하세요.</p></div>'
            f'<nav aria-label="사이트 메뉴">{links}</nav></div>'
            f'<div class="bottom"><span>기준일 {CHECKED}</span><span>© 2026 japantrip.haesis.com</span></div>'
            f'</div></footer>')


def set_meta(head, soup, attr, key, content):
    tag = head.find("meta", attrs={attr: key})
    if tag is None:
        tag = soup.new_tag("meta")
        tag[attr] = key
        head.append(tag)
        head.append("\n")
    tag["content"] = content


def fix_head(soup, pre, url, title, desc, image):
    head = soup.head
    for link in head.find_all("link", rel="stylesheet"):
        link.decompose()
    for link in head.find_all("link", rel=lambda r: r and ("preconnect" in r or "icon" in r)):
        link.decompose()
    head.append(frag(
        f'<link rel="preconnect" href="https://cdn.jsdelivr.net" crossorigin>\n'
        f'<link rel="stylesheet" href="{FONT_CSS}">\n'
        f'<link rel="stylesheet" href="{pre}style.css?v={CSS_VER}">\n'
        f'<link rel="icon" href="{pre}favicon.svg" type="image/svg+xml">\n'))
    set_meta(head, soup, "name", "description", desc)
    set_meta(head, soup, "name", "theme-color", "#1d2a44")
    set_meta(head, soup, "property", "og:site_name", SITE)
    set_meta(head, soup, "property", "og:title", title)
    set_meta(head, soup, "property", "og:description", desc)
    set_meta(head, soup, "property", "og:url", url)
    set_meta(head, soup, "property", "og:image", image)
    set_meta(head, soup, "name", "twitter:card", "summary_large_image")


def first_text(article):
    lead = article.find("p", class_="lead") or article.find(class_="summary-lead")
    if lead and lead.get_text(strip=True):
        return lead.get_text(" ", strip=True)
    for p in article.find_all("p"):
        t = p.get_text(" ", strip=True)
        if len(t) > 30:
            return t
    return ""


def trim(t, n=150):
    t = re.sub(r"\s+", " ", t).strip()
    return t if len(t) <= n else t[: n - 1].rstrip() + "…"


def replace_block_refs(article, page_blocks):
    for s in list(article.find_all(string=re.compile(r"블록"))):
        if isinstance(s, Comment):
            continue
        t = str(s)
        t = re.sub(r"[^.]*?블록 [A-P]~[A-P] 순서로[^.]*\.\s*", "", t)
        t = re.sub(r"[^.]*?[A-P]~[A-P] 블록 순서로[^.]*\.\s*", "", t)
        t = re.sub(r"[^.]*?블록 [A-P]부터 [A-P]까지[^.]*\.\s*", "", t)
        t = re.sub(r"(예산|이) 블록", r"\1 항목", t)

        def rep(m):
            name = page_blocks.get(m.group(1)) or HUB_BLOCKS.get(m.group(1), m.group(1))
            return f"‘{name}’ 항목"
        t = re.sub(r"\b([A-P]) 블록", rep, t)
        if t != str(s):
            s.replace_with(t)


def process_article(soup, article, pre, rel_dir):
    # 자리표시 문단 제거
    for p in article.find_all("p"):
        if re.fullmatch(r"_[^_]+_", p.get_text(strip=True)):
            p.decompose()

    # 헤딩 원문 -> 블록 문자 맵 (이 페이지 기준)
    page_blocks = {}
    for h in article.find_all("h2"):
        m = re.match(r"^([A-P])\.\s+(.*)$", h.get_text(strip=True))
        if m:
            page_blocks[m.group(1)] = clean_heading(h.get_text(strip=True), 2)

    # id 부여 + 접두어 제거 (기존 #앵커 호환을 위해 id는 원문 기준)
    for h in article.find_all(["h2", "h3"]):
        raw = h.get_text(strip=True)
        if not h.get("id"):
            h["id"] = slug(raw)
        new = clean_heading(raw, 2 if h.name == "h2" else 3)
        if h.name == "h2":
            new = RENAME.get(new, new)
        if new != raw:
            h.clear()
            h.append(new)

    # 섹션 단위 정리
    for h2 in list(article.find_all("h2")):
        if h2.parent is None:
            continue
        name = h2.get_text(strip=True)
        nodes = section_nodes(h2)
        if name in DROP_SECTIONS:
            for n in nodes:
                n.extract()
            h2.decompose()
        elif name in UNWRAP_HEADINGS:
            h2.decompose()
        elif name == "히어로" or h2.get("id") == "a-히어로":
            build_summary(soup, article, h2, nodes)
        elif name == "점프 탭":
            build_jump(soup, h2, nodes)
        elif name in FINEPRINT and h2.parent.name != "section":
            sec = soup.new_tag("section", attrs={"class": "fineprint"})
            h2.insert_before(sec)
            sec.append(h2.extract())
            for n in nodes:
                sec.append(n.extract())
        elif name in ("이 메뉴의 글", "이 주제의 글"):
            build_linklist(soup, nodes)

    # 빈 섹션 제거
    for h2 in list(article.find_all("h2")):
        if h2.parent is None or (h2.parent.name == "section"):
            continue
        if not text_of(section_nodes(h2)) and not any(
                isinstance(n, Tag) and n.find(["img", "table", "a"]) for n in section_nodes(h2)):
            for n in section_nodes(h2):
                n.extract()
            h2.decompose()

    # fineprint 섹션은 글 끝으로 모은다
    fps = article.find_all("section", class_="fineprint", recursive=False)
    for sec in fps:
        article.append(sec.extract())

    replace_block_refs(article, page_blocks)

    # 바로가기는 요약 박스 바로 뒤에
    jump = article.find("nav", class_="jump")
    anchor = article.find("div", class_="summary") or article.find("figure", class_="hero")
    if jump and anchor and anchor.find_next_sibling() is not jump:
        anchor.insert_after(jump.extract())

    for img in article.find_all("img", alt=True):
        img["alt"] = re.sub(r"\s*\(자리표시\)", "", img["alt"])

    for bq in article.find_all("blockquote"):
        if not bq.get_text(strip=True):
            bq.decompose()


def build_summary(soup, article, h2, nodes):
    box = soup.new_tag("div", attrs={"class": "summary"})
    h2.insert_before(box)
    h1 = article.find("h1")
    h1t = h1.get_text(strip=True) if h1 else ""
    actions = []
    for n in nodes:
        n = n.extract()
        if not isinstance(n, Tag):
            if str(n).strip():
                box.append(n)
            continue
        if n.name == "p" and n.get_text(strip=True) in (h1t, h1t.replace(" 여행 가이드", "")):
            continue
        if n.name in ("ul", "ol"):
            for li in n.find_all("li", recursive=False):
                t = li.get_text(strip=True)
                if re.match(r"^(도시명|마지막 확인일)\s*:", t):
                    li.decompose()
                elif re.match(r"^한 줄 요약\s*:", t):
                    p = soup.new_tag("p", attrs={"class": "summary-lead"})
                    p.string = re.sub(r"^한 줄 요약\s*:\s*", "", t)
                    box.append(p)
                    li.decompose()
                elif re.match(r"^(버튼|바로가기)\s*:", t):
                    actions.extend(a.extract() for a in li.find_all("a"))
                    li.decompose()
            if n.find("li"):
                box.append(n)
            continue
        box.append(n)
    if actions:
        div = soup.new_tag("div", attrs={"class": "actions"})
        for i, a in enumerate(actions):
            a["class"] = ["btn", "primary"] if i == 0 else ["btn"]
            div.append(a)
        box.append(div)
    h2.decompose()
    if not box.get_text(strip=True):
        box.decompose()


def build_jump(soup, h2, nodes):
    links = []
    for n in nodes:
        if isinstance(n, Tag):
            links.extend(a.extract() for a in n.find_all("a"))
        n.extract()
    nav = soup.new_tag("nav", attrs={"class": "jump", "aria-label": "이 글의 섹션"})
    for a in links:
        nav.append(a)
    h2.replace_with(nav)


def build_linklist(soup, nodes):
    for n in nodes:
        if not isinstance(n, Tag):
            continue
        rows = []
        if "tbl" in n.get("class", []) and n.table:
            for tr in n.table.find_all("tr"):
                tds = tr.find_all("td")
                if tds and tds[0].a:
                    rows.append((tds[0].a.get("href"), tds[0].get_text(strip=True),
                                 tds[1].get_text(" ", strip=True) if len(tds) > 1 else ""))
        elif n.name == "ul":
            for li in n.find_all("li", recursive=False):
                a = li.find("a")
                if a:
                    desc = li.get_text(" ", strip=True)[len(a.get_text(" ", strip=True)):].lstrip(" :：")
                    rows.append((a.get("href"), a.get_text(strip=True), desc))
        if rows:
            div = soup.new_tag("div", attrs={"class": "linklist"})
            for href, name, desc in rows:
                div.append(frag(f'<a href="{html.escape(href)}"><b>{html.escape(name)}</b>'
                                f'{f"<span>{html.escape(desc)}</span>" if desc else ""}</a>'))
            n.replace_with(div)


def post_head(soup, article, section, pre, rel_dir, is_section_index):
    """meta, h1, lead를 post-head로 묶고 hero를 그 뒤에, 브레드크럼을 맨 앞에."""
    if article.find("header", class_="post-head"):
        return
    h1 = article.find("h1")
    meta = article.find("div", class_="meta")
    lead = article.find("p", class_="lead")
    hero = article.find("figure", class_="hero")
    head = soup.new_tag("header", attrs={"class": "post-head"})
    if meta:
        for sp in meta.find_all("span"):
            t = sp.get_text(strip=True)
            if t.startswith("상태"):
                sp.decompose()
            elif t == MENU_NAME.get(section):
                sp["class"] = ["cat"]
        head.append(meta.extract())
    if h1:
        head.append(h1.extract())
    if lead and lead.get_text(strip=True) != (h1.get_text(strip=True) if h1 else ""):
        head.append(lead.extract())
    elif lead:
        lead.decompose()
    article.insert(0, head)
    if hero:
        head.insert_after(hero.extract())

    crumbs = [f'<li><a href="{pre}index.html">홈</a></li>']
    if section:
        if is_section_index:
            crumbs.append(f"<li>{MENU_NAME[section]}</li>")
        else:
            crumbs.append(f'<li><a href="{pre}{section}/index.html">{MENU_NAME[section]}</a></li>')
            crumbs.append(f"<li>{html.escape(h1.get_text(strip=True) if h1 else '')}</li>")
    article.insert(0, frag(f'<ol class="crumbs" aria-label="현재 위치">{"".join(crumbs)}</ol>'))


def fix_images(article):
    hero = article.find("figure", class_="hero")
    if hero and hero.img:
        hero.img["src"] = img_variant(jpg_of(hero.img["src"]), "-lg")
        hero.img["width"], hero.img["height"] = "1280", "717"
        hero.img["fetchpriority"] = "high"
    for img in article.find_all("img"):
        if hero and img is hero.img:
            continue
        img["src"] = img_variant(jpg_of(img["src"]), "-sm")
        img["loading"] = "lazy"
        img["width"], img["height"] = "640", "400"


def fix_side(side, pre, section):
    if not side or side.find("h3") is None or not section:
        return
    h3 = side.find("h3")
    h3.clear()
    h3.append(frag(f'<a href="{pre}{section}/index.html">{MENU_NAME[section]}</a>'))
    first = side.find("li")
    if first and first.a and first.a.get("href", "").endswith(f"{section}/index.html"):
        first.decompose()
    side["aria-label"] = f"{MENU_NAME[section]} 메뉴"


def process_page(path):
    rel = path.relative_to(ROOT)
    parts = rel.parts[:-1]
    depth = len(parts)
    pre = "../" * depth
    section = parts[0] if parts and parts[0] in MENU_NAME else None
    url = BASE + "/" + ("/".join(parts) + "/" if parts else "")
    is_home = depth == 0
    soup = BeautifulSoup(path.read_text(encoding="utf-8"), "html.parser")

    old_header = soup.find("header", class_=["top", "site-header"])
    new_header = frag(header_html(pre, section))
    if old_header:
        old_header.replace_with(new_header)
    old_footer = soup.body.find("footer", recursive=False)
    new_footer = frag(footer_html(pre))
    if old_footer:
        old_footer.replace_with(new_footer)
    else:
        soup.body.append(new_footer)

    if is_home:
        build_home(soup, pre)
        article = soup.find("main")
    else:
        article = soup.find("article")
        post_head(soup, article, section, pre, parts, depth == 1)
        process_article(soup, article, pre, parts)
        fix_images(article)
        fix_side(soup.find("aside", class_="side"), pre, section)

    title_tag = soup.head.find("title")
    title = title_tag.get_text(strip=True)
    desc = trim(first_text(article) or title)
    hero = article.find("figure", class_="hero") if not is_home else None
    image = f"{BASE}/img/osaka-hub.jpg"
    if hero and hero.img:
        image = f"{BASE}/img/{os.path.basename(jpg_of(hero.img['src']))}"
    fix_head(soup, pre, url, title, desc, image)

    out = str(soup)
    out = re.sub(r"\n\s*\n", "\n", out)
    path.write_text(out, encoding="utf-8", newline="\n")


def build_home(soup, pre):
    main = soup.find("main")
    if main.find(class_="section"):
        cards = main.find("div", class_="cards", attrs={"data-cities": True})
    else:
        allcards = main.find_all("div", class_="cards")
        cards = allcards[-1] if allcards else None
    city_html = ""
    if cards:
        cards["data-cities"] = "1"
        for img in cards.find_all("img"):
            img["src"] = img_variant(jpg_of(img["src"]), "-sm")
            img["loading"] = "lazy"
            img["width"], img["height"] = "640", "400"
        for img in cards.find_all("img", alt=True):
            img["alt"] = re.sub(r"\s*\(자리표시\)", "", img["alt"])
        for s in cards.find_all("span"):
            s.string = re.sub(r"\s*\(자리표시\)", "", s.get_text())
        city_html = str(cards)
    hero_bg = img_variant("img/osaka-hub.jpg", "-lg")
    pick = [
        ("calendar", "며칠 가나요?", "2박 3일부터 4박 5일까지 일수별 일정", "itineraries/index.html"),
        ("users", "누구와 가나요?", "아이 동반, 부모님 동반 가족 일정", "itineraries/index.html"),
        ("wallet", "예산은 얼마나?", "항공권만이 아닌 총액으로 계산", "tools/budget-calculator/index.html"),
        ("heart", "무엇을 하고 싶나요?", "온천, 테마파크, 미식 테마별 모음", "regions/themes/index.html"),
    ]
    pick_html = "".join(
        f'<a href="{pre}{href}"><i>{ICONS[ic]}</i><b>{t}</b><span>{d}</span></a>' for ic, t, d, href in pick)
    menu_html = "".join(
        f'<a href="{pre}{k}/index.html"><small>{i + 1:02d}</small><b>{v}</b><span>{d}</span></a>'
        for i, (k, v, d) in enumerate(MENU))
    main.clear()
    main.append(frag(f'''
<section class="home-hero" style="background-image:url('{pre}{hero_bg}')"><div class="wrap">
<span class="eyebrow">기준일 {CHECKED}</span>
<h1>아이와 함께하는<br><em>일본 가족 여행</em>, 한 곳에서</h1>
<p>항공권부터 입국, 도시 선택, 일정, 교통, 현장 정보까지. 한국인 가족 여행자에게 필요한 내용만 공식 자료를 바탕으로 정리했습니다.</p>
<div class="actions"><a class="btn primary" href="{pre}itineraries/index.html">일정 둘러보기</a><a class="btn light" href="{pre}regions/index.html">도시 고르기</a></div>
</div></section>
<section class="section"><div class="section-head"><div><h2>어디서부터 시작할까요?</h2><p>질문 하나만 골라도 맞는 글로 안내합니다.</p></div></div>
<div class="pick">{pick_html}</div></section>
<section class="section"><div class="section-head"><div><h2>지금 바뀌는 제도</h2><p>출발 전에 꼭 알아야 할 변경 사항</p></div></div>
<div class="notice"><a href="{pre}onsite/tax-free-2026-11/index.html"><span class="tag">11월부터</span><div><b>일본 면세 환급 절차 변경</b><span>11월 1일 구매분부터 세금 포함 결제 후 출국 때 환급받는 방식</span></div></a>
<a href="{pre}prepare/entry/index.html"><span class="tag">입국</span><div><b>Visit Japan Web 입국·세관</b><span>입국 등록과 세관 신고를 미리 준비하는 방법</span></div></a></div></section>
<section class="section"><div class="section-head"><div><h2>도시별 여행 가이드</h2><p>공항 접근, 숙소 권역, 아이 동반 코스, 예산까지 도시마다 정리했습니다.</p></div><a class="more" href="{pre}regions/index.html">전체 지역 보기 →</a></div>
{city_html}</section>
<section class="section"><div class="section-head"><div><h2>메뉴별로 찾기</h2><p>준비부터 현장까지 여행 순서대로</p></div></div>
<div class="menu-grid">{menu_html}</div></section>
'''))
    main.attrs = {}
    layout = main.find_parent("div", class_="layout")
    if layout:
        layout.unwrap()
    t = soup.head.find("title")
    t.string = f"{SITE} | 한국인 가족 일본 여행 준비·일정·교통"


def main():
    pages = sorted(p for p in ROOT.rglob("index.html"))
    for p in pages:
        process_page(p)
    print(f"{len(pages)} pages processed")


if __name__ == "__main__":
    sys.exit(main())
