EXTRA = {}


def _add(lang, title, date, intro, summary_h, contact_h, summary, headings, body):
    sections = []
    blocks = body.strip().split('\n---\n')
    assert len(headings) == len(blocks) == 13, lang
    for number, (heading, block) in enumerate(zip(headings, blocks), 1):
        content = []
        lines = block.strip().splitlines()
        i = 0
        while i < len(lines):
            line = lines[i]
            if line.startswith('@'):
                entries = []
                while i < len(lines) and lines[i].startswith('@'):
                    key, value = lines[i][1:].split('|', 1)
                    entries.append(f'<div><dt>{key}</dt><dd>{value}</dd></div>')
                    i += 1
                content.append('<dl class="rows">' + ''.join(entries) + '</dl>')
                continue
            if line.startswith('*'):
                entries = []
                while i < len(lines) and lines[i].startswith('*'):
                    entries.append('<li>' + lines[i][1:] + '</li>')
                    i += 1
                content.append('<ul>' + ''.join(entries) + '</ul>')
                continue
            content.append('<p>' + line + '</p>')
            i += 1
        replacements = {
            '{apple}': 'https://www.apple.com/legal/privacy/',
            '{p1}': 'https://policies.google.com/technologies/partner-sites?hl=' + lang,
            '{p2}': 'https://policies.google.com/privacy?hl=' + lang,
            '{email}': '<a href="mailto:ekqlszzzz@naver.com">ekqlszzzz@naver.com</a>',
        }
        replacements['GitHub Pages'] = '<a href="https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement">GitHub Pages</a>'
        for token, value in replacements.items():
            content = [item.replace(token, value) for item in content]
        sections.append((f'{number}. {heading}', content))
    EXTRA[lang] = dict(title=title, date=date, intro=intro, summary_h=summary_h,
                       summary=summary, contact_h=contact_h, sections=sections)


_add('en-gb', 'Lumiclean Privacy Policy', 'Effective date: 5 November 2026',
     'Lumiclean (the "App", for Android and iOS) respects your privacy. This policy explains what information the App handles and how.',
     'At a glance', 'Contact', [
         'Your photo and video files are never sent to a server. Cleanup, compression and enhancement all happen on your phone.',
         'There is no sign-up or login, and we run no server of our own.',
         'Only on iPhone, when you view a photo full screen, the App sends the photo’s coordinates to Apple to look up the place name.',
         'Ads are shown by Google AdMob, and you choose whether they are personalised.',
     ], ['Information the App collects', 'Photo location', 'Information collected by third parties for ads', 'Opting out of personalised ads', 'Payments (Premium)', 'App lock', 'Information stored on your device', 'Permissions', 'Retention and deletion', 'Children’s privacy', 'Your rights', 'Privacy officer and contact', 'Changes to this policy'], '''
The App has no sign-up or login, and we run no server. Your photos, videos and usage history are not sent to us.
The App reads your photo library to find similar photos, screenshots and large files. Photo analysis, compression and enhancement all happen <strong>on your device</strong>. The AI model used for enhancement (Real-ESRGAN) is built into the App, so your photos never need to leave your phone.
On iPhone, if the original of a photo you enhance or compress is stored only in iCloud Photos, iOS may download it from your iCloud. That transfer is between you and Apple and does not pass through us.
Enhanced photos and compressed copies are saved to your photo library. When you delete photos, your phone asks you to confirm, and on iOS deleted photos move to Recently Deleted.
---
Photos can contain the coordinates of where they were taken. On iPhone, when you view a photo full screen, the App shows that place as a neighbourhood name. To do this it sends <strong>only the photo’s coordinates</strong> to Apple’s place-name lookup service. The photo file and other information are not sent.
Place names the App receives are kept on your device, up to 500, so the same place is not looked up twice. Apple handles these requests under the <a href="{apple}">Apple Privacy Policy</a>.
On Android the App does not show place names and does not send coordinates off your device. On any device, the App never asks for or uses your current location.
---
The App is free and uses <strong>Google AdMob</strong> by Google LLC to show ads. AdMob may collect and process the following information to serve and measure ads and prevent fraud.
@Collected by|Google LLC (AdMob)
@Data|Advertising ID (Android advertising ID; iOS IDFA, only if you allow tracking), IP address, device and OS information, app usage such as ad views and clicks, approximate location inferred from IP
@Purpose|Showing ads and personalised ads, measuring ad performance, preventing invalid clicks
See <a href="{p1}">How Google uses information from sites or apps that use its services</a> and the <a href="{p2}">Google Privacy Policy</a>.
The App also downloads a public promotion list and promotional images and videos for our apps from boksday.github.io (GitHub Pages), and caches them on your device. No photos from your library are sent for this purpose. The hosting provider may receive your IP address and network request metadata. Tapping a promotion opens an external store link.
---
*Android: go to <strong>Settings → Google → Ads</strong> on your phone to delete or reset your advertising ID.
*iOS: you can choose whether to allow tracking on first launch, and change it anytime in <strong>Settings → Privacy &amp; Security → Tracking</strong>.
*Users in the EEA, the UK and Switzerland can choose their ad privacy consent on first launch. Users in some US states can opt out of the sale or sharing of personal information. In both cases you can change your choice anytime in the App under <strong>Settings → Ad privacy settings</strong>.
*If consent cannot be confirmed or tracking is not allowed, the App requests only non-personalised ads.
---
Premium purchases are processed by the App Store or Google Play. Premium offers monthly and yearly auto-renewing subscriptions and a lifetime, non-consumable purchase. Neither the App nor we receive card numbers or other payment details. The App checks the Premium entitlement reported by the store and stores that status, plan and expiry date on your device so it can be used offline.
---
When App lock is on, the App asks for Face ID, Touch ID, fingerprint or your device passcode when you open it. Your phone’s operating system does the check, and the App receives only whether it succeeded. The App never reads or stores your face, fingerprint or passcode, and it has no passcode of its own.
---
The App stores the following <strong>only on your device</strong>. It contains no photo files, and we cannot see it.
@Cleanup history|IDs of photos you set aside to delete or chose to keep, how many you deleted and how much space you freed, groups you chose to keep
@Analysis results|File size of each photo, similar-photo results, records of compressed copies and space saved by compression
@Place names|iOS only. Rounded coordinates and neighbourhood names, up to 500
@Settings|App lock, appearance, language, which tips you have seen, Premium status, plan and expiry date
---
@Photos and videos|Used to find photos to clean up, view them full screen, compress and enhance them, and to save enhanced photos and compressed copies to your library.
@Photo location|Android only. Lets the App read the location stored in photo files without it being removed. This information is not sent off your device.
@Face ID / biometrics|Used only when App lock is on.
@Tracking|iOS only. Used for personalised ads. The App works the same if you do not allow it.
@Internet|Used for ads, downloading our app promotions, purchase checks and iPhone place names.
The App does not ask for location or microphone permission. You can change or turn off photo access anytime in your phone’s settings.
---
Information stored on your device is removed when you delete the App. Photos saved to your photo library stay there after you delete the App, and you can remove them in your Photos app. We keep no information of our own. Information collected by third parties (Google, Apple, GitHub, the stores) is kept according to their policies.
---
The App is not directed primarily at children under 13 (under 14 in Korea) and does not knowingly collect their personal information.
---
All information the App stores is on your device, so you can review and delete it yourself. For ad-related information, you can opt out of personalised ads as described in section 4.
---
Privacy officer: BySide operator<br>Contact: {email}
---
If this policy changes, we will post the update on this page with a new effective date. The Korean version is the original; if versions differ, the Korean version prevails.
''')

_add('sv', 'Lumicleans integritetspolicy', 'Gäller från: 5 november 2026',
     'Lumiclean (”appen”, för Android och iOS) respekterar din integritet. Den här policyn beskriver vilka uppgifter appen hanterar och hur.',
     'I korthet', 'Kontakt', [
         'Dina foto- och videofiler skickas aldrig till en server. Rensning, komprimering och förbättring sker på din telefon.',
         'Ingen registrering eller inloggning krävs, och vi driver ingen egen server.',
         'Endast på iPhone, när du visar ett foto i helskärm, skickar appen fotots koordinater till Apple för att hämta platsnamnet.',
         'Annonser visas av Google AdMob, och du väljer om de ska vara anpassade.',
     ], ['Uppgifter som appen samlar in', 'Platsinformation i foton', 'Uppgifter som tredje parter samlar in för annonser', 'Välja bort anpassade annonser', 'Betalningar (Premium)', 'Applås', 'Uppgifter som lagras på din enhet', 'Behörigheter', 'Lagring och radering', 'Barns integritet', 'Dina rättigheter', 'Integritetsansvarig och kontakt', 'Ändringar i policyn'], '''
Appen har ingen registrering eller inloggning, och vi driver ingen server. Dina foton, videor och din användningshistorik skickas inte till oss.
Appen läser ditt fotobibliotek för att hitta liknande foton, skärmbilder och stora filer. Fotoanalys, komprimering och förbättring sker <strong>på din enhet</strong>. AI-modellen för förbättring (Real-ESRGAN) är inbyggd i appen, så dina foton behöver aldrig lämna telefonen.
Om originalet till ett foto som du förbättrar eller komprimerar på iPhone bara finns i iCloud-bilder kan iOS hämta det från ditt iCloud. Överföringen sker mellan dig och Apple och går inte via oss.
Förbättrade foton och komprimerade kopior sparas i ditt fotobibliotek. När du raderar foton ber telefonen dig bekräfta, och på iOS flyttas raderade foton till Senast raderade.
---
Foton kan innehålla koordinaterna för platsen där de togs. När du visar ett foto i helskärm på iPhone visar appen platsen som ett områdesnamn. Den skickar då <strong>endast fotots koordinater</strong> till Apples tjänst för platsnamn. Fotofilen och andra uppgifter skickas inte.
Upp till 500 hämtade platsnamn sparas på enheten så att samma plats inte behöver sökas upp igen. Apple behandlar förfrågningarna enligt <a href="{apple}">Apples integritetspolicy</a>.
På Android visar appen inte platsnamn och skickar inga koordinater från enheten. Appen begär eller använder aldrig din aktuella plats, oavsett enhet.
---
Appen är gratis och använder <strong>Google AdMob</strong> från Google LLC för annonser. AdMob kan samla in och behandla följande uppgifter för att visa och mäta annonser och förebygga bedrägerier.
@Insamlare|Google LLC (AdMob)
@Uppgifter|Annons-ID (Androids annons-ID; iOS IDFA endast om du tillåter spårning), IP-adress, uppgifter om enhet och operativsystem, appanvändning såsom annonsvisningar och klick, ungefärlig plats härledd från IP-adressen
@Ändamål|Visa annonser och anpassade annonser, mäta annonsresultat, förebygga ogiltiga klick
Se <a href="{p1}">Så använder Google information från webbplatser eller appar som använder våra tjänster</a> och <a href="{p2}">Googles integritetspolicy</a>.
Appen hämtar även en offentlig lista med reklam för våra appar samt reklambilder och videor från boksday.github.io (GitHub Pages) och cachelagrar dem på enheten. Inga foton från ditt bibliotek skickas för detta ändamål. Värdtjänstleverantören kan få din IP-adress och metadata om nätverksförfrågningar. Om du trycker på en sådan annons öppnas en extern butikslänk.
---
*Android: gå till <strong>Inställningar → Google → Annonser</strong> på telefonen för att radera eller återställa ditt annons-ID.
*iOS: du kan välja om spårning ska tillåtas första gången du öppnar appen och ändra detta när som helst i <strong>Inställningar → Integritet och säkerhet → Spårning</strong>.
*Användare i EES, Storbritannien och Schweiz kan välja sitt samtycke för annonsintegritet första gången appen öppnas. Användare i vissa amerikanska delstater kan välja bort försäljning eller delning av personuppgifter. I båda fallen kan valet ändras när som helst i appens <strong>Inställningar → Annonsintegritet</strong>.
*Om samtycke inte kan bekräftas eller spårning inte tillåts begär appen endast annonser som inte är anpassade.
---
Premiumköp hanteras av App Store eller Google Play. Premium erbjuder månads- och årsabonnemang som förnyas automatiskt samt ett livstidsköp som inte förbrukas. Varken appen eller vi får kortnummer eller andra betalningsuppgifter. Appen kontrollerar Premiumbehörigheten som butiken rapporterar och sparar status, abonnemangsform och utgångsdatum på enheten så att uppgifterna kan användas offline.
---
När applåset är aktiverat begär appen Face ID, Touch ID, fingeravtryck eller enhetens lösenkod när du öppnar den. Telefonens operativsystem gör kontrollen, och appen får endast veta om den lyckades. Appen läser eller lagrar aldrig ansiktsdata, fingeravtryck eller lösenkod och har ingen egen lösenkod.
---
Appen lagrar följande <strong>endast på din enhet</strong>. Uppgifterna innehåller inga fotofiler, och vi kan inte se dem.
@Rensningshistorik|ID för foton som du lagt undan för radering eller valt att behålla, antal raderade foton och frigjort utrymme, grupper du valt att behålla
@Analysresultat|Varje fotos filstorlek, resultat för liknande foton, uppgifter om komprimerade kopior och utrymme som sparats genom komprimering
@Platsnamn|Endast iOS. Avrundade koordinater och områdesnamn, upp till 500
@Inställningar|Applås, utseende, språk, vilka tips du har sett, Premiumstatus, abonnemangsform och utgångsdatum
---
@Foton och videor|Används för att hitta foton att rensa, visa dem i helskärm, komprimera och förbättra dem samt spara förbättrade foton och komprimerade kopior i biblioteket.
@Platsinformation i foton|Endast Android. Gör det möjligt att läsa platsinformationen i fotofiler utan att den tas bort. Informationen skickas inte från enheten.
@Face ID / biometri|Används endast när applåset är aktiverat.
@Spårning|Endast iOS. Används för anpassade annonser. Appen fungerar likadant om du inte tillåter det.
@Internet|Används för annonser, hämtning av reklam för våra appar, köpkontroller och platsnamn på iPhone.
Appen begär inte plats- eller mikrofonbehörighet. Du kan när som helst ändra eller stänga av fotoåtkomst i telefonens inställningar.
---
Uppgifter som lagras på enheten tas bort när du raderar appen. Foton som sparats i fotobiblioteket finns kvar efter att appen raderats och kan tas bort i appen Bilder. Vi lagrar inga egna uppgifter. Uppgifter som tredje parter (Google, Apple, GitHub, butikerna) samlar in lagras enligt deras policyer.
---
Appen riktar sig inte främst till barn under 13 år (under 14 i Korea) och samlar inte medvetet in deras personuppgifter.
---
Alla uppgifter som appen lagrar finns på din enhet, så du kan granska och radera dem själv. För annonsrelaterade uppgifter kan du välja bort anpassade annonser enligt avsnitt 4.
---
Integritetsansvarig: BySides operatör<br>Kontakt: {email}
---
Om denna policy ändras publicerar vi uppdateringen på denna sida med ett nytt ikraftträdandedatum. Den koreanska versionen är originalet; vid skillnader gäller den koreanska versionen.
''')

