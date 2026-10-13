// Twemoji SVG → 노노그램 후보. 크기마다 build.py 기준(통짜 아님, 여유 비율 ≥ 0.30, 줄 추론만으로 풀림)을 통과한 것만 남긴다.
// 사용: node gen.mjs <twemoji svg 폴더> <퍼즐 폴더> <출력 json>
import fs from "node:fs";
import { Resvg } from "@resvg/resvg-js";

const [svgDir, puzzleDir, outFile] = process.argv.slice(2);
const SIZES = [10, 15, 20, 25, 30];
const RES = 600; // 렌더 해상도(정사각형으로 자른 뒤)
const MAX_COLORS = 6;

const ann = (lang, derived) => {
  const pkg = derived ? "cldr-annotations-derived-full/annotationsDerived" : "cldr-annotations-full/annotations";
  const file = `node_modules/${pkg}/${lang}/${derived ? "annotations" : "annotations"}.json`;
  const j = JSON.parse(fs.readFileSync(file, "utf8"));
  return (derived ? j.annotationsDerived : j.annotations).annotations;
};
const LANGS = { ko: "ko", en: "en", ja: "ja", "zh-Hans": "zh", "zh-Hant": "zh-Hant" };
const names = {};
for (const [k, l] of Object.entries(LANGS)) names[k] = { ...ann(l, true), ...ann(l, false) };
const tts = (lang, ch) => (names[lang][ch] ?? names[lang][ch.replace(/️/g, "")] ?? names[lang][ch + "️"])?.tts?.[0];

const used = new Set(fs.readdirSync(puzzleDir).map((f) => f.replace(/\.json$/, "").replace(/-(5|10|15|20|25|30)$/, "")));
for (const id of ["apple", "balloon", "cactus", "cat", "cherry", "coffee", "duck", "fox", "frog", "ghost", "heart", "house", "icecream", "lighthouse", "mushroom"]) used.add(id);

const lum = ([r, g, b]) => (0.2126 * r + 0.7152 * g + 0.0722 * b) / 255;
const dist = (a, b) => Math.hypot(a[0] - b[0], a[1] - b[1], a[2] - b[2]);
const hex = (c) => "#" + c.map((v) => Math.round(v).toString(16).padStart(2, "0")).join("").toUpperCase();

function render(svg) {
  const img = new Resvg(svg, { fitTo: { mode: "width", value: RES } }).render();
  const { width: w, height: h } = img, px = img.pixels;
  let x0 = w, y0 = h, x1 = -1, y1 = -1;
  for (let y = 0; y < h; y++) for (let x = 0; x < w; x++) if (px[(y * w + x) * 4 + 3] > 40) { x0 = Math.min(x0, x); x1 = Math.max(x1, x); y0 = Math.min(y0, y); y1 = Math.max(y1, y); }
  if (x1 < 0) return null;
  const side = Math.max(x1 - x0 + 1, y1 - y0 + 1), cx = (x0 + x1) / 2, cy = (y0 + y1) / 2;
  return { w, h, px, sx: cx - side / 2, sy: cy - side / 2, side };
}

/** 칸마다 덮인 비율과 가장 많은 색. 흰색·아주 밝은 색은 빈칸으로 둔다. */
function grid(r, n, minCover = 0.45, lightCut = 0.86, ox = 0, oy = 0) {
  const cells = [];
  for (let j = 0; j < n; j++) {
    const row = [];
    for (let i = 0; i < n; i++) {
      const counts = new Map(); let cover = 0, total = 0;
      const step = r.side / n, ax = r.sx + (i + ox) * step, ay = r.sy + (j + oy) * step;
      for (let y = Math.floor(ay); y < ay + step; y++) for (let x = Math.floor(ax); x < ax + step; x++) {
        total++;
        if (x < 0 || y < 0 || x >= r.w || y >= r.h) continue;
        const o = (y * r.w + x) * 4, a = r.px[o + 3];
        if (a < 128) continue;
        cover++;
        const key = (r.px[o] >> 3) << 10 | (r.px[o + 1] >> 3) << 5 | (r.px[o + 2] >> 3);
        const c = counts.get(key) ?? { n: 0, rgb: [r.px[o], r.px[o + 1], r.px[o + 2]] };
        c.n++; counts.set(key, c);
      }
      if (cover / total < minCover) { row.push(null); continue; }
      const top = [...counts.values()].sort((a, b) => b.n - a.n)[0].rgb;
      const sat = Math.max(...top) - Math.min(...top);
      row.push(lum(top) > lightCut && sat < 40 ? null : top);
    }
    cells.push(row);
  }
  return cells;
}

