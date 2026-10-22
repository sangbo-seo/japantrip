# 썸네일 이미지 제작 목록

기준일 2026-10-22. 총 25장 (도시 허브 5, 일정 9, 이동 4, 가이드 7). 이미지 생성 모델에 한 장씩 프롬프트를 넣어 만듭니다.

## 공통 규칙
1. 모든 이미지는 가로 16:9, 1600x900 픽셀, JPG로 저장합니다.
2. 파일명은 아래 표의 output_file 그대로 쓰고 05-assets\thumbnails\img\ 폴더에 둡니다. 사이트 경로는 /img/<파일명> 입니다.
3. 글자, 로고, 간판 문구는 넣지 않습니다. 사이트에서 제목을 따로 얹습니다.
4. 아이는 뒷모습이나 실루엣으로만 나오게 합니다. 얼굴이 보이면 다시 생성합니다.
5. 지브리, 디즈니, 닌텐도, 앙팡맨 등 저작권 캐릭터와 상표는 넣지 않습니다. USJ 글도 입구와 일반적인 지구본 조형물로만 표현합니다.
6. AI가 만든 실존 장소 이미지는 세부가 실제와 다를 수 있습니다. 성, 신사, 온천 건물은 생성 후 실제 사진과 형태를 대조하고, 이상하면 다시 생성합니다.
7. 게시 시 이미지 하단 또는 글 끝에 "AI 생성 이미지" 표기를 넣는 것을 권장합니다.
8. 완성 후 각 글의 thumbnail_alt 가 실제 이미지 내용과 맞는지 확인합니다.

## 공통 스타일 문구 (모든 프롬프트 뒤에 붙임)
```
photorealistic travel editorial photograph, 16:9 landscape, 1600x900, natural soft light, warm and bright color grade, shallow depth of field, clean composition with calm space for a title overlay on the left or bottom third
```

## 공통 네거티브 프롬프트
```
text, letters, logos, watermark, brand names, signage with readable characters, recognizable cartoon or game characters, theme-park mascots, distorted hands, extra fingers, visible faces of children, crowds, low resolution, oversaturated colors
```

## 목록
| 번호 | 파일명 | 종류 | 지역 | 글 제목 |
|---|---|---|---|---|
| 1 | departure-checklist.jpg | 가이드 | 전체 | 출국 전 체크리스트 |
| 2 | flight-total-cost.jpg | 비교 | 전체 | 항공권 총액 비교 |
| 3 | fukuoka-hub.jpg | 도시 허브 | 후쿠오카 | 후쿠오카 여행 가이드 |
| 4 | kumamoto-hub.jpg | 도시 허브 | 구마모토 | 구마모토 여행 가이드 |
| 5 | osaka-hub.jpg | 도시 허브 | 오사카 | 오사카 여행 가이드 |
| 6 | tokyo-hub.jpg | 도시 허브 | 도쿄 | 도쿄 여행 가이드 |
| 7 | matsuyama-hub.jpg | 도시 허브 | 마쓰야마 | 마쓰야마 여행 가이드 |
| 8 | dogo-onsen-honkan-guide.jpg | 가이드 | 마쓰야마 | 도고온천 본관 이용 가이드 |
| 9 | matsuyama-uchiko-daytrip.jpg | 가이드 | 마쓰야마 | 마쓰야마에서 우치코 당일치기 |
| 10 | osaka-3n4d-family.jpg | 일정 | 오사카 | 오사카 3박 4일 가족 일정 |
| 11 | fukuoka-2n3d.jpg | 일정 | 후쿠오카 | 후쿠오카 2박 3일 총액 예시 |
| 12 | kumamoto-3n4d-family.jpg | 일정 | 구마모토 | 구마모토 3박 4일 가족 일정 (구마모토성, 시내, 아소 렌터카) |
| 13 | tokyo-3n4d-family.jpg | 일정 | 도쿄 | 도쿄 3박 4일 가족 일정 |
| 14 | matsuyama-3n4d-slow.jpg | 일정 | 마쓰야마 | 마쓰야마 3박 4일 느린 가족 일정: 도고온천 숙박, 성과 동물원 |
| 15 | osaka-2n3d-family.jpg | 일정 | 오사카 | 오사카 2박 3일 가족 일정 |
| 16 | osaka-4n5d-kyoto-family.jpg | 일정 | 오사카 | 오사카 4박 5일 가족 일정과 교토 당일치기 |
| 17 | fukuoka-3n4d-family.jpg | 일정 | 후쿠오카 | 후쿠오카 3박 4일 가족 일정 |
| 18 | fukuoka-4n5d-family.jpg | 일정 | 후쿠오카 | 후쿠오카 4박 5일 가족 일정 |
| 19 | tokyo-airport-to-city.jpg | 가이드 | 도쿄 | 하네다·나리타에서 도쿄 시내까지 |
| 20 | kmj-airport-to-city.jpg | 가이드 | 구마모토 | 구마모토공항에서 시내까지: 공항버스·택시·렌터카 비교 |
| 21 | myj-airport-to-dogo.jpg | 가이드 | 마쓰야마 | 마쓰야마공항에서 시내·도고온천까지: 리무진 버스, 택시, 렌터카 비교 |
| 22 | kumamoto-aso-kurokawa-rentcar.jpg | 가이드 | 구마모토 | 구마모토에서 아소·구로카와 렌터카 일정 |
| 23 | tax-free-2026-11.jpg | 가이드 | 전체 | 2026년 11월 일본 면세 환급 절차 |
| 24 | no-data-esim.jpg | 가이드 | 전체 | 데이터가 안 될 때 대처법 |
| 25 | kumamoto-earthquake-status.jpg | 가이드 | 구마모토 | 구마모토 지진 이후 여행 가능 여부와 확인 방법 |