_add('da', 'Lumicleans privatlivspolitik', 'Gældende fra: 5. november 2026',
     'Lumiclean (”appen”, til Android og iOS) respekterer dit privatliv. Denne politik forklarer, hvilke oplysninger appen behandler, og hvordan.',
     'Overblik', 'Kontakt', [
         'Dine foto- og videofiler sendes aldrig til en server. Oprydning, komprimering og forbedring foregår på din telefon.',
         'Der er ingen tilmelding eller login, og vi driver ingen egen server.',
         'Kun på iPhone, når du ser et foto i fuld skærm, sender appen fotoets koordinater til Apple for at finde stednavnet.',
         'Annoncer vises af Google AdMob, og du vælger, om de skal være tilpassede.',
     ], ['Oplysninger, som appen indsamler', 'Placering i fotos', 'Oplysninger, som tredjeparter indsamler til annoncer', 'Fravalg af tilpassede annoncer', 'Betalinger (Premium)', 'Applås', 'Oplysninger gemt på din enhed', 'Tilladelser', 'Opbevaring og sletning', 'Børns privatliv', 'Dine rettigheder', 'Privatlivsansvarlig og kontakt', 'Ændringer af denne politik'], '''
Appen har ingen tilmelding eller login, og vi driver ingen server. Dine fotos, videoer og din brugshistorik sendes ikke til os.
Appen læser dit fotobibliotek for at finde lignende fotos, skærmbilleder og store filer. Fotoanalyse, komprimering og forbedring foregår <strong>på din enhed</strong>. AI-modellen til forbedring (Real-ESRGAN) er indbygget i appen, så dine fotos aldrig behøver at forlade telefonen.
Hvis originalen til et foto, du forbedrer eller komprimerer på iPhone, kun findes i iCloud-fotos, kan iOS hente den fra din iCloud. Overførslen sker mellem dig og Apple og går ikke gennem os.
Forbedrede fotos og komprimerede kopier gemmes i dit fotobibliotek. Når du sletter fotos, beder telefonen om bekræftelse, og på iOS flyttes slettede fotos til Slettet for nylig.
---
Fotos kan indeholde koordinater for, hvor de blev taget. Når du ser et foto i fuld skærm på iPhone, viser appen stedet som navnet på et lokalområde. Den sender <strong>kun fotoets koordinater</strong> til Apples tjeneste til opslag af stednavne. Fotofilen og andre oplysninger sendes ikke.
Op til 500 modtagne stednavne gemmes på din enhed, så samme sted ikke skal slås op igen. Apple behandler disse forespørgsler efter <a href="{apple}">Apples privatlivspolitik</a>.
På Android viser appen ikke stednavne og sender ikke koordinater fra din enhed. Appen beder aldrig om og bruger aldrig din aktuelle placering på nogen enhed.
---
Appen er gratis og bruger <strong>Google AdMob</strong> fra Google LLC til at vise annoncer. AdMob kan indsamle og behandle følgende oplysninger for at levere og måle annoncer og forebygge svindel.
@Indsamles af|Google LLC (AdMob)
@Oplysninger|Annonce-id (Androids annonce-id; iOS IDFA kun med tilladelse til sporing), IP-adresse, oplysninger om enhed og operativsystem, appbrug såsom annoncevisninger og klik, omtrentlig placering udledt af IP-adressen
@Formål|Vise annoncer og tilpassede annoncer, måle annonceresultater, forhindre ugyldige klik
Se <a href="{p1}">Sådan bruger Google oplysninger fra websites eller apps, der bruger vores tjenester</a> og <a href="{p2}">Googles privatlivspolitik</a>.
Appen henter også en offentlig liste med reklamer for vores apps samt reklamebilleder og videoer fra boksday.github.io (GitHub Pages) og gemmer dem i en cache på enheden. Ingen fotos fra dit bibliotek sendes til dette formål. Hostingudbyderen kan modtage din IP-adresse og metadata om netværksforespørgsler. Et tryk på en reklame åbner et eksternt butikslink.
---
*Android: gå til <strong>Indstillinger → Google → Annoncer</strong> på telefonen for at slette eller nulstille dit annonce-id.
*iOS: du kan vælge, om sporing skal tillades ved første start, og ændre det når som helst under <strong>Indstillinger → Anonymitet &amp; sikkerhed → Sporing</strong>.
*Brugere i EØS, Storbritannien og Schweiz kan vælge deres samtykke til annonceprivatliv ved første start. Brugere i visse amerikanske delstater kan fravælge salg eller deling af personoplysninger. I begge tilfælde kan valget ændres når som helst i appen under <strong>Indstillinger → Privatliv for annoncer</strong>.
*Hvis samtykket ikke kan bekræftes, eller sporing ikke er tilladt, anmoder appen kun om annoncer, der ikke er tilpassede.
---
Premiumkøb behandles af App Store eller Google Play. Premium tilbyder månedlige og årlige abonnementer med automatisk fornyelse samt et livstidskøb, der ikke forbruges. Hverken appen eller vi modtager kortnumre eller andre betalingsoplysninger. Appen kontrollerer den Premiumadgang, butikken oplyser om, og gemmer status, abonnementstype og udløbsdato på enheden til offlinebrug.
---
Når applås er slået til, beder appen om Face ID, Touch ID, fingeraftryk eller enhedens kode, når du åbner den. Telefonens operativsystem udfører kontrollen, og appen får kun at vide, om den lykkedes. Appen læser eller gemmer aldrig ansigtsdata, fingeraftryk eller koden og har ingen egen kode.
---
Appen gemmer følgende <strong>kun på din enhed</strong>. Oplysningerne indeholder ingen fotofiler, og vi kan ikke se dem.
@Oprydningshistorik|Id'er for fotos, du har lagt til side til sletning eller valgt at beholde, antal slettede fotos og frigjort plads, grupper du har valgt at beholde
@Analyseresultater|Hvert fotos filstørrelse, resultater for lignende fotos, registreringer af komprimerede kopier og plads sparet ved komprimering
@Stednavne|Kun iOS. Afrundede koordinater og navne på lokalområder, op til 500
@Indstillinger|Applås, udseende, sprog, hvilke tips du har set, Premiumstatus, abonnementstype og udløbsdato
---
@Fotos og videoer|Bruges til at finde fotos til oprydning, se dem i fuld skærm, komprimere og forbedre dem samt gemme forbedrede fotos og komprimerede kopier i biblioteket.
@Placering i fotos|Kun Android. Lader appen læse placeringen gemt i fotofiler, uden at den fjernes. Oplysningerne sendes ikke fra enheden.
@Face ID / biometri|Bruges kun, når applås er slået til.
@Sporing|Kun iOS. Bruges til tilpassede annoncer. Appen fungerer på samme måde, hvis du ikke tillader det.
@Internet|Bruges til annoncer, hentning af reklamer for vores apps, købskontrol og stednavne på iPhone.
Appen beder ikke om adgang til placering eller mikrofon. Du kan til enhver tid ændre eller slå fotoadgang fra i telefonens indstillinger.
---
Oplysninger gemt på enheden fjernes, når du sletter appen. Fotos gemt i fotobiblioteket bliver der, efter at appen er slettet, og du kan fjerne dem i appen Fotos. Vi opbevarer ingen egne oplysninger. Oplysninger indsamlet af tredjeparter (Google, Apple, GitHub, butikkerne) opbevares efter deres politikker.
---
Appen er ikke primært rettet mod børn under 13 år (under 14 i Korea) og indsamler ikke bevidst deres personoplysninger.
---
Alle oplysninger, appen gemmer, er på din enhed, så du selv kan gennemse og slette dem. For annonceoplysninger kan du fravælge tilpassede annoncer som beskrevet i afsnit 4.
---
Privatlivsansvarlig: BySides operatør<br>Kontakt: {email}
---
Hvis denne politik ændres, offentliggør vi opdateringen på denne side med en ny ikrafttrædelsesdato. Den koreanske version er originalen; ved forskelle gælder den koreanske version.
''')

