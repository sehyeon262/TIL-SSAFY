# 반응형 Profile 페이지 구현

## 분석 흐름과 학습 내용
✨ 주요 기능

1. 상단 헤더바

- bg-warning-subtle 배경 + 중앙 정렬 제목
- “Bori” 텍스트에 Google Fonts Rubik Dirt 적용

2. 페이지 전환 네비게이션 (F03)

- nav nav-pills 구성
기본 정보 수정 / 포트폴리오 수정 탭
현재 페이지에 active 적용

3. 기본 정보 수정 폼 (F02)

회원 번호, ID: 읽기 전용(disabled)
Email: 로컬파트 입력 + @example.com 표시(aria-describedby로 접근성 보강)
Nickname / 나이: 입력 + Update 버튼
자산/연봉: $ 프리픽스가 있는 input-group 구성, 숫자 입력 유도(inputmode="numeric", pattern="\d*")
Bootstrap form-label, form-control, input-group 활용

4. 투자 성향(우측 컬럼)

투자상품 선호도: 주식/채권/부동산/가상화폐 (체크박스)
투자 스타일: 안정적/중립적/공격적 (라디오)
관심 종목: 정보기술/소비재/금융 (체크박스)
d-flex flex-column + flex-grow-1로 섹션 간 여백 자연스러운 배치

5. 프로필 이미지 / 자기소개

원형 크롭(ratio-1x1, rounded-circle, overflow-hidden)
자기소개 텍스트영역 + Update 버튼

---------------------------------------------------------------

🧰 기술 스택

- HTML5, CSS3

- Bootstrap 5.3.8 (CDN)

- Google Fonts – Rubik Dirt (CDN)

---------------------------------------------------------------

## 📝 느낀점

- 컴포넌트 선택이 설계를 좌우한다
: 단순한 폼이라도 container → row → col 그리드와 input-group, form-check, nav-pills 같은 역할이 분명한 컴포넌트를 고르면 구조가 자연스럽게 잡힘을 체감했다.

- 여백은 ‘규칙’로 관리해야 편하다
: 임의 margin보다 g-4, gap-*, py-*처럼 부트스트랩 스케일을 쓰니 반응형에서 일관성이 생겼다. 특히 우측 컬럼의 수직 정렬은 d-flex flex-column + flex-grow-1로 깔끔하게 해결.

- 이미지 라운딩은 CSS 트릭보다 유틸 조합이 안전
: 프로필은 ratio-1x1 + rounded-circle + overflow-hidden + object-fit: cover 조합이 가장 단단했다. 브라우저/해상도 차이에도 모양이 무너지지 않았다.