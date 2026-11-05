"""루미클린(/lumiclean/privacy/) 개인정보처리방침을 18개 언어로 만든다.

    python3 scripts/pages/lumiclean_privacy.py

앱 소개·지원 페이지가 아직 없어 gen.py와 따로 둔다. 문구는 lumiclean_content.py와 lumiclean_extra_privacy.py에 있다.
"""
import html
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from content import HTML_LANG as BASE_HTML_LANG, LANG_NAME as BASE_LANG_NAME  # noqa: E402
from lumiclean_extra_privacy import EXTRA  # noqa: E402
LANGS = ['ko', 'en', 'en-gb', 'ja', 'zh-hans', 'zh-hant', 'sv', 'da', 'nb', 'nl', 'de', 'fr', 'es', 'pt', 'it', 'tr', 'ru', 'ar']
HTML_LANG = {**BASE_HTML_LANG, **{c: c for c in LANGS}, 'en-gb': 'en-GB', 'zh-hans': 'zh-Hans', 'zh-hant': 'zh-Hant'}
LANG_NAME = {**BASE_LANG_NAME, 'en-gb': 'English (UK)', 'sv': 'Svenska', 'da': 'Dansk', 'nb': 'Norsk bokmål', 'nl': 'Nederlands', 'de': 'Deutsch', 'fr': 'Français', 'es': 'Español', 'pt': 'Português', 'it': 'Italiano', 'tr': 'Türkçe', 'ru': 'Русский', 'ar': 'العربية'}
from lumiclean_content import NAME, privacy  # noqa: E402

SITE = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
BASE = 'https://boksday.github.io'
CURRENT = ' aria-current="page"'
LANG_LABEL = {'ko': '언어', 'en': 'Language', 'ja': '言語', 'zh-hans': '语言', 'zh-hant': '語言', 'en-gb': 'Language', 'sv': 'Språk', 'da': 'Sprog', 'nb': 'Språk', 'nl': 'Taal', 'de': 'Sprache', 'fr': 'Langue', 'es': 'Idioma', 'pt': 'Idioma', 'it': 'Lingua', 'tr': 'Dil', 'ru': 'Язык', 'ar': 'اللغة'}

# 한국어(기본 주소)에서만: 기기 언어가 한국어가 아니면 맞는 언어 페이지로 보낸다. 앱은 기본 주소를 연다.
REDIRECT = """<script>
    (function () {
      if (/[?&]lang=ko\\b/.test(location.search)) return;
      var l = ((navigator.languages && navigator.languages[0]) || navigator.language || '').toLowerCase();
      if (!l || /^ko/.test(l)) return;
      var target = 'en';
      if (/^en-gb/.test(l)) target = 'en-gb';
      else if (/^(sv|da|nb|no|nl|de|fr|es|pt|it|tr|ru|ar)(-|$)/.test(l)) target = l.split('-')[0] === 'no' ? 'nb' : l.split('-')[0];
      else if (/^ja/.test(l)) target = 'ja';
      else if (/^zh-(hant|tw|hk|mo)/.test(l)) target = 'zh-hant';
      else if (/^zh/.test(l)) target = 'zh-hans';
      location.replace(location.pathname.replace(/\\/?$/, '/') + target + '/');
    })();
  </script>"""


def path(lang):
    return '/lumiclean/privacy/' + ('' if lang == 'ko' else f'{lang}/')


def page(lang):
    e = html.escape
    p = EXTRA[lang] if lang in EXTRA else privacy(lang)
    langs = ''.join(
        f'<a href="{path(c)}{"?lang=ko" if c == "ko" else ""}" hreflang="{HTML_LANG[c]}" lang="{HTML_LANG[c]}"'
        f'{CURRENT if c == lang else ""}>{LANG_NAME[c]}</a>'
        for c in LANGS)
    alternates = '\n  '.join(
        [f'<link rel="alternate" hreflang="{HTML_LANG[c]}" href="{BASE}{path(c)}">' for c in LANGS]
        + [f'<link rel="alternate" hreflang="x-default" href="{BASE}{path("ko")}">'])
    summary = ''.join(f'<li>{e(x)}</li>' for x in p['summary'])
    sections = '\n'.join(
        f'    <section>\n      <h2>{e(h)}</h2>\n      ' + '\n      '.join(parts) + '\n    </section>'
        for h, parts in p['sections'])
    redirect = ('\n  ' + REDIRECT) if lang == 'ko' else ''
    return f"""<!doctype html>
<html lang="{HTML_LANG[lang]}" dir="{'rtl' if lang == 'ar' else 'ltr'}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <meta name="color-scheme" content="light dark">
  <meta name="theme-color" content="#F4F4F2" media="(prefers-color-scheme: light)">
  <meta name="theme-color" content="#0F0F10" media="(prefers-color-scheme: dark)">
  <title>{e(p['title'])}</title>
  <meta name="description" content="{e(p['summary'][0])}">
  {alternates}
  <link rel="icon" href="/lumiclean/icon.png">
  <link rel="apple-touch-icon" href="/lumiclean/icon.png">
  <link rel="stylesheet" href="/lumiclean/privacy.css">{redirect}
</head>
<body>
  <main>
    <header class="masthead">
      <img class="app-icon" src="/lumiclean/icon.png" width="64" height="64" alt="">
      <p class="app-name">{e(NAME.get(lang, "Lumiclean"))}</p>
      <h1>{e(p['title'])}</h1>
      <p class="date">{e(p['date'])}</p>
    </header>
    <nav class="langs" aria-label="{LANG_LABEL[lang]}">{langs}</nav>
    <p class="intro">{e(p['intro'])}</p>
    <section class="summary" aria-labelledby="summary-h">
      <h2 id="summary-h">{e(p['summary_h'])}</h2>
      <ul>{summary}</ul>
    </section>
{sections}
    <footer>
      <a class="mail" href="mailto:ekqlszzzz@naver.com">{e(p['contact_h'])} · ekqlszzzz@naver.com</a>
    </footer>
  </main>
</body>
</html>
"""


for lang in LANGS:
    full = os.path.join(SITE, path(lang).lstrip('/'), 'index.html')
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, 'w') as f:
        f.write(page(lang))
print('ok')