_add('nb', 'Lumicleans personvernerklæring', 'Gjelder fra: 5. november 2026',
     'Lumiclean («appen», for Android og iOS) respekterer personvernet ditt. Denne erklæringen forklarer hvilke opplysninger appen behandler, og hvordan.',
     'Kort oversikt', 'Kontakt', [
         'Bilde- og videofilene dine sendes aldri til en server. Rydding, komprimering og forbedring skjer på telefonen din.',
         'Det er ingen registrering eller innlogging, og vi driver ingen egen server.',
         'Bare på iPhone, når du viser et bilde i fullskjerm, sender appen bildets koordinater til Apple for å finne stedsnavnet.',
         'Annonser vises av Google AdMob, og du velger om de skal være personlig tilpasset.',
     ], ['Opplysninger appen samler inn', 'Stedsinformasjon i bilder', 'Opplysninger tredjeparter samler inn for annonser', 'Velge bort personlig tilpassede annonser', 'Betalinger (Premium)', 'Applås', 'Opplysninger lagret på enheten din', 'Tillatelser', 'Oppbevaring og sletting', 'Barns personvern', 'Dine rettigheter', 'Personvernansvarlig og kontakt', 'Endringer i erklæringen'], '''
Appen har ingen registrering eller innlogging, og vi driver ingen server. Bilder, videoer og brukshistorikk sendes ikke til oss.
Appen leser bildebiblioteket ditt for å finne lignende bilder, skjermbilder og store filer. Bildeanalyse, komprimering og forbedring skjer <strong>på enheten din</strong>. KI-modellen for forbedring (Real-ESRGAN) er innebygd i appen, så bildene dine aldri trenger å forlate telefonen.
Hvis originalen til et bilde du forbedrer eller komprimerer på iPhone, bare finnes i iCloud-bilder, kan iOS laste den ned fra din iCloud. Overføringen skjer mellom deg og Apple og går ikke via oss.
Forbedrede bilder og komprimerte kopier lagres i bildebiblioteket ditt. Når du sletter bilder, ber telefonen om bekreftelse, og på iOS flyttes slettede bilder til Nylig slettet.
---
Bilder kan inneholde koordinatene til stedet der de ble tatt. Når du viser et bilde i fullskjerm på iPhone, viser appen stedet som et områdenavn. Den sender <strong>bare bildets koordinater</strong> til Apples tjeneste for stedsnavn. Bildefilen og andre opplysninger sendes ikke.
Inntil 500 mottatte stedsnavn lagres på enheten, slik at samme sted ikke må slås opp igjen. Apple behandler forespørslene i henhold til <a href="{apple}">Apples personvernerklæring</a>.
På Android viser appen ikke stedsnavn og sender ikke koordinater ut av enheten. Appen ber aldri om eller bruker din nåværende posisjon, uansett enhet.
---
Appen er gratis og bruker <strong>Google AdMob</strong> fra Google LLC til å vise annonser. AdMob kan samle inn og behandle følgende opplysninger for å vise og måle annonser og forebygge svindel.
@Samles inn av|Google LLC (AdMob)
@Opplysninger|Annonse-ID (Androids annonse-ID; iOS IDFA bare hvis du tillater sporing), IP-adresse, enhets- og operativsysteminformasjon, appbruk som annonsevisninger og klikk, omtrentlig posisjon utledet fra IP-adressen
@Formål|Vise annonser og personlig tilpassede annonser, måle annonseresultater, forhindre ugyldige klikk
Se <a href="{p1}">Slik bruker Google informasjon fra nettsteder eller apper som bruker tjenestene våre</a> og <a href="{p2}">Googles personvernregler</a>.
Appen laster også ned en offentlig liste med reklame for våre apper samt reklamebilder og videoer fra boksday.github.io (GitHub Pages), og mellomlagrer dem på enheten. Ingen bilder fra biblioteket ditt sendes for dette formålet. Vertsleverandøren kan motta IP-adressen din og metadata om nettverksforespørsler. Når du trykker på en slik annonse, åpnes en ekstern butikklenke.
---
*Android: gå til <strong>Innstillinger → Google → Annonser</strong> på telefonen for å slette eller tilbakestille annonse-ID-en.
*iOS: du kan velge om du tillater sporing ved første oppstart og endre dette når som helst i <strong>Innstillinger → Personvern og sikkerhet → Sporing</strong>.
*Brukere i EØS, Storbritannia og Sveits kan velge samtykke for annonsepersonvern ved første oppstart. Brukere i enkelte amerikanske delstater kan velge bort salg eller deling av personopplysninger. I begge tilfeller kan valget endres når som helst under <strong>Innstillinger → Personvern for annonser</strong> i appen.
*Hvis samtykke ikke kan bekreftes eller sporing ikke er tillatt, ber appen bare om annonser som ikke er personlig tilpasset.
---
Premiumkjøp behandles av App Store eller Google Play. Premium tilbyr månedlige og årlige abonnementer med automatisk fornyelse samt et livstidskjøp som ikke forbrukes. Verken appen eller vi mottar kortnumre eller andre betalingsopplysninger. Appen kontrollerer Premiumtilgangen som butikken rapporterer og lagrer status, abonnementstype og utløpsdato på enheten for bruk uten nett.
---
Når applås er på, ber appen om Face ID, Touch ID, fingeravtrykk eller enhetens kode når du åpner den. Telefonens operativsystem utfører kontrollen, og appen får bare vite om den lyktes. Appen leser eller lagrer aldri ansiktsdata, fingeravtrykk eller koden og har ingen egen kode.
---
Appen lagrer følgende <strong>bare på enheten din</strong>. Opplysningene inneholder ingen bildefiler, og vi kan ikke se dem.
@Ryddehistorikk|ID-er for bilder du har lagt til side for sletting eller valgt å beholde, antall slettede bilder og frigjort plass, grupper du har valgt å beholde
@Analyseresultater|Filstørrelsen til hvert bilde, resultater for lignende bilder, registreringer av komprimerte kopier og plass spart ved komprimering
@Stedsnavn|Bare iOS. Avrundede koordinater og områdenavn, inntil 500
@Innstillinger|Applås, utseende, språk, hvilke tips du har sett, Premiumstatus, abonnementstype og utløpsdato
---
@Bilder og videoer|Brukes til å finne bilder å rydde, vise dem i fullskjerm, komprimere og forbedre dem, og lagre forbedrede bilder og komprimerte kopier i biblioteket.
@Stedsinformasjon i bilder|Bare Android. Lar appen lese posisjonen i bildefiler uten at den fjernes. Informasjonen sendes ikke ut av enheten.
@Face ID / biometri|Brukes bare når applås er på.
@Sporing|Bare iOS. Brukes for personlig tilpassede annonser. Appen fungerer likt hvis du ikke tillater det.
@Internett|Brukes til annonser, nedlasting av reklame for våre apper, kjøpskontroll og stedsnavn på iPhone.
Appen ber ikke om tillatelse til posisjon eller mikrofon. Du kan når som helst endre eller slå av bildetilgang i telefonens innstillinger.
---
Opplysninger på enheten fjernes når du sletter appen. Bilder lagret i bildebiblioteket blir værende etter at appen er slettet, og du kan fjerne dem i Bilder-appen. Vi oppbevarer ingen egne opplysninger. Opplysninger samlet inn av tredjeparter (Google, Apple, GitHub, butikkene) oppbevares etter deres retningslinjer.
---
Appen er ikke primært rettet mot barn under 13 år (under 14 i Korea) og samler ikke bevisst inn personopplysningene deres.
---
Alle opplysninger appen lagrer, er på enheten din, så du kan gjennomgå og slette dem selv. For annonseopplysninger kan du velge bort personlig tilpassede annonser som beskrevet i punkt 4.
---
Personvernansvarlig: BySides operatør<br>Kontakt: {email}
---
Hvis denne erklæringen endres, publiserer vi oppdateringen på denne siden med en ny ikrafttredelsesdato. Den koreanske versjonen er originalen; ved forskjeller gjelder den koreanske versjonen.
''')

