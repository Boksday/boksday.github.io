"""내곁의 디데이 웹 페이지 문구(5개 언어)."""

E = '<a href="mailto:ekqlszzzz@naver.com">ekqlszzzz@naver.com</a>'

APP = {
    'ko': '내곁의 디데이',
    'en': 'BySide D-Day',
    'ja': 'BySide D-Day',
    'zh-hans': 'BySide D-Day',
    'zh-hant': 'BySide D-Day',
}


def g(lang):
    """Google 정책 링크(언어별)."""
    hl = {'ko': 'ko', 'en': 'en', 'ja': 'ja', 'zh-hans': 'zh-CN', 'zh-hant': 'zh-TW'}[lang]
    return (f'https://policies.google.com/technologies/partner-sites?hl={hl}',
            f'https://policies.google.com/privacy?hl={hl}')


INTRO = {
    'ko': {
        'title': '내곁의 디데이 · 사진으로 꾸미는 디데이',
        'desc': '좋아하는 사진으로 디데이를 꾸미고, 음력 생신·100일 기념일까지 그날이 오기 전에 먼저 알려 주는 디데이 앱',
        'nav': ('화면', '기능', '고객 지원'),
        'h1': '소중한 날을<br><em>곁에</em> 두세요',
        'lead': '좋아하는 사진으로 디데이를 꾸미고,<br>그날이 오기 전에 먼저 알려 드려요.',
        'chips': ['사진 앨범·위젯 무료', '100일마다 알림', '음력 생신 자동 계산'],
        'store': ('App Store 출시 준비 중', 'Google Play 출시 준비 중'),
        'screens_h': '이렇게 생겼어요', 'screens_sub': '옆으로 넘겨 보세요.',
        'feat_h': '필요한 건 다 무료예요', 'feat_sub': '유료는 광고 제거 하나뿐이에요. 한 번 사면 평생이에요.',
        'features': [
            ('사진 앨범', '디데이마다 사진을 넣어 앨범처럼 모아 봐요.'),
            ('음력 생신', '해마다 양력으로 자동 계산해요. 윤달도 챙겨요.'),
            ('100일마다 알림', '당일·1·3·7일 전, 100일·1000일 기념일 전에 먼저 알려 드려요.'),
            ('홈·잠금 화면 위젯', '보고 싶은 디데이를 골라 크게 띄워요.'),
            ('달력과 여러 보기', '목록·카드·앨범·달력, 분류별 색과 정렬.'),
            ('공유 카드', '사진 배경 카드로 카카오톡·인스타그램에 보내요.'),
        ],
        'promise_h': '내 기록은 내 폰에만',
        'promise': ['회원가입이 없어요. 날짜와 사진은 서버로 보내지 않고 폰에만 저장해요.',
                    '폰을 바꿀 때는 백업 파일 하나로 사진까지 그대로 옮겨요.'],
        'footer': ('고객 지원', '개인정보처리방침', '문의'),
    },
    'en': {
        'title': 'BySide D-Day · Count down to the days that matter',
        'desc': 'Decorate each D-Day with a photo and get reminded before birthdays, lunar birthdays and anniversaries arrive.',
        'nav': ('Screens', 'Features', 'Support'),
        'h1': 'Keep the days<br>that matter <em>close</em>',
        'lead': 'Decorate each D-Day with a favorite photo,<br>and get a reminder before the day arrives.',
        'chips': ['Photo album and widgets, free', 'Every-100-days reminders', 'Lunar birthdays'],
        'store': ('Coming soon to the App Store', 'Coming soon to Google Play'),
        'screens_h': 'Take a look', 'screens_sub': 'Swipe to see more.',
        'feat_h': 'Everything you need is free', 'feat_sub': 'The only purchase is removing ads, and it is yours for life.',
        'features': [
            ('Photo album', 'Add a photo to each D-Day and see them together like an album.'),
            ('Lunar birthdays', 'Converted to the solar calendar every year, leap months included.'),
            ('Reminders', 'On the day, 1, 3 or 7 days before, and before every 100 and 1,000 days.'),
            ('Home and Lock Screen widgets', 'Pick the D-Day you want to see and show it big.'),
            ('Calendar and views', 'List, card, album and calendar views, with category colors and sorting.'),
            ('Share cards', 'Turn a D-Day into a photo card for messages and Instagram.'),
        ],
        'promise_h': 'Your days stay on your phone',
        'promise': ['No account. Dates and photos are never sent to a server; they stay on your phone.',
                    'Moving to a new phone? One backup file brings everything over, photos included.'],
        'footer': ('Support', 'Privacy Policy', 'Contact'),
    },
    'ja': {
        'title': 'BySide D-Day · 写真で彩る記念日カウント',
        'desc': '好きな写真で記念日を彩り、旧暦の誕生日や100日記念日も、その日が来る前にお知らせする記念日アプリ。',
        'nav': ('画面', '機能', 'サポート'),
        'h1': '大切な日を、<br>いつも<em>そばに</em>',
        'lead': '好きな写真で記念日を彩り、<br>その日が来る前にお知らせします。',
        'chips': ['写真アルバム・ウィジェット無料', '100日ごとにお知らせ', '旧暦の誕生日に対応'],
        'store': ('App Store 近日公開', 'Google Play 近日公開'),
        'screens_h': 'アプリの画面', 'screens_sub': '横にスワイプしてご覧ください。',
        'feat_h': '必要な機能はすべて無料', 'feat_sub': '有料は広告の削除だけ。一度の購入でずっと使えます。',
        'features': [
            ('写真アルバム', '記念日ごとに写真を設定して、アルバムのように並べて見られます。'),
            ('旧暦の誕生日', '毎年新暦に自動で変換。閏月にも対応します。'),
            ('100日ごとにお知らせ', '当日、1・3・7日前、100日・1000日の記念日の前にお知らせします。'),
            ('ホーム・ロック画面ウィジェット', '見たい記念日を選んで大きく表示できます。'),
            ('カレンダーと表示切り替え', 'リスト・カード・アルバム・カレンダー、カテゴリの色分けと並べ替え。'),
            ('シェアカード', '写真を背景にしたカードで LINE や Instagram にシェア。'),
        ],
        'promise_h': '記録はあなたのスマートフォンだけに',
        'promise': ['会員登録は不要です。日付や写真はサーバーに送らず、端末にだけ保存します。',
                    '機種変更はバックアップファイルひとつで、写真まで丸ごと移せます。'],
        'footer': ('サポート', 'プライバシーポリシー', 'お問い合わせ'),
    },
    'zh-hans': {
        'title': 'BySide D-Day · 用照片装饰的纪念日倒数',
        'desc': '用喜欢的照片装饰纪念日，农历生日、100天纪念日都会提前提醒你的纪念日应用。',
        'nav': ('界面', '功能', '客户支持'),
        'h1': '把重要的日子<br><em>放在身边</em>',
        'lead': '用喜欢的照片装饰每个纪念日，<br>在那天到来之前先提醒你。',
        'chips': ['照片相册和小组件免费', '每 100 天提醒', '农历生日自动换算'],
        'store': ('即将登陆 App Store', '即将登陆 Google Play'),
        'screens_h': '应用界面', 'screens_sub': '左右滑动查看。',
        'feat_h': '需要的功能全部免费', 'feat_sub': '唯一的付费项目是移除广告，一次购买永久有效。',
        'features': [
            ('照片相册', '为每个纪念日添加照片，像相册一样集中查看。'),
            ('农历生日', '每年自动换算成公历，闰月也能处理。'),
            ('每 100 天提醒', '当天、提前 1・3・7 天，以及 100 天、1000 天纪念日前提醒你。'),
            ('主屏幕和锁定屏幕小组件', '选择想看的纪念日，大大地显示出来。'),
            ('日历和多种视图', '列表・卡片・相册・日历，按分类配色和排序。'),
            ('分享卡片', '把纪念日做成照片背景的卡片，分享到微信或 Instagram。'),
        ],
        'promise_h': '记录只保存在你的手机上',
        'promise': ['无需注册账号。日期和照片不会发送到服务器，只保存在手机上。',
                    '换手机时，一个备份文件就能连照片一起迁移。'],
        'footer': ('客户支持', '隐私政策', '联系我们'),
    },
    'zh-hant': {
        'title': 'BySide D-Day · 用照片裝飾的紀念日倒數',
        'desc': '用喜歡的照片裝飾紀念日，農曆生日、100 天紀念日都會提前提醒你的紀念日 App。',
        'nav': ('畫面', '功能', '客戶支援'),
        'h1': '把重要的日子<br><em>放在身邊</em>',
        'lead': '用喜歡的照片裝飾每個紀念日，<br>在那天到來之前先提醒你。',
        'chips': ['照片相簿和小工具免費', '每 100 天提醒', '農曆生日自動換算'],
        'store': ('即將登上 App Store', '即將登上 Google Play'),
        'screens_h': 'App 畫面', 'screens_sub': '左右滑動查看。',
        'feat_h': '需要的功能全部免費', 'feat_sub': '唯一的付費項目是移除廣告，一次購買永久有效。',
        'features': [
            ('照片相簿', '為每個紀念日加入照片，像相簿一樣集中查看。'),
            ('農曆生日', '每年自動換算成國曆，閏月也能處理。'),
            ('每 100 天提醒', '當天、提前 1・3・7 天，以及 100 天、1000 天紀念日前提醒你。'),
            ('主畫面與鎖定畫面小工具', '選擇想看的紀念日，大大地顯示出來。'),
            ('日曆和多種檢視', '列表・卡片・相簿・日曆，依分類配色與排序。'),
            ('分享卡片', '把紀念日做成照片背景的卡片，分享到 LINE 或 Instagram。'),
        ],
        'promise_h': '記錄只存在你的手機裡',
        'promise': ['不用註冊帳號。日期和照片不會傳到伺服器，只儲存在手機上。',
                    '換手機時，一個備份檔就能連照片一起搬移。'],
        'footer': ('客戶支援', '隱私權政策', '聯絡我們'),
    },
}


