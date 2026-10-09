"""내곁의 스도쿠 웹 페이지 문구(5개 언어)."""

E = '<a href="mailto:ekqlszzzz@naver.com">ekqlszzzz@naver.com</a>'

APP = {
    'ko': '내곁의 스도쿠',
    'en': 'BySide:Sudoku',
    'ja': 'BySide:Sudoku',
    'zh-hans': 'BySide:Sudoku',
    'zh-hant': 'BySide:Sudoku',
}


def g(lang):
    """Google 정책 링크(언어별)."""
    hl = {'ko': 'ko', 'en': 'en', 'ja': 'ja', 'zh-hans': 'zh-CN', 'zh-hant': 'zh-TW'}[lang]
    return (f'https://policies.google.com/technologies/partner-sites?hl={hl}',
            f'https://policies.google.com/privacy?hl={hl}')


INTRO = {
    'ko': {
        'title': '내곁의 스도쿠 · 하루 한 판 두뇌 운동',
        'desc': '모두에게 같은 오늘의 퍼즐, 브론즈에서 마스터까지 6단계 티어, 위젯과 Game Center까지. 손에 착 붙는 스도쿠.',
        'nav': ('화면', '기능', '고객 지원'),
        'h1': '매일 한 판,<br><em>두뇌 운동</em>',
        'lead': '모두에게 같은 오늘의 퍼즐을 풀고,<br>브론즈에서 마스터까지 티어를 올려 보세요.',
        'chips': ['오늘의 퍼즐', '6단계 티어', '위젯 · Game Center'],
        'store': ('App Store 출시 준비 중', 'Google Play 출시 준비 중'),
        'screens_h': '이렇게 생겼어요', 'screens_sub': '옆으로 넘겨 보세요.',
        'shots': [
            ('01-home', '오늘의 퍼즐과 티어 6개가 보이는 첫 화면'),
            ('02-game', '숫자 타일 키패드와 메모가 있는 게임 화면'),
            ('03-tier', '완성하고 다음 티어가 열린 결과 화면'),
            ('04-widget', '오늘의 퍼즐과 연속 일수를 보여 주는 홈·잠금 화면 위젯'),
            ('05-stats', '연속 일수와 티어별 기록, 오늘의 퍼즐 달력'),
            ('06-dark', '다크 모드 게임 화면'),
        ],
        'feat_h': '할 맛 나게 만들었어요', 'feat_sub': '처음이어도, 매일 해도 즐겁게.',
        'features': [
            ('오늘의 퍼즐', '매일 새 퍼즐 한 판, 모든 사람이 같은 문제를 풀어요. 연속 일수와 달력으로 이어 가요.'),
            ('6단계 티어', '브론즈부터 마스터까지. 이기면 다음 티어가 열리고 트로피가 화려해져요.'),
            ('손에 착 붙는 숫자 타일', '남은 개수가 보이는 3×3 키패드, 메모·되돌리기·지우기, 같은 숫자 강조.'),
            ('실수 세 번, 힌트 한 번', '남은 기회는 하트로 보여 줘요. 힌트는 한 판에 한 번 무료예요.'),
            ('위젯과 Game Center', '홈·잠금 화면 위젯, 오늘의 퍼즐 순위표와 티어별 최고 기록, 업적.'),
            ('누구나 편하게', '처음이면 게임 방법 안내. 다크 모드, 큰 글자, VoiceOver, 인터넷 없이도 플레이.'),
        ],
        'promise_h': '내 기록은 내 폰에만',
        'promise': ['회원가입이 없어요. 기록과 하던 게임은 서버로 보내지 않고 폰에만 저장해요.',
                    'Game Center는 직접 로그인했을 때만 점수와 업적을 Apple에 올려요.'],
        'footer': ('고객 지원', '개인정보처리방침', '문의'),
    },
    'en': {
        'title': 'BySide:Sudoku · One puzzle a day, one sharper mind',
        'desc': 'The same Daily Puzzle for everyone, six tiers from Bronze to Master, widgets and Game Center. Sudoku that feels great to play.',
        'nav': ('Screens', 'Features', 'Support'),
        'h1': 'One puzzle a day,<br><em>sharp mind</em>',
        'lead': 'Solve the same Daily Puzzle as everyone<br>and climb from Bronze to Master.',
        'chips': ['Daily Puzzle', 'Six tiers', 'Widgets · Game Center'],
        'store': ('Coming soon to the App Store', 'Coming soon to Google Play'),
        'screens_h': 'Take a look', 'screens_sub': 'Swipe to see more.',
        'shots': [
            ('01-home', 'Home screen with the Daily Puzzle and six tiers'),
            ('02-game', 'Game screen with the number-tile keypad and notes'),
            ('03-tier', 'Result screen after a win, with the next tier unlocked'),
            ('04-widget', 'Home and Lock Screen widgets with the Daily Puzzle and streak'),
            ('05-stats', 'Streak, stats by tier and the Daily Puzzle calendar'),
            ('06-dark', 'Game screen in dark mode'),
        ],
        'feat_h': 'Made to feel good', 'feat_sub': 'Fun on day one, and on day one hundred.',
        'features': [
            ('Daily Puzzle', 'A fresh puzzle every day, the same for everyone. Keep your streak going on the calendar.'),
            ('Six tiers', 'Bronze to Master. Win to unlock the next tier and watch your trophy get fancier.'),
            ('Number tiles that feel right', 'A 3×3 keypad that shows what is left, notes, undo, erase and matching highlights.'),
            ('Three mistakes, one free hint', 'Hearts show the chances you have left. One hint per game is free.'),
            ('Widgets and Game Center', 'Home and Lock Screen widgets, Daily Puzzle and best-time leaderboards, achievements.'),
            ('Made for everyone', 'A quick guide for newcomers. Dark mode, larger text, VoiceOver and offline play.'),
        ],
        'promise_h': 'Your records stay on your phone',
        'promise': ['No account. Your stats and games are never sent to our server; they stay on your phone.',
                    'Scores and achievements go to Apple only when you sign in to Game Center.'],
        'footer': ('Support', 'Privacy Policy', 'Contact'),
    },
    'ja': {
        'title': 'BySide:Sudoku · 毎日1問で脳トレ',
        'desc': 'みんな同じ「今日のパズル」、ブロンズからマスターまで6段階のランク、ウィジェットとGame Center。指になじむ数独(ナンプレ)。',
        'nav': ('画面', '機能', 'サポート'),
        'h1': '毎日1問で<br><em>脳トレ</em>',
        'lead': 'みんな同じ「今日のパズル」を解いて、<br>ブロンズからマスターへランクアップ。',
        'chips': ['今日のパズル', '6段階のランク', 'ウィジェット・Game Center'],
        'store': ('App Store 近日公開', 'Google Play 近日公開'),
        'screens_h': 'アプリの画面', 'screens_sub': '横にスワイプしてご覧ください。',
        'shots': [
            ('01-home', '今日のパズルと6つのランクが並ぶホーム画面'),
            ('02-game', '数字タイルとメモのあるゲーム画面'),
            ('03-tier', 'クリアして次のランクが開放された結果画面'),
            ('04-widget', '今日のパズルと連続日数を表示するウィジェット'),
            ('05-stats', '連続日数、ランク別の記録、今日のパズルのカレンダー'),
            ('06-dark', 'ダークモードのゲーム画面'),
        ],
        'feat_h': '遊びやすさにこだわりました', 'feat_sub': '初めてでも、毎日でも楽しく。',
        'features': [
            ('今日のパズル', '毎日新しい1問、みんな同じ問題。連続日数とカレンダーで続けられます。'),
            ('6段階のランク', 'ブロンズからマスターまで。クリアで次のランクが開放され、トロフィーも豪華に。'),
            ('指になじむ数字タイル', '残り個数がわかる3×3キーパッド、メモ・元に戻す・消す、同じ数字のハイライト。'),
            ('ミスは3回、ヒントは1回無料', '残りのチャンスはハートで表示。ヒントは1ゲームに1回無料です。'),
            ('ウィジェットとGame Center', 'ホーム・ロック画面のウィジェット、今日のパズルとランク別ベストのランキング、実績。'),
            ('だれでも快適に', '初めての方には遊び方ガイド。ダークモード、大きな文字、VoiceOver、オフライン対応。'),
        ],
        'promise_h': '記録はあなたのスマホだけに',
        'promise': ['登録は不要。記録や途中のゲームはサーバーに送らず、スマホの中だけに保存します。',
                    'Game Centerにサインインしたときだけ、スコアと実績をAppleに送ります。'],
        'footer': ('サポート', 'プライバシーポリシー', 'お問い合わせ'),
    },
    'zh-hans': {
        'title': 'BySide:Sudoku · 每天一局练脑力',
        'desc': '人人相同的每日一题，从青铜到大师的 6 个段位，还有小组件和 Game Center。手感舒服的数独。',
        'nav': ('界面', '功能', '客户支持'),
        'h1': '每天一局<br><em>练脑力</em>',
        'lead': '和所有人挑战同一道每日一题，<br>从青铜一路升到大师。',
        'chips': ['每日一题', '6 个段位', '小组件 · Game Center'],
        'store': ('即将登陆 App Store', '即将登陆 Google Play'),
        'screens_h': '界面一览', 'screens_sub': '左右滑动查看更多。',
        'shots': [
            ('01-home', '显示每日一题和 6 个段位的首页'),
            ('02-game', '有数字方块键盘和笔记的游戏界面'),
            ('03-tier', '完成后解锁下一段位的结果界面'),
            ('04-widget', '显示每日一题和连续天数的小组件'),
            ('05-stats', '连续天数、各段位记录和每日一题日历'),
            ('06-dark', '深色模式下的游戏界面'),
        ],
        'feat_h': '越玩越顺手', 'feat_sub': '新手好上手，天天玩也不腻。',
        'features': [
            ('每日一题', '每天一道新题，所有人做同一道。用连续天数和日历坚持下去。'),
            ('6 个段位', '从青铜到大师。赢一局解锁下一段位，奖杯越来越华丽。'),
            ('顺手的数字方块', '显示剩余数量的 3×3 键盘，笔记、撤销、擦除，高亮相同数字。'),
            ('出错 3 次，免费提示 1 次', '剩余机会用爱心显示。每局 1 次免费提示。'),
            ('小组件和 Game Center', '主屏幕和锁定屏幕小组件，每日一题和各段位最佳排行榜，成就。'),
            ('人人都好上手', '新手教程。深色模式、大字体、VoiceOver，没网也能玩。'),
        ],
        'promise_h': '记录只留在你的手机里',
        'promise': ['无需注册。记录和进行中的游戏不会发送到服务器，只保存在手机里。',
                    '只有登录 Game Center 时，分数和成就才会发送给 Apple。'],
        'footer': ('客户支持', '隐私政策', '联系我们'),
    },
    'zh-hant': {
        'title': 'BySide:Sudoku · 每天一局練腦力',
        'desc': '人人相同的每日一題，從青銅到大師的 6 個段位，還有小工具和 Game Center。手感舒服的數獨。',
        'nav': ('畫面', '功能', '客戶支援'),
        'h1': '每天一局<br><em>練腦力</em>',
        'lead': '和所有人挑戰同一道每日一題，<br>從青銅一路升到大師。',
        'chips': ['每日一題', '6 個段位', '小工具・Game Center'],
        'store': ('即將登陸 App Store', '即將登陸 Google Play'),
        'screens_h': '畫面一覽', 'screens_sub': '左右滑動查看更多。',
        'shots': [
            ('01-home', '顯示每日一題和 6 個段位的首頁'),
            ('02-game', '有數字方塊鍵盤和筆記的遊戲畫面'),
            ('03-tier', '完成後解鎖下一段位的結果畫面'),
            ('04-widget', '顯示每日一題和連續天數的小工具'),
            ('05-stats', '連續天數、各段位紀錄和每日一題日曆'),
            ('06-dark', '深色模式下的遊戲畫面'),
        ],
        'feat_h': '越玩越順手', 'feat_sub': '新手好上手，天天玩也不膩。',
        'features': [
            ('每日一題', '每天一道新題，所有人做同一道。用連續天數和日曆堅持下去。'),
            ('6 個段位', '從青銅到大師。贏一局解鎖下一段位，獎盃越來越華麗。'),
            ('順手的數字方塊', '顯示剩餘數量的 3×3 鍵盤，筆記、復原、清除，標示相同數字。'),
            ('出錯 3 次，免費提示 1 次', '剩餘機會用愛心顯示。每局 1 次免費提示。'),
            ('小工具和 Game Center', '主畫面和鎖定畫面小工具，每日一題和各段位最佳排行榜，成就。'),
            ('人人都好上手', '新手教學。深色模式、大字體、VoiceOver，沒網路也能玩。'),
        ],
        'promise_h': '紀錄只留在你的手機裡',
        'promise': ['免註冊。紀錄和進行中的遊戲不會傳送到伺服器，只儲存在手機裡。',
                    '只有登入 Game Center 時，分數和成就才會傳送給 Apple。'],
        'footer': ('客戶支援', '隱私權政策', '聯絡我們'),
    },
}