_add('nl', 'Privacybeleid van Lumiclean', 'Ingangsdatum: 5 november 2026',
     'Lumiclean (de “app”, voor Android en iOS) respecteert je privacy. Dit beleid legt uit welke gegevens de app verwerkt en hoe.',
     'In één oogopslag', 'Contact', [
         'Je foto- en videobestanden worden nooit naar een server verzonden. Opruimen, comprimeren en verbeteren gebeurt op je telefoon.',
         'Er is geen registratie of aanmelding en we beheren geen eigen server.',
         'Alleen op iPhone, wanneer je een foto schermvullend bekijkt, stuurt de app de coördinaten van de foto naar Apple om de plaatsnaam op te zoeken.',
         'Advertenties worden getoond door Google AdMob. Je kiest zelf of ze gepersonaliseerd zijn.',
     ], ['Gegevens die de app verzamelt', 'Locatiegegevens in foto’s', 'Gegevens die derden verzamelen voor advertenties', 'Gepersonaliseerde advertenties uitschakelen', 'Betalingen (Premium)', 'Appvergrendeling', 'Gegevens op je apparaat', 'Machtigingen', 'Bewaren en verwijderen', 'Privacy van kinderen', 'Je rechten', 'Privacyverantwoordelijke en contact', 'Wijzigingen in dit beleid'], '''
De app heeft geen registratie of aanmelding en we beheren geen server. Je foto’s, video’s en gebruiksgeschiedenis worden niet naar ons verzonden.
De app leest je fotobibliotheek om vergelijkbare foto’s, schermafbeeldingen en grote bestanden te vinden. Fotoanalyse, compressie en verbetering gebeuren <strong>op je apparaat</strong>. Het AI-model voor verbetering (Real-ESRGAN) is ingebouwd in de app, zodat je foto’s je telefoon nooit hoeven te verlaten.
Als het origineel van een foto die je op iPhone verbetert of comprimeert alleen in iCloud-foto’s staat, kan iOS dit uit je iCloud downloaden. Deze overdracht vindt plaats tussen jou en Apple en loopt niet via ons.
Verbeterde foto’s en gecomprimeerde kopieën worden in je fotobibliotheek opgeslagen. Als je foto’s verwijdert, vraagt je telefoon om bevestiging. Op iOS worden verwijderde foto’s naar Recent verwijderd verplaatst.
---
Foto’s kunnen de coördinaten bevatten van de plek waar ze zijn gemaakt. Op iPhone toont de app de buurtnaam wanneer je een foto schermvullend bekijkt. Hiervoor stuurt de app <strong>alleen de coördinaten van de foto</strong> naar Apples dienst voor het opzoeken van plaatsnamen. Het fotobestand en andere gegevens worden niet verzonden.
Maximaal 500 ontvangen plaatsnamen worden op je apparaat bewaard om dezelfde plaats niet opnieuw te hoeven opzoeken. Apple verwerkt deze verzoeken volgens het <a href="{apple}">privacybeleid van Apple</a>.
Op Android toont de app geen plaatsnamen en worden geen coördinaten buiten je apparaat verzonden. Op geen enkel apparaat vraagt of gebruikt de app je huidige locatie.
---
De app is gratis en gebruikt <strong>Google AdMob</strong> van Google LLC voor advertenties. AdMob kan de volgende gegevens verzamelen en verwerken om advertenties aan te bieden en te meten en fraude te voorkomen.
@Verzameld door|Google LLC (AdMob)
@Gegevens|Advertentie-ID (Android-advertentie-ID; iOS IDFA alleen als je tracking toestaat), IP-adres, apparaat- en besturingssysteemgegevens, appgebruik zoals advertentieweergaven en klikken, geschatte locatie afgeleid van het IP-adres
@Doel|Advertenties en gepersonaliseerde advertenties tonen, advertentieresultaten meten, ongeldige klikken voorkomen
Zie <a href="{p1}">Hoe Google informatie gebruikt van sites of apps die onze services gebruiken</a> en het <a href="{p2}">privacybeleid van Google</a>.
De app downloadt ook een openbare promotielijst en promotionele afbeeldingen en video’s voor onze apps van boksday.github.io (GitHub Pages) en bewaart deze in de cache op je apparaat. Hiervoor worden geen foto’s uit je bibliotheek verzonden. De hostingprovider kan je IP-adres en metadata van netwerkverzoeken ontvangen. Als je op een promotie tikt, wordt een externe winkellink geopend.
---
*Android: ga op je telefoon naar <strong>Instellingen → Google → Advertenties</strong> om je advertentie-ID te verwijderen of opnieuw in te stellen.
*iOS: bij de eerste start kun je kiezen of je tracking toestaat. Je kunt dit altijd wijzigen via <strong>Instellingen → Privacy en beveiliging → Tracking</strong>.
*Gebruikers in de EER, het VK en Zwitserland kunnen bij de eerste start hun toestemming voor advertentieprivacy kiezen. Gebruikers in bepaalde Amerikaanse staten kunnen de verkoop of het delen van persoonsgegevens weigeren. In beide gevallen kun je je keuze altijd wijzigen in de app via <strong>Instellingen → Advertentieprivacy</strong>.
*Als toestemming niet kan worden bevestigd of tracking niet is toegestaan, vraagt de app alleen niet-gepersonaliseerde advertenties aan.
---
Premiumaankopen worden verwerkt door de App Store of Google Play. Premium biedt maand- en jaarabonnementen die automatisch worden verlengd en een levenslange, niet-verbruikbare aankoop. De app en wij ontvangen geen kaartnummers of andere betalingsgegevens. De app controleert het door de winkel gemelde recht op Premium en slaat de status, het abonnementstype en de vervaldatum op je apparaat op voor offline gebruik.
---
Als appvergrendeling is ingeschakeld, vraagt de app bij het openen om Face ID, Touch ID, een vingerafdruk of de toegangscode van je apparaat. Het besturingssysteem voert de controle uit en de app ontvangt alleen of die is gelukt. De app leest of bewaart nooit gezichtsgegevens, vingerafdrukken of je toegangscode en heeft geen eigen toegangscode.
---
De app bewaart het volgende <strong>alleen op je apparaat</strong>. Deze gegevens bevatten geen fotobestanden en wij kunnen ze niet zien.
@Opruimgeschiedenis|ID’s van foto’s die je voor verwijdering hebt klaargezet of wilt bewaren, het aantal verwijderde foto’s en vrijgemaakte ruimte, groepen die je wilt bewaren
@Analyseresultaten|Bestandsgrootte van elke foto, resultaten voor vergelijkbare foto’s, gegevens over gecomprimeerde kopieën en bespaarde ruimte
@Plaatsnamen|Alleen iOS. Afgeronde coördinaten en buurtnamen, maximaal 500
@Instellingen|Appvergrendeling, weergave, taal, bekeken tips, Premiumstatus, abonnementstype en vervaldatum
---
@Foto’s en video’s|Voor het vinden van foto’s om op te ruimen, schermvullende weergave, compressie, verbetering en het opslaan van verbeterde foto’s en gecomprimeerde kopieën in je bibliotheek.
@Fotolocatie|Alleen Android. Hiermee leest de app locatiegegevens in fotobestanden zonder dat ze worden verwijderd. Deze gegevens worden niet buiten je apparaat verzonden.
@Face ID / biometrie|Alleen gebruikt als appvergrendeling is ingeschakeld.
@Tracking|Alleen iOS. Voor gepersonaliseerde advertenties. De app werkt hetzelfde als je dit niet toestaat.
@Internet|Voor advertenties, het downloaden van promoties voor onze apps, aankoopcontroles en plaatsnamen op iPhone.
De app vraagt geen toegang tot je locatie of microfoon. Je kunt de fototoegang altijd wijzigen of uitschakelen in de instellingen van je telefoon.
---
Gegevens op je apparaat worden verwijderd als je de app verwijdert. Foto’s in je fotobibliotheek blijven behouden; je kunt ze verwijderen in je Foto’s-app. Wij bewaren zelf geen gegevens. Gegevens die derden (Google, Apple, GitHub, de winkels) verzamelen, worden volgens hun beleid bewaard.
---
De app is niet primair gericht op kinderen jonger dan 13 jaar (14 jaar in Korea) en verzamelt niet bewust hun persoonsgegevens.
---
Alle gegevens die de app bewaart staan op je apparaat, zodat je ze zelf kunt bekijken en verwijderen. Voor advertentiegegevens kun je gepersonaliseerde advertenties uitschakelen zoals beschreven in onderdeel 4.
---
Privacyverantwoordelijke: de beheerder van BySide<br>Contact: {email}
---
Als dit beleid verandert, plaatsen we de wijziging op deze pagina met een nieuwe ingangsdatum. De Koreaanse versie is het origineel; bij verschillen geldt de Koreaanse versie.
''')

_add('de', 'Datenschutzerklärung von Lumiclean', 'Gültig ab: 5. November 2026',
     'Lumiclean (die „App“, für Android und iOS) respektiert Ihre Privatsphäre. Diese Erklärung erläutert, welche Daten die App verarbeitet und wie.',
     'Auf einen Blick', 'Kontakt', [
         'Ihre Foto- und Videodateien werden niemals an einen Server gesendet. Aufräumen, Komprimieren und Verbessern erfolgen auf Ihrem Telefon.',
         'Es gibt keine Registrierung oder Anmeldung, und wir betreiben keinen eigenen Server.',
         'Nur auf dem iPhone sendet die App beim Anzeigen eines Fotos im Vollbild dessen Koordinaten an Apple, um den Ortsnamen abzufragen.',
         'Werbung wird von Google AdMob angezeigt. Sie entscheiden, ob sie personalisiert wird.',
     ], ['Von der App erhobene Daten', 'Standortdaten in Fotos', 'Von Dritten für Werbung erhobene Daten', 'Personalisierte Werbung ablehnen', 'Zahlungen (Premium)', 'App-Sperre', 'Auf Ihrem Gerät gespeicherte Daten', 'Berechtigungen', 'Aufbewahrung und Löschung', 'Datenschutz für Kinder', 'Ihre Rechte', 'Datenschutzverantwortlicher und Kontakt', 'Änderungen dieser Erklärung'], '''
Die App hat keine Registrierung oder Anmeldung, und wir betreiben keinen Server. Ihre Fotos, Videos und Ihr Nutzungsverlauf werden nicht an uns gesendet.
Die App liest Ihre Fotomediathek, um ähnliche Fotos, Bildschirmfotos und große Dateien zu finden. Fotoanalyse, Komprimierung und Verbesserung erfolgen <strong>auf Ihrem Gerät</strong>. Das KI-Modell zur Verbesserung (Real-ESRGAN) ist in die App integriert. Ihre Fotos müssen das Telefon daher niemals verlassen.
Wenn das Original eines Fotos, das Sie auf dem iPhone verbessern oder komprimieren, nur in iCloud-Fotos liegt, kann iOS es aus Ihrer iCloud herunterladen. Diese Übertragung erfolgt zwischen Ihnen und Apple und läuft nicht über uns.
Verbesserte Fotos und komprimierte Kopien werden in Ihrer Fotomediathek gespeichert. Beim Löschen von Fotos bittet Ihr Telefon um Bestätigung. Unter iOS werden gelöschte Fotos nach „Zuletzt gelöscht“ verschoben.
---
Fotos können die Koordinaten ihres Aufnahmeorts enthalten. Wenn Sie ein Foto auf dem iPhone im Vollbild anzeigen, zeigt die App den Ort als Namen eines Stadtteils oder Gebiets an. Dazu sendet sie <strong>nur die Koordinaten des Fotos</strong> an Apples Dienst zur Ortsnamensabfrage. Die Fotodatei und andere Daten werden nicht gesendet.
Bis zu 500 erhaltene Ortsnamen werden auf Ihrem Gerät gespeichert, damit derselbe Ort nicht erneut abgefragt werden muss. Apple verarbeitet diese Anfragen gemäß der <a href="{apple}">Datenschutzerklärung von Apple</a>.
Unter Android zeigt die App keine Ortsnamen an und sendet keine Koordinaten vom Gerät. Die App fragt auf keinem Gerät nach Ihrem aktuellen Standort und verwendet ihn nicht.
---
Die App ist kostenlos und verwendet <strong>Google AdMob</strong> von Google LLC für Werbung. AdMob kann folgende Daten erheben und verarbeiten, um Werbung bereitzustellen, ihre Wirkung zu messen und Betrug zu verhindern.
@Erhoben durch|Google LLC (AdMob)
@Daten|Werbe-ID (Android-Werbe-ID; iOS-IDFA nur bei erlaubtem Tracking), IP-Adresse, Geräte- und Betriebssystemdaten, App-Nutzung wie Anzeigenaufrufe und Klicks, aus der IP-Adresse abgeleiteter ungefährer Standort
@Zweck|Anzeige von Werbung und personalisierter Werbung, Messung der Werbeleistung, Verhinderung ungültiger Klicks
Siehe <a href="{p1}">So verwendet Google Daten von Websites oder Apps, auf bzw. in denen unsere Dienste genutzt werden</a> und die <a href="{p2}">Datenschutzerklärung von Google</a>.
Die App lädt außerdem eine öffentliche Werbeliste sowie Werbebilder und -videos für unsere Apps von boksday.github.io (GitHub Pages) herunter und speichert sie im Cache auf Ihrem Gerät. Dafür werden keine Fotos aus Ihrer Mediathek gesendet. Der Hostinganbieter kann Ihre IP-Adresse und Metadaten von Netzwerkanfragen erhalten. Wenn Sie auf eine solche Werbung tippen, öffnet sich ein externer Store-Link.
---
*Android: Unter <strong>Einstellungen → Google → Werbung</strong> auf Ihrem Telefon können Sie Ihre Werbe-ID löschen oder zurücksetzen.
*iOS: Beim ersten Start können Sie entscheiden, ob Sie Tracking erlauben. Dies lässt sich jederzeit unter <strong>Einstellungen → Datenschutz &amp; Sicherheit → Tracking</strong> ändern.
*Nutzer im EWR, im Vereinigten Königreich und in der Schweiz können beim ersten Start ihre Datenschutzeinwilligung für Werbung wählen. Nutzer in bestimmten US-Bundesstaaten können den Verkauf oder die Weitergabe personenbezogener Daten ablehnen. In beiden Fällen lässt sich die Auswahl jederzeit in der App unter <strong>Einstellungen → Datenschutz für Werbung</strong> ändern.
*Wenn die Einwilligung nicht bestätigt werden kann oder Tracking nicht erlaubt ist, fordert die App nur nicht personalisierte Werbung an.
---
Premiumkäufe werden vom App Store oder von Google Play abgewickelt. Premium bietet automatisch verlängerbare Monats- und Jahresabonnements sowie einen lebenslangen, nicht verbrauchbaren Kauf. Weder die App noch wir erhalten Kartennummern oder andere Zahlungsdaten. Die App prüft die vom Store gemeldete Premiumberechtigung und speichert den Status, den Tarif und das Ablaufdatum auf Ihrem Gerät für die Offline-Nutzung.
---
Bei aktivierter App-Sperre fordert die App beim Öffnen Face ID, Touch ID, einen Fingerabdruck oder den Gerätecode an. Das Betriebssystem Ihres Telefons führt die Prüfung durch. Die App erfährt nur, ob sie erfolgreich war. Sie liest oder speichert weder Gesichts- oder Fingerabdruckdaten noch den Code und hat keinen eigenen Code.
---
Die App speichert Folgendes <strong>nur auf Ihrem Gerät</strong>. Diese Daten enthalten keine Fotodateien, und wir können sie nicht einsehen.
@Aufräumverlauf|Kennungen der zum Löschen vorgemerkten oder zum Behalten ausgewählten Fotos, Anzahl gelöschter Fotos und freigegebener Speicherplatz, zum Behalten ausgewählte Gruppen
@Analyseergebnisse|Dateigröße jedes Fotos, Ergebnisse zu ähnlichen Fotos, Aufzeichnungen komprimierter Kopien und durch Komprimierung gesparter Speicherplatz
@Ortsnamen|Nur iOS. Gerundete Koordinaten und Gebiets- bzw. Stadtteilnamen, bis zu 500
@Einstellungen|App-Sperre, Darstellung, Sprache, bereits angezeigte Tipps, Premiumstatus, Tarif und Ablaufdatum
---
@Fotos und Videos|Zum Finden von Fotos zum Aufräumen, zur Vollbildanzeige, Komprimierung und Verbesserung sowie zum Speichern verbesserter Fotos und komprimierter Kopien in Ihrer Mediathek.
@Fotostandort|Nur Android. Ermöglicht das Lesen der in Fotodateien gespeicherten Standortdaten, ohne dass diese entfernt werden. Diese Daten werden nicht vom Gerät gesendet.
@Face ID / Biometrie|Nur bei aktivierter App-Sperre verwendet.
@Tracking|Nur iOS. Für personalisierte Werbung. Die App funktioniert auch ohne diese Erlaubnis genauso.
@Internet|Für Werbung, das Herunterladen von Werbung für unsere Apps, Kaufprüfungen und Ortsnamen auf dem iPhone.
Die App fordert keine Standort- oder Mikrofonberechtigung an. Sie können den Fotozugriff jederzeit in den Telefoneinstellungen ändern oder deaktivieren.
---
Auf Ihrem Gerät gespeicherte Daten werden beim Löschen der App entfernt. Fotos in Ihrer Fotomediathek bleiben erhalten und können in der Fotos-App gelöscht werden. Wir bewahren selbst keine Daten auf. Von Dritten (Google, Apple, GitHub, den Stores) erhobene Daten werden nach deren Richtlinien aufbewahrt.
---
Die App richtet sich nicht vorrangig an Kinder unter 13 Jahren (unter 14 in Korea) und erhebt nicht wissentlich deren personenbezogene Daten.
---
Alle von der App gespeicherten Daten liegen auf Ihrem Gerät, sodass Sie diese selbst einsehen und löschen können. Für werbebezogene Daten können Sie personalisierte Werbung wie in Abschnitt 4 beschrieben ablehnen.
---
Datenschutzverantwortlicher: Betreiber von BySide<br>Kontakt: {email}
---
Bei Änderungen veröffentlichen wir die aktualisierte Erklärung auf dieser Seite mit einem neuen Gültigkeitsdatum. Die koreanische Version ist das Original; bei Abweichungen ist sie maßgeblich.
''')

