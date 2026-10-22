# URL 규칙

기준일 2026-10-22. 사이트 빌더가 이 규칙으로 경로와 파일을 대응시킵니다.

## 글 URL

| 글 종류 | URL | 대응 파일 |
|---|---|---|
| 도시 허브 | /regions/{id}/ | 03-content/02-regions/{권역}/{id}/index.md |
| 일정 글 | /itineraries/{id}/ | 03-content/03-itineraries/posts/{id}.md |
| 지역 하위 글 | /regions/{id}/ | 03-content/02-regions/{권역}/{id}.md |
| 준비 글 | /prepare/{id}/ | 03-content/01-prepare/{하위}/{id}.md |
| 이동 글 | /transport/{id}/ | 03-content/04-transport/{하위}/{id}.md |
| 현장 글 | /onsite/{id}/ | 03-content/05-onsite/{하위}/{id}.md |
| 도구 글 | /tools/{id}/ | 03-content/06-tools/{하위}/{id}.md |

## 메뉴·허브 페이지 URL

| 종류 | URL | 대응 파일 |
|---|---|---|
| 1차 메뉴 | /{menu}/ | 03-content/{NN}-{menu}/_index.md |
| 하위 허브 | /{menu}/{하위slug}/ | 03-content/{NN}-{menu}/{하위slug}/_index.md |
| 권역 허브 | /regions/{권역slug}/ | 03-content/02-regions/{권역slug}/_index.md |

## 목록 필터 URL

- 일정 목록: /itineraries/?region={지역id}&duration={일수id}
- 필터는 URL 쿼리로 유지합니다. 같은 필터 안은 OR, 필터끼리는 AND입니다.

## 이미지

- 본문 이미지는 /img/파일명. 썸네일 목록은 05-assets/thumbnails/thumbnail-list.md 에 있습니다.
