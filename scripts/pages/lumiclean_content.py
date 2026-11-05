"""루미클린(Lumiclean) 개인정보처리방침 문구. 한국어판이 원문이다. 고치면 시행일도 바꾼다."""

E = '<a href="mailto:ekqlszzzz@naver.com">ekqlszzzz@naver.com</a>'

NAME = {
    'ko': '루미클린',
    'en': 'Lumiclean',
    'ja': 'Lumiclean',
    'zh-hans': 'Lumiclean',
    'zh-hant': 'Lumiclean',
}


def g(lang):
    """Google 정책 링크(언어별)."""
    hl = {'ko': 'ko', 'en': 'en', 'ja': 'ja', 'zh-hans': 'zh-CN', 'zh-hant': 'zh-TW'}[lang]
    return (f'https://policies.google.com/technologies/partner-sites?hl={hl}',
            f'https://policies.google.com/privacy?hl={hl}')


APPLE = {
    'ko': 'https://www.apple.com/kr/legal/privacy/',
    'en': 'https://www.apple.com/legal/privacy/',
    'ja': 'https://www.apple.com/jp/legal/privacy/',
    'zh-hans': 'https://www.apple.com.cn/legal/privacy/',
    'zh-hant': 'https://www.apple.com/tw/legal/privacy/',
}


def rows(items):
    """[(이름, 설명)]을 휴대폰 폭에서도 읽히는 줄 목록으로 만든다."""
    body = ''.join(f'<div><dt>{t}</dt><dd>{d}</dd></div>' for t, d in items)
    return f'<dl class="rows">{body}</dl>'


