"""개인정보처리방침(5개 언어). 각 항목은 (제목, HTML 본문)."""

E = '<a href="mailto:ekqlszzzz@naver.com">ekqlszzzz@naver.com</a>'
API = '<a href="https://www.exchangerate-api.com">exchangerate-api.com</a>'

PRIVACY = {
    'ko': {
        'title': '내곁의 여비 개인정보처리방침',
        'date': '시행일: 2026년 10월 9일',
        'intro': "'내곁의 여비'(이하 \"앱\", Android·iOS)는 이용자의 개인정보를 소중히 다루며, 「개인정보 보호법」 등 관련 법령을 지킵니다. 이 방침은 앱이 어떤 정보를 어떻게 다루는지 설명합니다.",
        'sections': [
            ('1. 앱이 직접 수집하는 정보', [
                '<p>앱은 회원가입이나 로그인이 없으며, 운영자가 운영하는 서버가 없어 이용자의 정보를 운영자에게 보내지 않습니다.</p>',
                '<p>이용자가 고른 통화 설정(내 나라 통화, 여행지 통화, 환율 목록), 지출 기록(금액, 통화, 분류, 결제 수단, 메모, 기록 시각), 환전 기록, 화면 테마·언어 설정, 마지막으로 받은 환율은 <strong>이용자의 기기 안에만 저장</strong>됩니다. 운영자는 이 내용을 볼 수 없습니다.</p>',
                '<p>처음 실행할 때 기본 통화와 언어를 정하기 위해 기기의 지역·언어 설정을 기기 안에서 읽습니다. 이 정보는 앱이 외부로 보내지 않습니다.</p>',
                '<p>휴대폰 자체 백업(iCloud, Google 계정 백업 등)을 켜 두었다면 운영체제가 다른 앱 데이터와 함께 이 앱의 데이터를 백업할 수 있습니다. 이 백업은 이용자와 Apple·Google 사이의 서비스이며 운영자는 접근할 수 없습니다.</p>',
            ]),
            ('2. 백업 파일·내보내기·공유', [
                '<p>이용자가 직접 <strong>백업 파일 내보내기</strong>(JSON)나 <strong>엑셀(CSV)로 내보내기</strong>, <strong>지출 내역 공유하기</strong>를 누르면 기기의 공유 창이 열리고, 파일이나 글을 보낼 곳(메신저, 드라이브, 파일 앱 등)은 이용자가 고릅니다. <strong>백업 불러오기</strong>는 이용자가 고른 파일 하나만 읽습니다. 이 과정에서 운영자에게 전송되는 정보는 없으며, 보낸 곳에서의 처리는 해당 서비스의 방침을 따릅니다.</p>',
            ]),
            ('3. 환율 정보 받기', [
                f'<p>앱은 최신 환율을 받기 위해 대략 하루 한 번 ExchangeRate-API({API})의 공개 주소(open.er-api.com)에 환율을 요청합니다. 이 요청에는 이용자가 입력한 금액이나 기록 등 개인정보가 들어가지 않습니다. 다만 일반적인 인터넷 요청과 마찬가지로 제공자는 요청을 보낸 기기의 IP 주소를 알 수 있습니다. 인터넷이 없으면 앱에 넣어 두었거나 마지막으로 받은 환율로 계산합니다.</p>',
            ]),
            ('4. 광고·분석·추적', [
                '<p>현재 버전의 앱에는 광고, 분석, 추적 SDK가 들어 있지 않습니다. 광고 식별자(Android 광고 ID, iOS IDFA)를 읽지 않으며, 다른 회사의 앱·웹사이트에 걸친 추적을 하지 않습니다. 앞으로 광고를 넣게 되면 시행 전에 이 방침을 고쳐 알리고, 필요한 동의를 받습니다.</p>',
            ]),
            ('5. 위젯·리뷰 요청', [
                '<ul><li>iOS 홈·잠금 화면 위젯(여행 위젯, 환율 위젯)을 쓰면, 앱이 이번 여행 합계·오늘 쓴 돈·환율 같은 표시용 값을 같은 기기의 위젯과 함께 쓰는 저장 공간(App Group)에 저장합니다. 위젯 편집에서 고른 통화와 배경색도 기기에만 저장됩니다. 이 값들은 기기 밖으로 나가지 않습니다.</li>'
                '<li>앱은 지출을 몇 번 기록한 뒤 App Store·Google Play의 평점 창을 한 번 띄울 수 있고, 설정의 \'리뷰 남기기\'로 스토어 리뷰 페이지를 엽니다. 평점과 리뷰는 Apple·Google에 직접 남기며, 운영자는 그 내용을 앱으로 받지 않습니다.</li></ul>',
            ]),
            ('6. 기기 권한', [
                '<p>앱은 카메라, 위치, 연락처, 사진, 마이크, 알림 권한을 사용하지 않습니다. Android에서는 인터넷(환율 받기)과 진동(버튼을 누를 때의 가벼운 진동) 권한만 선언되어 있습니다. iOS에서는 따로 묻는 권한이 없습니다.</p>',
            ]),
            ('7. 개인정보의 처리 목적·제3자 제공·처리 위탁', [
                '<p>운영자는 이용자의 개인정보를 수집하지 않으므로 이를 제3자에게 제공하거나 처리를 위탁하지 않습니다.</p>',
            ]),
            ('8. 보관 및 파기', [
                '<p>기기에 저장된 정보는 이용자가 앱에서 지출·환전 기록을 지우거나 앱을 삭제하면 함께 지워집니다. 이용자가 내보낸 백업·CSV 파일은 이용자가 보관한 곳에서 직접 지워야 합니다. 운영자가 따로 보관하는 정보는 없습니다. 환율 제공자(ExchangeRate-API)가 받은 요청 정보의 보관 기간은 해당 회사의 방침을 따릅니다.</p>',
            ]),
            ('9. 아동의 개인정보', [
                '<p>앱은 만 14세 미만 아동(해외는 만 13세 미만)을 주 대상으로 하지 않으며, 아동의 개인정보를 의도적으로 수집하지 않습니다.</p>',
            ]),
            ('10. 이용자의 권리', [
                '<p>앱에 저장된 정보는 모두 이용자의 기기에 있으므로 이용자가 앱에서 직접 열람·수정·삭제할 수 있습니다. 그 밖의 요청은 아래 연락처로 보내 주세요.</p>',
            ]),
            ('11. 개인정보 보호책임자·문의', [
                f'<p>개인정보 보호책임자: 내곁의 운영자<br>연락처: {E}</p>',
            ]),
            ('12. 방침의 변경', [
                '<p>이 방침이 바뀌면 이 페이지에 시행일과 함께 알립니다. 이 방침은 한국어 원문을 기준으로 하며, 다른 언어판과 뜻이 다르면 한국어판을 따릅니다.</p>',
            ]),
        ],
    },
    'en': {
        'title': 'BySide Trip Privacy Policy',
        'date': 'Effective date: October 9, 2026',
        'intro': 'BySide Trip (내곁의 여비, the "App", for Android and iOS) respects your privacy. This policy explains what information the App handles and how.',
        'sections': [
            ('1. Information the App collects', [
                '<p>The App has no sign-up or login, and we do not run a server for it, so your information is never sent to us.</p>',
                '<p>Your currency settings (home currency, trip currency, currency list), expenses (amount, currency, category, payment method, memo, time recorded), cash exchanges, theme and language settings, and the most recently downloaded exchange rates are <strong>stored only on your device</strong>. We cannot see them.</p>',
                "<p>On first launch, the App reads your device's region and language settings on the device to choose a default currency and language. The App does not send this anywhere.</p>",
                "<p>If you have turned on your phone's own backup (such as iCloud or Google account backup), the operating system may back up this App's data along with other app data. That backup is a service between you and Apple or Google, and we have no access to it.</p>",
            ]),
            ('2. Backup files, export, and sharing', [
                "<p>When you tap <strong>Export backup file</strong> (JSON), <strong>Export to Excel (CSV)</strong>, or <strong>Share expenses</strong>, your device's share sheet opens and you choose where the file or text goes (a messenger, a cloud drive, the Files app, and so on). <strong>Import backup</strong> reads only the one file you pick. Nothing is sent to us in this process, and wherever you send it handles it under its own policy.</p>",
            ]),
            ('3. Exchange rates', [
                f"<p>To get current exchange rates, the App requests rates from ExchangeRate-API's open endpoint (open.er-api.com, {API}) about once a day. The request contains no personal information such as amounts or records you entered. As with any web request, the provider can see your device's IP address. Without an internet connection, the App uses the rates bundled with the App or the last rates it downloaded.</p>",
            ]),
            ('4. Advertising, analytics, and tracking', [
                "<p>The current version of the App includes no advertising, analytics, or tracking SDKs. It does not read advertising identifiers (the Android Advertising ID or the iOS IDFA) and does not track you across other companies' apps or websites. If we add advertising in the future, we will update this policy before it takes effect and ask for any consent that is required.</p>",
            ]),
            ('5. Widgets and review requests', [
                "<ul><li>If you use the iOS Home Screen or Lock Screen widgets (the trip widget and the rates widget), the App saves display values such as this trip's total, today's spending, and rates to storage shared with the widgets on the same device (an App Group). The currencies and background colors you choose when editing a widget are also stored only on your device. These values never leave your device.</li>"
                "<li>After you log a few expenses, the App may show the App Store or Google Play rating prompt once, and <strong>Settings → Write a review</strong> opens the store's review page. Ratings and reviews go directly to Apple or Google, and we do not receive them through the App.</li></ul>",
            ]),
            ('6. Device permissions', [
                '<p>The App does not use the camera, location, contacts, photos, microphone, or notifications. On Android it declares only internet access (to download rates) and vibration (a light tap when you press buttons). On iOS it asks for no permissions.</p>',
            ]),
            ('7. Purpose of processing, sharing, and processors', [
                '<p>We do not collect your personal information, so we do not share it with or entrust its processing to anyone.</p>',
            ]),
            ('8. Retention and deletion', [
                '<p>Data on your device is deleted when you delete expense or exchange records in the App or uninstall the App. Backup and CSV files you exported must be deleted from wherever you saved them. We do not keep any copy. Request information received by the rate provider (ExchangeRate-API) is retained according to its policy.</p>',
            ]),
            ('9. Children', [
                "<p>The App is not directed at children under 14 in Korea or under 13 elsewhere, and does not knowingly collect children's personal information.</p>",
            ]),
            ('10. Your rights', [
                '<p>All information stored by the App is on your device, so you can view, edit, and delete it directly in the App. For any other request, contact us below.</p>',
            ]),
            ('11. Privacy contact', [
                f'<p>Privacy officer: BySide (내곁의) developer<br>Email: {E}</p>',
            ]),
            ('12. Changes to this policy', [
                '<p>If this policy changes, we will post the update on this page with a new effective date. The Korean version of this policy is the original; if a translation differs in meaning, the Korean version prevails.</p>',
            ]),
        ],
    },
    'ja': {
        'title': 'BySide 旅行 プライバシーポリシー',
        'date': '施行日：2026年10月9日',
        'intro': '「BySide 旅行」（韓国語名「내곁의 여비」、以下「本アプリ」、Android・iOS）は、利用者のプライバシーを大切にしています。このポリシーでは、本アプリがどのような情報をどのように扱うかを説明します。',
        'sections': [
            ('1. 本アプリが扱う情報', [
                '<p>本アプリにはアカウント登録やログインがなく、運営者のサーバーもないため、利用者の情報が運営者に送られることはありません。</p>',
                '<p>利用者が選んだ通貨の設定（自分の通貨、旅行先の通貨、為替リスト）、支出の記録（金額、通貨、分類、支払い方法、メモ、記録時刻）、両替の記録、テーマ・言語の設定、最後に受け取った為替レートは、<strong>利用者の端末の中にだけ保存</strong>されます。運営者はこれらを見ることができません。</p>',
                '<p>初回起動時、既定の通貨と言語を決めるために端末の地域・言語設定を端末内で読み取ります。この情報を本アプリが外部に送ることはありません。</p>',
                '<p>端末自体のバックアップ（iCloud、Google アカウントのバックアップなど）を有効にしている場合、OS がほかのアプリのデータと一緒に本アプリのデータをバックアップすることがあります。このバックアップは利用者と Apple・Google との間のサービスであり、運営者はアクセスできません。</p>',
            ]),
            ('2. バックアップファイル・書き出し・共有', [
                '<p>利用者が<strong>バックアップファイルを書き出す</strong>（JSON）、<strong>Excel（CSV）で書き出す</strong>、<strong>支出の履歴を共有</strong>を押すと端末の共有シートが開き、ファイルや文章の送り先（メッセージアプリ、クラウドドライブ、ファイルアプリなど）は利用者が選びます。<strong>バックアップを読み込む</strong>では、利用者が選んだファイルひとつだけを読み込みます。この過程で運営者に送られる情報はなく、送り先での取り扱いはそのサービスのポリシーに従います。</p>',
            ]),
            ('3. 為替レートの取得', [
                f'<p>本アプリは最新の為替レートを取得するため、おおむね1日1回 ExchangeRate-API（{API}）の公開アドレス（open.er-api.com）にレートを問い合わせます。この問い合わせには、利用者が入力した金額や記録などの個人情報は含まれません。ただし一般的なインターネット通信と同様に、提供元は問い合わせた端末の IP アドレスを知ることができます。インターネットに接続していないときは、アプリに内蔵されたレートまたは最後に受け取ったレートで換算します。</p>',
            ]),
            ('4. 広告・分析・トラッキング', [
                '<p>現在のバージョンの本アプリには、広告・分析・トラッキングの SDK は含まれていません。広告識別子（Android の広告 ID、iOS の IDFA）を読み取らず、ほかの企業のアプリやウェブサイトをまたいだトラッキングも行いません。今後広告を導入する場合は、実施前にこのポリシーを改定してお知らせし、必要な同意をいただきます。</p>',
            ]),
            ('5. ウィジェット・レビューのお願い', [
                '<ul><li>iOS のホーム画面・ロック画面ウィジェット（旅行ウィジェット、レートウィジェット）を使う場合、本アプリは今回の旅行の合計・今日使ったお金・レートなどの表示用の値を、同じ端末のウィジェットと共有する保存領域（App Group）に保存します。ウィジェットの編集で選んだ通貨と背景色も端末にだけ保存されます。これらの値が端末の外に出ることはありません。</li>'
                '<li>本アプリは支出を何回か記録したあと、App Store・Google Play の評価画面を一度表示することがあります。また、設定の「レビューを書く」でストアのレビューページを開きます。評価やレビューは Apple・Google に直接送られ、運営者が本アプリを通じて受け取ることはありません。</li></ul>',
            ]),
            ('6. 端末の権限', [
                '<p>本アプリはカメラ、位置情報、連絡先、写真、マイク、通知の権限を使用しません。Android ではインターネット（レートの取得）と振動（ボタンを押したときの軽い振動）の権限だけを宣言しています。iOS では許可を求める権限はありません。</p>',
            ]),
            ('7. 利用目的・第三者提供・委託', [
                '<p>運営者は利用者の個人情報を収集しないため、第三者に提供したり、取り扱いを委託したりすることはありません。</p>',
            ]),
            ('8. 保存期間と削除', [
                '<p>端末に保存された情報は、利用者が本アプリで支出・両替の記録を削除するか、本アプリを削除すると一緒に削除されます。利用者が書き出したバックアップ・CSV ファイルは、保存した場所から利用者自身が削除してください。運営者が別に保管している情報はありません。レート提供元（ExchangeRate-API）が受け取った問い合わせ情報の保存期間は、同社のポリシーに従います。</p>',
            ]),
            ('9. 子どもの個人情報', [
                '<p>本アプリは13歳未満（韓国では14歳未満）の子どもを主な対象としておらず、子どもの個人情報を意図的に収集することはありません。</p>',
            ]),
            ('10. 利用者の権利', [
                '<p>本アプリが保存する情報はすべて利用者の端末にあるため、利用者が本アプリで直接閲覧・修正・削除できます。そのほかのご要望は下記の連絡先までお送りください。</p>',
            ]),
            ('11. お問い合わせ窓口', [
                f'<p>個人情報保護責任者：BySide（내곁의）運営者<br>メール：{E}</p>',
            ]),
            ('12. ポリシーの変更', [
                '<p>このポリシーを変更する場合は、施行日とともにこのページでお知らせします。このポリシーは韓国語版を原文とし、翻訳版と意味が異なる場合は韓国語版が優先されます。</p>',
            ]),
        ],
    },
    'zh-hans': {
        'title': 'BySide 旅行 隐私政策',
        'date': '生效日期：2026年10月9日',
        'intro': '“BySide 旅行”（韩文名“내곁의 여비”，以下简称“本应用”，适用于 Android 和 iOS）重视你的隐私。本政策说明本应用处理哪些信息以及如何处理。',
        'sections': [
            ('1. 本应用处理的信息', [
                '<p>本应用无需注册或登录，开发者也没有为其运营服务器，因此你的信息不会发送给我们。</p>',
                '<p>你选择的货币设置（你的货币、旅行地货币、汇率列表）、支出记录（金额、货币、分类、支付方式、备注、记录时间）、兑换记录、主题和语言设置，以及最后一次获取的汇率，<strong>只保存在你的设备上</strong>。我们无法查看这些内容。</p>',
                '<p>首次打开时，本应用会在设备上读取地区和语言设置，用来决定默认货币和语言。本应用不会把这些信息发送到任何地方。</p>',
                '<p>如果你开启了手机自带的备份（如 iCloud、Google 账号备份），操作系统可能会把本应用的数据和其他应用数据一起备份。该备份是你与 Apple 或 Google 之间的服务，我们无法访问。</p>',
            ]),
            ('2. 备份文件、导出和分享', [
                '<p>当你点按<strong>导出备份文件</strong>（JSON）、<strong>导出为 Excel（CSV）</strong>或<strong>分享支出明细</strong>时，设备会打开分享面板，由你选择文件或文字的去处（聊天应用、云盘、“文件”应用等）。<strong>导入备份</strong>只读取你选择的那一个文件。此过程中不会向我们发送任何信息，接收方如何处理以其自身政策为准。</p>',
            ]),
            ('3. 获取汇率', [
                f'<p>为获取最新汇率，本应用大约每天一次向 ExchangeRate-API（{API}）的公开地址（open.er-api.com）请求汇率。该请求不包含你输入的金额或记录等个人信息。不过与一般网络请求一样，提供方可以看到发出请求的设备的 IP 地址。没有网络时，本应用使用内置的汇率或最后一次获取的汇率进行换算。</p>',
            ]),
            ('4. 广告、分析与追踪', [
                '<p>当前版本的本应用不包含广告、分析或追踪 SDK，不读取广告标识符（Android 广告 ID、iOS IDFA），也不会跨其他公司的应用或网站追踪你。如果今后加入广告，我们会在生效前修改并公布本政策，并征得必要的同意。</p>',
            ]),
            ('5. 小组件与评分请求', [
                '<ul><li>使用 iOS 主屏幕或锁定屏幕小组件（旅行小组件、汇率小组件）时，本应用会把本次旅行合计、今天的花费、汇率等用于显示的数值，保存到同一设备上与小组件共享的存储空间（App Group）。你在编辑小组件时选择的货币和背景颜色也只保存在设备上。这些数值不会离开你的设备。</li>'
                '<li>记录几次支出后，本应用可能会显示一次 App Store 或 Google Play 的评分窗口；设置中的“写评论”会打开商店的评论页面。评分和评论直接提交给 Apple 或 Google，我们不会通过本应用接收。</li></ul>',
            ]),
            ('6. 设备权限', [
                '<p>本应用不使用相机、位置、通讯录、照片、麦克风或通知权限。在 Android 上只声明了网络（获取汇率）和振动（按下按钮时的轻微振动）权限。在 iOS 上不会请求任何权限。</p>',
            ]),
            ('7. 处理目的、向第三方提供与委托处理', [
                '<p>我们不收集你的个人信息，因此不会向第三方提供，也不会委托他人处理。</p>',
            ]),
            ('8. 保存与删除', [
                '<p>当你在本应用中删除支出或兑换记录，或卸载本应用时，设备上保存的信息会一并删除。你导出的备份文件和 CSV 文件需要在保存的位置自行删除。我们不另行保存任何信息。汇率提供方（ExchangeRate-API）收到的请求信息的保存期限以其政策为准。</p>',
            ]),
            ('9. 儿童的个人信息', [
                '<p>本应用并非主要面向未满 13 岁（韩国为未满 14 岁）的儿童，也不会有意收集儿童的个人信息。</p>',
            ]),
            ('10. 你的权利', [
                '<p>本应用保存的信息都在你的设备上，你可以直接在应用中查看、修改和删除。其他请求请通过下方联系方式发送给我们。</p>',
            ]),
            ('11. 联系方式', [
                f'<p>个人信息保护负责人：BySide（내곁의）开发者<br>邮箱：{E}</p>',
            ]),
            ('12. 政策变更', [
                '<p>本政策如有变更，我们会在本页面公布并注明生效日期。本政策以韩文版为准，译文与韩文版含义不一致时，以韩文版为准。</p>',
            ]),
        ],
    },
    'zh-hant': {
        'title': 'BySide 旅行 隱私權政策',
        'date': '生效日期：2026年10月9日',
        'intro': '「BySide 旅行」（韓文名「내곁의 여비」，以下簡稱「本 App」，適用於 Android 與 iOS）重視你的隱私。本政策說明本 App 處理哪些資訊以及如何處理。',
        'sections': [
            ('1. 本 App 處理的資訊', [
                '<p>本 App 不需註冊或登入，開發者也沒有為其經營伺服器，因此你的資訊不會傳送給我們。</p>',
                '<p>你選擇的貨幣設定（你的貨幣、旅行地貨幣、匯率清單）、支出記錄（金額、貨幣、分類、付款方式、備註、記錄時間）、換匯記錄、主題與語言設定，以及最後一次取得的匯率，<strong>只儲存在你的裝置上</strong>。我們無法查看這些內容。</p>',
                '<p>第一次開啟時，本 App 會在裝置上讀取地區與語言設定，用來決定預設貨幣和語言。本 App 不會把這些資訊傳送到任何地方。</p>',
                '<p>如果你開啟了手機本身的備份（如 iCloud、Google 帳戶備份），作業系統可能會把本 App 的資料與其他 App 資料一起備份。該備份是你與 Apple 或 Google 之間的服務，我們無法存取。</p>',
            ]),
            ('2. 備份檔案、匯出與分享', [
                '<p>當你點一下<strong>匯出備份檔案</strong>（JSON）、<strong>匯出為 Excel（CSV）</strong>或<strong>分享支出明細</strong>時，裝置會打開分享選單，由你選擇檔案或文字的去處（通訊 App、雲端硬碟、「檔案」App 等）。<strong>匯入備份</strong>只會讀取你選擇的那一個檔案。過程中不會傳送任何資訊給我們，接收方如何處理以其自身政策為準。</p>',
            ]),
            ('3. 取得匯率', [
                f'<p>為取得最新匯率，本 App 大約每天一次向 ExchangeRate-API（{API}）的公開位址（open.er-api.com）請求匯率。此請求不包含你輸入的金額或記錄等個人資訊。不過與一般網路請求相同，提供者可以看到發出請求的裝置 IP 位址。沒有網路時，本 App 會使用內建的匯率或最後一次取得的匯率換算。</p>',
            ]),
            ('4. 廣告、分析與追蹤', [
                '<p>目前版本的本 App 不包含廣告、分析或追蹤 SDK，不讀取廣告識別碼（Android 廣告 ID、iOS IDFA），也不會跨其他公司的 App 或網站追蹤你。若日後加入廣告，我們會在實施前修改並公告本政策，並取得必要的同意。</p>',
            ]),
            ('5. 小工具與評分請求', [
                '<ul><li>使用 iOS 主畫面或鎖定畫面小工具（旅行小工具、匯率小工具）時，本 App 會把本次旅行合計、今天的花費、匯率等顯示用的數值，儲存在同一台裝置上與小工具共用的儲存空間（App Group）。你在編輯小工具時選擇的貨幣與背景顏色也只儲存在裝置上。這些數值不會離開你的裝置。</li>'
                '<li>記錄幾次支出後，本 App 可能會顯示一次 App Store 或 Google Play 的評分視窗；設定中的「撰寫評論」會開啟商店的評論頁面。評分與評論會直接送到 Apple 或 Google，我們不會透過本 App 收到。</li></ul>',
            ]),
            ('6. 裝置權限', [
                '<p>本 App 不使用相機、位置、聯絡人、照片、麥克風或通知權限。在 Android 上只宣告了網路（取得匯率）與震動（按下按鈕時的輕微震動）權限。在 iOS 上不會要求任何權限。</p>',
            ]),
            ('7. 處理目的、提供第三方與委託處理', [
                '<p>我們不蒐集你的個人資訊，因此不會提供給第三方，也不會委託他人處理。</p>',
            ]),
            ('8. 保存與刪除', [
                '<p>當你在本 App 中刪除支出或換匯記錄，或刪除本 App 時，裝置上儲存的資訊會一併刪除。你匯出的備份檔與 CSV 檔需要在儲存的位置自行刪除。我們不另外保存任何資訊。匯率提供者（ExchangeRate-API）收到的請求資訊保存期間依其政策為準。</p>',
            ]),
            ('9. 兒童的個人資訊', [
                '<p>本 App 並非主要以未滿 13 歲（韓國為未滿 14 歲）的兒童為對象，也不會刻意蒐集兒童的個人資訊。</p>',
            ]),
            ('10. 你的權利', [
                '<p>本 App 儲存的資訊都在你的裝置上，你可以直接在 App 中查看、修改與刪除。其他請求請透過下方聯絡方式寄給我們。</p>',
            ]),
            ('11. 聯絡方式', [
                f'<p>個人資料保護負責人：BySide（내곁의）開發者<br>電子郵件：{E}</p>',
            ]),
            ('12. 政策變更', [
                '<p>本政策如有變更，我們會在本頁面公告並註明生效日期。本政策以韓文版為準，譯文與韓文版意思不一致時，以韓文版為準。</p>',
            ]),
        ],
    },
}
