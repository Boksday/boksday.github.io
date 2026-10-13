# 내곁의 노노그램 퍼즐

앱은 켤 때 `nonogram/index.json`(퍼즐 목록)을 확인하고, 바뀌었을 때만 받는다(ETag).
퍼즐 내용(`nonogram/puzzles/<id>.json`)은 사용자가 그 퍼즐을 누를 때 받는다.

## 퍼즐 추가·수정·삭제

1. `nonogram/puzzles/<id>.json`을 만들거나 고치거나 지운다. 파일 이름과 `id`가 같아야 한다.
   `{"id", "name": {ko, en, ja, zh-Hans, zh-Hant}, "palette": {"글자": "#RRGGBB"}, "rows": ["..r..", ...]}`
2. `python3 scripts/nonogram/build.py` — 모든 퍼즐을 검사하고(답이 하나뿐이고 줄 추론만으로 풀리는지)
   `index.json`을 다시 만든다. 하나라도 틀리면 목록을 쓰지 않는다.
3. 커밋하고 push한다. 몇 분 뒤 앱에 보인다.

- 크기는 5~30. 판 크기로 앱의 티어가 정해진다(5 튜토리얼, 10 입문, 15 초급, 20 중급, 25 고급, 30 마스터).
- 통짜 모양(모든 가로·세로줄이 칠한 덩어리 하나 이하)은 너무 쉬워서 받지 않는다. 그림 안에 구멍이 있어야 한다.
- 별 난이도는 줄마다 남는 여유 칸 비율로 매긴다. 이어지는 칸이 길수록(여유가 적을수록) 별이 적다. 문턱은 `STAR_THRESHOLDS`이고 앱 `logic/difficulty.ts`와 같다. 5×5보다 큰 판에서 별 1~2개(여유 비율 0.30 미만)는 너무 쉬워서 받지 않는다. 그림 안의 흰색·아주 밝은 색은 빈칸과 헷갈리니 칠하지 않고 비워 구멍으로 만든다.
- 앱에 든 퍼즐과 같은 id는 쓸 수 없다(`solver.py`의 `BUILT_IN_IDS`).
- 퍼즐을 고치면 `rev`가 바뀌어 이미 받은 앱도 그 퍼즐만 다시 받는다.
- 그림 출처는 `nonogram/CREDITS.md`.

## Twemoji에서 새 퍼즐 만들기

`scripts/nonogram/twemoji/`에 2026-10-13에 229개를 만든 도구가 있다. 먼저 `npm install`을 하고,
[Twemoji](https://github.com/jdecked/twemoji) 릴리스의 `assets/svg` 폴더를 받아 둔다.

1. `node gen.mjs <svg 폴더> ../../../nonogram/puzzles cands.json`: 그림마다 10~30 크기로 줄여 보고,
   build.py 기준을 통과한 판만 후보로 남긴다. 이미 있는 퍼즐과 이름이 같은 그림, 피부색·국기·가족 이모지는 뺀다.
2. `node sheet.mjs cands.json sheet.html max 0 80`: 번호 붙은 썸네일 시트를 만든다. Chrome으로 열어
   알아보기 쉬운 그림만 골라 `keep-all.txt`에 한 줄에 하나씩 적는다. 남자/여자/사람 버전처럼 같은 그림은 하나만 남긴다.
3. `node assign.mjs cands.json`: 그림 하나를 한 크기에만 나눈다. 크기별 시트를 다시 보고,
   그 크기에서 알아보기 어려운 그림은 `forbid.json`(`{"그림": [10, 15]}`)에, 10×10에서 알아볼 수 있는 그림은 `ok10.txt`에 적고 다시 나눈다.
4. `assign.json`대로 퍼즐 파일을 쓰고 이름을 다듬은 뒤 `python3 scripts/nonogram/build.py`로 검사한다.