function quantize(cells) {
  let pal = [];
  for (const row of cells) for (const c of row) if (c) { const p = pal.find((q) => dist(q.rgb, c) < 30); if (p) p.n++; else pal.push({ rgb: c, n: 1 }); }
  // 가까운 색부터 합친다. 6색 이하, 서로 55 이상 떨어질 때까지.
  for (;;) {
    let best = null;
    for (let a = 0; a < pal.length; a++) for (let b = a + 1; b < pal.length; b++) { const d = dist(pal[a].rgb, pal[b].rgb); if (!best || d < best.d) best = { a, b, d }; }
    if (!best || (pal.length <= MAX_COLORS && best.d >= 55)) break;
    const [A, B] = [pal[best.a], pal[best.b]];
    const keep = A.n >= B.n ? A : B; keep.n = A.n + B.n;
    pal = pal.filter((p) => p !== (keep === A ? B : A));
  }
  pal.sort((a, b) => b.n - a.n);
  const letters = "abcdefgh";
  const rows = cells.map((row) => row.map((c) => { if (!c) return "."; let k = 0, d = Infinity; pal.forEach((p, i) => { const e = dist(p.rgb, c); if (e < d) { d = e; k = i; } }); return letters[k]; }).join(""));
  const palette = Object.fromEntries(pal.map((p, i) => [letters[i], hex(p.rgb)]));
  return { rows, palette };
}

// build.py와 같은 검사
const runsOf = (line) => (line.match(/[^.]+/g) ?? []).map((s) => s.length);
const columns = (rows) => [...rows[0]].map((_, c) => rows.map((r) => r[c]).join(""));
function slack(rows) {
  const lines = [...rows, ...columns(rows)]; let t = 0;
  for (const l of lines) { const r = runsOf(l); if (r.length) t += (l.length - (r.reduce((a, b) => a + b, 0) + r.length - 1)) / l.length; }
  return t / lines.length;
}
const solid = (rows) => [...rows, ...columns(rows)].every((l) => runsOf(l).length <= 1);
function solveLine(cells, clues) {
  const n = cells.length, m = clues.length, memo = new Map();
  const can = (i, k) => { const key = i * 64 + k; if (memo.has(key)) return memo.get(key); let ok = false;
    if (k === m) ok = cells.slice(i).every((v) => v !== 1);
    else { if (i < n && cells[i] !== 1 && can(i + 1, k)) ok = true; const len = clues[k];
      if (!ok && i + len <= n && cells.slice(i, i + len).every((v) => v !== 0) && (i + len === n || cells[i + len] !== 1)) ok = can(Math.min(i + len + 1, n), k + 1); }
    memo.set(key, ok); return ok; };
  if (!can(0, 0)) return null;
  const cf = Array(n).fill(false), ce = Array(n).fill(false), seen = new Set();
  const mark = (i, k) => { const key = i * 64 + k; if (seen.has(key) || !can(i, k)) return; seen.add(key);
    if (k === m) { for (let j = i; j < n; j++) ce[j] = true; return; }
    if (i < n && cells[i] !== 1 && can(i + 1, k)) { ce[i] = true; mark(i + 1, k); }
    const len = clues[k];
    if (i + len <= n && cells.slice(i, i + len).every((v) => v !== 0) && (i + len === n || cells[i + len] !== 1) && can(Math.min(i + len + 1, n), k + 1)) {
      for (let j = i; j < i + len; j++) cf[j] = true; if (i + len < n) ce[i + len] = true; mark(Math.min(i + len + 1, n), k + 1); } };
  mark(0, 0);
  return cells.map((v, j) => (v !== -1 ? v : cf[j] && !ce[j] ? 1 : ce[j] && !cf[j] ? 0 : -1));
}
function lineSolvable(rows) {
  const H = rows.length, W = rows[0].length;
  const rc = rows.map(runsOf), cc = columns(rows).map(runsOf);
  const g = Array.from({ length: H }, () => Array(W).fill(-1));
  let changed = true;
  while (changed) { changed = false;
    for (let r = 0; r < H; r++) { const nx = solveLine(g[r], rc[r]); if (!nx) return false; for (let c = 0; c < W; c++) if (nx[c] !== g[r][c]) { g[r][c] = nx[c]; changed = true; } }
    for (let c = 0; c < W; c++) { const nx = solveLine(g.map((x) => x[c]), cc[c]); if (!nx) return false; for (let r = 0; r < H; r++) if (nx[r] !== g[r][c]) { g[r][c] = nx[r]; changed = true; } } }
  return g.every((row) => row.every((v) => v !== -1));
}