_add('fr', 'Politique de confidentialité de Lumiclean', 'Date d’entrée en vigueur : 5 novembre 2026',
     'Lumiclean (l’« application », pour Android et iOS) respecte votre vie privée. Cette politique explique quelles informations l’application traite et comment.',
     'En bref', 'Contact', [
         'Vos fichiers photo et vidéo ne sont jamais envoyés à un serveur. Le nettoyage, la compression et l’amélioration s’effectuent sur votre téléphone.',
         'Il n’y a ni inscription ni connexion, et nous n’exploitons aucun serveur propre.',
         'Uniquement sur iPhone, lorsque vous affichez une photo en plein écran, l’application envoie ses coordonnées à Apple pour obtenir le nom du lieu.',
         'Les publicités sont diffusées par Google AdMob. Vous choisissez si elles sont personnalisées.',
     ], ['Informations collectées par l’application', 'Localisation des photos', 'Informations collectées par des tiers pour la publicité', 'Refuser les publicités personnalisées', 'Paiements (Premium)', 'Verrouillage de l’application', 'Informations stockées sur votre appareil', 'Autorisations', 'Conservation et suppression', 'Vie privée des enfants', 'Vos droits', 'Responsable de la confidentialité et contact', 'Modifications de cette politique'], '''
L’application ne nécessite ni inscription ni connexion, et nous n’exploitons aucun serveur. Vos photos, vidéos et votre historique d’utilisation ne nous sont pas envoyés.
L’application lit votre photothèque pour trouver des photos similaires, des captures d’écran et des fichiers volumineux. L’analyse, la compression et l’amélioration des photos s’effectuent <strong>sur votre appareil</strong>. Le modèle d’IA utilisé pour l’amélioration (Real-ESRGAN) est intégré à l’application : vos photos n’ont jamais besoin de quitter votre téléphone.
Sur iPhone, si l’original d’une photo à améliorer ou à compresser se trouve uniquement dans Photos iCloud, iOS peut le télécharger depuis votre iCloud. Ce transfert a lieu entre vous et Apple, sans passer par nous.
Les photos améliorées et les copies compressées sont enregistrées dans votre photothèque. Lorsque vous supprimez des photos, votre téléphone demande confirmation. Sur iOS, les photos supprimées sont déplacées dans Suppressions récentes.
---
Les photos peuvent contenir les coordonnées de leur lieu de prise de vue. Sur iPhone, lorsque vous affichez une photo en plein écran, l’application indique ce lieu par un nom de quartier. Pour cela, elle envoie <strong>uniquement les coordonnées de la photo</strong> au service de recherche de noms de lieux d’Apple. Le fichier photo et les autres informations ne sont pas envoyés.
Les noms reçus sont conservés sur votre appareil, jusqu’à 500, pour éviter de rechercher à nouveau le même lieu. Apple traite ces demandes selon sa <a href="{apple}">politique de confidentialité</a>.
Sur Android, l’application n’affiche pas les noms de lieux et ne transmet pas les coordonnées hors de votre appareil. Sur aucun appareil elle ne demande ni n’utilise votre position actuelle.
---
L’application est gratuite et utilise <strong>Google AdMob</strong>, de Google LLC, pour afficher des publicités. AdMob peut collecter et traiter les informations suivantes pour diffuser et mesurer les publicités et prévenir la fraude.
@Collectées par|Google LLC (AdMob)
@Données|Identifiant publicitaire (identifiant Android ; IDFA iOS uniquement si vous autorisez le suivi), adresse IP, informations sur l’appareil et le système d’exploitation, utilisation de l’application telle que les affichages et clics publicitaires, localisation approximative déduite de l’IP
@Finalités|Afficher des publicités et des publicités personnalisées, mesurer leur efficacité, prévenir les clics incorrects
Consultez <a href="{p1}">Comment Google utilise les informations provenant des sites ou applications qui utilisent ses services</a> et les <a href="{p2}">Règles de confidentialité de Google</a>.
L’application télécharge aussi une liste publique de promotions ainsi que des images et vidéos promotionnelles pour nos applications depuis boksday.github.io (GitHub Pages), puis les met en cache sur votre appareil. Aucune photo de votre photothèque n’est envoyée à cette fin. L’hébergeur peut recevoir votre adresse IP et les métadonnées des requêtes réseau. Toucher une promotion ouvre un lien externe vers une boutique.
---
*Android : ouvrez <strong>Paramètres → Google → Annonces</strong> sur votre téléphone pour supprimer ou réinitialiser votre identifiant publicitaire.
*iOS : vous pouvez choisir d’autoriser ou non le suivi au premier lancement, puis modifier ce choix à tout moment dans <strong>Réglages → Confidentialité et sécurité → Suivi</strong>.
*Les utilisateurs de l’EEE, du Royaume-Uni et de Suisse peuvent choisir leur consentement relatif à la confidentialité publicitaire au premier lancement. Dans certains États américains, les utilisateurs peuvent refuser la vente ou le partage de leurs données personnelles. Dans les deux cas, le choix peut être modifié à tout moment dans l’application sous <strong>Paramètres → Confidentialité des annonces</strong>.
*Si le consentement ne peut pas être confirmé ou si le suivi n’est pas autorisé, l’application demande uniquement des publicités non personnalisées.
---
Les achats Premium sont traités par l’App Store ou Google Play. Premium propose des abonnements mensuels et annuels à renouvellement automatique ainsi qu’un achat à vie non consommable. Ni l’application ni nous ne recevons de numéros de carte ou d’autres informations de paiement. L’application vérifie le droit d’accès Premium indiqué par la boutique et conserve ce statut, la formule et la date d’expiration sur votre appareil pour permettre une utilisation hors ligne.
---
Lorsque le verrouillage est activé, l’application demande Face ID, Touch ID, votre empreinte digitale ou le code de votre appareil à l’ouverture. Le système d’exploitation du téléphone effectue la vérification ; l’application sait seulement si elle a réussi. Elle ne lit ni ne conserve vos données faciales, empreintes ou code, et ne possède pas de code propre.
---
L’application conserve les informations suivantes <strong>uniquement sur votre appareil</strong>. Elles ne contiennent aucun fichier photo et nous ne pouvons pas les consulter.
@Historique du nettoyage|Identifiants des photos mises de côté pour suppression ou choisies pour être conservées, nombre de photos supprimées et espace libéré, groupes que vous avez choisi de conserver
@Résultats d’analyse|Taille de chaque photo, résultats de similarité, historique des copies compressées et espace économisé par compression
@Noms de lieux|iOS uniquement. Coordonnées arrondies et noms de quartiers, jusqu’à 500
@Paramètres|Verrouillage, apparence, langue, conseils déjà consultés, statut Premium, formule et date d’expiration
---
@Photos et vidéos|Pour trouver les photos à nettoyer, les afficher en plein écran, les compresser et les améliorer, ainsi qu’enregistrer les photos améliorées et les copies compressées dans votre photothèque.
@Localisation des photos|Android uniquement. Permet de lire la localisation contenue dans les fichiers photo sans qu’elle soit supprimée. Ces informations ne quittent pas votre appareil.
@Face ID / biométrie|Utilisés uniquement lorsque le verrouillage est activé.
@Suivi|iOS uniquement. Pour les publicités personnalisées. L’application fonctionne de la même façon si vous refusez.
@Internet|Pour les publicités, le téléchargement de promotions de nos applications, la vérification des achats et les noms de lieux sur iPhone.
L’application ne demande pas l’accès à votre position ni au microphone. Vous pouvez modifier ou désactiver l’accès aux photos à tout moment dans les réglages du téléphone.
---
Les informations stockées sur votre appareil sont supprimées lorsque vous supprimez l’application. Les photos enregistrées dans la photothèque restent présentes ; vous pouvez les supprimer dans l’application Photos. Nous ne conservons aucune information de notre côté. Les informations collectées par des tiers (Google, Apple, GitHub et les boutiques) sont conservées selon leurs politiques.
---
L’application ne s’adresse pas principalement aux enfants de moins de 13 ans (14 ans en Corée) et ne collecte pas sciemment leurs données personnelles.
---
Toutes les informations conservées par l’application se trouvent sur votre appareil : vous pouvez les consulter et les supprimer vous-même. Pour les données publicitaires, vous pouvez refuser les publicités personnalisées comme décrit à la section 4.
---
Responsable de la confidentialité : l’exploitant de BySide<br>Contact : {email}
---
En cas de modification, nous publierons la mise à jour sur cette page avec une nouvelle date d’entrée en vigueur. La version coréenne est l’original ; en cas de divergence, elle prévaut.
''')

