# 앱 소개·개인정보처리방침·고객 지원 페이지 생성

`/trip/`(내곁의 여비), `/dday/`(내곁의 디데이), `/sudoku/`(내곁의 스도쿠), `/nonogram/`(내곁의 노노그램)의 세 페이지를 5개 언어(ko, en, ja, zh-hans, zh-hant)로 만든다.
문구는 `content.py`·`privacy.py`·`support.py`(여비), `dday_content.py`(디데이), `sudoku_content.py`(스도쿠), `nonogram_content.py`(노노그램)에 있다. 고친 뒤 실행한다.

```
python3 scripts/pages/gen.py          # 전부
python3 scripts/pages/gen.py dday     # 하나만
```

- 한국어는 기본 주소(`/trip/privacy/`)이고, 기기 언어가 한국어가 아니면 그 언어 페이지로 넘어간다. 앱은 기본 주소를 연다.
- 개인정보처리방침을 고치면 시행일도 바꾼다. 한국어판이 원문이다.
- 스토어 주소가 생기면 `gen.py`의 `App(..., store_urls=(App Store, Google Play))`를 채운다.
- 스크린샷(`<앱>/img/<언어>/01-….jpg`)이 없으면 화면 구역을 빼고, 공유 이미지(`header.jpg`)가 없으면 아이콘을 쓴다.
- `/nonogram/`에는 앱이 받는 `index.json`·`puzzles/`·`CREDITS.md`가 함께 있다. 생성기는 `index.html`만 덮어쓰고 다른 파일은 건드리지 않는다.
