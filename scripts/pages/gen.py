"""boksday.github.io 의 여비(/trip/)·디데이(/dday/) 소개·개인정보·지원 페이지를 5개 언어로 만든다."""
import html
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
import content  # noqa: E402
import dday_content  # noqa: E402
from content import EMAIL, HTML_LANG, LANG_NAME, LANGS  # noqa: E402
from privacy import PRIVACY as TRIP_PRIVACY  # noqa: E402
from support import SUPPORT as TRIP_SUPPORT  # noqa: E402

SITE = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
BASE = 'https://boksday.github.io'

DARK_ALT = {
    'ko': '다크 모드 지출 화면',
    'en': 'Expenses screen in dark mode',
    'ja': 'ダークモードの支出画面',
    'zh-hans': '深色模式下的支出页面',
    'zh-hant': '深色模式下的支出頁面',
}
LANG_LABEL = {'ko': '언어', 'en': 'Language', 'ja': '言語', 'zh-hans': '语言', 'zh-hant': '語言'}

DDAY_KO_SHOTS = [
    ('/dday/img/01-album.jpg', '사진으로 꾸민 디데이가 앨범처럼 모여 있는 첫 화면'),
    ('/dday/img/02-milestones.jpg', '100일·1000일 기념일까지 남은 날을 보여 주는 화면'),
    ('/dday/img/03-lunar.jpg', '음력 생신을 해마다 양력으로 바꿔 주는 화면'),
    ('/dday/img/04-calendar.jpg', '이번 달 디데이를 달력으로 보는 화면'),
    ('/dday/img/05-share.jpg', '디데이를 사진 공유 카드로 만드는 화면'),
    ('/dday/img/06-views.jpg', '목록·카드·앨범·달력 보기를 고르는 화면'),
    ('/dday/img/07-dark.jpg', '다크 모드 화면'),
]


READY = {
    'ko': ('App Store에서 받기', 'Google Play에서 받기'),
    'en': ('Download on the App Store', 'Get it on Google Play'),
    'ja': ('App Store からダウンロード', 'Google Play で手に入れよう'),
    'zh-hans': ('在 App Store 下载', '在 Google Play 下载'),
    'zh-hant': ('在 App Store 下載', '在 Google Play 下載'),
}


class App:
    def __init__(self, slug, names, intro, privacy, support, store_urls=('', '')):
        self.slug = slug
        self.store_urls = store_urls
        self.names = names
        self.intro = intro
        self._privacy = privacy
        self.support = support

    def privacy(self, lang):
        return self._privacy(lang) if callable(self._privacy) else self._privacy[lang]

    def path(self, section, lang):
        """section: '' | 'privacy/' | 'support/'"""
        sub = '' if lang == 'ko' else f'{lang}/'
        return f'/{self.slug}/{section}{sub}'

    def screenshots(self, lang):
        """[(src, alt)] 언어별 스크린샷. 없으면 빈 목록."""
        if self.slug == 'dday':
            return DDAY_KO_SHOTS if lang == 'ko' else []
        img_dir = os.path.join(SITE, 'trip/img', lang)
        files = sorted(f[:-4] for f in os.listdir(img_dir) if f[0].isdigit() and f.endswith('.jpg'))
        alts = dict(self.intro[lang]['shots'])
        return [(f'/trip/img/{lang}/{f}.jpg', alts.get(f, DARK_ALT[lang] if 'dark' in f else '')) for f in files]


def lang_menu(app, section, lang):
    items = []
    for code in LANGS:
        href = app.path(section, code) + ('?lang=ko' if code == 'ko' else '')
        current = ' aria-current="page"' if code == lang else ''
        items.append(f'<a href="{href}" hreflang="{HTML_LANG[code]}" lang="{HTML_LANG[code]}"{current}>{LANG_NAME[code]}</a>')
    return f'<nav class="langs" aria-label="{LANG_LABEL[lang]}">' + ''.join(items) + '</nav>'


def alternates(app, section):
    out = [f'<link rel="alternate" hreflang="{HTML_LANG[c]}" href="{BASE}{app.path(section, c)}">' for c in LANGS]
    out.append(f'<link rel="alternate" hreflang="x-default" href="{BASE}{app.path(section, "ko")}">')
    return '\n  '.join(out)