_add('es', 'Política de privacidad de Lumiclean', 'Fecha de entrada en vigor: 5 de noviembre de 2026',
     'Lumiclean (la «aplicación», para Android e iOS) respeta tu privacidad. Esta política explica qué información trata la aplicación y cómo.',
     'De un vistazo', 'Contacto', [
         'Tus archivos de fotos y vídeos nunca se envían a un servidor. La limpieza, la compresión y la mejora se realizan en tu teléfono.',
         'No hay registro ni inicio de sesión, y no gestionamos ningún servidor propio.',
         'Solo en iPhone, al ver una foto a pantalla completa, la aplicación envía sus coordenadas a Apple para consultar el nombre del lugar.',
         'Google AdMob muestra los anuncios y tú eliges si son personalizados.',
     ], ['Información que recopila la aplicación', 'Ubicación de las fotos', 'Información que terceros recopilan para anuncios', 'Rechazar los anuncios personalizados', 'Pagos (Premium)', 'Bloqueo de la aplicación', 'Información guardada en tu dispositivo', 'Permisos', 'Conservación y eliminación', 'Privacidad de los menores', 'Tus derechos', 'Responsable de privacidad y contacto', 'Cambios en esta política'], '''
La aplicación no tiene registro ni inicio de sesión, y no gestionamos ningún servidor. No recibimos tus fotos, vídeos ni historial de uso.
La aplicación lee tu fototeca para encontrar fotos similares, capturas de pantalla y archivos grandes. El análisis, la compresión y la mejora de fotos se realizan <strong>en tu dispositivo</strong>. El modelo de IA para la mejora (Real-ESRGAN) está integrado en la aplicación, por lo que tus fotos nunca tienen que salir del teléfono.
En iPhone, si el original de una foto que mejoras o comprimes solo está en Fotos en iCloud, iOS puede descargarlo de tu iCloud. Esa transferencia se realiza entre tú y Apple y no pasa por nosotros.
Las fotos mejoradas y las copias comprimidas se guardan en tu fototeca. Al eliminar fotos, el teléfono pide confirmación y, en iOS, las fotos eliminadas pasan a Eliminado recientemente.
---
Las fotos pueden contener las coordenadas del lugar donde se tomaron. En iPhone, al ver una foto a pantalla completa, la aplicación muestra el lugar como nombre de un barrio o zona. Para ello envía <strong>solo las coordenadas de la foto</strong> al servicio de consulta de nombres de lugares de Apple. No se envían el archivo de la foto ni otros datos.
Los nombres recibidos se guardan en tu dispositivo, hasta un máximo de 500, para no consultar el mismo lugar de nuevo. Apple trata estas solicitudes según su <a href="{apple}">Política de privacidad</a>.
En Android, la aplicación no muestra nombres de lugares ni envía coordenadas fuera del dispositivo. La aplicación nunca solicita ni utiliza tu ubicación actual en ningún dispositivo.
---
La aplicación es gratuita y utiliza <strong>Google AdMob</strong> de Google LLC para mostrar anuncios. AdMob puede recopilar y tratar los siguientes datos para mostrar y medir anuncios y prevenir el fraude.
@Recopilados por|Google LLC (AdMob)
@Datos|Identificador publicitario (ID publicitario de Android; IDFA de iOS solo si permites el seguimiento), dirección IP, datos del dispositivo y del sistema operativo, uso de la aplicación como visualizaciones y clics en anuncios, ubicación aproximada deducida de la IP
@Finalidad|Mostrar anuncios y anuncios personalizados, medir su rendimiento, evitar clics no válidos
Consulta <a href="{p1}">Cómo utiliza Google la información de sitios web o aplicaciones que usan sus servicios</a> y la <a href="{p2}">Política de privacidad de Google</a>.
La aplicación también descarga una lista pública de promociones e imágenes y vídeos promocionales de nuestras aplicaciones desde boksday.github.io (GitHub Pages), y los almacena en caché en tu dispositivo. No se envían fotos de tu fototeca para este fin. El proveedor de alojamiento puede recibir tu dirección IP y metadatos de las solicitudes de red. Al tocar una promoción se abre un enlace externo a una tienda.
---
*Android: ve a <strong>Ajustes → Google → Anuncios</strong> en tu teléfono para eliminar o restablecer el identificador publicitario.
*iOS: puedes elegir si permites el seguimiento al iniciar por primera vez y cambiarlo cuando quieras en <strong>Ajustes → Privacidad y seguridad → Rastreo</strong>.
*Los usuarios del EEE, Reino Unido y Suiza pueden elegir su consentimiento de privacidad publicitaria al iniciar por primera vez. Los usuarios de algunos estados de EE. UU. pueden rechazar la venta o el intercambio de datos personales. En ambos casos se puede cambiar la elección en cualquier momento en <strong>Ajustes → Privacidad de anuncios</strong> de la aplicación.
*Si no se puede confirmar el consentimiento o no se permite el seguimiento, la aplicación solo solicita anuncios no personalizados.
---
Las compras Premium las procesa el App Store o Google Play. Premium ofrece suscripciones mensuales y anuales con renovación automática y una compra de por vida no consumible. Ni la aplicación ni nosotros recibimos números de tarjeta ni otros datos de pago. La aplicación comprueba el derecho a Premium que comunica la tienda y guarda el estado, el plan y la fecha de vencimiento en tu dispositivo para usarlo sin conexión.
---
Cuando el bloqueo está activado, la aplicación pide Face ID, Touch ID, huella dactilar o el código del dispositivo al abrirla. El sistema operativo del teléfono realiza la comprobación y la aplicación solo recibe si fue correcta. No lee ni guarda datos faciales, huellas ni tu código, y no tiene un código propio.
---
La aplicación guarda lo siguiente <strong>solo en tu dispositivo</strong>. Estos datos no contienen archivos de fotos y no podemos verlos.
@Historial de limpieza|Identificadores de fotos apartadas para eliminar o elegidas para conservar, número de fotos eliminadas y espacio liberado, grupos elegidos para conservar
@Resultados de análisis|Tamaño de cada foto, resultados de fotos similares, registro de copias comprimidas y espacio ahorrado con la compresión
@Nombres de lugares|Solo iOS. Coordenadas redondeadas y nombres de barrios o zonas, hasta 500
@Ajustes|Bloqueo, apariencia, idioma, consejos que has visto, estado de Premium, plan y fecha de vencimiento
---
@Fotos y vídeos|Para encontrar fotos que limpiar, verlas a pantalla completa, comprimirlas y mejorarlas, y guardar fotos mejoradas y copias comprimidas en tu fototeca.
@Ubicación de las fotos|Solo Android. Permite leer la ubicación guardada en los archivos de fotos sin que se elimine. Estos datos no salen del dispositivo.
@Face ID / biometría|Solo se utiliza cuando el bloqueo está activado.
@Seguimiento|Solo iOS. Para anuncios personalizados. La aplicación funciona igual si no lo permites.
@Internet|Para anuncios, descargar promociones de nuestras aplicaciones, comprobar compras y consultar nombres de lugares en iPhone.
La aplicación no solicita permisos de ubicación ni de micrófono. Puedes cambiar o desactivar el acceso a las fotos en cualquier momento en los ajustes del teléfono.
---
La información guardada en tu dispositivo se elimina al borrar la aplicación. Las fotos guardadas en la fototeca permanecen y puedes borrarlas en la aplicación Fotos. Nosotros no conservamos información propia. Los datos recopilados por terceros (Google, Apple, GitHub y las tiendas) se conservan según sus políticas.
---
La aplicación no está dirigida principalmente a menores de 13 años (14 en Corea) y no recopila deliberadamente sus datos personales.
---
Toda la información que guarda la aplicación está en tu dispositivo, así que puedes revisarla y eliminarla. Para los datos publicitarios, puedes rechazar los anuncios personalizados como se describe en la sección 4.
---
Responsable de privacidad: el operador de BySide<br>Contacto: {email}
---
Si cambia esta política, publicaremos la actualización en esta página con una nueva fecha de entrada en vigor. La versión coreana es la original; si hay diferencias, prevalece la versión coreana.
''')