## 이미지별 프롬프트

### 1. departure-checklist.jpg
- 글: 출국 전 체크리스트 (03-content//01-prepare/timeline/departure-checklist.md)
- 대체 텍스트(alt): 여권과 휴대폰 화면의 QR, 변환 플러그를 펼쳐 놓은 출국 준비물
- 프롬프트:

```
Flat lay on a light wooden desk: a Korean passport-style navy booklet (no readable text), a smartphone showing a generic QR code, a Japanese type-A travel plug adapter, a small coin purse with yen coins, and a printed checklist with blurred lines. Soft window light, top-down view.
```

### 2. flight-total-cost.jpg
- 글: 항공권 총액 비교 (03-content//01-prepare/flights/flight-total-cost.md)
- 대체 텍스트(alt): 항공권 가격표와 여권, 비행기 창밖 풍경이 놓인 여행 준비 책상
- 프롬프트:

```
Top-down travel planning desk: a laptop with an abstract blurred price comparison table (no readable text), a passport-style booklet, a small toy airplane, a calculator and a coffee cup. Soft morning light, clean and bright.
```

### 3. fukuoka-hub.jpg
- 글: 후쿠오카 여행 가이드 (03-content//02-regions/kyushu/fukuoka/index.md)
- 대체 텍스트(alt): 
- 프롬프트:

```
Hakata, Fukuoka riverside at dusk along the Naka river, rows of yatai food stall lanterns glowing warmly, reflections on the water, relaxed crowd as small silhouettes, no readable text.
```

### 4. kumamoto-hub.jpg
- 글: 구마모토 여행 가이드 (03-content//02-regions/kyushu/kumamoto/index.md)
- 대체 텍스트(alt): 구마모토성 천수각과 성곽 전경
- 프롬프트:

```
Kumamoto Castle main keep and stone walls under a clear blue sky, cherry or green trees in front, wide panoramic composition, calm and majestic, no readable text.
```

### 5. osaka-hub.jpg
- 글: 오사카 여행 가이드 (03-content//02-regions/kansai/osaka/index.md)
- 대체 텍스트(alt): 도톤보리 강변과 오사카성이 함께 보이는 오사카 시내 전경
- 프롬프트:

```
Dotonbori canal in Osaka at dusk with colorful generic neon signs (no readable text), a river boat, and in the distance a subtle silhouette of Osaka Castle tower composited naturally, wide panoramic view.
```

### 6. tokyo-hub.jpg
- 글: 도쿄 여행 가이드 (03-content//02-regions/kanto/tokyo/index.md)
- 대체 텍스트(alt): 도쿄 도심 거리에서 전철역으로 향하는 가족 여행자
- 프롬프트:

```
A Tokyo street at morning with a family of three (seen from behind) walking toward a station entrance, tall city buildings, a generic commuter train passing on an elevated line, clean bright urban light, no readable text or logos.
```

### 7. matsuyama-hub.jpg
- 글: 마쓰야마 여행 가이드 (03-content//02-regions/etc/matsuyama/index.md)
- 대체 텍스트(alt): 언덕 위 마쓰야마성과 도고온천 본관 전경
- 프롬프트:

```
Matsuyama Castle on a hill above a small city in Shikoku, with a ropeway line below and a hint of an old wooden bathhouse roof in the lower town, soft sunset sky, no readable text.
```

### 8. dogo-onsen-honkan-guide.jpg
- 글: 도고온천 본관 이용 가이드 (03-content//02-regions/etc/matsuyama/dogo-onsen-honkan-guide.md)
- 대체 텍스트(alt): 저녁 조명이 켜진 도고온천 본관 정면
- 프롬프트:

```
Dogo Onsen Honkan, the historic wooden Japanese bathhouse with its three-story roof and glowing evening lanterns, wet stone street after rain, warm golden light, a few small blurred silhouettes, no readable text.
```

### 9. matsuyama-uchiko-daytrip.jpg
- 글: 마쓰야마에서 우치코 당일치기 (03-content//02-regions/etc/matsuyama/matsuyama-uchiko-daytrip.md)
- 대체 텍스트(alt): 흰 벽 옛 상가가 이어진 우치코 옛 거리
- 프롬프트:

```
A quiet old merchant street in Uchiko, Ehime, with white plaster walls and wooden lattice houses and a tiled roofline, soft afternoon sun, a parent and child walking in the distance from behind, no readable text.
```

### 10. osaka-3n4d-family.jpg
- 글: 오사카 3박 4일 가족 일정 (03-content//03-itineraries/posts/osaka-3n4d-family.md)
- 대체 텍스트(alt): 도톤보리 강변을 걷는 부모와 초등학생 자녀의 뒷모습
- 프롬프트:

```
A parent and an elementary-school child holding hands, seen from behind, walking along the Dotonbori canal in Osaka at dusk, glowing generic neon signs (no readable text), warm lights, cheerful mood.
```

### 11. fukuoka-2n3d.jpg
- 글: 후쿠오카 2박 3일 총액 예시 (03-content//03-itineraries/posts/fukuoka-2n3d.md)
- 대체 텍스트(alt): 후쿠오카 하카타 시내 야타이 거리의 저녁 풍경
- 프롬프트:

```
Fukuoka Nakasu yatai street at night, a row of small food stall lanterns, steam rising from ramen bowls on a counter, a parent and a child seated seen from behind, warm cozy lighting, no readable text.
```

### 12. kumamoto-3n4d-family.jpg
- 글: 구마모토 3박 4일 가족 일정 (구마모토성, 시내, 아소 렌터카) (03-content//03-itineraries/posts/kumamoto-3n4d-family.md)
- 대체 텍스트(alt): 구마모토성 천수각과 성곽
- 프롬프트:

```
A family of three seen from behind standing on the wide green Aso grassland looking toward a long volcanic mountain ridge, grazing cattle nearby, big blue sky with soft clouds, calm and open mood, no readable text.
```

### 13. tokyo-3n4d-family.jpg
- 글: 도쿄 3박 4일 가족 일정 (03-content//03-itineraries/posts/tokyo-3n4d-family.md)
- 대체 텍스트(alt): 도쿄 거리에서 지도를 보며 걷는 부모와 초등학생 아이
- 프롬프트:

```
A parent and an elementary-school child seen from behind looking at a city map on a smartphone beside a Tokyo crossing, tall buildings and a distant red tower silhouette, soft evening light, friendly mood, no readable text or logos.
```

### 14. matsuyama-3n4d-slow.jpg
- 글: 마쓰야마 3박 4일 느린 가족 일정: 도고온천 숙박, 성과 동물원 (03-content//03-itineraries/posts/matsuyama-3n4d-slow.md)
- 대체 텍스트(alt): 도고온천 본관 앞 상점가를 걷는 가족
- 프롬프트:

```
A family of three seen from behind strolling slowly along the covered shopping arcade in front of Dogo Onsen Honkan at evening, paper lanterns, relaxed slow-travel mood, warm light, no readable text.
```

### 15. osaka-2n3d-family.jpg
- 글: 오사카 2박 3일 가족 일정 (03-content//03-itineraries/posts/osaka-2n3d-family.md)
- 대체 텍스트(alt): USJ 입구로 걸어가는 부모와 초등학생 자녀의 뒷모습
- 프롬프트:

```
A parent and an elementary-school child seen from behind walking toward a generic bright theme-park entrance gate with a large globe-like sculpture (no logos, no characters), sunny day, balloons, festive mood.
```

### 16. osaka-4n5d-kyoto-family.jpg
- 글: 오사카 4박 5일 가족 일정과 교토 당일치기 (03-content//03-itineraries/posts/osaka-4n5d-kyoto-family.md)
- 대체 텍스트(alt): 교토 후시미이나리 신사의 붉은 도리이 길을 걷는 가족의 뒷모습
- 프롬프트:

```
A parent and an elementary-school child seen from behind walking through the long tunnel of vermilion torii gates at Fushimi Inari shrine in Kyoto, dappled light, no readable text.
```

### 17. fukuoka-3n4d-family.jpg
- 글: 후쿠오카 3박 4일 가족 일정 (03-content//03-itineraries/posts/fukuoka-3n4d-family.md)
- 대체 텍스트(alt): 후쿠오카 우미노나카미치 해변공원과 마린월드 수족관 풍경
- 프롬프트:

```
Uminonakamichi seaside park in Fukuoka with fields of colorful flowers by the bay, a family with a child on a bike seen from behind, a distant large aquarium building, sunny day, no readable text.
```

### 18. fukuoka-4n5d-family.jpg
- 글: 후쿠오카 4박 5일 가족 일정 (03-content//03-itineraries/posts/fukuoka-4n5d-family.md)
- 대체 텍스트(alt): 후쿠오카 노코노시마 섬 꽃 공원과 하카타만 풍경
- 프롬프트:

```
Nokonoshima island in Hakata Bay, Fukuoka, rolling flower fields with a view over the blue bay and the city skyline across the water, a parent and child walking among flowers seen from behind, gentle light, no readable text.
```

### 19. tokyo-airport-to-city.jpg
- 글: 하네다·나리타에서 도쿄 시내까지 (03-content//04-transport/airport/tokyo-airport-to-city.md)
- 대체 텍스트(alt): 하네다공항 전철 승강장에서 캐리어를 끄는 가족
- 프롬프트:

```
A family of three (parents and an elementary-school child, seen from behind) pulling suitcases along an airport train platform in Tokyo, a generic commuter train arriving, clean modern station, morning light, no logos.
```

### 20. kmj-airport-to-city.jpg
- 글: 구마모토공항에서 시내까지: 공항버스·택시·렌터카 비교 (03-content//04-transport/airport/kmj-airport-to-city.md)
- 대체 텍스트(alt): 아소 구마모토공항 버스 승강장 앞 공항버스
- 프롬프트:

```
A generic airport limousine bus parked at a small regional airport bus stop in Kyushu, Japan, a family loading suitcases (seen from behind), clear sky, distant green mountains, no readable text or logos.
```

### 21. myj-airport-to-dogo.jpg
- 글: 마쓰야마공항에서 시내·도고온천까지: 리무진 버스, 택시, 렌터카 비교 (03-content//04-transport/airport/myj-airport-to-dogo.md)
- 대체 텍스트(alt): 마쓰야마공항 앞 이요테쓰 리무진 버스
- 프롬프트:

```
A generic airport shuttle bus leaving a small regional airport in Shikoku, Japan, with citrus orchards and hills in the background, a family waiting at the stop (seen from behind), warm afternoon light, no readable text or logos.
```

### 22. kumamoto-aso-kurokawa-rentcar.jpg
- 글: 구마모토에서 아소·구로카와 렌터카 일정 (03-content//04-transport/car/kumamoto-aso-kurokawa-rentcar.md)
- 대체 텍스트(alt): 아소 구사센리 초원과 말
- 프롬프트:

```
A compact rental car driving on a road through the wide green Kusasenri grassland of Aso, Kyushu, grazing horses in the field, smoke-free volcanic crater ridge in the distance, big sky, no readable text.
```

### 23. tax-free-2026-11.jpg
- 글: 2026년 11월 일본 면세 환급 절차 (03-content//05-onsite/shopping/tax-free-2026-11.md)
- 대체 텍스트(alt): 일본 공항 출국장의 면세 절차 단말기에 여권을 대는 모습
- 프롬프트:

```
Japanese airport departure hall, a traveler with a suitcase holding a passport up to a generic self-service kiosk terminal, bright modern interior, shallow depth of field, no readable text or logos.
```

### 24. no-data-esim.jpg
- 글: 데이터가 안 될 때 대처법 (03-content//05-onsite/help/no-data-esim.md)
- 대체 텍스트(alt): 일본 거리에서 휴대폰 지도가 안 열려 화면을 확인하는 여행자의 뒷모습
- 프롬프트:

```
Back view of a traveler holding a smartphone on a quiet Japanese city street at dusk, the phone screen glowing with a blank loading map, lanterns and shop signs blurred in the background (no readable text).
```

### 25. kumamoto-earthquake-status.jpg
- 글: 구마모토 지진 이후 여행 가능 여부와 확인 방법 (03-content//05-onsite/help/kumamoto-earthquake-status.md)
- 대체 텍스트(alt): 구마모토성 전경과 안내 표지
- 프롬프트:

```
Kumamoto Castle main keep seen from a stone path on a calm clear day, a small neutral information signboard with abstract unreadable marks in the foreground, peaceful and reassuring mood, no people close up.
```

## 생성 후 할 일
- 만든 파일을 img 폴더에 저장하고 04-tracking\thumbnail-status.csv 의 상태를 "완료"로 바꿉니다.
- 메뉴 허브 페이지와 홈 배너용 이미지는 이번 목록에 없습니다. 필요하면 별도로 정합니다.

### 26. kyushu-region.jpg
- 글: 규슈 권역 가이드 (03-content/02-regions/kyushu/_index.md)
- 대체 텍스트(alt): 규슈 신칸센과 구마모토성이 함께 보이는 풍경 (자리표시)
- 프롬프트:

```
A compact Japanese regional landscape: a quiet harbour town in Kyushu with small fishing boats, a low green mountain ridge behind, and a narrow coastal road; soft morning light, calm and unhurried travel mood, no readable text.
```

### 27. kansai-region.jpg
- 글: 간사이 권역 가이드 (03-content/02-regions/kansai/_index.md)
- 대체 텍스트(alt): 오사카 도톤보리 강변과 교토 후시미이나리의 붉은 도리이 길을 나란히 보여 주는 간사이 대표 풍경
- 프롬프트:

```
A split-feel wide panorama of the Kansai region: on one side the Dotonbori canal in Osaka at dusk with colorful generic neon signs (no readable text), on the other side a path of vermilion torii gates, blended naturally into one coherent scene, warm lights, no readable text.
```

### 28. kanto-region.jpg
- 글: 간토 권역 가이드 (03-content/02-regions/kanto/_index.md)
- 대체 텍스트(alt): 도쿄 야경을 배경으로 전철로 이동하는 가족의 뒷모습
- 프롬프트:

```
A family of three seen from behind riding a commuter train through Tokyo at dusk, city lights and a dense skyline outside the windows, warm interior lighting, calm travel mood, no logos or readable text.
```

### 29. etc-region.jpg
- 글: 주부·시코쿠·기타 권역 가이드 (03-content/02-regions/etc/_index.md)
- 대체 텍스트(alt): 마쓰야마 시내 골목과 멀리 보이는 성, 혹은 도고온천 거리 풍경
- 프롬프트:

```
A quiet old town street in Matsuyama, Shikoku, with wooden machiya-style shopfronts and a tiled roofline, a hilltop Japanese castle keep visible in the distance above the town, late afternoon sunlight, quiet slow-travel mood, no readable text.
```

## 추가된 항목 (권역 허브)
| 번호 | 파일명 | 종류 | 지역 | 글 제목 |
|---|---|---|---|---|
| 26 | kyushu-region.jpg | 권역 허브 | 규슈 | 규슈 권역 가이드 |
| 27 | kansai-region.jpg | 권역 허브 | 간사이 | 간사이 권역 가이드 |
| 28 | kanto-region.jpg | 권역 허브 | 간토 | 간토 권역 가이드 |
| 29 | etc-region.jpg | 권역 허브 | 주부·시코쿠·기타 | 주부·시코쿠·기타 권역 가이드 |

### 30. beppu-hub.jpg
- 글: 벳푸 여행 가이드 (03-content/02-regions/kyushu/beppu/index.md)
- 대체 텍스트(alt): 벳푸 간나와 온천지구에서 피어오르는 증기와 지옥순례 풍경
- 프롬프트:

```
Beppu hot spring town in Kyushu with steam rising from vents and rooftops, a red torii gate by a steaming Jigoku pond, morning light, calm mood, no readable text.
```

### 31. nagasaki-hub.jpg
- 글: 나가사키 여행 가이드 (03-content/02-regions/kyushu/nagasaki/index.md)
- 대체 텍스트(alt): 나가사키 야경과 오우라 천주당 풍경
- 프롬프트:

```
Nagasaki night view from Mount Inasa with a starry city lights panorama over the harbour and long bridges, deep blue night sky, tranquil, no readable text.
```

### 32. kyoto-hub.jpg
- 글: 교토 여행 가이드 (03-content/02-regions/kansai/kyoto/index.md)
- 대체 텍스트(alt): 교토 가와라마치 거리와 오층탑이 함께 보이는 교토 시내 풍경
- 프롬프트:

```
A calm path of vermilion torii gates on a forested mountainside in Kyoto, dappled morning light, a parent and child walking seen from behind, no readable text.
```

### 33. kobe-hub.jpg
- 글: 고베 여행 가이드 (03-content/02-regions/kansai/kobe/index.md)
- 대체 텍스트(alt): 하버랜드 앞 항구 야경과 배경의 고베 시가지가 함께 보이는 풍경
- 프롬프트:

```
Kobe harbour at dusk with the Kobe Port Tower silhouette, ships and a lit Ferris wheel by the waterfront, warm lights, family silhouettes by the promenade, no readable text.
```

### 34. nara-hub.jpg
- 글: 나라 여행 가이드 (03-content/02-regions/kansai/nara/index.md)
- 대체 텍스트(alt): 나라공원에서 풀을 뜯는 사슴과 뒤로 보이는 도다이지 대불전 지붕
- 프롬프트:

```
Nara park in soft afternoon light, a gentle deer close to a wall of the Great Buddha Hall in the background, a parent and child seen from behind feeding the deer, peaceful mood, no readable text.
```

### 35. yokohama-hub.jpg
- 글: 요코하마 여행 가이드 (03-content/02-regions/kanto/yokohama/index.md)
- 대체 텍스트(alt): 미나토미라이와 바다를 배경으로 걷는 가족 여행자
- 프롬프트:

```
Yokohama Minato Mirai skyline at dusk with the Landmark Tower and Cosmo Clock ferris wheel reflected on the bay, gentle evening colors, a family strolling seen from behind, no readable text.
```

### 36. hakone-hub.jpg
- 글: 하코네 여행 가이드 (03-content/02-regions/kanto/hakone/index.md)
- 대체 텍스트(alt): 아시노코 호수 위를 가르는 해적선과 멀리 보이는 후지산
- 프롬프트:

```
Lake Ashi in Hakone with its red torii gate on the shore, a sightseeing ship on the water and Mount Fuji in the distance, soft morning mist, no readable text.
```

### 37. nagoya-hub.jpg
- 글: 나고야 여행 가이드 (03-content/02-regions/etc/nagoya/index.md)
- 대체 텍스트(alt): 나고야성 본마루어전과 멀리 보이는 센트레아, 또는 사카에 오아시스21 전경
- 프롬프트:

```
Nagoya Castle keep with golden shachihoko ornaments viewed from the garden, clear blue sky, a parent and child seen from behind on the path, spring greenery, no readable text.
```

### 38. takamatsu-hub.jpg
- 글: 다카마쓰 여행 가이드 (03-content/02-regions/etc/takamatsu/index.md)
- 대체 텍스트(alt): 리쓰린 공원 남호와 기쿠게쓰테이, 혹은 나오시마 항구의 빨간 호박과 세토나이카이 풍경
- 프롬프트:

```
Ritsurin Garden in Takamatsu with a tranquil pond, stone bridges and pine trees, autumn colors, a parent and child walking on a path seen from behind, calm composition, no readable text.
```

### 39. sapporo-hub.jpg
- 글: 삿포로 여행 가이드 (03-content/02-regions/etc/sapporo/index.md)
- 대체 텍스트(alt): 눈 덮인 오도리공원과 삿포로 TV타워, 멀리 홋카이도대학 캠퍼스
- 프롬프트:

```
Sapporo Odori Park in winter with snow-covered trees, a skating rink and glowing ice lanterns, evening lights, children playing gently in the distance, no readable text.
```

### 40. okinawa-hub.jpg
- 글: 오키나와 여행 가이드 (03-content/02-regions/etc/okinawa/index.md)
- 대체 텍스트(alt): 국제거리의 번화한 거리와 유이레일, 혹은 차탄 해변과 만좌모 전망
- 프롬프트:

```
Okinawa blue ocean and white sand beach with a red shisa statue on a stone wall in the foreground, a parent and child walking along the shore seen from behind, bright clear sky, no readable text.
```