# 한국어(기본 주소)에서만: 기기 언어가 한국어가 아니면 맞는 언어 페이지로 보낸다.
# 앱은 언어 없이 /trip/privacy/ 같은 기본 주소를 연다. 언어 메뉴에서 한국어를 고르면 ?lang=ko로 멈춘다.
# 예전 주소의 #en도 영어 페이지로 보낸다.
REDIRECT = """<script>
    (function () {
      if (/[?&]lang=ko\\b/.test(location.search)) return;
      var target = null;
      if (location.hash === '#en') target = 'en';
      else {
        var l = ((navigator.languages && navigator.languages[0]) || navigator.language || '').toLowerCase();
        if (!l || /^ko/.test(l)) return;
        if (/^ja/.test(l)) target = 'ja';
        else if (/^zh-(hant|tw|hk|mo)/.test(l)) target = 'zh-hant';
        else if (/^zh/.test(l)) target = 'zh-hans';
        else target = 'en';
      }
      location.replace(location.pathname.replace(/\\/?$/, '/') + target + '/');
    })();
  </script>"""


def head(app, lang, section, title, desc, css, og_image=None):
    e = html.escape
    og = ''
    if og_image:
        og = f"""
  <meta property="og:type" content="website">
  <meta property="og:title" content="{e(app.names[lang])}">
  <meta property="og:description" content="{e(desc)}">
  <meta property="og:image" content="{BASE}{og_image}">
  <meta property="og:url" content="{BASE}{app.path(section, lang)}">"""
    redirect = ('\n  ' + REDIRECT) if lang == 'ko' else ''
    return f"""<!doctype html>
<html lang="{HTML_LANG[lang]}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{e(title)}</title>
  <meta name="description" content="{e(desc)}">{og}
  {alternates(app, section)}
  <link rel="icon" href="/{app.slug}/icon.png">
  <link rel="stylesheet" href="{css}">{redirect}
</head>"""


def write(path, text):
    full = os.path.join(SITE, path.lstrip('/'), 'index.html')
    os.makedirs(os.path.dirname(full), exist_ok=True)
    # 빈 자리(스크린샷 없음 등)가 남긴 줄 끝 공백과 빈 줄 겹침을 정리한다.
    lines = [line.rstrip() for line in text.split('\n')]
    out = []
    for line in lines:
        if line == '' and out and out[-1] == '':
            continue
        out.append(line)
    with open(full, 'w') as f:
        f.write('\n'.join(out))


