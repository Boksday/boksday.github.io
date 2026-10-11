"""내곁의 노노그램 웹 페이지 문구(5개 언어)."""

E = '<a href="mailto:ekqlszzzz@naver.com">ekqlszzzz@naver.com</a>'

APP = {
    'ko': '내곁의 노노그램',
    'en': 'BySide Nonogram',
    'ja': 'BySide ノノグラム',
    'zh-hans': 'BySide 数织',
    'zh-hant': 'BySide 數織',
}

GITHUB_PRIVACY = 'https://docs.github.com/site-policy/privacy-policies/github-general-privacy-statement'


def g(lang):
    """Google 정책 링크(언어별)."""
    hl = {'ko': 'ko', 'en': 'en', 'ja': 'ja', 'zh-hans': 'zh-CN', 'zh-hant': 'zh-TW'}[lang]
    return (f'https://policies.google.com/technologies/partner-sites?hl={hl}',
            f'https://policies.google.com/privacy?hl={hl}')


INTRO = {
    'ko': {
        'title': '내곁의 노노그램 · 숫자를 따라 칠하면 그림이 피어나요',
        'desc': '숫자 단서를 따라 칸을 칠하면 숨은 픽셀 그림이 색으로 피어나는 그림 로직 퍼즐. 5×5 튜토리얼부터 30×30까지, 새 그림이 계속 더해져요.',
        'nav': ('화면', '기능', '고객 지원'),
        'h1': '숫자를 따라 칠하면<br><em>그림이 피어나요</em>',
        'lead': '줄마다 적힌 숫자를 단서로 칸을 칠해 보세요.<br>다 칠하면 숨은 그림이 색으로 나타나요.',
        'chips': ['5×5 ~ 30×30', '하트 3개 · 힌트 1번', '메달 모으기'],
        'store': ('App Store 출시 준비 중', 'Google Play 출시 준비 중'),
        'screens_h': '이렇게 생겼어요', 'screens_sub': '옆으로 넘겨 보세요.',
        'shots': [],
        'feat_h': '천천히, 한 칸씩', 'feat_sub': '처음이어도 튜토리얼부터 차근차근.',
        'features': [
            ('숨은 그림이 색으로 피어나요', '숫자는 이어서 칠할 칸의 길이예요. 모두 칠하면 픽셀 그림이 색을 입고 나타나요.'),
            ('5×5부터 30×30까지', '튜토리얼 5×5에서 시작해 10×10, 15×15, 20×20, 25×25, 마스터 30×30까지 판 크기별로 올라가요.'),
            ('누르거나 끌어서 칠하기', '칠하기와 X 표시를 오가며 풀어요. 손가락을 끌면 한 줄을 한 번에 칠할 수 있어요.'),
            ('하트 3개, 힌트 1번', '틀리면 하트가 줄어요. 막히면 지금 단서로 확실한 칸 하나를 힌트로 알려 줘요.'),
            ('메달 세 가지', '완성, 실수 없이, 힌트 없이. 그림마다 메달을 모아 보세요.'),
            ('큰 판도 편하게', '25×25·30×30은 두 손가락으로 확대해서 풀어요. 다크 모드, 5개 언어, 진동 켜고 끄기.'),
        ],
        'promise_h': '내 기록은 내 폰에만',
        'promise': ['회원가입이 없어요. 푼 그림과 설정은 폰에만 저장해요.',
                    '새 그림은 서버에서 계속 받아 와요.'],
        'note': '일부 그림은 Twemoji(© Twitter, Inc. 외, CC BY 4.0)를 바탕으로 만들었어요.',
        'footer': ('고객 지원', '개인정보처리방침', '문의'),
    },
    'en': {
        'title': 'BySide Nonogram · Fill by the numbers, watch a picture bloom',
        'desc': 'A picture logic puzzle: fill cells by the number clues and a hidden pixel picture blooms into color. From a 5×5 tutorial to 30×30, with new pictures added over time.',
        'nav': ('Screens', 'Features', 'Support'),
        'h1': 'Fill by the numbers,<br><em>watch it bloom</em>',
        'lead': 'Use the numbers on each line as clues to fill the cells.<br>Finish, and the hidden picture appears in color.',
        'chips': ['5×5 to 30×30', '3 hearts · 1 hint', 'Collect medals'],
        'store': ('Coming soon to the App Store', 'Coming soon to Google Play'),
        'screens_h': 'Take a look', 'screens_sub': 'Swipe to see more.',
        'shots': [],
        'feat_h': 'One cell at a time', 'feat_sub': 'New to nonograms? Start with the tutorial.',
        'features': [
            ('A picture blooms into color', 'Each number is a run of filled cells. Fill them all and a pixel picture appears in color.'),
            ('From 5×5 to 30×30', 'Start with the 5×5 tutorial and work up through 10×10, 15×15, 20×20, 25×25 and the 30×30 Master boards.'),
            ('Tap or drag to fill', 'Switch between Fill and Mark X. Drag your finger to fill a whole line at once.'),
            ('3 hearts, 1 hint', 'Each mistake costs a heart. Stuck? A hint shows one cell the current clues already settle.'),
            ('Three medals', 'Cleared, No mistakes and No hints. Collect them for every picture.'),
            ('Big boards made easy', 'Pinch to zoom on 25×25 and 30×30 boards. Dark mode, five languages and vibration on or off.'),
        ],
        'promise_h': 'Your progress stays on your phone',
        'promise': ['No account. Solved pictures and settings are saved only on your phone.',
                    'New pictures keep arriving from our server.'],
        'note': 'Some pictures are based on Twemoji (© Twitter, Inc. and other contributors, CC BY 4.0).',
        'footer': ('Support', 'Privacy Policy', 'Contact'),
    },
    'ja': {
        'title': 'BySide ノノグラム · 数字どおりに塗ると絵が咲く',
        'desc': '数字のヒントどおりにマスを塗ると、隠れたドット絵が色づいて現れるお絵かきロジックパズル。5×5のチュートリアルから30×30まで、新しい絵も追加されます。',
        'nav': ('画面', '機能', 'サポート'),
        'h1': '数字どおりに塗ると<br><em>絵が咲く</em>',
        'lead': '各列の数字を手がかりにマスを塗りましょう。<br>塗り終えると隠れた絵が色づいて現れます。',
        'chips': ['5×5〜30×30', 'ハート3つ・ヒント1回', 'メダル集め'],
        'store': ('App Store 近日公開', 'Google Play 近日公開'),
        'screens_h': 'アプリの画面', 'screens_sub': '横にスワイプしてご覧ください。',
        'shots': [],
        'feat_h': '1マスずつ、じっくり', 'feat_sub': '初めてでもチュートリアルから順番に。',
        'features': [
            ('隠れた絵が色づいて現れる', '数字は続けて塗るマスの長さ。全部塗るとドット絵が色をまとって現れます。'),
            ('5×5から30×30まで', 'チュートリアルの5×5から、10×10、15×15、20×20、25×25、マスターの30×30まで盤の大きさ別に進みます。'),
            ('タップやドラッグで塗る', '「塗る」と「×をつける」を切り替えて解きます。指をドラッグすれば1列をまとめて塗れます。'),
            ('ハート3つ、ヒント1回', 'ミスするとハートが減ります。行き詰まったら、今の手がかりで確定するマスを1つヒントで教えます。'),
            ('3種類のメダル', 'クリア、ノーミス、ヒントなし。絵ごとにメダルを集めましょう。'),
            ('大きな盤も快適に', '25×25・30×30は2本指で拡大して解けます。ダークモード、5か国語、振動のオン・オフ。'),
        ],
        'promise_h': '記録はあなたのスマホだけに',
        'promise': ['登録は不要。解いた絵や設定はスマホの中だけに保存します。',
                    '新しい絵はサーバーから順次届きます。'],
        'note': '一部の絵はTwemoji(© Twitter, Inc. ほか、CC BY 4.0)をもとに作りました。',
        'footer': ('サポート', 'プライバシーポリシー', 'お問い合わせ'),
    },
    'zh-hans': {
        'title': 'BySide 数织 · 照着数字涂色，让图画绽放',
        'desc': '照着数字线索涂格子，隐藏的像素画就会绽放出色彩的图画逻辑谜题。从 5×5 新手教程到 30×30，还会不断加入新图画。',
        'nav': ('界面', '功能', '客户支持'),
        'h1': '照着数字涂色，<br><em>让图画绽放</em>',
        'lead': '以每行每列的数字为线索涂格子。<br>涂完后，隐藏的图画就会带着色彩出现。',
        'chips': ['5×5 ~ 30×30', '3 颗心 · 1 次提示', '收集奖牌'],
        'store': ('即将登陆 App Store', '即将登陆 Google Play'),
        'screens_h': '界面一览', 'screens_sub': '左右滑动查看更多。',
        'shots': [],
        'feat_h': '一格一格，慢慢来', 'feat_sub': '新手也能从教程一步步开始。',
        'features': [
            ('隐藏的图画绽放色彩', '数字表示连续涂色的格数。全部涂完，像素画就会带着色彩出现。'),
            ('从 5×5 到 30×30', '从 5×5 新手教程开始，按棋盘大小一路挑战 10×10、15×15、20×20、25×25 和大师级 30×30。'),
            ('点按或拖动涂色', '在“涂色”和“标记 X”之间切换。手指拖动可以一次涂满一整行。'),
            ('3 颗心，1 次提示', '出错会失去一颗心。卡住时，提示会告诉你一个根据当前线索已经能确定的格子。'),
            ('三种奖牌', '完成、零失误、不用提示。每幅图都来收集奖牌吧。'),
            ('大棋盘也轻松', '25×25 和 30×30 可以用双指放大来解。深色模式、5 种语言、振动开关。'),
        ],
        'promise_h': '记录只留在你的手机里',
        'promise': ['无需注册。解开的图画和设置只保存在手机里。',
                    '新图画会陆续从服务器送达。'],
        'note': '部分图画以 Twemoji（© Twitter, Inc. 及其他贡献者，CC BY 4.0）为基础制作。',
        'footer': ('客户支持', '隐私政策', '联系我们'),
    },
    'zh-hant': {
        'title': 'BySide 數織 · 照著數字塗色，讓圖畫綻放',
        'desc': '照著數字線索塗格子，隱藏的像素畫就會綻放出色彩的圖畫邏輯謎題。從 5×5 新手教學到 30×30，還會不斷加入新圖畫。',
        'nav': ('畫面', '功能', '客戶支援'),
        'h1': '照著數字塗色，<br><em>讓圖畫綻放</em>',
        'lead': '以每行每列的數字為線索塗格子。<br>塗完後，隱藏的圖畫就會帶著色彩出現。',
        'chips': ['5×5 ~ 30×30', '3 顆心・1 次提示', '收集獎牌'],
        'store': ('即將登陸 App Store', '即將登陸 Google Play'),
        'screens_h': '畫面一覽', 'screens_sub': '左右滑動查看更多。',
        'shots': [],
        'feat_h': '一格一格，慢慢來', 'feat_sub': '新手也能從教學一步步開始。',
        'features': [
            ('隱藏的圖畫綻放色彩', '數字表示連續塗色的格數。全部塗完，像素畫就會帶著色彩出現。'),
            ('從 5×5 到 30×30', '從 5×5 新手教學開始，依棋盤大小一路挑戰 10×10、15×15、20×20、25×25 和大師級 30×30。'),
            ('點一下或拖曳塗色', '在「塗色」和「標記 X」之間切換。手指拖曳可以一次塗滿一整行。'),
            ('3 顆心，1 次提示', '出錯會失去一顆心。卡住時，提示會告訴你一個依目前線索已經能確定的格子。'),
            ('三種獎牌', '完成、零失誤、不用提示。每幅圖都來收集獎牌吧。'),
            ('大棋盤也輕鬆', '25×25 和 30×30 可以用雙指放大來解。深色模式、5 種語言、震動開關。'),
        ],
        'promise_h': '紀錄只留在你的手機裡',
        'promise': ['免註冊。解開的圖畫和設定只儲存在手機裡。',
                    '新圖畫會陸續從伺服器送達。'],
        'note': '部分圖畫以 Twemoji（© Twitter, Inc. 及其他貢獻者，CC BY 4.0）為基礎製作。',
        'footer': ('客戶支援', '隱私權政策', '聯絡我們'),
    },
}


