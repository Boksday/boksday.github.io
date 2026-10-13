// 후보를 번호 붙은 썸네일 시트(HTML)로. 사용: node sheet.mjs cands.json out.html <크기|max> <시작> <개수> [slug목록파일]
import fs from "node:fs";
const [file, out, sizeArg, start, count, listFile] = process.argv.slice(2);
const all = JSON.parse(fs.readFileSync(file, "utf8"));
const bySlug = new Map();
for (const c of all) { const l = bySlug.get(c.slug) ?? []; l.push(c); bySlug.set(c.slug, l); }
let slugs = listFile ? fs.readFileSync(listFile, "utf8").split("\n").filter(Boolean) : [...bySlug.keys()];
if (sizeArg !== "max") slugs = slugs.filter((s) => bySlug.get(s).some((c) => c.size === +sizeArg));
slugs = slugs.slice(+start, +start + +count);
let h = `<body style="margin:0;background:#FBF6EE;display:flex;flex-wrap:wrap;width:2000px;font:600 13px -apple-system,sans-serif">`;
slugs.forEach((slug, k) => {
  const list = bySlug.get(slug);
  const c = sizeArg === "max" ? list.reduce((a, b) => (b.size > a.size ? b : a)) : list.find((x) => x.size === +sizeArg);
  const cell = Math.floor(150 / c.size);
  h += `<div style="width:200px;height:200px;text-align:center;box-sizing:border-box;padding-top:6px"><svg width="${cell * c.size}" height="${cell * c.size}">`;
  c.rows.forEach((r, y) => [...r].forEach((ch, x) => { if (ch !== ".") h += `<rect x="${x * cell}" y="${y * cell}" width="${cell}" height="${cell}" fill="${c.palette[ch]}"/>`; }));
  h += `</svg><div>${+start + k} ${slug.slice(0, 22)}</div><div style="color:#888;font-weight:400">${c.name.ko.slice(0, 14)} [${list.map((x) => x.size).join(",")}]</div></div>`;
});
fs.writeFileSync(out, h);
console.log(slugs.length);
