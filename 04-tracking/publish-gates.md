# 게시 전 검증 게이트

1. 필수 필드 11개가 모두 채워졌는가 (id, title, summary, menu, type, region, last_checked, published, status, thumbnail, slug)
2. last_checked 가 게시일 이전 90일 이내인가
3. est_cost 에 cost_basis 가 같이 있는가
4. hub 또는 next_step 링크가 최소 1개 있는가
5. 같은 글이 두 메뉴에 중복 등록되지 않았는가 (menu 1개)
6. 썸네일 alt 와 요약(60자 이내)

## 갱신 주기
- 가이드·비교: 90일
- 도시허브: 180일
- 일정: 365일