_add('pt', 'Política de Privacidade do Lumiclean', 'Data de vigência: 5 de novembro de 2026',
     'O Lumiclean (o “aplicativo”, para Android e iOS) respeita sua privacidade. Esta política explica quais informações o aplicativo trata e como.',
     'Visão geral', 'Contato', [
         'Seus arquivos de fotos e vídeos nunca são enviados a um servidor. A limpeza, a compressão e a melhoria são feitas no seu celular.',
         'Não há cadastro nem login, e não mantemos servidor próprio.',
         'Somente no iPhone, ao ver uma foto em tela cheia, o aplicativo envia as coordenadas da foto à Apple para consultar o nome do local.',
         'Os anúncios são exibidos pelo Google AdMob, e você escolhe se serão personalizados.',
     ], ['Informações coletadas pelo aplicativo', 'Localização das fotos', 'Informações coletadas por terceiros para anúncios', 'Como recusar anúncios personalizados', 'Pagamentos (Premium)', 'Bloqueio do aplicativo', 'Informações armazenadas no dispositivo', 'Permissões', 'Retenção e exclusão', 'Privacidade de crianças', 'Seus direitos', 'Responsável pela privacidade e contato', 'Alterações nesta política'], '''
O aplicativo não tem cadastro nem login, e não mantemos servidor. Suas fotos, vídeos e histórico de uso não são enviados a nós.
O aplicativo lê sua biblioteca de fotos para encontrar fotos semelhantes, capturas de tela e arquivos grandes. A análise, a compressão e a melhoria de fotos acontecem <strong>no seu dispositivo</strong>. O modelo de IA usado na melhoria (Real-ESRGAN) está integrado ao aplicativo, então suas fotos nunca precisam sair do celular.
No iPhone, se o original de uma foto que você melhora ou comprime estiver apenas no Fotos do iCloud, o iOS poderá baixá-lo do seu iCloud. Essa transferência ocorre entre você e a Apple e não passa por nós.
As fotos melhoradas e as cópias comprimidas são salvas na sua biblioteca. Ao excluir fotos, o celular pede confirmação e, no iOS, as fotos excluídas vão para Apagados.
---
Fotos podem conter as coordenadas de onde foram tiradas. No iPhone, ao ver uma foto em tela cheia, o aplicativo mostra o local como nome de um bairro ou região. Para isso, envia <strong>somente as coordenadas da foto</strong> ao serviço de consulta de nomes de locais da Apple. O arquivo da foto e outras informações não são enviados.
Até 500 nomes de locais recebidos ficam no dispositivo para evitar consultas repetidas do mesmo local. A Apple trata essas solicitações conforme a <a href="{apple}">Política de Privacidade da Apple</a>.
No Android, o aplicativo não mostra nomes de locais nem envia coordenadas para fora do dispositivo. Em nenhum dispositivo o aplicativo solicita ou usa sua localização atual.
---
O aplicativo é gratuito e usa o <strong>Google AdMob</strong>, da Google LLC, para exibir anúncios. O AdMob pode coletar e tratar as seguintes informações para fornecer e medir anúncios e prevenir fraudes.
@Coletadas por|Google LLC (AdMob)
@Dados|ID de publicidade (ID de publicidade do Android; IDFA do iOS somente se você permitir rastreamento), endereço IP, informações do dispositivo e sistema operacional, uso do aplicativo como visualizações e cliques em anúncios, localização aproximada inferida do IP
@Finalidade|Exibir anúncios e anúncios personalizados, medir o desempenho dos anúncios, impedir cliques inválidos
Veja <a href="{p1}">Como o Google usa informações de sites ou aplicativos que utilizam nossos serviços</a> e a <a href="{p2}">Política de Privacidade do Google</a>.
O aplicativo também baixa uma lista pública de promoções e imagens e vídeos promocionais dos nossos aplicativos de boksday.github.io (GitHub Pages), armazenando-os em cache no dispositivo. Nenhuma foto da sua biblioteca é enviada para esse fim. O provedor de hospedagem pode receber seu endereço IP e metadados das solicitações de rede. Ao tocar em uma promoção, abre-se um link externo para uma loja.
---
*Android: acesse <strong>Configurações → Google → Anúncios</strong> no celular para excluir ou redefinir seu ID de publicidade.
*iOS: você pode escolher se permite rastreamento ao abrir pela primeira vez e mudar a escolha a qualquer momento em <strong>Ajustes → Privacidade e Segurança → Rastreamento</strong>.
*Usuários no EEE, Reino Unido e Suíça podem escolher seu consentimento de privacidade de anúncios na primeira abertura. Usuários de alguns estados dos EUA podem recusar a venda ou o compartilhamento de dados pessoais. Em ambos os casos, a escolha pode ser alterada a qualquer momento no aplicativo em <strong>Configurações → Privacidade de anúncios</strong>.
*Se não for possível confirmar o consentimento ou se o rastreamento não for permitido, o aplicativo solicita apenas anúncios não personalizados.
---
As compras Premium são processadas pela App Store ou pelo Google Play. O Premium oferece assinaturas mensais e anuais com renovação automática e uma compra vitalícia não consumível. Nem o aplicativo nem nós recebemos números de cartão ou outros dados de pagamento. O aplicativo verifica o direito de acesso Premium informado pela loja e salva o status, o plano e a data de expiração no dispositivo para uso offline.
---
Quando o bloqueio está ativado, o aplicativo solicita Face ID, Touch ID, impressão digital ou o código do dispositivo ao ser aberto. O sistema operacional faz a verificação e o aplicativo recebe apenas se ela foi bem-sucedida. O aplicativo nunca lê nem armazena dados faciais, impressões digitais ou o código e não possui código próprio.
---
O aplicativo guarda as seguintes informações <strong>somente no seu dispositivo</strong>. Elas não contêm arquivos de fotos e não podemos vê-las.
@Histórico de limpeza|Identificadores de fotos separadas para excluir ou escolhidas para manter, quantidade de fotos excluídas e espaço liberado, grupos escolhidos para manter
@Resultados da análise|Tamanho de cada foto, resultados de fotos semelhantes, registros de cópias comprimidas e espaço economizado com a compressão
@Nomes de locais|Somente iOS. Coordenadas arredondadas e nomes de bairros ou regiões, até 500
@Configurações|Bloqueio, aparência, idioma, dicas já vistas, status Premium, plano e data de expiração
---
@Fotos e vídeos|Para encontrar fotos a limpar, visualizá-las em tela cheia, comprimir e melhorar, além de salvar fotos melhoradas e cópias comprimidas na biblioteca.
@Localização das fotos|Somente Android. Permite ler a localização contida nos arquivos de fotos sem que ela seja removida. Essas informações não saem do dispositivo.
@Face ID / biometria|Usados apenas quando o bloqueio está ativado.
@Rastreamento|Somente iOS. Para anúncios personalizados. O aplicativo funciona da mesma forma se você não permitir.
@Internet|Para anúncios, baixar promoções dos nossos aplicativos, verificar compras e consultar nomes de locais no iPhone.
O aplicativo não pede permissões de localização ou microfone. Você pode alterar ou desativar o acesso às fotos a qualquer momento nas configurações do celular.
---
As informações armazenadas no dispositivo são removidas quando você exclui o aplicativo. As fotos salvas na biblioteca permanecem e podem ser excluídas no aplicativo Fotos. Não guardamos informações próprias. Dados coletados por terceiros (Google, Apple, GitHub e as lojas) são mantidos conforme as políticas deles.
---
O aplicativo não é direcionado principalmente a menores de 13 anos (14 na Coreia) e não coleta intencionalmente seus dados pessoais.
---
Todas as informações que o aplicativo guarda estão no seu dispositivo, e você pode consultá-las e excluí-las. Para dados de anúncios, você pode recusar anúncios personalizados conforme a seção 4.
---
Responsável pela privacidade: operador do BySide<br>Contato: {email}
---
Se esta política mudar, publicaremos a atualização nesta página com uma nova data de vigência. A versão coreana é a original; em caso de divergências, ela prevalece.
''')

_add('it', 'Informativa sulla privacy di Lumiclean', 'Data di entrata in vigore: 5 novembre 2026',
     'Lumiclean (l’“app”, per Android e iOS) rispetta la tua privacy. Questa informativa spiega quali dati tratta l’app e come.',
     'In breve', 'Contatti', [
         'I tuoi file di foto e video non vengono mai inviati a un server. Pulizia, compressione e miglioramento avvengono sul tuo telefono.',
         'Non sono previsti registrazione o accesso e non gestiamo server propri.',
         'Solo su iPhone, quando visualizzi una foto a schermo intero, l’app ne invia le coordinate ad Apple per cercare il nome del luogo.',
         'Gli annunci sono mostrati da Google AdMob e sei tu a scegliere se personalizzarli.',
     ], ['Dati raccolti dall’app', 'Posizione delle foto', 'Dati raccolti da terzi per gli annunci', 'Rifiutare gli annunci personalizzati', 'Pagamenti (Premium)', 'Blocco dell’app', 'Dati memorizzati sul dispositivo', 'Autorizzazioni', 'Conservazione ed eliminazione', 'Privacy dei minori', 'I tuoi diritti', 'Responsabile della privacy e contatti', 'Modifiche all’informativa'], '''
L’app non prevede registrazione o accesso e non gestiamo alcun server. Le tue foto, i video e la cronologia di utilizzo non ci vengono inviati.
L’app legge la tua libreria fotografica per trovare foto simili, screenshot e file di grandi dimensioni. Analisi, compressione e miglioramento delle foto avvengono <strong>sul tuo dispositivo</strong>. Il modello di IA per il miglioramento (Real-ESRGAN) è integrato nell’app, quindi le tue foto non devono mai lasciare il telefono.
Su iPhone, se l’originale di una foto da migliorare o comprimere è disponibile solo in Foto di iCloud, iOS può scaricarlo dal tuo iCloud. Il trasferimento avviene tra te e Apple e non passa attraverso di noi.
Le foto migliorate e le copie compresse vengono salvate nella libreria fotografica. Quando elimini foto, il telefono chiede conferma e, su iOS, le foto eliminate vengono spostate in Eliminati di recente.
---
Le foto possono contenere le coordinate del luogo in cui sono state scattate. Su iPhone, quando visualizzi una foto a schermo intero, l’app mostra il nome del quartiere o della zona. Per farlo invia <strong>solo le coordinate della foto</strong> al servizio di ricerca dei nomi dei luoghi di Apple. Il file della foto e gli altri dati non vengono inviati.
Fino a 500 nomi di luoghi ricevuti vengono conservati sul dispositivo per evitare di cercare di nuovo lo stesso luogo. Apple tratta queste richieste secondo la propria <a href="{apple}">Informativa sulla privacy</a>.
Su Android, l’app non mostra i nomi dei luoghi e non invia coordinate fuori dal dispositivo. Su nessun dispositivo l’app richiede o utilizza la tua posizione attuale.
---
L’app è gratuita e utilizza <strong>Google AdMob</strong> di Google LLC per mostrare annunci. AdMob può raccogliere e trattare i seguenti dati per pubblicare e misurare gli annunci e prevenire frodi.
@Raccolti da|Google LLC (AdMob)
@Dati|ID pubblicitario (ID pubblicitario Android; IDFA iOS solo se autorizzi il tracciamento), indirizzo IP, informazioni sul dispositivo e sul sistema operativo, utilizzo dell’app come visualizzazioni e clic sugli annunci, posizione approssimativa dedotta dall’IP
@Finalità|Mostrare annunci e annunci personalizzati, misurarne il rendimento, prevenire clic non validi
Consulta <a href="{p1}">Come Google utilizza le informazioni di siti o app che usano i suoi servizi</a> e le <a href="{p2}">Norme sulla privacy di Google</a>.
L’app scarica inoltre un elenco pubblico di promozioni e immagini e video promozionali delle nostre app da boksday.github.io (GitHub Pages) e li memorizza nella cache sul dispositivo. A questo scopo non vengono inviate foto della tua libreria. Il fornitore di hosting può ricevere il tuo indirizzo IP e i metadati delle richieste di rete. Toccando una promozione si apre un collegamento esterno a uno store.
---
*Android: vai in <strong>Impostazioni → Google → Annunci</strong> sul telefono per eliminare o reimpostare l’ID pubblicitario.
*iOS: puoi scegliere se autorizzare il tracciamento al primo avvio e modificare la scelta in qualsiasi momento in <strong>Impostazioni → Privacy e sicurezza → Tracciamento</strong>.
*Gli utenti nello SEE, nel Regno Unito e in Svizzera possono scegliere il consenso relativo alla privacy degli annunci al primo avvio. Gli utenti di alcuni Stati degli USA possono rifiutare la vendita o la condivisione dei dati personali. In entrambi i casi, puoi modificare la scelta in qualsiasi momento nell’app in <strong>Impostazioni → Privacy degli annunci</strong>.
*Se il consenso non può essere confermato o il tracciamento non è consentito, l’app richiede solo annunci non personalizzati.
---
Gli acquisti Premium vengono elaborati dall’App Store o da Google Play. Premium offre abbonamenti mensili e annuali con rinnovo automatico e un acquisto a vita non consumabile. Né l’app né noi riceviamo numeri di carta o altri dati di pagamento. L’app verifica il diritto di accesso a Premium comunicato dallo store e salva stato, piano e data di scadenza sul dispositivo per l’utilizzo offline.
---
Quando il blocco è attivo, all’apertura l’app richiede Face ID, Touch ID, impronta digitale o codice del dispositivo. Il sistema operativo del telefono esegue la verifica e l’app riceve solo l’esito. Non legge né conserva dati del volto, impronte o codice e non dispone di un codice proprio.
---
L’app conserva quanto segue <strong>solo sul tuo dispositivo</strong>. Questi dati non includono file di foto e non possiamo consultarli.
@Cronologia della pulizia|Identificativi delle foto messe da parte per l’eliminazione o scelte da conservare, numero di foto eliminate e spazio liberato, gruppi scelti da conservare
@Risultati dell’analisi|Dimensione di ogni foto, risultati delle foto simili, registrazioni delle copie compresse e spazio risparmiato con la compressione
@Nomi dei luoghi|Solo iOS. Coordinate arrotondate e nomi di quartieri o zone, fino a 500
@Impostazioni|Blocco, aspetto, lingua, suggerimenti già visualizzati, stato Premium, piano e data di scadenza
---
@Foto e video|Per trovare foto da pulire, visualizzarle a schermo intero, comprimerle e migliorarle, e salvare foto migliorate e copie compresse nella libreria.
@Posizione delle foto|Solo Android. Consente di leggere la posizione contenuta nei file delle foto senza che venga rimossa. Questi dati non vengono inviati fuori dal dispositivo.
@Face ID / biometria|Usati solo quando il blocco dell’app è attivo.
@Tracciamento|Solo iOS. Per gli annunci personalizzati. L’app funziona allo stesso modo se non lo autorizzi.
@Internet|Per gli annunci, il download delle promozioni delle nostre app, la verifica degli acquisti e i nomi dei luoghi su iPhone.
L’app non richiede autorizzazioni per posizione o microfono. Puoi modificare o disattivare l’accesso alle foto in qualsiasi momento nelle impostazioni del telefono.
---
I dati memorizzati sul dispositivo vengono rimossi quando elimini l’app. Le foto salvate nella libreria rimangono e puoi eliminarle nell’app Foto. Non conserviamo dati per conto nostro. I dati raccolti da terzi (Google, Apple, GitHub e gli store) vengono conservati secondo le rispettive informative.
---
L’app non è rivolta principalmente a minori di 13 anni (14 in Corea) e non raccoglie consapevolmente i loro dati personali.
---
Tutti i dati conservati dall’app sono sul tuo dispositivo, quindi puoi consultarli ed eliminarli autonomamente. Per i dati pubblicitari puoi rifiutare gli annunci personalizzati come descritto nella sezione 4.
---
Responsabile della privacy: il gestore di BySide<br>Contatti: {email}
---
In caso di modifiche, pubblicheremo l’aggiornamento su questa pagina con una nuova data di entrata in vigore. La versione coreana è l’originale; in caso di differenze, prevale la versione coreana.
''')

