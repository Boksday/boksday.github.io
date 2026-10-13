// 남긴 그림을 크기 단계에 나눈다. 단순한 그림은 작은 판, 복잡한 그림은 큰 판. 그림 하나는 한 단계에만.
// 사용: node assign.mjs [cands.json]  (keep-all.txt, forbid.json, ok10.txt를 현재 폴더에서 읽는다)
import fs from "node:fs";
const a = JSON.parse(fs.readFileSync(process.argv[2] ?? "cands.json", "utf8"));
const keep = fs.readFileSync("keep-all.txt", "utf8").trim().split("\n");
// 눈으로 보고 그 크기에서 알아보기 어려웠던 그림
const forbid = fs.existsSync("forbid.json") ? JSON.parse(fs.readFileSync("forbid.json", "utf8")) : {};
// 10×10은 눈으로 확인해 알아볼 수 있던 것만 쓴다.
const ok10 = fs.existsSync("ok10.txt") ? new Set(fs.readFileSync("ok10.txt", "utf8").trim().split("\n")) : null;
const ok = (s, size) => (size !== 10 || !ok10 || ok10.has(s)) && by.get(s).some((c) => c.size === size) && !(forbid[s] ?? []).includes(size);
const by = new Map();
for (const c of a) { if (!by.has(c.slug)) by.set(c.slug, []); by.get(c.slug).push(c); }
// 복잡도: 가장 큰 판에서 옆 칸과 색이 다른 경계 비율
const detail = (slug) => {
  const c = by.get(slug).reduce((x, y) => (y.size > x.size ? y : x)); let t = 0;
  c.rows.forEach((r, j) => [...r].forEach((ch, i) => { if (i && r[i - 1] !== ch) t++; if (j && c.rows[j - 1][i] !== ch) t++; }));
  return t / (c.size * c.size);
};
const sizes = [10, 15, 20, 25, 30];
const n10 = ok10 ? [...ok10].filter((s) => keep.includes(s)).length : Math.floor(keep.length / 5);
const per = Math.floor((keep.length - n10) / 4), extra = (keep.length - n10) % 4;
const left = new Set(keep), out = {};
const order = keep.map((s) => [s, detail(s)]).sort((x, y) => x[1] - y[1]);
sizes.forEach((size, k) => {
  const want = size === 10 ? n10 : per + (k >= 5 - extra ? 1 : 0);
  // 이 크기로 만들 수 있는 것 중 단순한 순서. 다음 크기들이 굶지 않게 이 크기만 가능한 것을 먼저.
  const can = order.filter(([s]) => left.has(s) && ok(s, size));
  const only = can.filter(([s]) => !sizes.some((z) => z > size && ok(s, z)));
  const pick = [...only, ...can.filter((x) => !only.includes(x))].slice(0, want).map(([s]) => s);
  pick.forEach((s) => left.delete(s));
  out[size] = pick;
});
fs.writeFileSync("assign.json", JSON.stringify(out, null, 1));
console.log(Object.fromEntries(Object.entries(out).map(([k, v]) => [k, v.length])), "unassigned", [...left]);
for (const [size, list] of Object.entries(out)) fs.writeFileSync(`tier-${size}.txt`, list.join("\n") + "\n");
