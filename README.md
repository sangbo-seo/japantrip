# 일본여행정보 사이트 작업 폴더

한국인 가족·가성비 일본 여행 정보 사이트의 구조, 설정, 템플릿, 콘텐츠를 모아 둔 폴더입니다.

| 폴더 | 내용 |
|---|---|
| 00-docs | 설계 문서 (메뉴 구조는 대화 기록, 와이어프레임, 필드 정의) |
| 01-config | 메뉴, 지역, 필터, 카드 필드, 목록 페이지, 홈 블록 설정 (JSON) |
| 02-templates | 글 4종 + 도시 페이지 템플릿 |
| 03-content | 메뉴 6개에 대응하는 콘텐츠 폴더. 각 폴더의 _index.md 가 메뉴 페이지 |
| 04-tracking | 글 진행표(CSV), 게시 전 검증 게이트 |

## 규칙
- 폴더명은 영문 슬러그, 표시명은 각 _index.md 의 title 에 있습니다.
- 글 1건은 한 메뉴에만 둡니다.
- last_checked 가 비어 있으면 게시하지 않습니다.
- 가격·시간·제도 수치는 확인 전에는 비워 둡니다.

## 사이트 레이아웃 정리 스크립트
`06-site`의 HTML을 다시 만들었다면 아래 명령으로 공통 헤더·푸터, 메타 태그, 섹션 정리, webp 이미지를 다시 적용합니다. 여러 번 실행해도 결과가 같습니다.

```
pip install beautifulsoup4 pillow
python scripts/polish_site.py
```

## 코스 중심 정리
- `scripts/courses/*.html`: 일정 글 본문(하루 코스 타임라인). 고친 뒤 `python scripts/apply_courses.py` 실행
- `scripts/trim_prices.py`: 도시 가이드에서 숙박·식비·총예산 금액을 덜어 냄 (교통·입장 요금은 유지)
- 마지막에 항상 `python scripts/polish_site.py` 실행