def privacy(lang):
    partner, gpriv = g(lang)
    gh = GITHUB_PRIVACY
    T = {
        'ko': ('내곁의 노노그램 개인정보처리방침', '시행일: 2026년 10월 11일',
               "'내곁의 노노그램'(이하 \"앱\", iOS·Android)은 이용자의 개인정보를 소중히 다루며, 「개인정보 보호법」 등 관련 법령을 지킵니다. 이 방침은 앱이 어떤 정보를 어떻게 다루는지 설명합니다.",
               [
                   ('1. 앱이 직접 수집하는 정보', [
                       '<p>앱은 회원가입이나 로그인이 없으며, 운영자가 운영하는 서버나 데이터베이스로 이용자의 정보를 보내지 않습니다. 운영자는 앱에서 어떤 정보도 받지 않습니다.</p>',
                       '<p>푼 그림과 하던 게임, 메달, 화면·언어·진동 설정은 <strong>이용자의 기기 안에만 저장</strong>됩니다. 운영자는 이 내용을 볼 수 없으며, 백업이나 다른 기기와의 동기화는 하지 않습니다.</p>',
                   ]),
                   ('2. 퍼즐 내려받기 (GitHub Pages)', [
                       f'<p>앱은 퍼즐 목록과 퍼즐 파일을 GitHub, Inc.가 운영하는 GitHub Pages(boksday.github.io)에서 내려받습니다. 여느 웹 요청과 마찬가지로 GitHub는 요청을 처리하면서 IP 주소와 요청 시각 등 기본 요청 정보를 받습니다. 이 정보는 GitHub가 <a href="{gh}">GitHub 개인정보 처리방침</a>에 따라 처리하며, 운영자는 받지 않습니다.</p>',
                   ]),
                   ('3. 광고를 위해 제3자가 수집하는 정보', [
                       '<p>앱은 무료로 제공되며, Google LLC의 <strong>Google AdMob</strong> 광고를 보여 줍니다. 모든 화면 아래에 배너 광고가 있고, 하트를 다 썼을 때 이용자가 고르면 하트 1개를 주는 보상형 광고를 보여 줍니다. AdMob은 광고 제공과 측정, 부정 사용 방지를 위해 다음 정보를 수집·처리할 수 있습니다.</p>',
                       '<table><tr><th>수집 주체</th><th>항목</th><th>목적</th></tr><tr><td>Google LLC (AdMob)</td><td>광고 ID(Android 광고 ID, iOS 광고 식별자 IDFA — iOS는 이용자가 추적을 허용한 경우에만), IP 주소, 기기·운영체제·앱 정보, 광고 노출·클릭 등 광고 상호작용 정보</td><td>광고 표시·맞춤형 광고, 광고 성과 측정, 부정 클릭 방지</td></tr></table>',
                       f'<p>Google의 정보 처리 방식은 <a href="{partner}">Google 파트너 사이트·앱의 데이터 사용 방식</a>과 <a href="{gpriv}">Google 개인정보처리방침</a>에서 확인할 수 있습니다.</p>',
                   ]),
                   ('4. 광고 동의와 맞춤형 광고 거부 방법', [
                       '<ul><li>유럽경제지역(EEA)·영국 등 동의가 필요한 지역에서는 Google의 동의 도구(UMP)로 광고 개인정보 동의를 묻고, 앱의 <strong>설정 → 광고 개인정보 설정</strong>에서 언제든 바꿀 수 있습니다(동의가 필요한 지역에서만 보입니다).</li><li>iOS: 앱 추적 투명성(ATT) 창에서 추적 허용 여부를 고를 수 있으며, <strong>설정 → 개인정보 보호 및 보안 → 추적</strong>에서 언제든 바꿀 수 있습니다. 허용하지 않으면 맞춤형이 아닌 광고만 보여 줍니다.</li><li>Android: 휴대폰 <strong>설정 → Google → 광고</strong>에서 광고 ID를 삭제하거나 재설정할 수 있습니다.</li></ul>',
                   ]),
                   ('5. 보관 및 파기', [
                       '<p>기기에 저장된 기록과 설정은 앱을 삭제하면 함께 지워집니다. 운영자가 따로 보관하는 정보는 없습니다. 제3자(Google, GitHub)가 수집한 정보의 보관 기간은 해당 회사의 방침을 따릅니다.</p>',
                   ]),
                   ('6. 아동의 개인정보', [
                       '<p>앱은 만 14세 미만 아동(해외는 만 13세 미만)을 주 대상으로 하지 않으며, 아동의 개인정보를 의도적으로 수집하지 않습니다.</p>',
                   ]),
                   ('7. 개인정보 보호책임자·문의', [
                       f'<p>개인정보 보호책임자: 내곁의 운영자<br>연락처: {E}</p>',
                   ]),
                   ('8. 방침의 변경', [
                       '<p>이 방침이 바뀌면 이 페이지에 시행일과 함께 알립니다. 이 방침은 한국어 원문을 기준으로 하며, 다른 언어판과 뜻이 다르면 한국어판을 따릅니다.</p>',
                   ]),
               ]),
        'en': ('BySide Nonogram Privacy Policy', 'Effective: October 11, 2026',
               'BySide Nonogram (the "app", iOS and Android) respects your privacy. This policy explains what information the app handles and how.',
               [
                   ('1. Information the app collects', [
                       '<p>The app has no account or sign-in, and it never sends your information to a server or database run by us. We receive no information from the app.</p>',
                       '<p>Your solved pictures, current game, medals and display, language and vibration settings are <strong>stored only on your device</strong>. We cannot see them, and they are not backed up or synced to other devices.</p>',
                   ]),
                   ('2. Downloading puzzles (GitHub Pages)', [
                       f'<p>The app downloads the puzzle list and puzzle files from GitHub Pages (boksday.github.io), run by GitHub, Inc. As with any web request, GitHub receives your IP address and basic request information such as the time of the request. GitHub processes it under the <a href="{gh}">GitHub General Privacy Statement</a>; we do not receive it.</p>',
                   ]),
                   ('3. Information collected by third parties for ads', [
                       '<p>The app is free and shows ads from <strong>Google AdMob</strong> (Google LLC): a banner at the bottom of every screen, and, if you choose it when you run out of hearts, a rewarded ad that gives you one heart. AdMob may collect and process the following to serve and measure ads and prevent fraud.</p>',
                       '<table><tr><th>Collected by</th><th>Data</th><th>Purpose</th></tr><tr><td>Google LLC (AdMob)</td><td>Advertising ID (Android advertising ID; on iOS, the IDFA only if you allow tracking), IP address, device, OS and app information, ad interactions such as views and clicks</td><td>Showing and personalizing ads, measuring ad performance, preventing invalid clicks</td></tr></table>',
                       f'<p>See <a href="{partner}">How Google uses information from sites or apps that use its services</a> and the <a href="{gpriv}">Google Privacy Policy</a>.</p>',
                   ]),
                   ('4. Ad consent and opting out of personalized ads', [
                       '<ul><li>Where consent is required (such as the EEA and the UK), the app asks for your ad privacy consent with Google\'s consent tool (UMP), and you can change it any time in the app under <strong>Settings → Ad privacy options</strong> (shown only where consent is required).</li><li>iOS: choose whether to allow tracking in the App Tracking Transparency prompt, and change it any time in <strong>Settings → Privacy &amp; Security → Tracking</strong>. If you do not allow it, only non-personalized ads are shown.</li><li>Android: delete or reset your advertising ID in <strong>Settings → Google → Ads</strong>.</li></ul>',
                   ]),
                   ('5. Retention and deletion', [
                       '<p>Records and settings stored on your device are deleted when you delete the app. We keep no information of our own. Information collected by third parties (Google, GitHub) is kept under their policies.</p>',
                   ]),
                   ("6. Children's privacy", [
                       '<p>The app is not directed primarily at children under 13 (under 14 in Korea) and does not knowingly collect their personal information.</p>',
                   ]),
                   ('7. Contact', [
                       f'<p>Privacy officer: BySide operator<br>Contact: {E}</p>',
                   ]),
                   ('8. Changes', [
                       '<p>If this policy changes, we will post the update on this page with a new effective date. The Korean version is the original; if versions differ, the Korean version prevails.</p>',
                   ]),
               ]),
        'ja': ('BySide ノノグラム プライバシーポリシー', '施行日：2026年10月11日',
               'BySide ノノグラム(以下「本アプリ」、iOS・Android)は、利用者のプライバシーを大切にします。本ポリシーでは、本アプリがどのような情報をどのように扱うかを説明します。',
               [
                   ('1. 本アプリが収集する情報', [
                       '<p>本アプリには会員登録やログインがなく、運営者のサーバーやデータベースに利用者の情報を送信しません。運営者は本アプリから何の情報も受け取りません。</p>',
                       '<p>解いた絵、途中のゲーム、メダル、表示・言語・振動の設定は<strong>利用者の端末内だけに保存</strong>されます。運営者はこれらを見ることができず、バックアップや他の端末との同期も行いません。</p>',
                   ]),
                   ('2. パズルのダウンロード(GitHub Pages)', [
                       f'<p>本アプリは、GitHub, Inc.が運営するGitHub Pages(boksday.github.io)からパズルの一覧とパズルファイルをダウンロードします。一般的なウェブのリクエストと同じく、GitHubはIPアドレスやリクエスト日時などの基本的なリクエスト情報を受け取ります。これらは<a href="{gh}">GitHubのプライバシーステートメント</a>に従ってGitHubが処理し、運営者は受け取りません。</p>',
                   ]),
                   ('3. 広告のために第三者が収集する情報', [
                       '<p>本アプリは無料で、Google LLCの<strong>Google AdMob</strong>による広告を表示します。すべての画面の下にバナー広告があり、ハートがなくなったときに利用者が選ぶと、ハートを1つもらえるリワード広告を表示します。AdMobは広告の配信・測定、不正防止のため、次の情報を収集・処理することがあります。</p>',
                       '<table><tr><th>収集者</th><th>項目</th><th>目的</th></tr><tr><td>Google LLC (AdMob)</td><td>広告ID(Androidの広告ID、iOSのIDFA — iOSはトラッキングを許可した場合のみ)、IPアドレス、端末・OS・アプリの情報、広告の表示・クリックなどのやり取りの情報</td><td>広告の表示・パーソナライズ、広告効果の測定、不正クリックの防止</td></tr></table>',
                       f'<p>詳しくは<a href="{partner}">Googleのサービスを使用するサイトやアプリから収集した情報のGoogleによる使用</a>と<a href="{gpriv}">Googleプライバシーポリシー</a>をご覧ください。</p>',
                   ]),
                   ('4. 広告の同意とパーソナライズ広告の停止', [
                       '<ul><li>EEA・英国など同意が必要な地域では、Googleの同意ツール(UMP)で広告のプライバシー同意をお聞きし、アプリの<strong>設定 → 広告のプライバシー設定</strong>でいつでも変更できます(同意が必要な地域でのみ表示されます)。</li><li>iOS:App Tracking Transparencyの画面でトラッキングを許可するか選べます。<strong>設定 → プライバシーとセキュリティ → トラッキング</strong>でいつでも変更できます。許可しない場合は、パーソナライズされていない広告のみを表示します。</li><li>Android:<strong>設定 → Google → 広告</strong>で広告IDを削除またはリセットできます。</li></ul>',
                   ]),
                   ('5. 保存期間と削除', [
                       '<p>端末に保存された記録と設定は、アプリを削除すると一緒に消えます。運営者が別に保管する情報はありません。第三者(Google、GitHub)が収集した情報の保存期間は各社のポリシーに従います。</p>',
                   ]),
                   ('6. 子どもの個人情報', [
                       '<p>本アプリは13歳未満(韓国は14歳未満)の子どもを主な対象としておらず、子どもの個人情報を意図的に収集しません。</p>',
                   ]),
                   ('7. お問い合わせ', [
                       f'<p>個人情報保護責任者:BySide 運営者<br>連絡先:{E}</p>',
                   ]),
                   ('8. ポリシーの変更', [
                       '<p>本ポリシーを変更する場合は、施行日とともに本ページでお知らせします。韓国語版を原文とし、各言語版と内容が異なる場合は韓国語版が優先されます。</p>',
                   ]),
               ]),
        'zh-hans': ('BySide 数织 隐私政策', '生效日期：2026年10月11日',
                    'BySide 数织（以下简称“本应用”，iOS 和 Android）重视你的隐私。本政策说明本应用处理哪些信息以及如何处理。',
                    [
                        ('1. 本应用收集的信息', [
                            '<p>本应用没有注册或登录，也不会把你的信息发送到运营者的服务器或数据库。运营者不会从本应用收到任何信息。</p>',
                            '<p>解开的图画、进行中的游戏、奖牌以及显示、语言和振动设置<strong>只保存在你的设备上</strong>。运营者无法查看，也不会备份或同步到其他设备。</p>',
                        ]),
                        ('2. 下载谜题（GitHub Pages）', [
                            f'<p>本应用从 GitHub, Inc. 运营的 GitHub Pages（boksday.github.io）下载谜题列表和谜题文件。与任何网页请求一样，GitHub 会收到你的 IP 地址和请求时间等基本请求信息。这些信息由 GitHub 按照 <a href="{gh}">GitHub 隐私声明</a>处理，运营者不会收到。</p>',
                        ]),
                        ('3. 第三方为广告收集的信息', [
                            '<p>本应用免费提供，并显示 Google LLC 的 <strong>Google AdMob</strong> 广告：每个界面底部都有横幅广告；心用完时，如果你选择观看，会显示奖励一颗心的激励广告。AdMob 可能为投放和衡量广告、防止作弊而收集和处理以下信息。</p>',
                            '<table><tr><th>收集方</th><th>项目</th><th>目的</th></tr><tr><td>Google LLC (AdMob)</td><td>广告标识符（Android 广告 ID；iOS 的 IDFA 仅在你允许跟踪时）、IP 地址、设备、系统和应用信息、广告展示和点击等互动信息</td><td>展示广告和个性化广告、衡量广告效果、防止无效点击</td></tr></table>',
                            f'<p>详见<a href="{partner}">Google 如何使用来自使用其服务的网站或应用的信息</a>和 <a href="{gpriv}">Google 隐私权政策</a>。</p>',
                        ]),
                        ('4. 广告同意与关闭个性化广告', [
                            '<ul><li>在欧洲经济区、英国等需要同意的地区，本应用会通过 Google 的同意工具（UMP）征求你的广告隐私同意，你可以随时在应用的<strong>设置 → 广告隐私设置</strong>中更改（仅在需要同意的地区显示）。</li><li>iOS：可在“App 跟踪透明度”弹窗中选择是否允许跟踪，之后可随时在<strong>设置 → 隐私与安全性 → 跟踪</strong>中更改。如不允许，只会显示非个性化广告。</li><li>Android：在<strong>设置 → Google → 广告</strong>中删除或重置广告 ID。</li></ul>',
                        ]),
                        ('5. 保存与删除', [
                            '<p>设备上的记录和设置会在删除应用时一并删除。运营者不另外保存任何信息。第三方（Google、GitHub）收集的信息按其各自的政策保存。</p>',
                        ]),
                        ('6. 儿童隐私', [
                            '<p>本应用并非主要面向 13 岁以下（韩国为 14 岁以下）的儿童，也不会有意收集儿童的个人信息。</p>',
                        ]),
                        ('7. 联系方式', [
                            f'<p>个人信息保护负责人：BySide 运营者<br>联系邮箱：{E}</p>',
                        ]),
                        ('8. 政策变更', [
                            '<p>本政策如有变更，将在本页面公布并注明生效日期。本政策以韩文版为准，其他语言版本与韩文版不一致时，以韩文版为准。</p>',
                        ]),
                    ]),
        'zh-hant': ('BySide 數織 隱私權政策', '生效日期：2026年10月11日',
                    'BySide 數織（以下簡稱「本應用程式」，iOS 和 Android）重視你的隱私。本政策說明本應用程式處理哪些資訊以及如何處理。',
                    [
                        ('1. 本應用程式蒐集的資訊', [
                            '<p>本應用程式沒有註冊或登入，也不會把你的資訊傳送到營運者的伺服器或資料庫。營運者不會從本應用程式收到任何資訊。</p>',
                            '<p>解開的圖畫、進行中的遊戲、獎牌以及顯示、語言和震動設定<strong>只儲存在你的裝置上</strong>。營運者無法查看，也不會備份或同步到其他裝置。</p>',
                        ]),
                        ('2. 下載謎題（GitHub Pages）', [
                            f'<p>本應用程式從 GitHub, Inc. 營運的 GitHub Pages（boksday.github.io）下載謎題列表和謎題檔案。與任何網頁請求一樣，GitHub 會收到你的 IP 位址和請求時間等基本請求資訊。這些資訊由 GitHub 依照 <a href="{gh}">GitHub 隱私權聲明</a>處理，營運者不會收到。</p>',
                        ]),
                        ('3. 第三方為廣告蒐集的資訊', [
                            '<p>本應用程式免費提供，並顯示 Google LLC 的 <strong>Google AdMob</strong> 廣告：每個畫面底部都有橫幅廣告；心用完時，如果你選擇觀看，會顯示獎勵一顆心的獎勵廣告。AdMob 可能為投放和衡量廣告、防止作弊而蒐集和處理以下資訊。</p>',
                            '<table><tr><th>蒐集方</th><th>項目</th><th>目的</th></tr><tr><td>Google LLC (AdMob)</td><td>廣告識別碼（Android 廣告 ID；iOS 的 IDFA 僅在你允許追蹤時）、IP 位址、裝置、系統和應用程式資訊、廣告曝光和點擊等互動資訊</td><td>顯示廣告和個人化廣告、衡量廣告成效、防止無效點擊</td></tr></table>',
                            f'<p>詳見<a href="{partner}">Google 如何使用採用其服務的網站或應用程式所提供的資訊</a>和 <a href="{gpriv}">Google 隱私權政策</a>。</p>',
                        ]),
                        ('4. 廣告同意與關閉個人化廣告', [
                            '<ul><li>在歐洲經濟區、英國等需要同意的地區，本應用程式會透過 Google 的同意工具（UMP）徵求你的廣告隱私權同意，你可以隨時在應用程式的<strong>設定 → 廣告隱私設定</strong>中更改（僅在需要同意的地區顯示）。</li><li>iOS：可在「App 追蹤透明度」視窗中選擇是否允許追蹤，之後可隨時在<strong>設定 → 隱私權與安全性 → 追蹤</strong>中更改。如不允許，只會顯示非個人化廣告。</li><li>Android：在<strong>設定 → Google → 廣告</strong>中刪除或重設廣告 ID。</li></ul>',
                        ]),
                        ('5. 保存與刪除', [
                            '<p>裝置上的紀錄和設定會在刪除應用程式時一併刪除。營運者不另外保存任何資訊。第三方（Google、GitHub）蒐集的資訊依其各自的政策保存。</p>',
                        ]),
                        ('6. 兒童隱私', [
                            '<p>本應用程式並非主要以 13 歲以下（韓國為 14 歲以下）的兒童為對象，也不會刻意蒐集兒童的個人資訊。</p>',
                        ]),
                        ('7. 聯絡方式', [
                            f'<p>個人資料保護負責人：BySide 營運者<br>聯絡信箱：{E}</p>',
                        ]),
                        ('8. 政策變更', [
                            '<p>本政策如有變更，將在本頁面公告並註明生效日期。本政策以韓文版為準，其他語言版本與韓文版不一致時，以韓文版為準。</p>',
                        ]),
                    ]),
    }
    title, date, intro, sections = T[lang]
    return {'title': title, 'date': date, 'intro': intro, 'sections': sections}


