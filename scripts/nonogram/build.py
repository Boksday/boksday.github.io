"""내곁의 노노그램 퍼즐 목록(nonogram/index.json)을 만든다.

퍼즐 하나는 nonogram/puzzles/<id>.json 파일 하나다. 이 스크립트가 모든 퍼즐을 검사하고(모양·색·5개 언어 이름,
찍지 않고 줄 추론만으로 답 하나로 풀리는지) 통과하면 목록을 다시 쓴다. 하나라도 틀리면 목록을 쓰지 않는다.
앱은 목록만 하루 한 번 받고, 퍼즐 파일은 사용자가 그 퍼즐을 누를 때 받는다.
rev는 퍼즐 내용으로 만든 값이라 퍼즐을 고치면 바뀌고, 앱은 rev가 바뀐 퍼즐만 다시 받는다.

사용법: python3 scripts/nonogram/build.py
"""
import glob
import hashlib
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(__file__))
from format import dump_puzzle  # noqa: E402
from solver import BUILT_IN_IDS, LANGS, stats  # noqa: E402

ROOT = os.path.join(os.path.dirname(__file__), '..', '..', 'nonogram')
FORMAT_VERSION = 2
MAX_SIZE = 30


def stars_of(rows, passes, first):
    """앱의 starsOf(logic/difficulty.ts)와 같은 계산"""
    size = max(len(rows), len(rows[0]))
    base = min(max(round((size - 5) / 5) + 1, 1), 5)
    adjust = 0
    if passes >= 6 or first < 0.5:
        adjust = 1
    elif passes <= 2 and first > 0.95:
        adjust = -1
    return min(max(base + adjust, 1), 5)


def validate(path, puzzle):
    errors = []
    pid = puzzle.get('id')
    if os.path.basename(path) != f'{pid}.json':
        errors.append('파일 이름과 id가 다름')
    if not isinstance(pid, str) or not re.fullmatch(r'[a-z0-9-]{1,40}', pid):
        errors.append('id는 소문자·숫자·- 40자 이내')
    if pid in BUILT_IN_IDS:
        errors.append('앱에 든 퍼즐과 id가 겹침')
    name = puzzle.get('name') or {}
    missing = [lang for lang in LANGS if not name.get(lang)]
    if missing:
        errors.append(f'이름 없는 언어 {missing}')
    rows, palette = puzzle.get('rows') or [], puzzle.get('palette') or {}
    if not rows or len(set(map(len, rows))) != 1:
        errors.append('줄 길이가 다름')
    elif not (5 <= len(rows) <= MAX_SIZE and 5 <= len(rows[0]) <= MAX_SIZE):
        errors.append(f'크기는 5~{MAX_SIZE}')
    if any(not re.fullmatch(r'#[0-9A-Fa-f]{6}', str(c)) for c in palette.values()):
        errors.append('색은 #RRGGBB')
    if any(ch != '.' and ch not in palette for row in rows for ch in row):
        errors.append('팔레트에 없는 글자')
    return errors


def main():
    entries, failed = [], 0
    for path in sorted(glob.glob(os.path.join(ROOT, 'puzzles', '*.json'))):
        puzzle = json.load(open(path, encoding='utf-8'))
        errors = validate(path, puzzle)
        if not errors:
            ok, passes, first, *_ = stats(puzzle['rows'])
            if not ok:
                errors.append('줄 추론만으로 안 풀림(답이 여러 개이거나 찍어야 함)')
        if errors:
            failed += 1
            print(f'✗ {os.path.basename(path)}: {" / ".join(errors)}')
            continue
        rows = puzzle['rows']
        # 손으로 고친 파일도 같은 모양으로 맞춰 둔다.
        formatted = dump_puzzle(puzzle)
        if open(path, encoding='utf-8').read() != formatted:
            with open(path, 'w', encoding='utf-8') as file:
                file.write(formatted)
        body = json.dumps({k: puzzle[k] for k in ('name', 'palette', 'rows')}, ensure_ascii=False, sort_keys=True)
        entries.append({
            'id': puzzle['id'],
            'file': f'puzzles/{puzzle["id"]}.json',
            'width': len(rows[0]),
            'height': len(rows),
            'stars': stars_of(rows, passes, first),
            'rev': hashlib.sha1(body.encode()).hexdigest()[:8],
        })
    if failed:
        print(f'{failed}개 실패. index.json을 쓰지 않았어요.')
        sys.exit(1)
    entries.sort(key=lambda e: (max(e['width'], e['height']), e['stars'], e['id']))
    index = {'version': FORMAT_VERSION, 'puzzles': entries}
    with open(os.path.join(ROOT, 'index.json'), 'w', encoding='utf-8') as file:
        json.dump(index, file, ensure_ascii=False, separators=(',', ':'))
        file.write('\n')
    from collections import Counter
    sizes = Counter(max(e['width'], e['height']) for e in entries)
    print(f'✓ {len(entries)}개 →  index.json  크기별 {dict(sorted(sizes.items()))}')


if __name__ == '__main__':
    main()