def intro(app, lang):
    c = app.intro[lang]
    e = html.escape
    shots = app.screenshots(lang)
    gallery = '\n        '.join(
        f'<figure><img src="{src}" width="600" height="1304" loading="lazy" alt="{e(a)}"></figure>'
        for src, a in shots[1:])
    chips = ''.join(f'<li>{e(x)}</li>' for x in c['chips'])
    feats = '\n        '.join(f'<li><strong>{e(t)}</strong><span>{e(d)}</span></li>' for t, d in c['features'])
    promise = ''.join(f'<p>{e(p)}</p>' for p in c['promise'])
    n_screens, n_feat, n_support = c['nav']
    f_support, f_privacy, f_contact = c['footer']
    og = f'/trip/img/{lang}/header.jpg' if app.slug == 'trip' else '/dday/img/header.jpg'
    css = f'/{app.slug}/{app.slug}.css'
    screens_nav = f'<a href="#screens">{e(n_screens)}</a>' if len(shots) > 1 else ''
    hero_shot = (f'<div class="hero-shot"><img src="{shots[0][0]}" width="600" height="1304" alt="{e(shots[0][1])}"></div>'
                 if shots else '')
    screens = f'''<section class="block" id="screens">
      <h2>{e(c['screens_h'])}</h2>
      <p class="sub">{e(c['screens_sub'])}</p>
      <div class="gallery" tabindex="0" aria-label="{e(c['screens_h'])}">
        {gallery}
      </div>
    </section>''' if len(shots) > 1 else ''
    note = f'<p class="note">{e(c["note"])}</p>' if c.get('note') else ''
    hero_class = 'hero' if shots else 'hero no-shot'
    buttons = []
    for i, url in enumerate(app.store_urls):
        if url:
            buttons.append(f'<a class="store-button" href="{url}">{e(READY[lang][i])}</a>')
        else:
            buttons.append(f'<span class="store-button pending">{e(c["store"][i])}</span>')
    store_buttons = '\n          '.join(buttons)
    return head(app, lang, '', c['title'], c['desc'], css, og) + f"""
<body>
  <header class="top">
    <div class="wrap">
      <a class="wordmark" href="/">{'내곁의' if lang == 'ko' else 'BySide'}</a>
      <nav class="sections">
        {screens_nav}
        <a href="#features">{e(n_feat)}</a>
        <a href="{app.path('support/', lang)}">{e(n_support)}</a>
      </nav>
    </div>
    <div class="wrap">{lang_menu(app, '', lang)}</div>
  </header>

  <section class="{hero_class}">
    <div class="wrap">
      <div class="hero-text">
        <img class="app-icon" src="/{app.slug}/icon.png" alt="{e(app.names[lang])}">
        <p class="app-name">{e(app.names[lang])}</p>
        <h1>{c['h1']}</h1>
        <p class="lead">{c['lead']}</p>
        <ul class="chips">{chips}</ul>
        <div class="store-buttons">
          {store_buttons}
        </div>
      </div>
      {hero_shot}
    </div>
  </section>

  <main class="wrap">
    {screens}

    <section class="block" id="features">
      <h2>{e(c['feat_h'])}</h2>
      <p class="sub">{e(c['feat_sub'])}</p>
      <ul class="features">
        {feats}
      </ul>
    </section>

    <section class="block">
      <div class="promise">
        <h2>{e(c['promise_h'])}</h2>
        {promise}
      </div>
      {note}
    </section>
  </main>

  <footer>
    <div class="wrap">
      <a href="{app.path('support/', lang)}">{e(f_support)}</a> · <a href="{app.path('privacy/', lang)}">{e(f_privacy)}</a> · {e(f_contact)} <a href="mailto:{EMAIL}">{EMAIL}</a>
    </div>
  </footer>
</body>
</html>
"""


def doc_page(app, lang, section, title, body):
    return head(app, lang, section, f'{title} · {app.names[lang]}', title, '/style.css') + f"""
<body>
  <main>
    <p class="muted crumbs"><a href="{app.path('', lang)}">{html.escape(app.names[lang])}</a></p>
    {lang_menu(app, section, lang)}
{body}
  </main>
</body>
</html>
"""


def privacy_page(app, lang):
    p = app.privacy(lang)
    parts = [f'    <h1>{html.escape(p["title"])}</h1>', f'    <p class="muted">{p["date"]}</p>', f'    <p>{html.escape(p["intro"])}</p>']
    for h, paras in p['sections']:
        parts.append(f'    <h2>{html.escape(h)}</h2>')
        parts.extend('    ' + x for x in paras)
    return doc_page(app, lang, 'privacy/', p['title'], '\n'.join(parts))


def support_page(app, lang):
    s = app.support[lang]
    priv = app.privacy(lang)['title']
    parts = [
        f'    <h1>{html.escape(s["title"])}</h1>',
        f'    <p>{html.escape(s["intro"])}</p>',
        f'    <p><strong>{html.escape(s["contact"])}:</strong> <a href="mailto:{EMAIL}">{EMAIL}</a></p>',
        f'    <p class="muted">{s["hint"]}</p>',
        f'    <h2>{html.escape(s["faq_h"])}</h2>',
    ]
    for q, a in s['faq']:
        parts.append(f'    <p><strong>{html.escape(q)}</strong><br>\n    {a}</p>')
    parts.append(f'    <p><a href="{app.path("privacy/", lang)}">{html.escape(priv)}</a></p>')
    return doc_page(app, lang, 'support/', s['title'], '\n'.join(parts))


APPS = [
    App('trip', content.APP, content.INTRO, TRIP_PRIVACY, TRIP_SUPPORT),
    App('dday', dday_content.APP, dday_content.INTRO, dday_content.privacy, dday_content.SUPPORT,
        ('', 'https://play.google.com/store/apps/details?id=com.naegyeot.dday')),
]

for app in APPS:
    if len(sys.argv) > 1 and app.slug not in sys.argv[1:]:
        continue
    for lang in LANGS:
        write(app.path('', lang), intro(app, lang))
        write(app.path('privacy/', lang), privacy_page(app, lang))
        write(app.path('support/', lang), support_page(app, lang))
print('ok')