SUPPORT = {
    'ko': {
        'title': '내곁의 노노그램 고객 지원',
        'intro': '사용하다 궁금한 점이나 불편한 점이 있으면 메일로 알려 주세요. 보통 2~3일 안에 답장드려요.',
        'contact': '문의',
        'hint': '앱 버전, 기기 종류, 어떤 화면에서 무엇을 했는지 적어 주시면 더 빨리 도와드릴 수 있어요.',
        'faq_h': '자주 묻는 질문',
        'faq': [
            ('어떻게 푸나요?', '줄 옆의 숫자는 그 줄에서 <strong>이어서 칠할 칸의 길이</strong>예요. "3 1"이면 3칸을 이어 칠하고, 한 칸 이상 띄운 뒤 1칸을 칠해요. 비어 있는 게 확실한 칸에는 <strong>X 표시</strong>를 하고, 손가락을 끌면 한 줄을 한 번에 칠할 수 있어요.'),
            ('하트를 다 쓰면 어떻게 되나요?', '틀릴 때마다 하트가 하나 줄고, 3개를 다 쓰면 멈춰요. <strong>광고 보고 하트 1개 받기</strong>로 이어서 풀거나, <strong>처음부터</strong> 다시 풀 수 있어요.'),
            ('힌트는 어떻게 쓰나요?', '한 그림에 <strong>1번</strong>은 무료이고, 그 뒤로는 광고를 보면 하나씩 더 받을 수 있어요. 지금 단서로 확실히 알 수 있는 칸 하나를 알려 줘요. 힌트 없이 풀면 \'힌트 없이\' 메달을 받아요.'),
            ('25×25·30×30 판이 너무 작아요.', '두 손가락을 벌려 <strong>확대</strong>하고, 두 손가락으로 끌어 보고 싶은 곳으로 옮겨요. 오므리면 다시 작아져요.'),
            ('앱을 지웠더니 기록이 사라졌어요.', '기록은 폰 안에만 저장돼요. 앱을 삭제하면 기록도 함께 지워지고, 백업이나 다른 폰으로 옮기기는 지원하지 않아요.'),
            ('진동을 끄고 싶어요.', '앱의 <strong>설정 → 진동</strong>에서 끌 수 있어요.'),
            ('언어나 화면(밝게·어둡게)을 바꾸고 싶어요.', '앱의 <strong>설정</strong>에서 <strong>언어</strong>와 <strong>화면</strong>을 고를 수 있어요. 기기 설정을 따르게 둘 수도 있어요.'),
            ('광고 개인정보 설정은 어디서 바꾸나요?', '동의가 필요한 지역(유럽경제지역·영국 등)에서는 앱의 <strong>설정 → 광고 개인정보 설정</strong>에서 바꿀 수 있어요. 아이폰은 <strong>설정 → 개인정보 보호 및 보안 → 추적</strong>, 안드로이드는 <strong>설정 → Google → 광고</strong>에서도 바꿀 수 있어요.'),
            ('퍼즐이 이상해요(답이 여러 개이거나 그림이 틀려요).', f'판 크기와 화면 캡처를 {E}로 보내 주세요. 확인해서 고칠게요.'),
        ],
    },
    'en': {
        'title': 'BySide Nonogram Support',
        'intro': 'If you have a question or run into a problem, please email us. We usually reply within two or three days.',
        'contact': 'Contact',
        'hint': 'Including the app version, your device and what you were doing helps us help you faster.',
        'faq_h': 'FAQ',
        'faq': [
            ('How do I play?', 'The numbers beside each line are the <strong>lengths of runs of filled cells</strong> in that line. "3 1" means three filled cells in a row, at least one gap, then one more. Use <strong>Mark X</strong> on cells you know are empty, and drag your finger to fill a whole line at once.'),
            ('What happens when I run out of hearts?', 'Each mistake costs a heart, and the game stops after three. Choose <strong>Watch an ad for 1 heart</strong> to keep going, or <strong>Start over</strong>.'),
            ('How do hints work?', 'You get <strong>1 free hint</strong> per picture, and can watch an ad for more. A hint shows one cell the current clues already settle. Solve without hints to earn the No hints medal.'),
            ('The 25×25 and 30×30 boards are too small.', 'Spread two fingers to <strong>zoom in</strong> and drag with two fingers to move around. Pinch to zoom back out.'),
            ('My progress is gone after deleting the app.', 'Progress is stored only on your phone. Deleting the app deletes it too, and backup or moving it to another phone is not supported.'),
            ('How do I turn off vibration?', 'Go to <strong>Settings → Vibration</strong> in the app.'),
            ('How do I change the language or appearance (light/dark)?', 'Choose <strong>Language</strong> and <strong>Appearance</strong> in the app\'s <strong>Settings</strong>. You can also leave them to follow your device.'),
            ('Where are the ad privacy options?', 'Where consent is required (such as the EEA and the UK), use <strong>Settings → Ad privacy options</strong> in the app. On iPhone you can also use <strong>Settings → Privacy &amp; Security → Tracking</strong>; on Android, <strong>Settings → Google → Ads</strong>.'),
            ('A puzzle looks wrong (more than one answer, or a broken picture).', f'Email {E} with the board size and a screenshot. We will check and fix it.'),
        ],
    },
    'ja': {
        'title': 'BySide ノノグラム サポート',
        'intro': 'ご質問や不具合があればメールでお知らせください。通常2〜3日以内にお返事します。',
        'contact': 'お問い合わせ',
        'hint': 'アプリのバージョン、端末の種類、どの画面で何をしたかを書いていただくと、より早く対応できます。',
        'faq_h': 'よくある質問',
        'faq': [
            ('遊び方は?', '列の横の数字は、その列で<strong>続けて塗るマスの長さ</strong>です。「3 1」なら3マス続けて塗り、1マス以上空けて1マス塗ります。空白だと確実なマスには<strong>×をつけ</strong>、指をドラッグすれば1列をまとめて塗れます。'),
            ('ハートがなくなるとどうなりますか?', 'ミスするたびにハートが1つ減り、3つなくなると止まります。<strong>広告を見てハートを1つもらう</strong>で続けるか、<strong>最初から</strong>やり直せます。'),
            ('ヒントの使い方は?', '1枚の絵につき<strong>1回</strong>は無料で、そのあとは広告を見るともう1回ずつもらえます。今の手がかりで確定するマスを1つ教えます。ヒントを使わずに解くと「ヒントなし」メダルがもらえます。'),
            ('25×25・30×30の盤が小さすぎます。', '2本指で広げて<strong>拡大</strong>し、2本指でドラッグして見たい所へ動かせます。つまむと元に戻ります。'),
            ('アプリを削除したら記録が消えました。', '記録はスマホの中だけに保存されます。アプリを削除すると記録も消え、バックアップや別のスマホへの移行には対応していません。'),
            ('振動をオフにしたいです。', 'アプリの<strong>設定 → 振動</strong>でオフにできます。'),
            ('言語や表示(ライト・ダーク)を変えたいです。', 'アプリの<strong>設定</strong>で<strong>言語</strong>と<strong>表示</strong>を選べます。端末の設定に合わせることもできます。'),
            ('広告のプライバシー設定はどこで変えますか?', '同意が必要な地域(EEA・英国など)では、アプリの<strong>設定 → 広告のプライバシー設定</strong>で変更できます。iPhoneは<strong>設定 → プライバシーとセキュリティ → トラッキング</strong>、Androidは<strong>設定 → Google → 広告</strong>でも変更できます。'),
            ('パズルがおかしいです(答えが複数ある、絵が崩れている)。', f'盤の大きさと画面のスクリーンショットを{E}までお送りください。確認して直します。'),
        ],
    },
    'zh-hans': {
        'title': 'BySide 数织 客户支持',
        'intro': '如有疑问或遇到问题，请发邮件告诉我们。我们通常会在两三天内回复。',
        'contact': '联系我们',
        'hint': '写明应用版本、设备型号以及在哪个界面做了什么，我们能更快帮你解决。',
        'faq_h': '常见问题',
        'faq': [
            ('怎么玩？', '每行每列旁的数字表示这一行<strong>连续涂色的格数</strong>。“3 1”表示先连续涂 3 格，至少空一格后再涂 1 格。确定是空白的格子可以<strong>标记 X</strong>，手指拖动可以一次涂满一整行。'),
            ('心用完了会怎样？', '每出错一次失去一颗心，3 颗都用完后本局会暂停。可以选择<strong>看广告获得1颗心</strong>继续，也可以<strong>从头开始</strong>。'),
            ('提示怎么用？', '每幅图可免费使用 <strong>1 次</strong>，之后看广告可再获得。提示会告诉你一个根据当前线索已经能确定的格子。不用提示解开可获得“不用提示”奖牌。'),
            ('25×25 和 30×30 的棋盘太小了。', '双指张开即可<strong>放大</strong>，双指拖动可以移动到想看的位置。双指捏合即可缩小。'),
            ('删除应用后记录不见了。', '记录只保存在手机里。删除应用后记录也会一并删除，不支持备份或转移到其他手机。'),
            ('想关闭振动。', '在应用的<strong>设置 → 振动</strong>中关闭。'),
            ('想更改语言或外观（浅色/深色）。', '在应用的<strong>设置</strong>中选择<strong>语言</strong>和<strong>外观</strong>，也可以跟随设备设置。'),
            ('在哪里更改广告隐私设置？', '在需要同意的地区（欧洲经济区、英国等），可在应用的<strong>设置 → 广告隐私设置</strong>中更改。iPhone 也可以在<strong>设置 → 隐私与安全性 → 跟踪</strong>中更改，Android 可以在<strong>设置 → Google → 广告</strong>中更改。'),
            ('谜题有问题（答案不止一个，或图画不对）。', f'请把棋盘大小和截图发送到 {E}。我们会确认并修正。'),
        ],
    },
    'zh-hant': {
        'title': 'BySide 數織 客戶支援',
        'intro': '如有疑問或遇到問題，請寄信告訴我們。我們通常會在兩三天內回覆。',
        'contact': '聯絡我們',
        'hint': '寫明 App 版本、裝置型號以及在哪個畫面做了什麼，我們能更快幫你解決。',
        'faq_h': '常見問題',
        'faq': [
            ('怎麼玩？', '每行每列旁的數字表示這一行<strong>連續塗色的格數</strong>。「3 1」表示先連續塗 3 格，至少空一格後再塗 1 格。確定是空白的格子可以<strong>標記 X</strong>，手指拖曳可以一次塗滿一整行。'),
            ('心用完了會怎樣？', '每出錯一次失去一顆心，3 顆都用完後本局會暫停。可以選擇<strong>看廣告獲得1顆心</strong>繼續，也可以<strong>從頭開始</strong>。'),
            ('提示怎麼用？', '每幅圖可免費使用 <strong>1 次</strong>，之後看廣告可再獲得。提示會告訴你一個依目前線索已經能確定的格子。不用提示解開可獲得「不用提示」獎牌。'),
            ('25×25 和 30×30 的棋盤太小了。', '雙指張開即可<strong>放大</strong>，雙指拖曳可以移動到想看的位置。雙指捏合即可縮小。'),
            ('刪除 App 後紀錄不見了。', '紀錄只儲存在手機裡。刪除 App 後紀錄也會一併刪除，不支援備份或轉移到其他手機。'),
            ('想關閉震動。', '在 App 的<strong>設定 → 震動</strong>中關閉。'),
            ('想更改語言或外觀（淺色／深色）。', '在 App 的<strong>設定</strong>中選擇<strong>語言</strong>和<strong>外觀</strong>，也可以跟隨裝置設定。'),
            ('在哪裡更改廣告隱私設定？', '在需要同意的地區（歐洲經濟區、英國等），可在 App 的<strong>設定 → 廣告隱私設定</strong>中更改。iPhone 也可以在<strong>設定 → 隱私權與安全性 → 追蹤</strong>中更改，Android 可以在<strong>設定 → Google → 廣告</strong>中更改。'),
            ('謎題有問題（答案不只一個，或圖畫不對）。', f'請把棋盤大小和截圖寄到 {E}。我們會確認並修正。'),
        ],
    },
}