const out = [];
const files = fs.readdirSync(svgDir).filter((f) => f.endsWith(".svg"));
for (const f of files) {
  const cps = f.replace(".svg", "").split("-").map((h) => parseInt(h, 16));
  if (cps.some((c) => (c >= 0x1f3fb && c <= 0x1f3ff) || (c >= 0x1f1e6 && c <= 0x1f1ff) || c === 0x20e3 || (c >= 0xe0000 && c <= 0xe007f))) continue;
  // 사람 둘 이상(가족·커플)은 작은 판에서 알아보기 어렵다.
  if (cps.filter((c) => [0x1f468, 0x1f469, 0x1f9d1, 0x1f466, 0x1f467, 0x1f48b, 0x2764].includes(c)).length >= 2) continue;
  if (cps.filter((c) => c !== 0x200d && c !== 0xfe0f).length > 3) continue;
  const ch = String.fromCodePoint(...cps);
  const n = Object.fromEntries(Object.keys(LANGS).map((k) => [k, tts(k, ch)]));
  if (Object.values(n).some((v) => !v)) continue;
  const slug = n.en.toLowerCase().normalize("NFKD").replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "");
  if (!slug || slug.length > 36 || used.has(slug)) continue;
  const r = render(fs.readFileSync(`${svgDir}/${f}`));
  if (!r) continue;
  for (const size of SIZES) {
    // 칸을 칠하는 기준을 바꿔 가며 처음 통과하는 판을 쓴다.
    const variants = [];
    for (const [ox, oy] of [[0, 0], [0.33, 0], [0, 0.33], [-0.33, 0], [0, -0.33], [0.33, 0.33]]) for (const [minCover, lightCut] of [[0.45, 0.86], [0.55, 0.86], [0.35, 0.86], [0.5, 0.8], [0.4, 0.92], [0.6, 0.8]]) variants.push([minCover, lightCut, ox, oy]);
    for (const [minCover, lightCut, ox, oy] of variants) {
      const { rows, palette } = quantize(grid(r, size, minCover, lightCut, ox, oy));
      const filled = rows.join("").replace(/\./g, "").length / (size * size);
      if (filled < 0.25 || filled > 0.85) continue;
      if (solid(rows)) continue;
      const s = slack(rows);
      if (s < 0.30) continue;
      if (!lineSolvable(rows)) continue;
      out.push({ id: `${slug}-${size}`, slug, cp: f.replace(".svg", ""), size, slack: +s.toFixed(3), name: n, palette, rows });
      break;
    }
  }
}
fs.writeFileSync(outFile, JSON.stringify(out));
const by = {}; for (const o of out) by[o.size] = (by[o.size] ?? 0) + 1;
console.log(out.length, "candidates", by, "emoji", new Set(out.map((o) => o.slug)).size);
