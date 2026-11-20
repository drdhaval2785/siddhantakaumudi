# Editorial decisions

## Authority and scope
- **E1. Order of witnesses.** The print with the Bālamanoramā (1910) comes first, then the 1908 Nirṇaya Sāgara print, then the Kāśikā and Bālamanoramā wording. The two typed lineages (this text and ashtadhyayi-data) are not independent.
- **E2. What gets changed.** Only clear faults are corrected: typing errors, damage from old fonts, wrong numbers, and stray characters. Variant readings between prints are recorded, not imposed.
- **E3. One fault per commit.** Each commit names the SK serial, the old and new reading, and the ground.

## Spelling (from the uniformity audit)
- **U1. Nasal before a stop inside a word.** It is written as the class nasal (8.4.58).
  - A nasal at the end of a word keeps the anusvāra.
  - The entries of 8.3 and 8.4 keep both spellings, because their examples need them.
  - The Vedic and svara sections (SK 3387 on) follow the print.
- **U2. The vowel ḷ.** It is written ऌ as a full vowel and ॢ as a vowel sign, as in कॢप्त by 8.2.18 कृपो रो लः, ऌदित्, ऌकार, and ऌति ऌ वा. लृ is kept where it is l + ṛ:
  - The lakāra names लृट्, लृङ्. Their vowels after ल run a, i, u, ṛ, e, o.
  - Roots with an ṛ marker, such as वेलृ and खेलृ. These are ṛdit for 7.4.2 नाग्लोपिशास्वृदिताम्. Writing them with ॢ would make them ḷdit, and they would wrongly take aṅ by 3.1.55 पुषादिद्युताद्यॢदितः परस्मैपदेषु.
- **U3.** Jihvāmūlīya and upadhmānīya are written ᳵ and ᳶ (U+1CF5, U+1CF6).
- **U4.** Quotation marks are a plain `'`.
- **U5.** SK cross-references use ASCII digits. Devanāgarī digits remain only as Vedic accent marks.
- **U6. Old-font damage.** The damage is reversed: an i-sign typed before a conjunct (कृदि्भः → कृद्भिः) and composite glyphs (अा → आ, एे → ऐ).
- **U7. ZWNJ.** The ZWNJ after a final virāma is removed.
- **U8. Pratīka dash.** A pratīka quoted with a cross-reference is joined to the number by one hyphen (उपसर्गादृति-74). The introductory dash after अत्र भाष्यम्, तदाहुः, स्मरन्ति हि and उक्तं च is an em dash.

- **U9. Pluta and split इति.** The pluta mark is written with the Devanāgarī numeral ३ (याति३). Numerals that count repeated forms (युवाभ्याम् 3) stay in ASCII. Where an SK number split a pratīka from its इति, the full pratīka is restored and इति is written separately (घेर्ङिति 245 इति).

## Numbering
- **N1. Sūtra numbers and serial order.**
  - Sūtra numbers follow the Aṣṭādhyāyī. Twelve wrong numbers were corrected.
  - SK 3187 and 3189 were in the wrong order: अवोदैधौद्म… stands before अकर्तरि च कारके, and घञि च after it.
- **N2. Dhātu numbers.** These follow the Dhātupāṭha data, so the dhātus run 1–1992 without a gap.
  - The base had skipped 1209 (असु).
  - It had put व्रज and मार्ग under one number.
  - It had numbered केत, the variant reading after पाठान्तरम्, as a root.

## Doubtful readings (settled 2026-11-20)
- **D1. Emended** (each on grammatical ground):
  - SK 2894 वोढुं वशक्यो → वोढुं शक्यो: stray व; वोढव्यः is glossed as वोढुं शक्यः (शकि लिङ् च, 3.3.172).
  - SK 2687 उपसर्गेन समा → उपसर्गेण समा: णत्व by रषाभ्यां नो णः समानपदे (8.4.1).
  - SK 2387 इतात्वं → इतीत्वं: घुमास्थागापाजहातिसां हलि (6.4.66) gives ईत्व, read इति + ईत्वं.
  - SK 3650 अन्त्रेति → अन्यत्रेति: pratīka of the vārttika सतिशिष्टस्वरबलीयस्त्वमन्यत्र विकरणेभ्यः.
  - SK 836 र्दानीयरूपा → दर्शनीयरूपा: the series दर्शनीयकल्पा … दर्शनीयपाशा; Tattvabodhinī दर्शनीयरूपेत्यादि.
  - Dhātu 1739 अञ्चु निशेषणे → विशेषणे, and 1851 धृष प्रहसने → प्रसहने: Dhātupāṭha.
- **D2. Kept**:
  - SK 836 बहुथा: थाल् (प्रकारवचने थाल्, 5.3.23) applies to बहु under किंसर्वनामबहुभ्यः (5.3.2), after pumvadbhāva of बह्वी; the word is attested in the kośas (Apte: बहुथा "in several ways").
  - Dhātu 1735 शृधु प्रहसने: the Dhātupāṭha data itself records both प्रहसने and प्रसहने.
  - The other dhātu-name differences from the Dhātupāṭha data are notation (dental न् and छ् for the nasal and च्छ in the data) or recension variants that the Kaumudī's own forms support (बहि: बंहते; ऊर्ज, चूर्ण, घूर्ण, बिल, वल्ह, क्षिवु, रघि, दण्डनिपातने). They are the Kaumudī's readings and stay.
- **D3.** Readings reported during the encoding of SK 1680–1690: शूर्पाभ्यां (1683) and चात्वारिंशत्कः (1687) emended; त्रिंशत्कः (1689) emended from the typed त्रिंशतिकः, which has no derivation (कन् takes no इट् here; Kāśikā त्रिंशत्कः), the typed reading being kept on record here; आर्धकौडबिकम् (1685) kept, since कुडब/कुडव is a ब/व spelling variant and the Bālamanoramā spells it with ब as well.

## Upstream issues (drdhaval2785/siddhantakaumudi, read 2026-11-20)
- **I1.** #74 SK 325 दादेर्धातोर्धः → दादेर्धातोर्घः (8.2.32 substitutes घ). Fixed.
- **I2.** #73 SK 311 यस्येति च number 6-4-184 → 6-4-148: already right in this text. #69 (ॠदुपध), #58 (ई३) and #71 were fixed upstream before the fork.
- **I3.** #64 special markup. The three passages had their numbers turned into SK links. Now the Liṅgānuśāsana citations read (लि १२१) and (लि १७) (त्वान्तं क्लीबम् is Liṅgānuśāsana 121 त्वष्यञौ तद्धितौ, not 120 निष्ठा च), the Māheśvarasūtra citation reads (मा.सू.-१४), and sk.json gives them as `cite` segments; the verse vārttika under SK 1088 carries `sloka: true`.
- **I4.** Not text issues, left as they are: #3 (n-gram check; superseded by the print checks here), #21 (links to dhātuvṛtti sites), #24 (DTD), #25 (CSS), #66 (Stardict placeholder).

## Open
- A second word-by-word pass against the 1910 print is still to be done, to catch faults that both typed texts share.