def privacy(lang):
    p1, p2 = g(lang)
    data = {
        'ko': ('내곁의 디데이 개인정보처리방침', '시행일: 2026년 10월 9일',
               "'내곁의 디데이'(이하 \"앱\", Android·iOS)는 이용자의 개인정보를 소중히 다루며, 「개인정보 보호법」 등 관련 법령을 지킵니다. 이 방침은 앱이 어떤 정보를 어떻게 다루는지 설명합니다.", [
            ('1. 앱이 직접 수집하는 정보', [
                '<p>앱은 회원가입이나 로그인이 없으며, 운영자가 운영하는 서버로 이용자의 정보를 보내지 않습니다.</p>',
                '<p>이용자가 입력한 디데이(이름, 날짜, 분류, 메모, 반복·알림 설정)와 화면 설정은 <strong>이용자의 기기 안에만 저장</strong>됩니다. 운영자는 이 내용을 볼 수 없습니다.</p>',
                '<p>디데이에 사진을 넣으면, 이용자가 고른 사진 한 장의 크기를 줄인 사본이 <strong>앱 안에만 저장</strong>되며 외부로 전송되지 않습니다. 사진 보관함 전체에 접근하지 않고 이용자가 고른 사진만 읽습니다. 공유 카드를 <strong>이미지로 저장</strong>할 때만 사진 보관함에 이미지를 추가합니다.</p>',
                '<p>이용자가 직접 만드는 <strong>백업 파일</strong>에는 디데이와 함께 앱에 넣은 사진 사본이 들어가며, 보낼 곳은 이용자가 고릅니다. 앱은 기록이 바뀔 때마다 기기 안(iOS 파일 앱의 이 앱 폴더)에 사진을 뺀 자동 백업 파일을 덮어씁니다. 이 파일은 휴대폰 자체 백업(iCloud, Google 백업)에 포함될 수 있으며, 그 백업은 이용자와 Apple·Google 사이의 서비스입니다.</p>',
            ]),
            ('2. 광고를 위해 제3자가 수집하는 정보', [
                '<p>앱은 무료로 제공되며, 광고 표시를 위해 Google LLC의 <strong>Google AdMob</strong>을 사용합니다. AdMob은 광고 제공과 측정, 부정 사용 방지를 위해 다음 정보를 수집·처리할 수 있습니다.</p>',
                '<table><tr><th>수집 주체</th><th>항목</th><th>목적</th></tr><tr><td>Google LLC (AdMob)</td><td>광고 ID(Android 광고 ID, iOS 광고 식별자 IDFA — iOS는 이용자가 추적을 허용한 경우에만), IP 주소, 기기·운영체제 정보, 광고 노출·클릭 등 앱 이용 정보, 대략적인 위치(IP 기반)</td><td>광고 표시·맞춤형 광고, 광고 성과 측정, 부정 클릭 방지</td></tr></table>',
                f'<p>Google의 정보 처리 방식은 <a href="{p1}">Google 파트너 사이트·앱의 데이터 사용 방식</a>과 <a href="{p2}">Google 개인정보처리방침</a>에서 확인할 수 있습니다.</p>',
            ]),
            ('3. 결제(광고 제거)', [
                '<p>광고 제거 구매와 쿠폰 사용은 Google Play 또는 App Store가 처리합니다. 앱과 운영자는 카드 번호 등 결제 정보를 받지 않으며, 스토어가 알려 주는 구매 여부만 기기에서 확인합니다. 광고 제거는 한 번 구매하는 상품이며 자동 결제가 없습니다.</p>',
            ]),
            ('4. 맞춤형 광고 거부 방법', [
                '<ul><li>Android: 휴대폰 <strong>설정 → Google → 광고</strong>에서 광고 ID를 삭제하거나 재설정할 수 있습니다.</li>'
                '<li>iOS: 처음 실행할 때 "추적 허용" 여부를 고를 수 있으며, <strong>설정 → 개인정보 보호 및 보안 → 추적</strong>에서 언제든 바꿀 수 있습니다.</li>'
                '<li>유럽경제지역(EEA)·영국·스위스 이용자는 처음 실행할 때 광고 개인정보 동의를 선택할 수 있습니다. 미국 일부 주의 이용자는 개인정보 판매·공유를 거부할 수 있습니다. 두 경우 모두 앱의 <strong>설정 → 광고 개인정보 설정</strong>에서 언제든 바꿀 수 있습니다.</li>'
                '<li>동의 확인이 되지 않거나 추적을 허용하지 않은 경우 앱은 맞춤형이 아닌 광고만 요청합니다.</li></ul>',
            ]),
            ('5. 알림·위젯·리뷰 요청', [
                '<p>디데이 알림은 기기의 로컬 알림으로 예약되며 외부로 전송되지 않습니다. 알림 권한은 이용자가 알림을 켤 때만 요청하며, 휴대폰 설정에서 언제든 끌 수 있습니다. 홈 화면·잠금 화면 위젯은 기기 안의 디데이 정보를 표시만 합니다. 앱은 App Store·Google Play의 평점 창을 띄울 수 있으며, 평점과 리뷰는 Apple·Google에 직접 남습니다.</p>',
            ]),
            ('6. 보관 및 파기', [
                '<p>기기에 저장된 디데이 정보와 사진은 이용자가 직접 삭제하거나 앱을 삭제하면 함께 지워집니다. 이용자가 내보낸 백업 파일은 보관한 곳에서 직접 지워야 합니다. 운영자가 따로 보관하는 정보는 없습니다. 제3자(Google, 스토어)가 수집한 정보의 보관 기간은 해당 회사의 방침을 따릅니다.</p>',
            ]),
            ('7. 아동의 개인정보', ['<p>앱은 만 14세 미만 아동(해외는 만 13세 미만)을 주 대상으로 하지 않으며, 아동의 개인정보를 의도적으로 수집하지 않습니다.</p>']),
            ('8. 이용자의 권리', ['<p>앱에 저장된 정보는 모두 이용자의 기기에 있으므로 이용자가 앱에서 직접 열람·수정·삭제할 수 있습니다. 광고 관련 정보에 대해서는 4항의 방법으로 맞춤형 광고를 거부할 수 있습니다.</p>']),
            ('9. 개인정보 보호책임자·문의', [f'<p>개인정보 보호책임자: 내곁의 운영자<br>연락처: {E}</p>']),
            ('10. 방침의 변경', ['<p>이 방침이 바뀌면 이 페이지에 시행일과 함께 알립니다. 이 방침은 한국어 원문을 기준으로 하며, 다른 언어판과 뜻이 다르면 한국어판을 따릅니다.</p>']),
        ]),
        'en': ('BySide D-Day Privacy Policy', 'Effective date: October 9, 2026',
               'BySide D-Day (내곁의 디데이, the "App", for Android and iOS) respects your privacy. This policy explains what information the App handles and how.', [
            ('1. Information the App collects', [
                '<p>The App has no sign-up or login, and it does not send your information to any server we run.</p>',
                '<p>The D-Days you enter (name, date, category, memo, repeat and reminder settings) and your display settings are <strong>stored only on your device</strong>. We cannot see them.</p>',
                '<p>If you add a photo to a D-Day, a resized copy of the one photo you pick is <strong>stored only inside the App</strong> and is never uploaded. The App does not access your whole photo library; it reads only the photo you choose. It adds an image to your photo library only when you tap <strong>Save image</strong> on a share card.</p>',
                '<p>A <strong>backup file</strong> you export contains your D-Days and copies of the photos you added, and you choose where it goes. Each time your records change, the App also overwrites an automatic backup file without photos on your device (in the App\'s folder in the iOS Files app). That file may be included in your phone\'s own backup (iCloud or Google backup), which is a service between you and Apple or Google.</p>',
            ]),
            ('2. Information collected by third parties for ads', [
                '<p>The App is free and uses <strong>Google AdMob</strong> by Google LLC to show ads. AdMob may collect and process the following information to serve and measure ads and prevent fraud.</p>',
                '<table><tr><th>Collected by</th><th>Data</th><th>Purpose</th></tr><tr><td>Google LLC (AdMob)</td><td>Advertising ID (Android Advertising ID; iOS IDFA only if you allow tracking), IP address, device and OS information, app usage such as ad impressions and clicks, approximate location (based on IP)</td><td>Showing ads and personalized ads, measuring ad performance, preventing invalid clicks</td></tr></table>',
                f'<p>See <a href="{p1}">How Google uses information from sites or apps that use its services</a> and the <a href="{p2}">Google Privacy Policy</a>.</p>',
            ]),
            ('3. Purchases (Remove ads)', ['<p>Purchases to remove ads and coupon redemptions are handled by Google Play or the App Store. Neither the App nor we receive payment details such as card numbers; the App only checks on your device whether the store reports a purchase. Remove ads is a one-time purchase with no recurring charges.</p>']),
            ('4. Opting out of personalized ads', [
                '<ul><li>Android: In your phone\'s <strong>Settings → Google → Ads</strong>, you can delete or reset your Advertising ID.</li>'
                '<li>iOS: You choose whether to allow tracking on first launch, and you can change it anytime in <strong>Settings → Privacy &amp; Security → Tracking</strong>.</li>'
                '<li>Users in the EEA, the UK and Switzerland can choose ad privacy consent on first launch. Users in some US states can opt out of the sale or sharing of personal information. In both cases you can change your choice anytime in the App\'s <strong>Settings → Ad privacy settings</strong>.</li>'
                '<li>If consent can\'t be confirmed or you don\'t allow tracking, the App requests only non-personalized ads.</li></ul>',
            ]),
            ('5. Reminders, widgets, and review requests', ['<p>D-Day reminders are scheduled as local notifications on your device and are not sent anywhere. The App asks for notification permission only when you turn reminders on, and you can turn it off anytime in your phone\'s settings. Home Screen and Lock Screen widgets only display D-Day information stored on your device. The App may show the App Store or Google Play rating prompt; ratings and reviews go directly to Apple or Google.</p>']),
            ('6. Retention and deletion', ['<p>D-Days and photos stored on your device are deleted when you delete them or uninstall the App. Backup files you exported must be deleted from wherever you keep them. We keep no copy. Information collected by third parties (Google, the stores) is retained according to their policies.</p>']),
            ('7. Children', ['<p>The App is not directed at children under 14 in Korea or under 13 elsewhere, and does not knowingly collect children\'s personal information.</p>']),
            ('8. Your rights', ['<p>All information stored by the App is on your device, so you can view, edit and delete it directly in the App. For ad-related information, you can opt out of personalized ads as described in section 4.</p>']),
            ('9. Privacy contact', [f'<p>Privacy officer: BySide (내곁의) developer<br>Email: {E}</p>']),
            ('10. Changes to this policy', ['<p>If this policy changes, we will post the update on this page with a new effective date. The Korean version of this policy is the original; if a translation differs in meaning, the Korean version prevails.</p>']),
        ]),
        'ja': ('BySide D-Day プライバシーポリシー', '施行日：2026年10月9日',
               '「BySide D-Day」（韓国語名「내곁의 디데이」、以下「本アプリ」、Android・iOS）は、利用者のプライバシーを大切にしています。このポリシーでは、本アプリがどのような情報をどのように扱うかを説明します。', [
            ('1. 本アプリが扱う情報', [
                '<p>本アプリには会員登録やログインがなく、運営者のサーバーに利用者の情報を送ることはありません。</p>',
                '<p>利用者が入力した記念日（名前、日付、カテゴリ、メモ、繰り返し・通知の設定）と表示設定は、<strong>利用者の端末の中にだけ保存</strong>されます。運営者はこれらを見ることができません。</p>',
                '<p>記念日に写真を設定すると、利用者が選んだ写真1枚を縮小したコピーが<strong>アプリの中にだけ保存</strong>され、外部に送られることはありません。写真ライブラリ全体にはアクセスせず、選んだ写真だけを読み込みます。シェアカードの<strong>画像を保存</strong>を押したときだけ、写真ライブラリに画像を追加します。</p>',
                '<p>利用者が書き出す<strong>バックアップファイル</strong>には、記念日とアプリに設定した写真のコピーが含まれ、保存先は利用者が選びます。また、記録が変わるたびに、写真を含まない自動バックアップファイルを端末内（iOS のファイルアプリの本アプリのフォルダ）に上書き保存します。このファイルは端末自体のバックアップ（iCloud、Google バックアップ）に含まれることがあり、そのバックアップは利用者と Apple・Google との間のサービスです。</p>',
            ]),
            ('2. 広告のために第三者が収集する情報', [
                '<p>本アプリは無料で提供され、広告の表示に Google LLC の <strong>Google AdMob</strong> を使用します。AdMob は広告の配信と効果測定、不正利用の防止のために、次の情報を収集・処理することがあります。</p>',
                '<table><tr><th>収集者</th><th>項目</th><th>目的</th></tr><tr><td>Google LLC（AdMob）</td><td>広告 ID（Android の広告 ID、iOS の IDFA。iOS は利用者がトラッキングを許可した場合のみ）、IP アドレス、端末・OS の情報、広告の表示・クリックなどの利用情報、おおよその位置（IP に基づく）</td><td>広告の表示・パーソナライズ広告、広告効果の測定、不正クリックの防止</td></tr></table>',
                f'<p>Google による情報の取り扱いは、<a href="{p1}">Google のサービスを使用するサイトやアプリから収集した情報の Google による使用</a>と<a href="{p2}">Google プライバシーポリシー</a>でご確認いただけます。</p>',
            ]),
            ('3. 決済（広告の削除）', ['<p>広告の削除の購入とクーポンの利用は、Google Play または App Store が処理します。本アプリと運営者はカード番号などの決済情報を受け取らず、ストアが知らせる購入の有無だけを端末で確認します。広告の削除は買い切りの商品で、自動課金はありません。</p>']),
            ('4. パーソナライズ広告を拒否する方法', [
                '<ul><li>Android：端末の<strong>設定 → Google → 広告</strong>で広告 ID を削除またはリセットできます。</li>'
                '<li>iOS：初回起動時に「トラッキングを許可」するかを選べ、<strong>設定 → プライバシーとセキュリティ → トラッキング</strong>でいつでも変更できます。</li>'
                '<li>欧州経済領域（EEA）・英国・スイスの利用者は、初回起動時に広告のプライバシーに関する同意を選べます。米国の一部の州の利用者は、個人情報の販売・共有を拒否できます。いずれの場合も、本アプリの<strong>設定 → 広告のプライバシー設定</strong>でいつでも変更できます。</li>'
                '<li>同意が確認できない場合やトラッキングを許可しない場合、本アプリはパーソナライズされていない広告だけをリクエストします。</li></ul>',
            ]),
            ('5. 通知・ウィジェット・レビューのお願い', ['<p>記念日の通知は端末のローカル通知として予約され、外部に送られることはありません。通知の許可は利用者が通知をオンにしたときだけ求め、端末の設定でいつでもオフにできます。ホーム画面・ロック画面のウィジェットは、端末内の記念日の情報を表示するだけです。本アプリは App Store・Google Play の評価画面を表示することがあり、評価とレビューは Apple・Google に直接送られます。</p>']),
            ('6. 保存期間と削除', ['<p>端末に保存された記念日と写真は、利用者が削除するか本アプリを削除すると一緒に削除されます。書き出したバックアップファイルは、保存した場所から利用者自身が削除してください。運営者が別に保管している情報はありません。第三者（Google、ストア）が収集した情報の保存期間は、各社のポリシーに従います。</p>']),
            ('7. 子どもの個人情報', ['<p>本アプリは13歳未満（韓国では14歳未満）の子どもを主な対象としておらず、子どもの個人情報を意図的に収集することはありません。</p>']),
            ('8. 利用者の権利', ['<p>本アプリが保存する情報はすべて利用者の端末にあるため、本アプリで直接閲覧・修正・削除できます。広告に関する情報は、4項の方法でパーソナライズ広告を拒否できます。</p>']),
            ('9. お問い合わせ窓口', [f'<p>個人情報保護責任者：BySide（내곁의）運営者<br>メール：{E}</p>']),
            ('10. ポリシーの変更', ['<p>このポリシーを変更する場合は、施行日とともにこのページでお知らせします。このポリシーは韓国語版を原文とし、翻訳版と意味が異なる場合は韓国語版が優先されます。</p>']),
        ]),
        'zh-hans': ('BySide D-Day 隐私政策', '生效日期：2026年10月9日',
                    '“BySide D-Day”（韩文名“내곁의 디데이”，以下简称“本应用”，适用于 Android 和 iOS）重视你的隐私。本政策说明本应用处理哪些信息以及如何处理。', [
            ('1. 本应用处理的信息', [
                '<p>本应用无需注册或登录，也不会把你的信息发送到我们运营的服务器。</p>',
                '<p>你输入的纪念日（名称、日期、分类、备注、重复和提醒设置）以及显示设置，<strong>只保存在你的设备上</strong>。我们无法查看这些内容。</p>',
                '<p>为纪念日添加照片时，你选择的那一张照片会被缩小并复制，<strong>只保存在应用内</strong>，不会上传。本应用不会访问整个照片图库，只读取你选择的照片。只有在分享卡片上点按<strong>保存图片</strong>时，才会向照片图库添加图片。</p>',
                '<p>你导出的<strong>备份文件</strong>包含纪念日和你添加的照片副本，保存位置由你选择。此外，每当记录发生变化，本应用会在设备上（iOS“文件”应用中本应用的文件夹）覆盖保存一个不含照片的自动备份文件。该文件可能包含在手机自带的备份（iCloud、Google 备份）中，这类备份是你与 Apple 或 Google 之间的服务。</p>',
            ]),
            ('2. 第三方为广告收集的信息', [
                '<p>本应用免费提供，并使用 Google LLC 的 <strong>Google AdMob</strong> 展示广告。AdMob 可能为投放和衡量广告、防止滥用而收集和处理以下信息。</p>',
                '<table><tr><th>收集方</th><th>项目</th><th>目的</th></tr><tr><td>Google LLC（AdMob）</td><td>广告标识符（Android 广告 ID、iOS IDFA；iOS 仅在你允许跟踪时）、IP 地址、设备和操作系统信息、广告展示和点击等使用信息、大致位置（基于 IP）</td><td>展示广告和个性化广告、衡量广告效果、防止无效点击</td></tr></table>',
                f'<p>Google 如何处理信息，请参阅<a href="{p1}">Google 如何使用来自使用其服务的网站或应用的信息</a>和<a href="{p2}">Google 隐私权政策</a>。</p>',
            ]),
            ('3. 付款（移除广告）', ['<p>移除广告的购买和兑换码的使用由 Google Play 或 App Store 处理。本应用和我们不会收到银行卡号等付款信息，只在设备上确认商店告知的购买状态。移除广告是一次性购买的项目，没有自动续费。</p>']),
            ('4. 拒绝个性化广告的方法', [
                '<ul><li>Android：在手机<strong>设置 → Google → 广告</strong>中可以删除或重置广告 ID。</li>'
                '<li>iOS：首次打开时可以选择是否“允许跟踪”，之后可随时在<strong>设置 → 隐私与安全性 → 跟踪</strong>中更改。</li>'
                '<li>欧洲经济区（EEA）、英国和瑞士的用户可在首次打开时选择广告隐私同意；美国部分州的用户可以拒绝出售或共享个人信息。两种情况都可以随时在本应用的<strong>设置 → 广告隐私设置</strong>中更改。</li>'
                '<li>如果无法确认同意或你不允许跟踪，本应用只请求非个性化广告。</li></ul>',
            ]),
            ('5. 提醒、小组件与评分请求', ['<p>纪念日提醒以设备本地通知的方式预约，不会发送到外部。只有在你开启提醒时才会请求通知权限，你可以随时在手机设置中关闭。主屏幕和锁定屏幕小组件只显示设备上的纪念日信息。本应用可能会显示 App Store 或 Google Play 的评分窗口，评分和评论会直接提交给 Apple 或 Google。</p>']),
            ('6. 保存与删除', ['<p>当你删除纪念日和照片或卸载本应用时，设备上保存的信息会一并删除。你导出的备份文件需要在保存的位置自行删除。我们不另行保存任何信息。第三方（Google、应用商店）收集的信息的保存期限以其政策为准。</p>']),
            ('7. 儿童的个人信息', ['<p>本应用并非主要面向未满 13 岁（韩国为未满 14 岁）的儿童，也不会有意收集儿童的个人信息。</p>']),
            ('8. 你的权利', ['<p>本应用保存的信息都在你的设备上，你可以直接在应用中查看、修改和删除。对于广告相关信息，你可以按第 4 条的方法拒绝个性化广告。</p>']),
            ('9. 联系方式', [f'<p>个人信息保护负责人：BySide（내곁의）开发者<br>邮箱：{E}</p>']),
            ('10. 政策变更', ['<p>本政策如有变更，我们会在本页面公布并注明生效日期。本政策以韩文版为准，译文与韩文版含义不一致时，以韩文版为准。</p>']),
        ]),
        'zh-hant': ('BySide D-Day 隱私權政策', '生效日期：2026年10月9日',
                    '「BySide D-Day」（韓文名「내곁의 디데이」，以下簡稱「本 App」，適用於 Android 與 iOS）重視你的隱私。本政策說明本 App 處理哪些資訊以及如何處理。', [
            ('1. 本 App 處理的資訊', [
                '<p>本 App 不需註冊或登入，也不會把你的資訊傳送到我們經營的伺服器。</p>',
                '<p>你輸入的紀念日（名稱、日期、分類、備註、重複與提醒設定）以及顯示設定，<strong>只儲存在你的裝置上</strong>。我們無法查看這些內容。</p>',
                '<p>為紀念日加入照片時，你選擇的那一張照片會縮小並複製，<strong>只儲存在 App 內</strong>，不會上傳。本 App 不會存取整個照片圖庫，只讀取你選擇的照片。只有在分享卡片上點一下<strong>儲存圖片</strong>時，才會在照片圖庫加入圖片。</p>',
                '<p>你匯出的<strong>備份檔案</strong>包含紀念日和你加入的照片副本，儲存位置由你選擇。此外，每當記錄有變動，本 App 會在裝置上（iOS「檔案」App 中本 App 的資料夾）覆寫一個不含照片的自動備份檔。這個檔案可能包含在手機本身的備份（iCloud、Google 備份）中，這類備份是你與 Apple 或 Google 之間的服務。</p>',
            ]),
            ('2. 第三方為廣告蒐集的資訊', [
                '<p>本 App 免費提供，並使用 Google LLC 的 <strong>Google AdMob</strong> 顯示廣告。AdMob 可能為投放與評估廣告、防止濫用而蒐集與處理下列資訊。</p>',
                '<table><tr><th>蒐集者</th><th>項目</th><th>目的</th></tr><tr><td>Google LLC（AdMob）</td><td>廣告識別碼（Android 廣告 ID、iOS IDFA；iOS 僅在你允許追蹤時）、IP 位址、裝置與作業系統資訊、廣告曝光與點擊等使用資訊、大致位置（依 IP）</td><td>顯示廣告與個人化廣告、評估廣告成效、防止無效點擊</td></tr></table>',
                f'<p>Google 如何處理資訊，請參閱<a href="{p1}">Google 如何使用採用其服務的網站或應用程式所提供的資訊</a>及<a href="{p2}">Google 隱私權政策</a>。</p>',
            ]),
            ('3. 付款（移除廣告）', ['<p>移除廣告的購買與兌換碼的使用由 Google Play 或 App Store 處理。本 App 與我們不會收到信用卡號碼等付款資訊，只在裝置上確認商店告知的購買狀態。移除廣告是一次性購買的項目，沒有自動續訂。</p>']),
            ('4. 拒絕個人化廣告的方法', [
                '<ul><li>Android：在手機<strong>設定 → Google → 廣告</strong>中可以刪除或重設廣告 ID。</li>'
                '<li>iOS：第一次開啟時可以選擇是否「允許追蹤」，之後可隨時在<strong>設定 → 隱私權與安全性 → 追蹤</strong>中變更。</li>'
                '<li>歐洲經濟區（EEA）、英國與瑞士的使用者可在第一次開啟時選擇廣告隱私同意；美國部分州的使用者可以拒絕出售或分享個人資訊。兩種情況都可以隨時在本 App 的<strong>設定 → 廣告隱私權設定</strong>中變更。</li>'
                '<li>如果無法確認同意或你不允許追蹤，本 App 只會請求非個人化廣告。</li></ul>',
            ]),
            ('5. 提醒、小工具與評分請求', ['<p>紀念日提醒以裝置本機通知的方式排程，不會傳送到外部。只有在你開啟提醒時才會要求通知權限，你可以隨時在手機設定中關閉。主畫面與鎖定畫面小工具只顯示裝置上的紀念日資訊。本 App 可能會顯示 App Store 或 Google Play 的評分視窗，評分與評論會直接送到 Apple 或 Google。</p>']),
            ('6. 保存與刪除', ['<p>當你刪除紀念日與照片或刪除本 App 時，裝置上儲存的資訊會一併刪除。你匯出的備份檔需要在儲存的位置自行刪除。我們不另外保存任何資訊。第三方（Google、應用程式商店）蒐集的資訊保存期間依其政策為準。</p>']),
            ('7. 兒童的個人資訊', ['<p>本 App 並非主要以未滿 13 歲（韓國為未滿 14 歲）的兒童為對象，也不會刻意蒐集兒童的個人資訊。</p>']),
            ('8. 你的權利', ['<p>本 App 儲存的資訊都在你的裝置上，你可以直接在 App 中查看、修改與刪除。對於廣告相關資訊，你可以依第 4 條的方法拒絕個人化廣告。</p>']),
            ('9. 聯絡方式', [f'<p>個人資料保護負責人：BySide（내곁의）開發者<br>電子郵件：{E}</p>']),
            ('10. 政策變更', ['<p>本政策如有變更，我們會在本頁面公告並註明生效日期。本政策以韓文版為準，譯文與韓文版意思不一致時，以韓文版為準。</p>']),
        ]),
    }
    t, d, intro, sections = data[lang]
    return {'title': t, 'date': d, 'intro': intro, 'sections': sections}


