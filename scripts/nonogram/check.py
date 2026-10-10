"""내곁의 노노그램 퍼즐 묶음(nonogram/packs.json) 검사.

앱은 받은 퍼즐 중 모양·색이 바르고, 찍지 않고 줄 단위 추론만으로 답 하나로 풀리는 것만 쓴다.
올리기 전에 같은 기준으로 확인한다. 사용법: python3 scripts/nonogram/check.py [nonogram/packs.json]
"""
import sys, json
from functools import lru_cache
def clue(line):
    out=[];n=0
    for v in line:
        if v: n+=1
        elif n: out.append(n); n=0
    if n: out.append(n)
    return out
def solve_line(bl, line):
    n=len(line);k=len(bl)
    def fits(s,L):
        if s+L>n: return False
        if any(line[x]==2 for x in range(s,s+L)): return False
        return s+L==n or line[s+L]!=1
    @lru_cache(None)
    def feas(j,i):
        if j==k: return all(line[x]!=1 for x in range(i,n))
        L=bl[j]
        for s in range(i,n-L+1):
            if s>i and line[s-1]==1: break
            if fits(s,L) and feas(j+1,min(s+L+1,n)): return True
        return False
    if not feas(0,0): return None
    cf=[0]*n;ce=[0]*n;seen=set()
    def walk(j,i):
        if (j,i) in seen: return
        seen.add((j,i))
        if j==k:
            for x in range(i,n): ce[x]=1
            return
        L=bl[j]
        for s in range(i,n-L+1):
            if s>i and line[s-1]==1: break
            nx=min(s+L+1,n)
            if not fits(s,L) or not feas(j+1,nx): continue
            for x in range(i,s): ce[x]=1
            for x in range(s,s+L): cf[x]=1
            if s+L<n: ce[s+L]=1
            walk(j+1,nx)
    walk(0,0)
    return [m if m else (1 if cf[x] and not ce[x] else 2 if ce[x] and not cf[x] else 0) for x,m in enumerate(line)]
def stats(rows):
    h=len(rows);w=len(rows[0])
    sol=[[c!='.' for c in r] for r in rows]
    rc=[clue(r) for r in sol]; cc=[clue([sol[r][c] for r in range(h)]) for c in range(w)]
    g=[[0]*w for _ in range(h)];passes=0;first=0;ch=True
    while ch:
        ch=False;passes+=1
        for r in range(h):
            s=solve_line(tuple(rc[r]),g[r])
            if s and s!=g[r]: g[r]=s;ch=True
        for c in range(w):
            col=[g[r][c] for r in range(h)]
            s=solve_line(tuple(cc[c]),col)
            if s and s!=col:
                for r in range(h): g[r][c]=s[r]
                ch=True
        if passes==1: first=sum(v!=0 for row in g for v in row)/(w*h)
    ok=all((g[r][c]==1)==sol[r][c] and g[r][c]!=0 for r in range(h) for c in range(w))
    fill=sum(map(sum,sol))/(w*h)
    unk=[(r,c) for r in range(h) for c in range(w) if g[r][c]==0]
    return ok,passes,first,fill,unk,rc,cc
LANGS = ['ko', 'en', 'ja', 'zh-Hans', 'zh-Hant']
BUILT_IN_IDS = set('heart mushroom sun tree house cat apple duck umbrella star penguin ghost coffee fox whale cherry icecream sailboat frog cactus owl rocket teapot snowman balloon lighthouse'.split())
if __name__ == '__main__':
    import re
    doc = json.load(open(sys.argv[1] if len(sys.argv) > 1 else 'nonogram/packs.json'))
    assert doc.get('version') == 1, 'version은 1'
    seen = set(); bad = 0
    for pack in doc['packs']:
        for p in pack['puzzles']:
            pid = p['id']; rows = p['rows']; errs = []
            if not re.fullmatch(r'[a-z0-9-]{1,40}', pid): errs.append('ID는 소문자·숫자·- 40자 이내')
            if pid in seen or pid in BUILT_IN_IDS: errs.append('ID 중복(앱에 든 퍼즐과도 겹치면 안 됨)')
            seen.add(pid)
            missing = [l for l in LANGS if not p['name'].get(l)]
            if missing: errs.append(f'이름 없는 언어 {missing}(영어로 대신 보임)')
            if len(set(map(len, rows))) != 1: errs.append('줄 길이가 다름')
            if not (5 <= len(rows) <= 30 and 5 <= len(rows[0]) <= 30): errs.append('크기는 5~30')
            if any(ch != '.' and ch not in p['palette'] for r in rows for ch in r): errs.append('팔레트에 없는 글자')
            if not errs:
                ok, passes, first, fill, unk, *_ = stats(rows)
                if not ok: errs.append(f'줄 추론만으로 안 풀림(정해지지 않는 칸 {unk[:6]}…)')
                info = f'{len(rows[0])}x{len(rows)} 바퀴 {passes} 첫바퀴 {first:.0%} 칠함 {fill:.0%}'
            else:
                info = ''
            bad += bool(errs)
            print(f"{'✗' if errs else '✓'} {pack['id']}/{pid} {info} {' / '.join(errs)}")
    sys.exit(1 if bad else 0)