def privacy(lang):
    p1, p2 = g(lang)
    apple = APPLE[lang]
    data = {
        'ko': {
            'title': '루미클린 개인정보처리방침',
            'date': '시행일: 2026년 11월 5일',
            'intro': "'루미클린'(Lumiclean, 이하 \"앱\", Android·iOS)은 이용자의 개인정보를 소중히 다루며, 「개인정보 보호법」 등 관련 법령을 지킵니다. 이 방침은 앱이 어떤 정보를 어떻게 다루는지 설명합니다.",
            'summary_h': '한눈에 보기',
            'summary': [
                '사진과 동영상 파일은 서버로 보내지 않습니다. 정리, 압축, 화질 개선은 모두 휴대폰 안에서 합니다.',
                '회원가입과 로그인이 없고, 운영자가 운영하는 서버도 없습니다.',
                'iPhone에서 사진을 크게 볼 때만 찍은 곳 이름을 알아내려고 사진의 좌표를 Apple에 보냅니다.',
                '광고는 Google AdMob이 보여 주며, 맞춤형 광고 여부는 이용자가 고를 수 있습니다.',
            ],
            'contact_h': '문의',
            'sections': [
                ('1. 앱이 직접 수집하는 정보', [
                    '<p>앱은 회원가입이나 로그인이 없으며, 운영자가 운영하는 서버가 없습니다. 이용자의 사진·동영상과 앱 사용 기록을 운영자에게 보내지 않습니다.</p>',
                    '<p>앱은 비슷한 사진, 스크린샷, 큰 파일을 찾으려고 사진 보관함을 읽습니다. 사진 분석과 압축, 화질 개선은 <strong>모두 기기 안에서</strong> 처리합니다. 화질 개선에 쓰는 인공지능 모델(Real-ESRGAN)은 앱 안에 들어 있어서 사진을 밖으로 보낼 일이 없습니다.</p>',
                    '<p>iPhone에서 화질을 높이거나 압축할 사진의 원본이 iCloud 사진에만 있으면, iOS가 이용자의 iCloud에서 원본을 내려받을 수 있습니다. 이 전송은 이용자와 Apple 사이에서 일어나며 운영자를 거치지 않습니다.</p>',
                    "<p>화질을 높인 사진과 압축한 사본은 이용자의 사진 보관함에 저장됩니다. 사진을 지울 때는 휴대폰이 확인 창을 띄우고, iOS에서는 지운 사진이 '최근 삭제된 항목'으로 옮겨집니다.</p>",
                ]),
                ('2. 사진 위치 정보', [
                    "<p>사진에는 찍은 곳의 좌표가 들어 있을 수 있습니다. iPhone에서 사진을 크게 볼 때 앱은 찍은 곳을 '서울 종로구'처럼 동네 이름으로 보여 줍니다. 이를 위해 <strong>사진의 좌표만</strong> Apple의 위치 이름 변환 서비스로 보냅니다. 사진 파일과 그 밖의 정보는 보내지 않습니다.</p>",
                    f'<p>받은 동네 이름은 같은 곳을 다시 묻지 않도록 기기 안에 최대 500개까지 저장합니다. Apple이 이 요청을 다루는 방식은 <a href="{apple}">Apple 개인정보 처리방침</a>을 따릅니다.</p>',
                    '<p>Android에서는 찍은 곳 이름을 보여 주지 않으며 좌표를 기기 밖으로 보내지 않습니다. 앱은 어느 기기에서도 이용자의 현재 위치를 묻거나 쓰지 않습니다.</p>',
                ]),
                ('3. 광고를 위해 제3자가 수집하는 정보', [
                    '<p>앱은 무료로 제공되며, 광고 표시를 위해 Google LLC의 <strong>Google AdMob</strong>을 사용합니다. AdMob은 광고 제공과 측정, 부정 사용 방지를 위해 다음 정보를 수집·처리할 수 있습니다.</p>',
                    rows([
                        ('수집 주체', 'Google LLC (AdMob)'),
                        ('항목', '광고 ID(Android 광고 ID, iOS 광고 식별자 IDFA. iOS는 이용자가 추적을 허용한 경우에만), IP 주소, 기기·운영체제 정보, 광고 노출·클릭 등 앱 이용 정보, IP로 짐작한 대략적인 위치'),
                        ('목적', '광고 표시와 맞춤형 광고, 광고 성과 측정, 부정 클릭 방지'),
                    ]),
                    f'<p>Google의 정보 처리 방식은 <a href="{p1}">Google 파트너 사이트·앱의 데이터 사용 방식</a>과 <a href="{p2}">Google 개인정보처리방침</a>에서 확인할 수 있습니다.</p>',
                    '<p>앱은 자체 앱 홍보 광고도 표시할 수 있습니다. 공개된 홍보 목록과 이미지·동영상을 boksday.github.io(GitHub Pages) (<a href="https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement">GitHub 개인정보처리방침</a>)에서 내려받아 기기에 캐시합니다. 이 요청을 처리하는 호스팅 제공자는 IP 주소와 요청 시각·요청 파일 등 요청 정보를 받을 수 있습니다. 이용자의 사진·동영상은 이 요청에 포함되지 않습니다. 홍보 광고를 누르면 외부 앱 스토어 페이지가 열립니다.</p>',
                ]),
                ('4. 맞춤형 광고 거부 방법', [
                    '<ul><li>Android: 휴대폰 <strong>설정 → Google → 광고</strong>에서 광고 ID를 삭제하거나 재설정할 수 있습니다.</li>'
                    '<li>iOS: 처음 실행할 때 추적 허용 여부를 고를 수 있으며, <strong>설정 → 개인정보 보호 및 보안 → 추적</strong>에서 언제든 바꿀 수 있습니다.</li>'
                    '<li>유럽경제지역(EEA)·영국·스위스 이용자는 처음 실행할 때 광고 개인정보 동의를 선택할 수 있습니다. 미국 일부 주의 이용자는 개인정보 판매·공유를 거부할 수 있습니다. 두 경우 모두 앱의 <strong>설정 → 광고 개인정보 설정</strong>에서 언제든 바꿀 수 있습니다.</li>'
                    '<li>동의를 확인하지 못했거나 추적을 허용하지 않은 경우 앱은 맞춤형이 아닌 광고만 요청합니다.</li></ul>',
                ]),
                ('5. 결제(프리미엄)', [
                    '<p>프리미엄 구매는 App Store 또는 Google Play가 처리합니다. 월간·연간 요금제는 해지할 때까지 자동 갱신되는 구독이며, 평생 이용권은 한 번 결제하는 상품입니다. 앱과 운영자는 카드 번호 등 결제 정보를 받지 않습니다. 앱은 스토어가 제공하는 구매·구독 정보를 확인하고, 프리미엄 이용 여부와 요금제, 만료 시각을 기기에 저장하여 이용 권한을 판단합니다.</p>',
                ]),
                ('6. 앱 잠금', [
                    '<p>앱 잠금을 켜면 앱을 열 때 Face ID, Touch ID, 지문 인식이나 기기 암호로 확인합니다. 확인은 휴대폰 운영체제가 하고, 앱은 성공했는지만 전달받습니다. 앱은 얼굴·지문 정보나 기기 암호를 읽거나 저장하지 않으며, 앱 자체 암호도 없습니다.</p>',
                ]),
                ('7. 기기 안에 저장하는 정보', [
                    '<p>앱은 다음 정보를 <strong>이용자의 기기 안에만</strong> 저장합니다. 사진 파일 자체는 들어 있지 않으며, 운영자는 이 내용을 볼 수 없습니다.</p>',
                    rows([
                        ('정리 기록', '지우려고 담아 둔 사진과 남기기로 한 사진의 식별 번호, 지운 개수와 비운 용량, 남겨 두기로 한 묶음'),
                        ('분석 결과', '사진별 파일 크기와 비슷한 사진을 찾은 결과, 압축한 사본 기록과 압축으로 줄인 용량'),
                        ('찍은 곳 이름', 'iOS만. 반올림한 좌표와 동네 이름, 최대 500개'),
                        ('설정', '앱 잠금, 화면 모드, 언어, 안내를 본 여부, 프리미엄 이용 여부, 요금제와 만료 시각'),
                    ]),
                ]),
                ('8. 접근 권한', [
                    rows([
                        ('사진·동영상', '정리할 사진 찾기, 크게 보기, 압축, 화질 개선에 씁니다. 화질을 높인 사진과 압축한 사본을 보관함에 저장할 때도 씁니다.'),
                        ('사진 속 위치 정보', 'Android만. 사진 파일에 담긴 위치 정보를 지우지 않은 채 읽기 위한 권한입니다. 이 정보를 기기 밖으로 보내지 않습니다.'),
                        ('Face ID·생체 인증', '앱 잠금을 켰을 때만 씁니다.'),
                        ('추적 허용', 'iOS만. 맞춤형 광고에 씁니다. 허용하지 않아도 앱은 똑같이 쓸 수 있습니다.'),
                        ('인터넷', '광고 표시, 자체 앱 홍보 목록·이미지·동영상 다운로드, 구매 확인, iPhone의 찍은 곳 이름 확인에 씁니다.'),
                    ]),
                    '<p>앱은 위치 권한과 마이크 권한을 요청하지 않습니다. 사진 접근 범위는 휴대폰 설정에서 언제든 바꾸거나 끌 수 있습니다.</p>',
                ]),
                ('9. 보관 및 파기', [
                    '<p>기기에 저장된 정보는 앱을 삭제하면 함께 지워집니다. 사진 보관함에 저장한 사진은 앱을 지워도 남으며, 이용자가 사진 앱에서 직접 지울 수 있습니다. 운영자가 따로 보관하는 정보는 없습니다. 제3자(Google, Apple, GitHub, 스토어)가 수집한 정보의 보관 기간은 해당 회사의 방침을 따릅니다.</p>',
                ]),
                ('10. 아동의 개인정보', ['<p>앱은 만 14세 미만 아동(해외는 만 13세 미만)을 주 대상으로 하지 않으며, 아동의 개인정보를 의도적으로 수집하지 않습니다.</p>']),
                ('11. 이용자의 권리', ['<p>앱에 저장된 정보는 모두 이용자의 기기에 있으므로 이용자가 직접 확인하고 지울 수 있습니다. 광고 관련 정보는 4항의 방법으로 맞춤형 광고를 거부할 수 있습니다.</p>']),
                ('12. 개인정보 보호책임자·문의', [f'<p>개인정보 보호책임자: 내곁의 운영자<br>연락처: {E}</p>']),
                ('13. 방침의 변경', ['<p>이 방침이 바뀌면 이 페이지에 시행일과 함께 알립니다. 이 방침은 한국어 원문을 기준으로 하며, 다른 언어판과 뜻이 다르면 한국어판을 따릅니다.</p>']),
            ],
        },
        'en': {
            'title': 'Lumiclean Privacy Policy',
            'date': 'Effective date: November 5, 2026',
            'intro': 'Lumiclean (the "App", for Android and iOS) respects your privacy. This policy explains what information the App handles and how.',
            'summary_h': 'At a glance',
            'summary': [
                'Your photo and video files are never sent to a server. Cleanup, compression and enhancement all happen on your phone.',
                'There is no sign-up or login, and we run no server of our own.',
                'Only on iPhone, when you view a photo full screen, the App sends the photo\'s coordinates to Apple to look up the place name.',
                'Ads are shown by Google AdMob, and you choose whether they are personalized.',
            ],
            'contact_h': 'Contact',
            'sections': [
                ('1. Information the App collects', [
                    '<p>The App has no sign-up or login, and we run no server. Your photos, videos and usage history are not sent to us.</p>',
                    '<p>The App reads your photo library to find similar photos, screenshots and large files. Photo analysis, compression and enhancement all happen <strong>on your device</strong>. The AI model used for enhancement (Real-ESRGAN) is built into the App, so your photos never need to leave your phone.</p>',
                    '<p>On iPhone, if the original of a photo you enhance or compress is stored only in iCloud Photos, iOS may download it from your iCloud. That transfer is between you and Apple and does not pass through us.</p>',
                    '<p>Enhanced photos and compressed copies are saved to your photo library. When you delete photos, your phone asks you to confirm, and on iOS deleted photos move to Recently Deleted.</p>',
                ]),
                ('2. Photo location', [
                    '<p>Photos can contain the coordinates of where they were taken. On iPhone, when you view a photo full screen, the App shows that place as a neighborhood name. To do this it sends <strong>only the photo\'s coordinates</strong> to Apple\'s place-name lookup service. The photo file and other information are not sent.</p>',
                    f'<p>Place names the App receives are kept on your device, up to 500, so the same place is not looked up twice. Apple handles these requests under the <a href="{apple}">Apple Privacy Policy</a>.</p>',
                    '<p>On Android the App does not show place names and does not send coordinates off your device. On any device, the App never asks for or uses your current location.</p>',
                ]),
                ('3. Information collected by third parties for ads', [
                    '<p>The App is free and uses <strong>Google AdMob</strong> by Google LLC to show ads. AdMob may collect and process the following information to serve and measure ads and prevent fraud.</p>',
                    rows([
                        ('Collected by', 'Google LLC (AdMob)'),
                        ('Data', 'Advertising ID (Android advertising ID; iOS IDFA, only if you allow tracking), IP address, device and OS information, app usage such as ad views and clicks, approximate location inferred from IP'),
                        ('Purpose', 'Showing ads and personalized ads, measuring ad performance, preventing invalid clicks'),
                    ]),
                    f'<p>See <a href="{p1}">How Google uses information from sites or apps that use its services</a> and the <a href="{p2}">Google Privacy Policy</a>.</p>',
                    '<p>The App may also show promotions for our own apps. It downloads a public promotion list, images and videos from boksday.github.io (GitHub Pages) (<a href="https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement">GitHub Privacy Statement</a>) and caches them on your device. The hosting provider may receive your IP address and request metadata, such as the time and requested file, when serving these requests. Your photos and videos are not included in these requests. Tapping a promotion opens an external app store page.</p>',
                ]),
                ('4. Opting out of personalized ads', [
                    '<ul><li>Android: go to <strong>Settings → Google → Ads</strong> on your phone to delete or reset your advertising ID.</li>'
                    '<li>iOS: you can choose whether to allow tracking on first launch, and change it anytime in <strong>Settings → Privacy &amp; Security → Tracking</strong>.</li>'
                    '<li>Users in the EEA, the UK and Switzerland can choose their ad privacy consent on first launch. Users in some US states can opt out of the sale or sharing of personal information. In both cases you can change your choice anytime in the App under <strong>Settings → Ad privacy settings</strong>.</li>'
                    '<li>If consent cannot be confirmed or tracking is not allowed, the App requests only non-personalized ads.</li></ul>',
                ]),
                ('5. Payments (Premium)', [
                    '<p>Premium purchases are processed by the App Store or Google Play. Monthly and yearly plans are auto-renewing subscriptions until canceled; lifetime access is a one-time purchase. Neither the App nor we receive card numbers or other payment details. The App checks purchase and subscription information provided by the store and saves Premium status, plan and expiration time on your device to determine access.</p>',
                ]),
                ('6. App lock', [
                    '<p>When App lock is on, the App asks for Face ID, Touch ID, fingerprint or your device passcode when you open it. Your phone\'s operating system does the check, and the App receives only whether it succeeded. The App never reads or stores your face, fingerprint or passcode, and it has no passcode of its own.</p>',
                ]),
                ('7. Information stored on your device', [
                    '<p>The App stores the following <strong>only on your device</strong>. It contains no photo files, and we cannot see it.</p>',
                    rows([
                        ('Cleanup history', 'IDs of photos you set aside to delete or chose to keep, how many you deleted and how much space you freed, groups you chose to keep'),
                        ('Analysis results', 'File size of each photo, similar-photo results, records of compressed copies and space saved by compression'),
                        ('Place names', 'iOS only. Rounded coordinates and neighborhood names, up to 500'),
                        ('Settings', 'App lock, appearance, language, which tips you have seen, Premium status, plan and expiration time'),
                    ]),
                ]),
                ('8. Permissions', [
                    rows([
                        ('Photos and videos', 'Used to find photos to clean up, view them full screen, compress and enhance them, and to save enhanced photos and compressed copies to your library.'),
                        ('Photo location', 'Android only. Lets the App read the location stored in photo files without it being removed. This information is not sent off your device.'),
                        ('Face ID / biometrics', 'Used only when App lock is on.'),
                        ('Tracking', 'iOS only. Used for personalized ads. The App works the same if you don\'t allow it.'),
                        ('Internet', 'Used for ads, downloading our app promotion list, images and videos, purchase checks and iPhone place names.'),
                    ]),
                    '<p>The App does not ask for location or microphone permission. You can change or turn off photo access anytime in your phone\'s settings.</p>',
                ]),
                ('9. Retention and deletion', [
                    '<p>Information stored on your device is removed when you delete the App. Photos saved to your photo library stay there after you delete the App, and you can remove them in your Photos app. We keep no information of our own. Information collected by third parties (Google, Apple, GitHub, the stores) is kept according to their policies.</p>',
                ]),
                ('10. Children\'s privacy', ['<p>The App is not directed primarily at children under 13 (under 14 in Korea) and does not knowingly collect their personal information.</p>']),
                ('11. Your rights', ['<p>All information the App stores is on your device, so you can review and delete it yourself. For ad-related information, you can opt out of personalized ads as described in section 4.</p>']),
                ('12. Privacy officer and contact', [f'<p>Privacy officer: BySide operator<br>Contact: {E}</p>']),
                ('13. Changes to this policy', ['<p>If this policy changes, we will post the update on this page with a new effective date. The Korean version is the original; if versions differ, the Korean version prevails.</p>']),
            ],
        },
        'ja': {
            'title': 'Lumiclean プライバシーポリシー',
            'date': '施行日：2026年11月5日',
            'intro': 'Lumiclean（以下「本アプリ」、Android・iOS）は利用者のプライバシーを大切にします。このポリシーでは、本アプリがどのような情報をどのように扱うかを説明します。',
            'summary_h': '概要',
            'summary': [
                '写真とビデオのファイルをサーバーに送ることはありません。整理・圧縮・高画質化はすべてスマートフォンの中で行います。',
                '会員登録やログインはなく、運営者が運営するサーバーもありません。',
                'iPhoneで写真を大きく表示するときだけ、撮影場所の名前を調べるために写真の座標をAppleに送ります。',
                '広告はGoogle AdMobが表示し、パーソナライズ広告にするかどうかは利用者が選べます。',
            ],
            'contact_h': 'お問い合わせ',
            'sections': [
                ('1. 本アプリが直接収集する情報', [
                    '<p>本アプリには会員登録やログインがなく、運営者が運営するサーバーもありません。利用者の写真・ビデオや利用履歴を運営者に送ることはありません。</p>',
                    '<p>本アプリは、似た写真、スクリーンショット、大きなファイルを見つけるために写真ライブラリを読み込みます。写真の分析、圧縮、高画質化は<strong>すべて端末の中で</strong>行います。高画質化に使うAIモデル（Real-ESRGAN）は本アプリに含まれているため、写真を外部に送る必要がありません。</p>',
                    '<p>iPhoneで高画質化または圧縮する写真のオリジナルがiCloud写真にしかない場合、iOSが利用者のiCloudからオリジナルをダウンロードすることがあります。この通信は利用者とAppleの間で行われ、運営者を経由しません。</p>',
                    '<p>高画質化した写真と圧縮したコピーは、利用者の写真ライブラリに保存されます。写真を削除するときは端末が確認画面を表示し、iOSでは削除した写真が「最近削除した項目」に移ります。</p>',
                ]),
                ('2. 写真の位置情報', [
                    '<p>写真には撮影場所の座標が含まれていることがあります。iPhoneで写真を大きく表示すると、本アプリは撮影場所を「東京都渋谷区」のような地名で表示します。そのために<strong>写真の座標だけ</strong>をAppleの地名変換サービスに送ります。写真ファイルやその他の情報は送りません。</p>',
                    f'<p>受け取った地名は、同じ場所を何度も問い合わせないよう端末内に最大500件まで保存します。Appleによる処理は<a href="{apple}">Appleのプライバシーポリシー</a>に従います。</p>',
                    '<p>Androidでは撮影場所の名前を表示せず、座標を端末の外に送りません。本アプリはどの端末でも利用者の現在地を求めたり使ったりしません。</p>',
                ]),
                ('3. 広告のために第三者が収集する情報', [
                    '<p>本アプリは無料で提供され、広告表示のためにGoogle LLCの<strong>Google AdMob</strong>を使用します。AdMobは広告の配信と測定、不正利用の防止のために、次の情報を収集・処理することがあります。</p>',
                    rows([
                        ('収集者', 'Google LLC（AdMob）'),
                        ('項目', '広告ID（Androidの広告ID、iOSの広告識別子IDFA。iOSは利用者がトラッキングを許可した場合のみ）、IPアドレス、端末・OS情報、広告の表示・クリックなどの利用情報、IPから推定したおおよその位置'),
                        ('目的', '広告表示とパーソナライズ広告、広告効果の測定、不正クリックの防止'),
                    ]),
                    f'<p>Googleによる情報の取り扱いは<a href="{p1}">Googleのサービスを使用するサイトやアプリから収集した情報のGoogleによる使用</a>と<a href="{p2}">Googleプライバシーポリシー</a>で確認できます。</p>',
                    '<p>本アプリは運営者の他のアプリの広告も表示することがあります。公開された広告一覧、画像、動画をboksday.github.io（GitHub Pages）からダウンロードし、端末にキャッシュします。ホスティング提供者は、このリクエストの処理時にIPアドレスやリクエスト日時・対象ファイルなどの情報を受け取ることがあります。利用者の写真や動画はリクエストに含まれません。広告をタップすると外部のアプリストアページが開きます。詳細は<a href="https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement">GitHubプライバシーに関する声明</a>をご覧ください。</p>',
                ]),
                ('4. パーソナライズ広告を拒否する方法', [
                    '<ul><li>Android：端末の<strong>設定 → Google → 広告</strong>で広告IDを削除またはリセットできます。</li>'
                    '<li>iOS：初回起動時にトラッキングを許可するか選べます。<strong>設定 → プライバシーとセキュリティ → トラッキング</strong>でいつでも変更できます。</li>'
                    '<li>欧州経済領域（EEA）・英国・スイスの利用者は、初回起動時に広告のプライバシーに関する同意を選べます。米国の一部の州の利用者は、個人情報の販売・共有を拒否できます。どちらも本アプリの<strong>設定 → 広告のプライバシー設定</strong>でいつでも変更できます。</li>'
                    '<li>同意が確認できない場合やトラッキングを許可していない場合、本アプリはパーソナライズされていない広告のみをリクエストします。</li></ul>',
                ]),
                ('5. 決済（プレミアム）', [
                    '<p>プレミアムの購入はApp StoreまたはGoogle Playが処理します。月額・年額プランは解約するまで自動更新されるサブスクリプションで、永久プランは買い切りの商品です。本アプリと運営者がカード番号などの決済情報を受け取ることはありません。本アプリはストアが提供する購入・サブスクリプション情報を確認し、プレミアムの利用状態、プラン、有効期限を端末に保存して利用権限を判定します。</p>',
                ]),
                ('6. アプリのロック', [
                    '<p>アプリのロックをオンにすると、本アプリを開くときにFace ID、Touch ID、指紋認証または端末のパスコードで確認します。確認は端末のOSが行い、本アプリは成功したかどうかだけを受け取ります。本アプリは顔・指紋の情報やパスコードを読み取ったり保存したりせず、独自のパスコードもありません。</p>',
                ]),
                ('7. 端末内に保存する情報', [
                    '<p>本アプリは次の情報を<strong>利用者の端末の中だけ</strong>に保存します。写真ファイルそのものは含まれず、運営者はこの内容を見ることができません。</p>',
                    rows([
                        ('整理の記録', '削除するために選んだ写真と残すことにした写真の識別番号、削除した数と空けた容量、残すことにしたグループ'),
                        ('分析結果', '写真ごとのファイルサイズと似た写真の検出結果、圧縮したコピーの記録と圧縮で減らした容量'),
                        ('撮影場所の名前', 'iOSのみ。丸めた座標と地名、最大500件'),
                        ('設定', 'アプリのロック、外観モード、言語、案内を見たかどうか、プレミアムの利用状態、プランと有効期限'),
                    ]),
                ]),
                ('8. アクセス権限', [
                    rows([
                        ('写真・ビデオ', '整理する写真を見つける、大きく表示する、圧縮する、高画質化するために使います。高画質化した写真と圧縮したコピーをライブラリに保存するときにも使います。'),
                        ('写真の位置情報', 'Androidのみ。写真ファイルに含まれる位置情報を削除せずに読み込むための権限です。この情報を端末の外に送ることはありません。'),
                        ('Face ID・生体認証', 'アプリのロックをオンにしたときだけ使います。'),
                        ('トラッキング', 'iOSのみ。パーソナライズ広告に使います。許可しなくても本アプリは同じように使えます。'),
                        ('インターネット', '広告の表示、自社アプリの広告一覧・画像・動画のダウンロード、購入の確認、iPhoneでの撮影場所の名前の確認に使います。'),
                    ]),
                    '<p>本アプリは位置情報とマイクの権限を求めません。写真へのアクセス範囲は端末の設定でいつでも変更またはオフにできます。</p>',
                ]),
                ('9. 保存期間と削除', [
                    '<p>端末に保存された情報は、本アプリを削除すると一緒に消えます。写真ライブラリに保存した写真は本アプリを削除しても残り、写真アプリで直接削除できます。運営者が別に保管する情報はありません。第三者（Google、Apple、GitHub、ストア）が収集した情報の保存期間は、各社のポリシーに従います。</p>',
                ]),
                ('10. 子どもの個人情報', ['<p>本アプリは13歳未満（韓国では14歳未満）の子どもを主な対象としておらず、子どもの個人情報を意図的に収集しません。</p>']),
                ('11. 利用者の権利', ['<p>本アプリが保存する情報はすべて利用者の端末にあるため、利用者が自分で確認・削除できます。広告に関する情報は、4項の方法でパーソナライズ広告を拒否できます。</p>']),
                ('12. 個人情報保護責任者・お問い合わせ', [f'<p>個人情報保護責任者：BySide 運営者<br>連絡先：{E}</p>']),
                ('13. ポリシーの変更', ['<p>このポリシーを変更する場合は、施行日とともにこのページでお知らせします。このポリシーは韓国語の原文を基準とし、他の言語版と内容が異なる場合は韓国語版に従います。</p>']),
            ],
        },
        'zh-hans': {
            'title': 'Lumiclean 隐私政策',
            'date': '生效日期：2026年11月5日',
            'intro': 'Lumiclean（以下称“本应用”，Android 和 iOS）重视您的隐私。本政策说明本应用处理哪些信息以及如何处理。',
            'summary_h': '概要',
            'summary': [
                '照片和视频文件不会发送到服务器。整理、压缩和画质增强都在手机上完成。',
                '无需注册或登录，我们也没有自己的服务器。',
                '仅在 iPhone 上放大查看照片时，本应用会把照片的坐标发送给 Apple，以查询拍摄地点的名称。',
                '广告由 Google AdMob 展示，是否接收个性化广告由您选择。',
            ],
            'contact_h': '联系我们',
            'sections': [
                ('1. 本应用直接收集的信息', [
                    '<p>本应用没有注册或登录，我们也不运营任何服务器。您的照片、视频和使用记录不会发送给我们。</p>',
                    '<p>本应用读取照片图库，以找出相似照片、截屏和大文件。照片分析、压缩和画质增强<strong>全部在设备上</strong>完成。画质增强所用的 AI 模型（Real-ESRGAN）内置于本应用中，因此照片无需离开您的手机。</p>',
                    '<p>在 iPhone 上，如果您要增强或压缩的照片原件只存在于 iCloud 照片中，iOS 可能会从您的 iCloud 下载原件。此传输发生在您与 Apple 之间，不经过我们。</p>',
                    '<p>增强后的照片和压缩后的副本会保存到您的照片图库。删除照片时，手机会弹出确认窗口；在 iOS 上，删除的照片会移到“最近删除”。</p>',
                ]),
                ('2. 照片位置信息', [
                    '<p>照片中可能包含拍摄地点的坐标。在 iPhone 上放大查看照片时，本应用会以地名显示拍摄地点。为此，本应用<strong>只把照片的坐标</strong>发送给 Apple 的地名转换服务，不会发送照片文件或其他信息。</p>',
                    f'<p>收到的地名会保存在设备上，最多 500 条，以免重复查询同一地点。Apple 对这些请求的处理遵循 <a href="{apple}">Apple 隐私政策</a>。</p>',
                    '<p>在 Android 上，本应用不显示拍摄地点名称，也不会把坐标发送到设备之外。在任何设备上，本应用都不会请求或使用您的当前位置。</p>',
                ]),
                ('3. 第三方为广告收集的信息', [
                    '<p>本应用免费提供，并使用 Google LLC 的 <strong>Google AdMob</strong> 展示广告。AdMob 可能为投放和衡量广告、防止欺诈而收集和处理以下信息。</p>',
                    rows([
                        ('收集方', 'Google LLC（AdMob）'),
                        ('信息', '广告 ID（Android 广告 ID、iOS 广告标识符 IDFA；iOS 仅在您允许跟踪时）、IP 地址、设备和操作系统信息、广告展示和点击等使用信息、根据 IP 推断的大致位置'),
                        ('目的', '展示广告和个性化广告、衡量广告效果、防止无效点击'),
                    ]),
                    f'<p>请参阅<a href="{p1}">Google 如何使用来自使用其服务的网站或应用的信息</a>和 <a href="{p2}">Google 隐私权政策</a>。</p>',
                    '<p>本应用也可能展示我们其他应用的推广广告。公开的推广列表、图片和视频从 boksday.github.io（GitHub Pages）下载并缓存在设备上。托管服务提供商在处理这些请求时可能收到 IP 地址以及请求时间、请求文件等请求信息。请求不包含您的照片或视频。点按推广广告会打开外部应用商店页面。详情请参阅<a href="https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement">GitHub 隐私声明</a>。</p>',
                ]),
                ('4. 拒绝个性化广告的方法', [
                    '<ul><li>Android：在手机的<strong>设置 → Google → 广告</strong>中删除或重置广告 ID。</li>'
                    '<li>iOS：首次启动时可选择是否允许跟踪，之后可随时在<strong>设置 → 隐私与安全性 → 跟踪</strong>中更改。</li>'
                    '<li>欧洲经济区（EEA）、英国和瑞士的用户可在首次启动时选择广告隐私同意。美国部分州的用户可以拒绝出售或共享个人信息。两种情况都可以随时在本应用的<strong>设置 → 广告隐私设置</strong>中更改。</li>'
                    '<li>如果无法确认同意或您未允许跟踪，本应用只请求非个性化广告。</li></ul>',
                ]),
                ('5. 付款（高级版）', [
                    '<p>高级版购买由 App Store 或 Google Play 处理。月度和年度方案为自动续订的订阅，直到您取消；终身方案为一次性购买。本应用和我们都不会收到卡号等付款信息。本应用确认商店提供的购买和订阅信息，并在设备上保存高级版权益状态、方案和到期时间，以判断使用权限。</p>',
                ]),
                ('6. 应用锁', [
                    '<p>开启应用锁后，打开本应用时会通过面容 ID、触控 ID、指纹或设备密码进行验证。验证由手机操作系统完成，本应用只收到是否成功的结果。本应用不会读取或保存您的面部、指纹信息或设备密码，也没有自己的密码。</p>',
                ]),
                ('7. 保存在设备上的信息', [
                    '<p>本应用<strong>只在您的设备上</strong>保存以下信息。其中不包含照片文件本身，我们也无法查看。</p>',
                    rows([
                        ('整理记录', '您选来删除和决定保留的照片的标识号、已删除数量和释放的空间、决定保留的分组'),
                        ('分析结果', '每张照片的文件大小和相似照片结果、压缩副本记录和压缩节省的空间'),
                        ('拍摄地点名称', '仅 iOS。四舍五入后的坐标和地名，最多 500 条'),
                        ('设置', '应用锁、外观模式、语言、是否看过提示、高级版权益状态、方案和到期时间'),
                    ]),
                ]),
                ('8. 访问权限', [
                    rows([
                        ('照片和视频', '用于找出要整理的照片、放大查看、压缩和画质增强，也用于把增强后的照片和压缩副本保存到图库。'),
                        ('照片位置信息', '仅 Android。用于读取照片文件中的位置信息而不将其去除。这些信息不会发送到设备之外。'),
                        ('面容 ID 和生物识别', '仅在开启应用锁时使用。'),
                        ('跟踪', '仅 iOS。用于个性化广告。不允许也能照常使用本应用。'),
                        ('网络', '用于展示广告、下载自有应用的推广列表及图片和视频、确认购买以及在 iPhone 上查询拍摄地点名称。'),
                    ]),
                    '<p>本应用不请求位置权限和麦克风权限。您可以随时在手机设置中更改或关闭照片访问范围。</p>',
                ]),
                ('9. 保存与删除', [
                    '<p>删除本应用时，设备上保存的信息会一并删除。保存到照片图库的照片在删除本应用后仍会保留，您可以在照片应用中自行删除。我们不另外保存任何信息。第三方（Google、Apple、GitHub、应用商店）收集的信息的保存期限遵循各公司的政策。</p>',
                ]),
                ('10. 儿童隐私', ['<p>本应用并非主要面向 13 岁以下（韩国为 14 岁以下）的儿童，也不会有意收集儿童的个人信息。</p>']),
                ('11. 您的权利', ['<p>本应用保存的信息全部位于您的设备上，您可以自行查看和删除。对于广告相关信息，您可以按第 4 条的方法拒绝个性化广告。</p>']),
                ('12. 个人信息保护负责人与联系方式', [f'<p>个人信息保护负责人：BySide 运营者<br>联系方式：{E}</p>']),
                ('13. 政策变更', ['<p>本政策如有变更，将在此页面公布并注明生效日期。本政策以韩文原文为准；若其他语言版本与韩文版含义不同，以韩文版为准。</p>']),
            ],
        },
        'zh-hant': {
            'title': 'Lumiclean 隱私權政策',
            'date': '生效日期：2026年11月5日',
            'intro': 'Lumiclean（以下稱「本 App」，Android 與 iOS）重視您的隱私。本政策說明本 App 處理哪些資訊以及如何處理。',
            'summary_h': '概要',
            'summary': [
                '照片與影片檔案不會傳送到伺服器。整理、壓縮與畫質提升都在手機上完成。',
                '無需註冊或登入，我們也沒有自己的伺服器。',
                '僅在 iPhone 上放大檢視照片時，本 App 會把照片的座標傳送給 Apple，以查詢拍攝地點的名稱。',
                '廣告由 Google AdMob 顯示，是否接收個人化廣告由您選擇。',
            ],
            'contact_h': '聯絡我們',
            'sections': [
                ('1. 本 App 直接收集的資訊', [
                    '<p>本 App 沒有註冊或登入，我們也不經營任何伺服器。您的照片、影片與使用紀錄不會傳送給我們。</p>',
                    '<p>本 App 會讀取照片圖庫，以找出相似照片、截圖與大型檔案。照片分析、壓縮與畫質提升<strong>全部在裝置上</strong>完成。畫質提升所用的 AI 模型（Real-ESRGAN）內建於本 App，因此照片不需離開您的手機。</p>',
                    '<p>在 iPhone 上，如果您要提升畫質或壓縮的照片原檔只存在於 iCloud 照片中，iOS 可能會從您的 iCloud 下載原檔。此傳輸發生在您與 Apple 之間，不經過我們。</p>',
                    '<p>提升畫質後的照片與壓縮後的副本會儲存到您的照片圖庫。刪除照片時，手機會顯示確認視窗；在 iOS 上，刪除的照片會移到「最近刪除」。</p>',
                ]),
                ('2. 照片位置資訊', [
                    '<p>照片中可能包含拍攝地點的座標。在 iPhone 上放大檢視照片時，本 App 會以地名顯示拍攝地點。為此，本 App <strong>只把照片的座標</strong>傳送給 Apple 的地名轉換服務，不會傳送照片檔案或其他資訊。</p>',
                    f'<p>收到的地名會儲存在裝置上，最多 500 筆，以免重複查詢同一地點。Apple 對這些請求的處理遵循 <a href="{apple}">Apple 隱私權政策</a>。</p>',
                    '<p>在 Android 上，本 App 不顯示拍攝地點名稱，也不會把座標傳送到裝置之外。在任何裝置上，本 App 都不會要求或使用您的目前位置。</p>',
                ]),
                ('3. 第三方為廣告收集的資訊', [
                    '<p>本 App 免費提供，並使用 Google LLC 的 <strong>Google AdMob</strong> 顯示廣告。AdMob 可能為放送與評估廣告、防止詐欺而收集和處理以下資訊。</p>',
                    rows([
                        ('收集者', 'Google LLC（AdMob）'),
                        ('資訊', '廣告 ID（Android 廣告 ID、iOS 廣告識別碼 IDFA；iOS 僅在您允許追蹤時）、IP 位址、裝置與作業系統資訊、廣告曝光與點擊等使用資訊、依 IP 推估的大略位置'),
                        ('目的', '顯示廣告與個人化廣告、評估廣告成效、防止無效點擊'),
                    ]),
                    f'<p>請參閱 <a href="{p1}">Google 如何使用與我們服務合作的網站或應用程式的資訊</a>與 <a href="{p2}">Google 隱私權政策</a>。</p>',
                    '<p>本 App 也可能顯示我們其他 App 的推廣廣告。公開的推廣清單、圖片與影片從 boksday.github.io（GitHub Pages）下載並快取至裝置。託管服務供應商處理這些請求時，可能收到 IP 位址以及請求時間、請求檔案等請求資訊。請求不包含您的照片或影片。點選推廣廣告會開啟外部應用程式商店頁面。詳情請參閱<a href="https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement">GitHub 隱私權聲明</a>。</p>',
                ]),
                ('4. 拒絕個人化廣告的方法', [
                    '<ul><li>Android：在手機的<strong>設定 → Google → 廣告</strong>中刪除或重設廣告 ID。</li>'
                    '<li>iOS：首次啟動時可選擇是否允許追蹤，之後可隨時在<strong>設定 → 隱私權與安全性 → 追蹤</strong>中變更。</li>'
                    '<li>歐洲經濟區（EEA）、英國與瑞士的使用者可在首次啟動時選擇廣告隱私同意。美國部分州的使用者可以拒絕出售或分享個人資訊。兩種情況都可以隨時在本 App 的<strong>設定 → 廣告隱私設定</strong>中變更。</li>'
                    '<li>若無法確認同意或您未允許追蹤，本 App 只會請求非個人化廣告。</li></ul>',
                ]),
                ('5. 付款（進階版）', [
                    '<p>進階版購買由 App Store 或 Google Play 處理。月繳與年繳方案是自動續訂的訂閱，直到您取消；終身方案為一次性購買。本 App 與我們都不會收到卡號等付款資訊。本 App 確認商店提供的購買與訂閱資訊，並在裝置上儲存進階版使用狀態、方案和到期時間，以判斷使用權限。</p>',
                ]),
                ('6. App 鎖定', [
                    '<p>開啟 App 鎖定後，打開本 App 時會以 Face ID、Touch ID、指紋或裝置密碼驗證。驗證由手機作業系統完成，本 App 只收到是否成功的結果。本 App 不會讀取或儲存您的臉部、指紋資訊或裝置密碼，也沒有自己的密碼。</p>',
                ]),
                ('7. 儲存在裝置上的資訊', [
                    '<p>本 App <strong>只在您的裝置上</strong>儲存以下資訊。其中不包含照片檔案本身，我們也無法查看。</p>',
                    rows([
                        ('整理紀錄', '您選來刪除與決定保留的照片識別碼、已刪除數量與釋放的空間、決定保留的群組'),
                        ('分析結果', '每張照片的檔案大小與相似照片結果、壓縮副本紀錄與壓縮節省的空間'),
                        ('拍攝地點名稱', '僅 iOS。四捨五入後的座標與地名，最多 500 筆'),
                        ('設定', 'App 鎖定、外觀模式、語言、是否看過提示、進階版使用狀態、方案和到期時間'),
                    ]),
                ]),
                ('8. 存取權限', [
                    rows([
                        ('照片與影片', '用於找出要整理的照片、放大檢視、壓縮與提升畫質，也用於把提升畫質的照片與壓縮副本儲存到圖庫。'),
                        ('照片位置資訊', '僅 Android。用於讀取照片檔案中的位置資訊而不將其移除。這些資訊不會傳送到裝置之外。'),
                        ('Face ID 與生物辨識', '僅在開啟 App 鎖定時使用。'),
                        ('追蹤', '僅 iOS。用於個人化廣告。不允許也能照常使用本 App。'),
                        ('網路', '用於顯示廣告、下載自有 App 的推廣清單及圖片與影片、確認購買，以及在 iPhone 上查詢拍攝地點名稱。'),
                    ]),
                    '<p>本 App 不要求位置權限與麥克風權限。您可以隨時在手機設定中變更或關閉照片存取範圍。</p>',
                ]),
                ('9. 保存與刪除', [
                    '<p>刪除本 App 時，裝置上儲存的資訊會一併刪除。儲存到照片圖庫的照片在刪除本 App 後仍會保留，您可以在照片 App 中自行刪除。我們不另外保存任何資訊。第三方（Google、Apple、GitHub、應用程式商店）收集的資訊保存期限依各公司的政策。</p>',
                ]),
                ('10. 兒童隱私', ['<p>本 App 並非主要以 13 歲以下（韓國為 14 歲以下）的兒童為對象，也不會刻意收集兒童的個人資訊。</p>']),
                ('11. 您的權利', ['<p>本 App 儲存的資訊全部位於您的裝置上，您可以自行查看與刪除。對於廣告相關資訊，您可以依第 4 條的方法拒絕個人化廣告。</p>']),
                ('12. 個人資料保護負責人與聯絡方式', [f'<p>個人資料保護負責人：BySide 營運者<br>聯絡方式：{E}</p>']),
                ('13. 政策變更', ['<p>本政策如有變更，將在此頁面公告並註明生效日期。本政策以韓文原文為準；若其他語言版本與韓文版意義不同，以韓文版為準。</p>']),
            ],
        },
    }
    return data[lang]
