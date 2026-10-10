# 내곁의 노노그램 퍼즐

앱은 켤 때 `nonogram/index.json`(퍼즐 목록)을 확인하고, 바뀌었을 때만 받는다(ETag).
퍼즐 내용(`nonogram/puzzles/<id>.json`)은 사용자가 그 퍼즐을 누를 때 받는다.

## 퍼즐 추가·수정·삭제

1. `nonogram/puzzles/<id>.json`을 만들거나 고치거나 지운다. 파일 이름과 `id`가 같아야 한다.
   `{"id", "name": {ko, en, ja, zh-Hans, zh-Hant}, "palette": {"글자": "#RRGGBB"}, "rows": ["..r..", ...]}`
2. `python3 scripts/nonogram/build.py` — 모든 퍼즐을 검사하고(답이 하나뿐이고 줄 추론만으로 풀리는지)
   `index.json`을 다시 만든다. 하나라도 틀리면 목록을 쓰지 않는다.
3. 커밋하고 push한다. 몇 분 뒤 앱에 보인다.

- 크기는 5~20(25·30은 앱에 확대 기능이 생긴 뒤). 판 크기로 앱의 티어(입문·초급·중급·고급)가 정해진다.
- 앱에 든 퍼즐과 같은 id는 쓸 수 없다(`solver.py`의 `BUILT_IN_IDS`).
- 퍼즐을 고치면 `rev`가 바뀌어 이미 받은 앱도 그 퍼즐만 다시 받는다.
- 그림 출처는 `nonogram/CREDITS.md`.