_add('tr', 'Lumiclean Gizlilik Politikası', 'Yürürlük tarihi: 5 Kasım 2026',
     'Lumiclean (Android ve iOS için “Uygulama”) gizliliğinize saygı duyar. Bu politika, Uygulamanın hangi bilgileri nasıl işlediğini açıklar.',
     'Kısa bakış', 'İletişim', [
         'Fotoğraf ve video dosyalarınız hiçbir zaman bir sunucuya gönderilmez. Temizleme, sıkıştırma ve iyileştirme telefonunuzda yapılır.',
         'Kayıt veya oturum açma yoktur; bize ait bir sunucu işletmeyiz.',
         'Yalnızca iPhone’da bir fotoğrafı tam ekran görüntülediğinizde Uygulama, yer adını sorgulamak için fotoğrafın koordinatlarını Apple’a gönderir.',
         'Reklamlar Google AdMob tarafından gösterilir; kişiselleştirilip kişiselleştirilmeyeceğini siz seçersiniz.',
     ], ['Uygulamanın topladığı bilgiler', 'Fotoğraf konumu', 'Üçüncü tarafların reklamlar için topladığı bilgiler', 'Kişiselleştirilmiş reklamları reddetme', 'Ödemeler (Premium)', 'Uygulama kilidi', 'Cihazınızda saklanan bilgiler', 'İzinler', 'Saklama ve silme', 'Çocukların gizliliği', 'Haklarınız', 'Gizlilik sorumlusu ve iletişim', 'Bu politikadaki değişiklikler'], '''
Uygulamada kayıt veya oturum açma yoktur ve sunucu işletmeyiz. Fotoğraflarınız, videolarınız ve kullanım geçmişiniz bize gönderilmez.
Uygulama, benzer fotoğrafları, ekran görüntülerini ve büyük dosyaları bulmak için fotoğraf arşivinizi okur. Fotoğraf analizi, sıkıştırma ve iyileştirme <strong>cihazınızda</strong> yapılır. İyileştirme için kullanılan yapay zekâ modeli (Real-ESRGAN) Uygulamaya dahildir; fotoğraflarınızın telefonunuzdan çıkması gerekmez.
iPhone’da iyileştirdiğiniz veya sıkıştırdığınız bir fotoğrafın aslı yalnızca iCloud Fotoğrafları’nda bulunuyorsa iOS bunu iCloud’unuzdan indirebilir. Bu aktarım sizinle Apple arasında gerçekleşir, bizim üzerimizden geçmez.
İyileştirilen fotoğraflar ve sıkıştırılan kopyalar fotoğraf arşivinize kaydedilir. Fotoğrafları sildiğinizde telefonunuz onay ister; iOS’ta silinen fotoğraflar Son Silinenler’e taşınır.
---
Fotoğraflar çekildikleri yerin koordinatlarını içerebilir. iPhone’da bir fotoğrafı tam ekran görüntülediğinizde Uygulama, yeri mahalle veya bölge adı olarak gösterir. Bunun için Apple’ın yer adı sorgulama hizmetine <strong>yalnızca fotoğrafın koordinatlarını</strong> gönderir. Fotoğraf dosyası ve diğer bilgiler gönderilmez.
Alınan yer adları, aynı yeri tekrar sorgulamamak için en fazla 500 adet olmak üzere cihazınızda saklanır. Apple bu istekleri <a href="{apple}">Apple Gizlilik Politikası</a> uyarınca işler.
Android’de Uygulama yer adlarını göstermez ve koordinatları cihazınızın dışına göndermez. Uygulama hiçbir cihazda mevcut konumunuzu istemez veya kullanmaz.
---
Uygulama ücretsizdir ve reklam göstermek için Google LLC’nin <strong>Google AdMob</strong> hizmetini kullanır. AdMob, reklam sunmak, ölçüm yapmak ve sahtekârlığı önlemek için aşağıdaki bilgileri toplayabilir ve işleyebilir.
@Toplayan|Google LLC (AdMob)
@Veriler|Reklam kimliği (Android reklam kimliği; iOS IDFA yalnızca takibe izin verirseniz), IP adresi, cihaz ve işletim sistemi bilgileri, reklam görüntüleme ve tıklama gibi uygulama kullanımı, IP adresinden çıkarılan yaklaşık konum
@Amaç|Reklam ve kişiselleştirilmiş reklam gösterme, reklam performansını ölçme, geçersiz tıklamaları önleme
<a href="{p1}">Google’ın hizmetlerini kullanan site veya uygulamalardaki bilgileri nasıl kullandığı</a> ve <a href="{p2}">Google Gizlilik Politikası</a> sayfalarına bakabilirsiniz.
Uygulama ayrıca boksday.github.io (GitHub Pages) adresinden uygulamalarımıza ait herkese açık bir tanıtım listesi, tanıtım görselleri ve videoları indirip cihazınızda önbelleğe alır. Bu amaçla arşivinizdeki hiçbir fotoğraf gönderilmez. Barındırma sağlayıcısı IP adresinizi ve ağ isteği meta verilerini alabilir. Bir tanıtıma dokunmak harici bir mağaza bağlantısı açar.
---
*Android: reklam kimliğinizi silmek veya sıfırlamak için telefonunuzda <strong>Ayarlar → Google → Reklamlar</strong> yolunu izleyin.
*iOS: ilk açılışta takibe izin verip vermeyeceğinizi seçebilir, daha sonra <strong>Ayarlar → Gizlilik ve Güvenlik → Takip</strong> bölümünden değiştirebilirsiniz.
*AEA, Birleşik Krallık ve İsviçre’deki kullanıcılar ilk açılışta reklam gizliliği onaylarını seçebilir. ABD’nin bazı eyaletlerindeki kullanıcılar kişisel bilgilerin satışını veya paylaşımını reddedebilir. Her iki durumda da seçiminizi Uygulamadaki <strong>Ayarlar → Reklam gizliliği ayarları</strong> bölümünden dilediğiniz zaman değiştirebilirsiniz.
*Onay doğrulanamıyorsa veya takibe izin verilmemişse Uygulama yalnızca kişiselleştirilmemiş reklamlar ister.
---
Premium satın alımları App Store veya Google Play tarafından işlenir. Premium, otomatik yenilenen aylık ve yıllık abonelikler ile tüketilmeyen bir ömür boyu satın alma seçeneği sunar. Uygulama ve biz, kart numaralarını veya diğer ödeme bilgilerini almayız. Uygulama, mağazanın bildirdiği Premium erişim hakkını kontrol eder; durumu, planı ve sona erme tarihini çevrimdışı kullanım için cihazınıza kaydeder.
---
Uygulama kilidi açıkken Uygulama açıldığında Face ID, Touch ID, parmak izi veya cihaz parolası ister. Kontrolü telefonunuzun işletim sistemi yapar; Uygulama yalnızca işlemin başarılı olup olmadığını öğrenir. Yüz veya parmak izi verilerinizi ya da parolanızı okumaz veya saklamaz; kendi parolası da yoktur.
---
Uygulama aşağıdaki bilgileri <strong>yalnızca cihazınızda</strong> saklar. Bunlar fotoğraf dosyası içermez ve biz bu bilgileri göremeyiz.
@Temizleme geçmişi|Silmek üzere ayırdığınız veya tutmayı seçtiğiniz fotoğrafların kimlikleri, silinen fotoğraf sayısı ve açılan alan, tutmayı seçtiğiniz gruplar
@Analiz sonuçları|Her fotoğrafın dosya boyutu, benzer fotoğraf sonuçları, sıkıştırılmış kopya kayıtları ve sıkıştırmayla kazanılan alan
@Yer adları|Yalnızca iOS. Yuvarlanmış koordinatlar ve mahalle veya bölge adları, en fazla 500
@Ayarlar|Uygulama kilidi, görünüm, dil, gördüğünüz ipuçları, Premium durumu, plan ve sona erme tarihi
---
@Fotoğraf ve videolar|Temizlenecek fotoğrafları bulmak, tam ekran görüntülemek, sıkıştırmak ve iyileştirmek; iyileştirilen fotoğrafları ve sıkıştırılmış kopyaları arşive kaydetmek için kullanılır.
@Fotoğraf konumu|Yalnızca Android. Fotoğraf dosyalarındaki konumu kaldırılmadan okumayı sağlar. Bu bilgiler cihazınızın dışına gönderilmez.
@Face ID / biyometri|Yalnızca Uygulama kilidi açıkken kullanılır.
@Takip|Yalnızca iOS. Kişiselleştirilmiş reklamlar için kullanılır. İzin vermeseniz de Uygulama aynı şekilde çalışır.
@İnternet|Reklamlar, uygulamalarımızın tanıtımlarını indirme, satın alma kontrolleri ve iPhone’da yer adları için kullanılır.
Uygulama konum veya mikrofon izni istemez. Telefon ayarlarından fotoğraf erişimini dilediğiniz zaman değiştirebilir veya kapatabilirsiniz.
---
Cihazda saklanan bilgiler Uygulamayı sildiğinizde kaldırılır. Fotoğraf arşivine kaydedilen fotoğraflar kalır; bunları Fotoğraflar uygulamasından silebilirsiniz. Biz ayrıca bilgi saklamayız. Üçüncü tarafların (Google, Apple, GitHub ve mağazalar) topladığı bilgiler kendi politikalarına göre saklanır.
---
Uygulama öncelikli olarak 13 yaşından küçük çocuklara (Kore’de 14) yönelik değildir ve onların kişisel bilgilerini bilerek toplamaz.
---
Uygulamanın sakladığı tüm bilgiler cihazınızdadır; bunları kendiniz inceleyebilir ve silebilirsiniz. Reklam verileri için 4. bölümde açıklandığı şekilde kişiselleştirilmiş reklamları reddedebilirsiniz.
---
Gizlilik sorumlusu: BySide işletmecisi<br>İletişim: {email}
---
Bu politika değişirse güncellemeyi yeni yürürlük tarihiyle birlikte bu sayfada yayımlarız. Korece sürüm asıldır; sürümler arasında farklılık olursa Korece sürüm geçerlidir.
''')

from lumiclean_privacy_ar_ru import register

register(_add)
