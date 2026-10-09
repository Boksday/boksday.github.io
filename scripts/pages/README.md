# 앱 소개·개인정보처리방침·고객 지원 페이지 생성

`/trip/`(내곁의 여비)와 `/dday/`(내곁의 디데이)의 세 페이지를 5개 언어(ko, en, ja, zh-hans, zh-hant)로 만든다.
문구는 `content.py`·`privacy.py`·`support.py`(여비), `dday_content.py`(디데이)에 있다. 고친 뒤 실행한다.

```
python3 scripts/pages/gen.py          # 둘 다
python3 scripts/pages/gen.py dday     # 하나만
```

- 한국어는 기본 주소(`/trip/privacy/`)이고, 기기 언어가 한국어가 아니면 그 언어 페이지로 넘어간다. 앱은 기본 주소를 연다.
- 개인정보처리방침을 고치면 시행일도 바꾼다. 한국어판이 원문이다.
- 스토어 주소가 생기면 `gen.py`의 `App(..., store_urls=(App Store, Google Play))`를 채운다.