SUPPORT = {
    'ko': {
        'title': '내곁의 디데이 고객 지원', 'intro': '궁금한 점이나 불편한 점은 아래 메일로 보내 주세요. 보통 2일 안에 답장드려요.', 'contact': '문의',
        'hint': '앱 버전, 기기 종류, 어떤 화면에서 무엇을 했는지 적어 주시면 더 빨리 도와드릴 수 있어요.', 'faq_h': '자주 묻는 질문',
        'faq': [
            ('광고 제거는 구독인가요?', '아니요. 광고 제거는 <strong>한 번 구매하면 평생</strong> 가는 상품이에요. 자동 결제나 갱신이 없어서 해지할 필요도 없어요.'),
            ('폰을 바꾸거나 앱을 다시 설치했더니 광고가 다시 보여요.', '같은 Apple ID·Google 계정으로 로그인한 뒤 앱의 <strong>설정 → 광고 제거 → 구매 복원</strong>을 눌러 주세요.'),
            ('쿠폰 코드는 어디에 넣나요?', '앱의 <strong>설정 → 쿠폰</strong>을 누르면 스토어의 코드 입력 화면이 열려요. 입력한 뒤 앱으로 돌아오면 광고가 사라져요.'),
            ('폰을 바꾸면 디데이가 사라지나요?', '디데이는 폰 안에만 저장돼요. 바꾸기 전에 <strong>설정 → 백업 파일 내보내기</strong>로 파일을 만들어 메일·클라우드 드라이브 등에 보관하고, 새 폰에서 <strong>백업 파일 불러오기</strong>를 하면 디데이에 넣은 사진까지 그대로 옮겨져요.'),
            ('알림이 오지 않아요.', "휴대폰 설정에서 '내곁의 디데이' 알림이 허용돼 있는지 확인해 주세요. 디데이마다 당일 알림·미리 알림이 켜져 있어야 해요. 알림 시각은 앱 설정에서 바꿀 수 있고, 휴대폰이 배터리를 아끼는 중이면 조금 늦게 올 수 있어요."),
            ('홈 화면 위젯은 어떻게 추가하나요?', "아이폰: 홈 화면 빈 곳을 길게 누르고 → 편집 → 위젯 추가 → '내곁의 디데이'<br>Android: 홈 화면 빈 곳을 길게 누르고 → 위젯 → '내곁의 디데이'"),
            ('음력 생일은 어떻게 계산되나요?', '한국천문연구원 기준 음력을 써요. 윤달 생일인데 그해에 그 윤달이 없으면 평달로, 30일인데 그달이 29일까지면 29일로 맞춰요.'),
        ],
    },
    'en': {
        'title': 'BySide D-Day Support', 'intro': 'If you have a question or a problem, email us. We usually reply within 2 days.', 'contact': 'Contact',
        'hint': 'Including your app version, device model, and what you did on which screen helps us help you faster.', 'faq_h': 'FAQ',
        'faq': [
            ('Is Remove ads a subscription?', 'No. Remove ads is a <strong>one-time purchase that lasts for life</strong>. There are no recurring charges, so there is nothing to cancel.'),
            ('Ads came back after I switched phones or reinstalled the app.', 'Sign in with the same Apple ID or Google account, then tap <strong>Settings → Remove ads → Restore purchase</strong> in the app.'),
            ('Where do I enter a coupon code?', 'Tap <strong>Settings → Coupon</strong> in the app to open the store\'s code screen. After you enter it and come back to the app, the ads go away.'),
            ('Will my D-Days disappear if I switch phones?', 'D-Days are stored only on your phone. Before switching, use <strong>Settings → Export backup file</strong> and keep the file in email or a cloud drive. On the new phone, use <strong>Import backup file</strong> to bring everything over, including the photos you added.'),
            ("I'm not getting reminders.", "Check that notifications for BySide D-Day are allowed in your phone's settings, and that each D-Day has its day-of or advance reminder turned on. You can change the reminder time in the app's settings. If your phone is saving battery, reminders may arrive a little late."),
            ('How do I add a Home Screen widget?', 'iPhone: touch and hold an empty area of the Home Screen → Edit → Add Widget → BySide D-Day<br>Android: touch and hold an empty area of the Home Screen → Widgets → BySide D-Day'),
            ('How are lunar birthdays calculated?', 'The App uses the lunar calendar published by the Korea Astronomy and Space Science Institute. If a leap-month birthday has no leap month that year, the regular month is used, and a 30th falls back to the 29th in a 29-day month.'),
        ],
    },
    'ja': {
        'title': 'BySide D-Day サポート', 'intro': 'ご不明な点やお困りのことがあれば、下記のメールアドレスまでお送りください。通常2日以内にお返事します。', 'contact': 'お問い合わせ',
        'hint': 'アプリのバージョン、端末の機種、どの画面で何をしたかを書いていただくと、より早くご案内できます。', 'faq_h': 'よくある質問',
        'faq': [
            ('広告の削除はサブスクリプションですか？', 'いいえ。広告の削除は<strong>一度購入すればずっと使える</strong>買い切りの商品です。自動課金や更新はないため、解約の必要もありません。'),
            ('機種変更や再インストールをしたら、また広告が表示されます。', '同じ Apple ID・Google アカウントでログインしたうえで、アプリの<strong>設定 → 広告の削除 → 購入を復元</strong>を押してください。'),
            ('クーポンコードはどこに入力しますか？', 'アプリの<strong>設定 → クーポン</strong>を押すと、ストアのコード入力画面が開きます。入力してアプリに戻ると、広告が消えます。'),
            ('機種変更すると記念日は消えますか？', '記念日は端末の中にだけ保存されます。機種変更の前に<strong>設定 → バックアップファイルを書き出す</strong>でファイルを作り、メールやクラウドドライブに保管してください。新しい端末で<strong>バックアップファイルを読み込む</strong>を行えば、記念日に設定した写真までそのまま移せます。'),
            ('通知が届きません。', '端末の設定で「BySide D-Day」の通知が許可されているか確認してください。記念日ごとに当日の通知・事前の通知がオンになっている必要があります。通知の時刻はアプリの設定で変更でき、端末が省電力中の場合は少し遅れて届くことがあります。'),
            ('ホーム画面ウィジェットはどう追加しますか？', 'iPhone：ホーム画面の空いている場所を長押し → 編集 → ウィジェットを追加 →「BySide D-Day」<br>Android：ホーム画面の空いている場所を長押し → ウィジェット →「BySide D-Day」'),
            ('旧暦の誕生日はどう計算されますか？', '韓国天文研究院の旧暦を使用しています。閏月の誕生日でその年に閏月がない場合は通常の月に、30日生まれでその月が29日までの場合は29日に合わせます。'),
        ],
    },
    'zh-hans': {
        'title': 'BySide D-Day 客户支持', 'intro': '如有疑问或遇到问题，请发邮件到下方地址。我们通常会在 2 天内回复。', 'contact': '联系我们',
        'hint': '写明应用版本、设备型号以及在哪个页面做了什么，我们能更快帮到你。', 'faq_h': '常见问题',
        'faq': [
            ('移除广告是订阅吗？', '不是。移除广告是<strong>一次购买、永久有效</strong>的项目，没有自动续费，也不需要取消。'),
            ('换了手机或重新安装后，广告又出现了。', '请用同一个 Apple ID 或 Google 账号登录，然后在应用中点按<strong>设置 → 移除广告 → 恢复购买</strong>。'),
            ('兑换码在哪里输入？', '在应用中点按<strong>设置 → 兑换码</strong>，会打开商店的兑换码输入页面。输入后回到应用，广告就会消失。'),
            ('换手机后纪念日会消失吗？', '纪念日只保存在手机上。换手机前，请用<strong>设置 → 导出备份文件</strong>生成文件，保存到邮箱或云盘；在新手机上用<strong>导入备份文件</strong>，连同你添加的照片都能完整迁移。'),
            ('收不到提醒。', '请在手机设置中确认已允许“BySide D-Day”的通知，并确认每个纪念日都开启了当天提醒或提前提醒。提醒时间可以在应用设置中更改；手机处于省电状态时，提醒可能会稍晚送达。'),
            ('怎样添加主屏幕小组件？', 'iPhone：长按主屏幕空白处 → 编辑 → 添加小组件 →“BySide D-Day”<br>Android：长按主屏幕空白处 → 小组件 →“BySide D-Day”'),
            ('农历生日是怎么计算的？', '使用韩国天文研究院发布的农历。闰月生日如果当年没有该闰月，按平月计算；30 日出生而当月只有 29 天时，按 29 日计算。'),
        ],
    },
    'zh-hant': {
        'title': 'BySide D-Day 客戶支援', 'intro': '如有疑問或遇到問題，請寄信到下方地址。我們通常會在 2 天內回覆。', 'contact': '聯絡我們',
        'hint': '寫明 App 版本、裝置型號以及在哪個頁面做了什麼，我們能更快協助你。', 'faq_h': '常見問題',
        'faq': [
            ('移除廣告是訂閱嗎？', '不是。移除廣告是<strong>一次購買、永久有效</strong>的項目，沒有自動續訂，也不需要取消。'),
            ('換了手機或重新安裝後，廣告又出現了。', '請用同一個 Apple ID 或 Google 帳戶登入，然後在 App 中點一下<strong>設定 → 移除廣告 → 恢復購買</strong>。'),
            ('兌換碼在哪裡輸入？', '在 App 中點一下<strong>設定 → 兌換碼</strong>，會開啟商店的兌換碼輸入畫面。輸入後回到 App，廣告就會消失。'),
            ('換手機後紀念日會不見嗎？', '紀念日只儲存在手機上。換手機前，請用<strong>設定 → 匯出備份檔案</strong>產生檔案，存到電子郵件或雲端硬碟；在新手機上用<strong>匯入備份檔案</strong>，連同你加入的照片都能完整搬移。'),
            ('收不到提醒。', '請在手機設定中確認已允許「BySide D-Day」的通知，並確認每個紀念日都開啟了當天提醒或提前提醒。提醒時間可以在 App 設定中變更；手機處於省電狀態時，提醒可能會稍晚送達。'),
            ('怎麼新增主畫面小工具？', 'iPhone：長按主畫面空白處 → 編輯 → 加入小工具 →「BySide D-Day」<br>Android：長按主畫面空白處 → 小工具 →「BySide D-Day」'),
            ('農曆生日是怎麼計算的？', '使用韓國天文研究院發布的農曆。閏月生日如果當年沒有該閏月，會以平月計算；30 日出生而當月只有 29 天時，會以 29 日計算。'),
        ],
    },
}