def privacy(lang):
    partner, gpriv = g(lang)
    T = {
        'ko': ('내곁의 스도쿠 개인정보처리방침', '시행일: 2026년 10월 9일',
               "'내곁의 스도쿠'(이하 \"앱\", iOS·Android)는 이용자의 개인정보를 소중히 다루며, 「개인정보 보호법」 등 관련 법령을 지킵니다. 이 방침은 앱이 어떤 정보를 어떻게 다루는지 설명합니다.",
               [
                   ('1. 앱이 직접 수집하는 정보', [
                       '<p>앱은 회원가입이나 로그인이 없으며, 운영자가 운영하는 서버로 이용자의 정보를 보내지 않습니다.</p>',
                       '<p>게임 기록(티어별 완료 수·시간, 오늘의 퍼즐을 푼 날), 하던 게임, 화면·언어 설정은 <strong>이용자의 기기 안에만 저장</strong>됩니다. 운영자는 이 내용을 볼 수 없습니다.</p>',
                   ]),
                   ('2. 광고를 위해 제3자가 수집하는 정보', [
                       '<p>앱은 무료로 제공되며, 추가 힌트나 이어서 풀기를 고르면 Google LLC의 <strong>Google AdMob</strong> 보상형 광고를 보여 줍니다. AdMob은 광고 제공과 측정, 부정 사용 방지를 위해 다음 정보를 수집·처리할 수 있습니다.</p>',
                       '<table><tr><th>수집 주체</th><th>항목</th><th>목적</th></tr><tr><td>Google LLC (AdMob)</td><td>광고 ID(Android 광고 ID, iOS 광고 식별자 IDFA — iOS는 이용자가 추적을 허용한 경우에만), IP 주소, 기기·운영체제 정보, 광고 노출·클릭 등 앱 이용 정보, 대략적인 위치(IP 기반)</td><td>광고 표시·맞춤형 광고, 광고 성과 측정, 부정 클릭 방지</td></tr></table>',
                       f'<p>Google의 정보 처리 방식은 <a href="{partner}">Google 파트너 사이트·앱의 데이터 사용 방식</a>과 <a href="{gpriv}">Google 개인정보처리방침</a>에서 확인할 수 있습니다.</p>',
                   ]),
                   ('3. Game Center (iOS)', [
                       '<p>이용자가 기기에서 Game Center에 로그인한 경우에만, 완성한 퍼즐의 시간(순위표)과 업적을 Apple의 Game Center로 보냅니다. 순위표에는 이용자의 Game Center 닉네임이 표시됩니다. 이 정보는 Apple이 처리하며 <a href="https://www.apple.com/legal/privacy/">Apple 개인정보처리방침</a>을 따릅니다. Game Center는 기기의 설정 앱에서 끌 수 있습니다.</p>',
                   ]),
                   ('4. 결제(광고 제거)', [
                       '<p>광고 제거 구매는 App Store 또는 Google Play가 처리합니다. 앱과 운영자는 카드 번호 등 결제 정보를 받지 않으며, 스토어가 알려 주는 구매 여부만 기기에서 확인합니다. 광고 제거는 한 번 구매하는 상품이며 자동 결제가 없습니다.</p>',
                   ]),
                   ('5. 맞춤형 광고 거부 방법', [
                       '<ul><li>iOS: 처음 실행할 때 "추적 허용" 여부를 고를 수 있으며, <strong>설정 → 개인정보 보호 및 보안 → 추적</strong>에서 언제든 바꿀 수 있습니다.</li><li>Android: 휴대폰 <strong>설정 → Google → 광고</strong>에서 광고 ID를 삭제하거나 재설정할 수 있습니다.</li><li>유럽경제지역(EEA)·영국·스위스 이용자는 처음 실행할 때 광고 개인정보 동의를 선택할 수 있고, 앱의 <strong>설정 → 광고 개인정보 설정</strong>에서 바꿀 수 있습니다.</li></ul>',
                   ]),
                   ('6. 위젯', [
                       '<p>홈 화면·잠금 화면 위젯은 기기 안의 기록(오늘의 퍼즐을 풀었는지, 연속 일수, 티어)을 표시만 하며 외부로 보내지 않습니다.</p>',
                   ]),
                   ('7. 보관 및 파기', [
                       '<p>기기에 저장된 기록은 앱을 삭제하면 함께 지워집니다. 운영자가 따로 보관하는 정보는 없습니다. 제3자(Google, Apple, 스토어)가 수집한 정보의 보관 기간은 해당 회사의 방침을 따릅니다.</p>',
                   ]),
                   ('8. 아동의 개인정보', [
                       '<p>앱은 만 14세 미만 아동(해외는 만 13세 미만)을 주 대상으로 하지 않으며, 아동의 개인정보를 의도적으로 수집하지 않습니다.</p>',
                   ]),
                   ('9. 개인정보 보호책임자·문의', [
                       f'<p>개인정보 보호책임자: 내곁의 운영자<br>연락처: {E}</p>',
                   ]),
                   ('10. 방침의 변경', [
                       '<p>이 방침이 바뀌면 이 페이지에 시행일과 함께 알립니다. 이 방침은 한국어 원문을 기준으로 하며, 다른 언어판과 뜻이 다르면 한국어판을 따릅니다.</p>',
                   ]),
               ]),
        'en': ('BySide:Sudoku Privacy Policy', 'Effective: October 9, 2026',
               'BySide:Sudoku (the "app", iOS and Android) respects your privacy. This policy explains what information the app handles and how.',
               [
                   ('1. Information the app collects', [
                       '<p>The app has no account or sign-in, and it never sends your information to a server run by us.</p>',
                       '<p>Your game records (games won and times by tier, the days you solved the Daily Puzzle), your current game and your display and language settings are <strong>stored only on your device</strong>. We cannot see them.</p>',
                   ]),
                   ('2. Information collected by third parties for ads', [
                       '<p>The app is free. When you choose an extra hint or to keep going after a loss, it shows a rewarded ad from <strong>Google AdMob</strong> (Google LLC). AdMob may collect and process the following to serve and measure ads and prevent fraud.</p>',
                       '<table><tr><th>Collected by</th><th>Data</th><th>Purpose</th></tr><tr><td>Google LLC (AdMob)</td><td>Advertising ID (Android advertising ID; on iOS, the IDFA only if you allow tracking), IP address, device and OS information, app usage such as ad views and clicks, approximate location (from IP)</td><td>Showing and personalizing ads, measuring ad performance, preventing invalid clicks</td></tr></table>',
                       f'<p>See <a href="{partner}">How Google uses information from sites or apps that use its services</a> and the <a href="{gpriv}">Google Privacy Policy</a>.</p>',
                   ]),
                   ('3. Game Center (iOS)', [
                       '<p>Only if you are signed in to Game Center on your device, the app sends your solve times (for leaderboards) and achievements to Apple Game Center. Leaderboards show your Game Center nickname. Apple processes this information under the <a href="https://www.apple.com/legal/privacy/">Apple Privacy Policy</a>. You can turn off Game Center in the Settings app.</p>',
                   ]),
                   ('4. Purchases (Remove Ads)', [
                       '<p>The Remove Ads purchase is handled by the App Store or Google Play. We never receive card numbers or other payment details; the app only checks on your device whether the store reports a purchase. Remove Ads is a one-time purchase with no automatic renewal.</p>',
                   ]),
                   ('5. Opting out of personalized ads', [
                       '<ul><li>iOS: choose whether to allow tracking on first launch, and change it any time in <strong>Settings → Privacy &amp; Security → Tracking</strong>.</li><li>Android: delete or reset your advertising ID in <strong>Settings → Google → Ads</strong>.</li><li>Users in the EEA, the UK and Switzerland can choose their ad privacy consent on first launch and change it in the app under <strong>Settings → Ad privacy settings</strong>.</li></ul>',
                   ]),
                   ('6. Widgets', [
                       '<p>Home Screen and Lock Screen widgets only display records stored on your device (whether you solved the Daily Puzzle, your streak and your tier) and send nothing elsewhere.</p>',
                   ]),
                   ('7. Retention and deletion', [
                       '<p>Records stored on your device are deleted when you delete the app. We keep no information of our own. Information collected by third parties (Google, Apple, the stores) is kept under their policies.</p>',
                   ]),
                   ("8. Children's privacy", [
                       '<p>The app is not directed primarily at children under 13 (under 14 in Korea) and does not knowingly collect their personal information.</p>',
                   ]),
                   ('9. Contact', [
                       f'<p>Privacy officer: BySide operator<br>Contact: {E}</p>',
                   ]),
                   ('10. Changes', [
                       '<p>If this policy changes, we will post the update on this page with a new effective date. The Korean version is the original; if versions differ, the Korean version prevails.</p>',
                   ]),
               ]),
        'ja': ('BySide:Sudoku プライバシーポリシー', '施行日：2026年10月9日',
               'BySide:Sudoku(以下「本アプリ」、iOS・Android)は、利用者のプライバシーを大切にします。本ポリシーでは、本アプリがどのような情報をどのように扱うかを説明します。',
               [
                   ('1. 本アプリが収集する情報', [
                       '<p>本アプリには会員登録やログインがなく、運営者のサーバーに利用者の情報を送信しません。</p>',
                       '<p>ゲームの記録(ランク別のクリア数・タイム、今日のパズルを解いた日)、途中のゲーム、表示・言語の設定は<strong>利用者の端末内だけに保存</strong>されます。運営者はこれらを見ることができません。</p>',
                   ]),
                   ('2. 広告のために第三者が収集する情報', [
                       '<p>本アプリは無料です。追加のヒントや続きから解くを選ぶと、Google LLCの<strong>Google AdMob</strong>によるリワード広告を表示します。AdMobは広告の配信・測定、不正防止のため、次の情報を収集・処理することがあります。</p>',
                       '<table><tr><th>収集者</th><th>項目</th><th>目的</th></tr><tr><td>Google LLC (AdMob)</td><td>広告ID(Androidの広告ID、iOSのIDFA — iOSはトラッキングを許可した場合のみ)、IPアドレス、端末・OS情報、広告の表示・クリックなどの利用情報、おおよその位置(IPに基づく)</td><td>広告の表示・パーソナライズ、広告効果の測定、不正クリックの防止</td></tr></table>',
                       f'<p>詳しくは<a href="{partner}">Googleのサービスを使用するサイトやアプリから収集した情報のGoogleによる使用</a>と<a href="{gpriv}">Googleプライバシーポリシー</a>をご覧ください。</p>',
                   ]),
                   ('3. Game Center(iOS)', [
                       '<p>端末でGame Centerにサインインしている場合に限り、クリアタイム(ランキング用)と実績をAppleのGame Centerに送信します。ランキングにはGame Centerのニックネームが表示されます。これらの情報は<a href="https://www.apple.com/legal/privacy/">Appleのプライバシーポリシー</a>に従ってAppleが処理します。Game Centerは設定アプリでオフにできます。</p>',
                   ]),
                   ('4. 購入(広告の削除)', [
                       '<p>広告の削除の購入はApp StoreまたはGoogle Playが処理します。運営者はカード番号などの決済情報を受け取らず、ストアが知らせる購入の有無だけを端末で確認します。広告の削除は買い切りで、自動更新はありません。</p>',
                   ]),
                   ('5. パーソナライズ広告の停止', [
                       '<ul><li>iOS:初回起動時にトラッキングを許可するか選べます。<strong>設定 → プライバシーとセキュリティ → トラッキング</strong>でいつでも変更できます。</li><li>Android:<strong>設定 → Google → 広告</strong>で広告IDを削除またはリセットできます。</li><li>EEA・英国・スイスの利用者は、初回起動時に広告のプライバシー同意を選び、アプリの<strong>設定 → 広告のプライバシー設定</strong>で変更できます。</li></ul>',
                   ]),
                   ('6. ウィジェット', [
                       '<p>ホーム画面・ロック画面のウィジェットは、端末内の記録(今日のパズルを解いたか、連続日数、ランク)を表示するだけで、外部には送信しません。</p>',
                   ]),
                   ('7. 保存期間と削除', [
                       '<p>端末に保存された記録は、アプリを削除すると一緒に消えます。運営者が別に保管する情報はありません。第三者(Google、Apple、ストア)が収集した情報の保存期間は各社のポリシーに従います。</p>',
                   ]),
                   ('8. 子どもの個人情報', [
                       '<p>本アプリは13歳未満(韓国は14歳未満)の子どもを主な対象としておらず、子どもの個人情報を意図的に収集しません。</p>',
                   ]),
                   ('9. お問い合わせ', [
                       f'<p>個人情報保護責任者:BySide 運営者<br>連絡先:{E}</p>',
                   ]),
                   ('10. ポリシーの変更', [
                       '<p>本ポリシーを変更する場合は、施行日とともに本ページでお知らせします。韓国語版を原文とし、各言語版と内容が異なる場合は韓国語版が優先されます。</p>',
                   ]),
               ]),
        'zh-hans': ('BySide:Sudoku 隐私政策', '生效日期：2026年10月9日',
                    'BySide:Sudoku（以下简称“本应用”，iOS 和 Android）重视你的隐私。本政策说明本应用处理哪些信息以及如何处理。',
                    [
                        ('1. 本应用收集的信息', [
                            '<p>本应用没有注册或登录，也不会把你的信息发送到运营者的服务器。</p>',
                            '<p>游戏记录（各段位的完成局数和用时、完成每日一题的日期）、进行中的游戏以及显示和语言设置<strong>只保存在你的设备上</strong>。运营者无法查看。</p>',
                        ]),
                        ('2. 第三方为广告收集的信息', [
                            '<p>本应用免费提供。当你选择额外提示或失败后继续时，会显示 Google LLC 的 <strong>Google AdMob</strong> 激励广告。AdMob 可能为投放和衡量广告、防止作弊而收集和处理以下信息。</p>',
                            '<table><tr><th>收集方</th><th>项目</th><th>目的</th></tr><tr><td>Google LLC (AdMob)</td><td>广告标识符（Android 广告 ID；iOS 的 IDFA 仅在你允许跟踪时）、IP 地址、设备和系统信息、广告展示和点击等使用信息、大致位置（基于 IP）</td><td>展示广告和个性化广告、衡量广告效果、防止无效点击</td></tr></table>',
                            f'<p>详见<a href="{partner}">Google 如何使用来自使用其服务的网站或应用的信息</a>和 <a href="{gpriv}">Google 隐私权政策</a>。</p>',
                        ]),
                        ('3. Game Center（iOS）', [
                            '<p>仅当你在设备上登录 Game Center 时，本应用才会把完成用时（用于排行榜）和成就发送到 Apple Game Center。排行榜会显示你的 Game Center 昵称。这些信息由 Apple 按照 <a href="https://www.apple.com/legal/privacy/">Apple 隐私政策</a>处理。你可以在“设置”中关闭 Game Center。</p>',
                        ]),
                        ('4. 购买（移除广告）', [
                            '<p>移除广告的购买由 App Store 或 Google Play 处理。运营者不会收到银行卡号等支付信息，本应用只在设备上确认商店告知的购买状态。移除广告为一次性购买，不会自动续费。</p>',
                        ]),
                        ('5. 关闭个性化广告', [
                            '<ul><li>iOS：首次启动时可选择是否允许跟踪，之后可随时在<strong>设置 → 隐私与安全性 → 跟踪</strong>中更改。</li><li>Android：在<strong>设置 → Google → 广告</strong>中删除或重置广告 ID。</li><li>欧洲经济区、英国和瑞士的用户可在首次启动时选择广告隐私同意，并在应用的<strong>设置 → 广告隐私设置</strong>中更改。</li></ul>',
                        ]),
                        ('6. 小组件', [
                            '<p>主屏幕和锁定屏幕小组件只显示设备上的记录（是否完成每日一题、连续天数、段位），不会发送到外部。</p>',
                        ]),
                        ('7. 保存与删除', [
                            '<p>设备上的记录会在删除应用时一并删除。运营者不另外保存任何信息。第三方（Google、Apple、商店）收集的信息按其各自的政策保存。</p>',
                        ]),
                        ('8. 儿童隐私', [
                            '<p>本应用并非主要面向 13 岁以下（韩国为 14 岁以下）的儿童，也不会有意收集儿童的个人信息。</p>',
                        ]),
                        ('9. 联系方式', [
                            f'<p>个人信息保护负责人：BySide 运营者<br>联系邮箱：{E}</p>',
                        ]),
                        ('10. 政策变更', [
                            '<p>本政策如有变更，将在本页面公布并注明生效日期。本政策以韩文版为准，其他语言版本与韩文版不一致时，以韩文版为准。</p>',
                        ]),
                    ]),
        'zh-hant': ('BySide:Sudoku 隱私權政策', '生效日期：2026年10月9日',
                    'BySide:Sudoku（以下簡稱「本應用程式」，iOS 和 Android）重視你的隱私。本政策說明本應用程式處理哪些資訊以及如何處理。',
                    [
                        ('1. 本應用程式蒐集的資訊', [
                            '<p>本應用程式沒有註冊或登入，也不會把你的資訊傳送到營運者的伺服器。</p>',
                            '<p>遊戲紀錄（各段位的完成局數和用時、完成每日一題的日期）、進行中的遊戲以及顯示和語言設定<strong>只儲存在你的裝置上</strong>。營運者無法查看。</p>',
                        ]),
                        ('2. 第三方為廣告蒐集的資訊', [
                            '<p>本應用程式免費提供。當你選擇額外提示或失敗後繼續時，會顯示 Google LLC 的 <strong>Google AdMob</strong> 獎勵廣告。AdMob 可能為投放和衡量廣告、防止作弊而蒐集和處理以下資訊。</p>',
                            '<table><tr><th>蒐集方</th><th>項目</th><th>目的</th></tr><tr><td>Google LLC (AdMob)</td><td>廣告識別碼（Android 廣告 ID；iOS 的 IDFA 僅在你允許追蹤時）、IP 位址、裝置和系統資訊、廣告曝光和點擊等使用資訊、大致位置（依 IP）</td><td>顯示廣告和個人化廣告、衡量廣告成效、防止無效點擊</td></tr></table>',
                            f'<p>詳見<a href="{partner}">Google 如何使用採用其服務的網站或應用程式所提供的資訊</a>和 <a href="{gpriv}">Google 隱私權政策</a>。</p>',
                        ]),
                        ('3. Game Center（iOS）', [
                            '<p>僅當你在裝置上登入 Game Center 時，本應用程式才會把完成用時（用於排行榜）和成就傳送到 Apple Game Center。排行榜會顯示你的 Game Center 暱稱。這些資訊由 Apple 依照 <a href="https://www.apple.com/legal/privacy/">Apple 隱私權政策</a>處理。你可以在「設定」中關閉 Game Center。</p>',
                        ]),
                        ('4. 購買（移除廣告）', [
                            '<p>移除廣告的購買由 App Store 或 Google Play 處理。營運者不會收到信用卡號等付款資訊，本應用程式只在裝置上確認商店告知的購買狀態。移除廣告為一次性購買，不會自動續訂。</p>',
                        ]),
                        ('5. 關閉個人化廣告', [
                            '<ul><li>iOS：首次啟動時可選擇是否允許追蹤，之後可隨時在<strong>設定 → 隱私權與安全性 → 追蹤</strong>中更改。</li><li>Android：在<strong>設定 → Google → 廣告</strong>中刪除或重設廣告 ID。</li><li>歐洲經濟區、英國和瑞士的使用者可在首次啟動時選擇廣告隱私權同意，並在應用程式的<strong>設定 → 廣告隱私權設定</strong>中更改。</li></ul>',
                        ]),
                        ('6. 小工具', [
                            '<p>主畫面和鎖定畫面小工具只顯示裝置上的紀錄（是否完成每日一題、連續天數、段位），不會傳送到外部。</p>',
                        ]),
                        ('7. 保存與刪除', [
                            '<p>裝置上的紀錄會在刪除應用程式時一併刪除。營運者不另外保存任何資訊。第三方（Google、Apple、商店）蒐集的資訊依其各自的政策保存。</p>',
                        ]),
                        ('8. 兒童隱私', [
                            '<p>本應用程式並非主要以 13 歲以下（韓國為 14 歲以下）的兒童為對象，也不會刻意蒐集兒童的個人資訊。</p>',
                        ]),
                        ('9. 聯絡方式', [
                            f'<p>個人資料保護負責人：BySide 營運者<br>聯絡信箱：{E}</p>',
                        ]),
                        ('10. 政策變更', [
                            '<p>本政策如有變更，將在本頁面公告並註明生效日期。本政策以韓文版為準，其他語言版本與韓文版不一致時，以韓文版為準。</p>',
                        ]),
                    ]),
    }
    title, date, intro, sections = T[lang]
    return {'title': title, 'date': date, 'intro': intro, 'sections': sections}


