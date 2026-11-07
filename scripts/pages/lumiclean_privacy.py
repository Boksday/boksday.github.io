# -*- coding: utf-8 -*-
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

ANALYTICS = {
'ko': ('앱은 회원가입이나 로그인이 없고 운영자가 운영하는 서버도 없습니다. 사진과 동영상 파일은 운영자에게 보내지 않습니다.', '앱은 사용 현황을 파악하고 개선하기 위해 Google LLC의 Firebase Analytics를 사용합니다. 앱 실행, 세션, 자동 구매 이벤트 등 자동 수집 이벤트, 앱 인스턴스 식별자, 기기·운영체제 정보와 IP 주소에서 추정한 대략적인 지역 등이 Google에 전송될 수 있으며, 운영자는 분석 결과를 볼 수 있습니다. 사진과 동영상 파일은 분석에 포함되지 않습니다. 분석 수집은 기본적으로 꺼져 있으며 지역별 동의 상태에 따라 제한됩니다. Google의 처리 방식은 <a href="https://policies.google.com/privacy">Google 개인정보처리방침</a>을 확인하세요.'),
'en': ('The App has no sign-up or login, and we run no server. Your photo and video files are not sent to us.', 'The App uses Google LLC’s Firebase Analytics to understand usage and improve the App. Automatically collected events such as app opens, sessions and automatic purchase events, sessions and automatic purchase events, an app instance identifier, device and operating system information, and approximate region inferred from IP address may be sent to Google; we can view analytics results. Photo and video files are not included in analytics. Analytics collection is off by default and is restricted according to regional consent status. See the <a href="https://policies.google.com/privacy">Google Privacy Policy</a>.'),
'en-gb': ('The App has no sign-up or login, and we run no server. Your photo and video files are not sent to us.', 'The App uses Google LLC’s Firebase Analytics to understand usage and improve the App. Automatically collected events such as app opens, sessions and automatic purchase events, sessions and automatic purchase events, an app instance identifier, device and operating system information, and approximate region inferred from IP address may be sent to Google; we can view analytics results. Photo and video files are not included in analytics. Analytics collection is off by default and is restricted according to regional consent status. See the <a href="https://policies.google.com/privacy">Google Privacy Policy</a>.'),
'ja': ('本アプリには会員登録やログインがなく、運営者が運営するサーバーもありません。写真や動画ファイルを運営者に送信することはありません。', '本アプリは利用状況の把握と改善のため、Google LLCのFirebase Analyticsを使用します。アプリの起動、セッション、自動購入イベントなど自動収集されるイベント、アプリインスタンス識別子、端末・OS情報、IPアドレスから推定されるおおよその地域がGoogleに送信される場合があり、運営者は分析結果を確認できます。写真や動画ファイルは分析に含まれません。分析データの収集は初期状態では無効で、地域ごとの同意状況に応じて制限されます。<a href="https://policies.google.com/privacy">Googleプライバシーポリシー</a>をご覧ください。'),
'zh-hans': ('本应用无需注册或登录，我们也不运营服务器。照片和视频文件不会发送给我们。', '本应用使用 Google LLC 的 Firebase Analytics 了解使用情况并改进应用。应用启动、会话和自动购买事件等自动收集的事件、应用实例标识符、设备及操作系统信息以及根据 IP 地址推断的大致地区可能会发送给 Google；我们可以查看分析结果。分析不包含照片或视频文件。分析数据收集默认关闭，并根据所在地区的同意状态受到限制。请参阅 <a href="https://policies.google.com/privacy">Google 隐私权政策</a>。'),
'zh-hant': ('本 App 無須註冊或登入，我們也不經營伺服器。照片與影片檔案不會傳送給我們。', '本 App 使用 Google LLC 的 Firebase Analytics 了解使用情況並改善 App。App 啟動、工作階段及自動購買事件等自動收集的事件、App 執行個體識別碼、裝置及作業系統資訊，以及依 IP 位址推測的大致地區可能會傳送給 Google；我們可以查看分析結果。分析不包含照片或影片檔案。分析資料收集預設關閉，並依所在地區的同意狀態受到限制。請參閱 <a href="https://policies.google.com/privacy">Google 隱私權政策</a>。'),
'sv': ('Appen kräver ingen registrering eller inloggning och vi driver ingen server. Dina foto- och videofiler skickas inte till oss.', 'Appen använder Firebase Analytics från Google LLC för att förstå användningen och förbättra appen. Automatiskt insamlade händelser som appstarter, sessioner och automatiska köphändelser, en appinstansidentifierare, enhets- och operativsysteminformation samt ungefärlig region baserad på IP-adressen kan skickas till Google; vi kan se analysresultaten. Foto- och videofiler ingår inte i analysen. Analysinsamling är avstängd som standard och begränsas utifrån samtyckesstatus i regionen. Se <a href="https://policies.google.com/privacy">Googles integritetspolicy</a>.'),
'da': ('Appen kræver ingen tilmelding eller login, og vi driver ingen server. Dine foto- og videofiler sendes ikke til os.', 'Appen bruger Firebase Analytics fra Google LLC til at forstå brugen og forbedre appen. Automatisk indsamlede hændelser som appstart, sessioner og automatiske købshændelser, en appinstansidentifikator, enheds- og operativsystemoplysninger samt omtrentligt område udledt af IP-adressen kan sendes til Google; vi kan se analyseresultaterne. Foto- og videofiler indgår ikke i analysen. Analyseindsamling er som standard slået fra og begrænses efter samtykkestatus i regionen. Se <a href="https://policies.google.com/privacy">Googles privatlivspolitik</a>.'),
'nb': ('Appen krever ingen registrering eller innlogging, og vi driver ingen server. Bilde- og videofilene dine sendes ikke til oss.', 'Appen bruker Firebase Analytics fra Google LLC for å forstå bruk og forbedre appen. Automatisk innsamlede hendelser som appstart, økter og automatiske kjøpshendelser, en appinstansidentifikator, enhets- og operativsysteminformasjon og omtrentlig område utledet fra IP-adressen kan sendes til Google; vi kan se analyseresultatene. Bilde- og videofiler inngår ikke i analysen. Analyseinnsamling er som standard slått av og begrenses ut fra samtykkestatus i regionen. Se <a href="https://policies.google.com/privacy">Googles personvernregler</a>.'),
'nl': ('De app vereist geen registratie of aanmelding en wij beheren geen server. Je foto- en videobestanden worden niet naar ons verzonden.', 'De app gebruikt Firebase Analytics van Google LLC om gebruik te begrijpen en de app te verbeteren. Automatisch verzamelde gebeurtenissen zoals het openen van de app, sessies en automatische aankoopgebeurtenissen, een app-instantie-ID, apparaat- en besturingssysteemgegevens en een geschatte regio afgeleid van het IP-adres kunnen naar Google worden verzonden; wij kunnen analyseresultaten bekijken. Foto- en videobestanden maken geen deel uit van de analyse. Analyseverzameling staat standaard uit en wordt beperkt op basis van de toestemmingsstatus in de regio. Zie het <a href="https://policies.google.com/privacy">privacybeleid van Google</a>.'),
'de': ('Die App erfordert keine Registrierung oder Anmeldung, und wir betreiben keinen Server. Ihre Foto- und Videodateien werden nicht an uns gesendet.', 'Die App verwendet Firebase Analytics von Google LLC, um die Nutzung zu verstehen und die App zu verbessern. Automatisch erfasste Ereignisse wie App-Starts, Sitzungen und automatische Kaufereignisse, eine App-Instanzkennung, Geräte- und Betriebssystemdaten sowie eine aus der IP-Adresse abgeleitete ungefähre Region können an Google gesendet werden; wir können Analyseergebnisse einsehen. Foto- und Videodateien sind nicht Teil der Analyse. Die Analyseerfassung ist standardmäßig deaktiviert und wird abhängig vom regionalen Einwilligungsstatus eingeschränkt. Siehe die <a href="https://policies.google.com/privacy">Datenschutzerklärung von Google</a>.'),
'fr': ('L’application ne nécessite ni inscription ni connexion, et nous n’exploitons aucun serveur. Vos fichiers photo et vidéo ne nous sont pas envoyés.', 'L’application utilise Firebase Analytics de Google LLC pour comprendre son utilisation et l’améliorer. Des événements collectés automatiquement, comme l’ouverture de l’application, les sessions et les événements d’achat automatiques, un identifiant d’instance, des informations sur l’appareil et le système, ainsi qu’une région approximative déduite de l’adresse IP peuvent être envoyés à Google ; nous pouvons consulter les résultats d’analyse. Les fichiers photo et vidéo ne sont pas inclus dans l’analyse. La collecte analytique est désactivée par défaut et limitée selon le statut du consentement dans la région. Consultez les <a href="https://policies.google.com/privacy">règles de confidentialité de Google</a>.'),
'es': ('La aplicación no requiere registro ni inicio de sesión y no gestionamos ningún servidor. Tus archivos de fotos y vídeos no se nos envían.', 'La aplicación usa Firebase Analytics de Google LLC para entender su uso y mejorarla. Pueden enviarse a Google eventos recopilados automáticamente, como aperturas de la aplicación, sesiones y eventos de compra automáticos, un identificador de instancia, información del dispositivo y del sistema operativo y una región aproximada inferida de la dirección IP; podemos consultar los resultados del análisis. Los archivos de fotos y vídeos no se incluyen en el análisis. La recopilación de analíticas está desactivada por defecto y se limita según el estado del consentimiento en la región. Consulta la <a href="https://policies.google.com/privacy">política de privacidad de Google</a>.'),
'pt': ('O aplicativo não exige cadastro nem login e não mantemos servidor. Seus arquivos de fotos e vídeos não são enviados a nós.', 'O aplicativo usa o Firebase Analytics da Google LLC para entender o uso e melhorar o aplicativo. Eventos coletados automaticamente, como aberturas do aplicativo, sessões e eventos de compra automáticos, um identificador de instância, informações do dispositivo e do sistema operacional e uma região aproximada inferida do endereço IP podem ser enviados ao Google; podemos consultar os resultados da análise. Arquivos de fotos e vídeos não são incluídos na análise. A coleta de análises fica desativada por padrão e é limitada conforme o estado do consentimento na região. Consulte a <a href="https://policies.google.com/privacy">Política de Privacidade do Google</a>.'),
'it': ('L’app non richiede registrazione o accesso e non gestiamo alcun server. I tuoi file di foto e video non ci vengono inviati.', 'L’app usa Firebase Analytics di Google LLC per comprenderne l’utilizzo e migliorarla. Eventi raccolti automaticamente, come le aperture dell’app, le sessioni e gli eventi di acquisto automatici, un identificatore dell’istanza, informazioni sul dispositivo e sul sistema operativo e un’area approssimativa dedotta dall’indirizzo IP possono essere inviati a Google; possiamo consultare i risultati delle analisi. I file di foto e video non sono inclusi nelle analisi. La raccolta analitica è disattivata per impostazione predefinita e limitata in base allo stato del consenso nella regione. Consulta le <a href="https://policies.google.com/privacy">norme sulla privacy di Google</a>.'),
' tr': ('', ''),
'ru': ('В Приложении нет регистрации и входа, и мы не управляем собственным сервером. Файлы фотографий и видео нам не отправляются.', 'Приложение использует Firebase Analytics компании Google LLC для изучения использования и улучшения Приложения. В Google могут передаваться автоматически собираемые события, например открытия приложения, сеансы и автоматические события покупок, идентификатор экземпляра приложения, сведения об устройстве и операционной системе, а также приблизительный регион, определённый по IP-адресу; мы можем просматривать результаты аналитики. Файлы фотографий и видео в аналитику не включаются. Сбор аналитики по умолчанию отключён и ограничивается в зависимости от статуса согласия в регионе. См. <a href="https://policies.google.com/privacy">Политику конфиденциальности Google</a>.'),
'ar': ('لا يتطلب التطبيق إنشاء حساب أو تسجيل الدخول، ولا ندير خادمًا خاصًا بنا. لا تُرسل إلينا ملفات الصور والفيديو.', 'يستخدم التطبيق Firebase Analytics من Google LLC لفهم استخدام التطبيق وتحسينه. قد تُرسل إلى Google الأحداث التي تُجمع تلقائيًا، مثل فتح التطبيق والجلسات وأحداث الشراء التلقائية، ومعرّف نسخة التطبيق، ومعلومات الجهاز ونظام التشغيل، والمنطقة التقريبية المستنتجة من عنوان IP؛ ويمكننا الاطلاع على نتائج التحليل. لا تتضمن التحليلات ملفات الصور والفيديو. يكون جمع بيانات التحليل متوقفًا افتراضيًا ويُقيّد وفق حالة الموافقة في المنطقة. راجع <a href="https://policies.google.com/privacy">سياسة خصوصية Google</a>.'),
}
ANALYTICS['tr'] = ('Uygulamada kayıt veya oturum açma yoktur ve sunucu işletmeyiz. Fotoğraf ve video dosyalarınız bize gönderilmez.', 'Uygulama, kullanımı anlamak ve uygulamayı geliştirmek için Google LLC’nin Firebase Analytics hizmetini kullanır. Uygulamanın açılması gibi otomatik toplanan olaylar, uygulama örneği tanımlayıcısı, cihaz ve işletim sistemi bilgileri ve IP adresinden tahmin edilen yaklaşık bölge Google’a gönderilebilir; analiz sonuçlarını görebiliriz. Fotoğraf ve video dosyaları analize dahil edilmez. Analiz verilerinin toplanması varsayılan olarak kapalıdır ve bölgedeki onay durumuna göre kısıtlanır. <a href="https://policies.google.com/privacy">Google Gizlilik Politikası</a>na bakın.')
del ANALYTICS[' tr']

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
    p = dict(p)
    p['sections'] = [(heading, list(parts)) for heading, parts in p['sections']]
    p['sections'][0][1][0:1] = [f'<p>{text}</p>' for text in ANALYTICS[lang]]
    p['date'] = p['date'].replace('5', '7')
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