SUPPORT = {
    'ko': {
        'title': '내곁의 스도쿠 고객 지원',
        'intro': '사용하다 궁금한 점이나 불편한 점이 있으면 메일로 알려 주세요. 보통 2~3일 안에 답장드려요.',
        'contact': '문의',
        'hint': '앱 버전, 기기 종류, 어떤 화면에서 무엇을 했는지 적어 주시면 더 빨리 도와드릴 수 있어요.',
        'faq_h': '자주 묻는 질문',
        'faq': [
            ('다음 티어가 잠겨 있어요.', '바로 앞 티어를 <strong>한 판 이기면</strong> 다음 티어가 열려요. 오늘의 퍼즐은 티어 해제에 들어가지 않아요.'),
            ('실수를 세 번 하면 어떻게 되나요?', '그 판이 멈춰요. 광고를 끝까지 보면 틀린 숫자를 지우고 기회 하나를 받아 <strong>이어서 풀기</strong>를 할 수 있고, 광고 없이 <strong>새 게임</strong>을 시작할 수도 있어요.'),
            ('힌트는 몇 번 쓸 수 있나요?', '한 판에 한 번은 무료예요. 그 뒤로는 짧은 광고를 끝까지 보면 힌트를 하나 더 받아요. 광고 제거를 사면 광고 없이 힌트를 쓸 수 있어요.'),
            ('광고 제거는 구독인가요?', '아니요. <strong>한 번 구매하면 평생</strong> 가는 상품이에요. 자동 결제가 없어요.'),
            ('폰을 바꾸거나 앱을 다시 설치했더니 광고가 다시 보여요.', '같은 Apple ID·Google 계정으로 로그인한 뒤 앱의 <strong>설정 → 광고 제거 → 구매 복원</strong>을 눌러 주세요.'),
            ('기록이 사라졌어요.', '기록은 폰 안에만 저장돼요. 앱을 삭제하면 기록도 함께 지워지고, 다른 폰으로 옮겨지지 않아요.'),
            ('Game Center 순위표에 기록이 안 보여요.', '기기의 <strong>설정 → Game Center</strong>에서 로그인돼 있어야 해요. 로그인한 뒤 완성한 판부터 순위표와 업적에 올라가요.'),
            ('홈 화면 위젯은 어떻게 추가하나요?', '아이폰: 홈 화면 빈 곳을 길게 누르고 → 편집 → 위젯 추가 → \'내곁의 스도쿠\''),
        ],
    },
    'en': {
        'title': 'BySide:Sudoku Support',
        'intro': 'If you have a question or run into a problem, please email us. We usually reply within two or three days.',
        'contact': 'Contact',
        'hint': 'Including the app version, your device and what you were doing helps us help you faster.',
        'faq_h': 'FAQ',
        'faq': [
            ('The next tier is locked.', '<strong>Win one game</strong> in the tier just before it to unlock it. The Daily Puzzle does not count toward unlocking tiers.'),
            ('What happens after three mistakes?', 'The game stops. Watch an ad to the end to clear the wrong numbers and get one more chance with <strong>Keep going</strong>, or start a <strong>New game</strong> without an ad.'),
            ('How many hints do I get?', 'One free hint per game. After that, watch a short ad to the end for another hint. With Remove Ads, hints come without ads.'),
            ('Is Remove Ads a subscription?', 'No. It is a <strong>one-time purchase that lasts forever</strong>, with no automatic renewal.'),
            ('Ads came back after I changed phones or reinstalled.', 'Sign in with the same Apple ID or Google account, then tap <strong>Settings → Remove ads → Restore purchase</strong> in the app.'),
            ('My records are gone.', 'Records are stored only on your phone. Deleting the app deletes them too, and they do not move to another phone.'),
            ("My times don't show on Game Center.", 'Make sure you are signed in under <strong>Settings → Game Center</strong> on your device. Games you finish after signing in are sent to leaderboards and achievements.'),
            ('How do I add the widget?', 'iPhone: touch and hold an empty area of the Home Screen → Edit → Add Widget → BySide:Sudoku.'),
        ],
    },
    'ja': {
        'title': 'BySide:Sudoku サポート',
        'intro': 'ご質問や不具合があればメールでお知らせください。通常2〜3日以内にお返事します。',
        'contact': 'お問い合わせ',
        'hint': 'アプリのバージョン、端末の種類、どの画面で何をしたかを書いていただくと、より早く対応できます。',
        'faq_h': 'よくある質問',
        'faq': [
            ('次のランクがロックされています。', 'ひとつ前のランクで<strong>1回クリア</strong>すると開放されます。今日のパズルはランクの開放に含まれません。'),
            ('3回ミスするとどうなりますか?', 'ゲームが止まります。広告を最後まで見ると、間違えた数字を消してチャンスを1回もらい<strong>続きから解く</strong>ことができます。広告なしで<strong>新しいゲーム</strong>を始めることもできます。'),
            ('ヒントは何回使えますか?', '1ゲームに1回は無料です。その後は短い広告を最後まで見るとヒントをもう1回もらえます。広告の削除を購入すると、広告なしでヒントを使えます。'),
            ('広告の削除はサブスクリプションですか?', 'いいえ。<strong>一度の購入でずっと</strong>使える買い切りです。自動更新はありません。'),
            ('機種変更や再インストール後に広告が表示されます。', '同じApple ID・Googleアカウントでサインインし、アプリの<strong>設定 → 広告の削除 → 購入を復元</strong>をタップしてください。'),
            ('記録が消えました。', '記録はスマホの中だけに保存されます。アプリを削除すると記録も消え、別のスマホには移りません。'),
            ('Game Centerのランキングに記録が出ません。', '端末の<strong>設定 → Game Center</strong>でサインインしている必要があります。サインイン後にクリアしたゲームからランキングと実績に反映されます。'),
            ('ウィジェットの追加方法は?', 'iPhone:ホーム画面の空いている所を長押し → 編集 → ウィジェットを追加 → BySide:Sudoku'),
        ],
    },
    'zh-hans': {
        'title': 'BySide:Sudoku 客户支持',
        'intro': '如有疑问或遇到问题，请发邮件告诉我们。我们通常会在两三天内回复。',
        'contact': '联系我们',
        'hint': '写明应用版本、设备型号以及在哪个界面做了什么，我们能更快帮你解决。',
        'faq_h': '常见问题',
        'faq': [
            ('下一个段位是锁着的。', '在前一个段位<strong>赢一局</strong>即可解锁。每日一题不计入段位解锁。'),
            ('出错 3 次会怎样？', '本局会暂停。看完广告即可清除错误数字并获得一次机会<strong>继续这一局</strong>，也可以不看广告直接开始<strong>新游戏</strong>。'),
            ('提示能用几次？', '每局 1 次免费。之后看完一段短广告可再获得 1 次提示。购买移除广告后，使用提示无需看广告。'),
            ('移除广告是订阅吗？', '不是。这是<strong>一次购买、永久有效</strong>的商品，不会自动续费。'),
            ('换手机或重新安装后又出现了广告。', '请使用相同的 Apple ID 或 Google 账号登录，然后在应用中点按<strong>设置 → 移除广告 → 恢复购买</strong>。'),
            ('记录不见了。', '记录只保存在手机里。删除应用后记录也会一并删除，且不会转移到其他手机。'),
            ('Game Center 排行榜上看不到我的成绩。', '需要在设备的<strong>设置 → Game Center</strong>中登录。登录后完成的游戏才会计入排行榜和成就。'),
            ('如何添加小组件？', 'iPhone：长按主屏幕空白处 → 编辑 → 添加小组件 → BySide:Sudoku'),
        ],
    },
    'zh-hant': {
        'title': 'BySide:Sudoku 客戶支援',
        'intro': '如有疑問或遇到問題，請寄信告訴我們。我們通常會在兩三天內回覆。',
        'contact': '聯絡我們',
        'hint': '寫明 App 版本、裝置型號以及在哪個畫面做了什麼，我們能更快幫你解決。',
        'faq_h': '常見問題',
        'faq': [
            ('下一個段位是鎖著的。', '在前一個段位<strong>贏一局</strong>即可解鎖。每日一題不計入段位解鎖。'),
            ('出錯 3 次會怎樣？', '本局會暫停。看完廣告即可清除錯誤數字並獲得一次機會<strong>繼續這一局</strong>，也可以不看廣告直接開始<strong>新遊戲</strong>。'),
            ('提示能用幾次？', '每局 1 次免費。之後看完一段短廣告可再獲得 1 次提示。購買移除廣告後，使用提示無需看廣告。'),
            ('移除廣告是訂閱嗎？', '不是。這是<strong>一次購買、永久有效</strong>的商品，不會自動續訂。'),
            ('換手機或重新安裝後又出現了廣告。', '請使用相同的 Apple ID 或 Google 帳號登入，然後在 App 中點一下<strong>設定 → 移除廣告 → 恢復購買</strong>。'),
            ('紀錄不見了。', '紀錄只儲存在手機裡。刪除 App 後紀錄也會一併刪除，且不會轉移到其他手機。'),
            ('Game Center 排行榜上看不到我的成績。', '需要在裝置的<strong>設定 → Game Center</strong>中登入。登入後完成的遊戲才會計入排行榜和成就。'),
            ('如何加入小工具？', 'iPhone：長按主畫面空白處 → 編輯 → 加入小工具 → BySide:Sudoku'),
        ],
    },
}
