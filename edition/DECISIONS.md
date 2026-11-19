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

## Numbering
- **N1. Sūtra numbers and serial order.**
  - Sūtra numbers follow the Aṣṭādhyāyī. Twelve wrong numbers were corrected.
  - SK 3187 and 3189 were in the wrong order: अवोदैधौद्म… stands before अकर्तरि च कारके, and घञि च after it.
- **N2. Dhātu numbers.** These follow the Dhātupāṭha data, so the dhātus run 1–1992 without a gap.
  - The base had skipped 1209 (असु).
  - It had put व्रज and मार्ग under one number.
  - It had numbered केत, the variant reading after पाठान्तरम्, as a root.

## Open
- 53 dhātu names differ from the Dhātupāṭha data only in spelling. Examples are 1605 बिल / विल and 1771 वल्ह / बल्ह. They wait for the reading of the print.
- A second word-by-word pass against the 1910 print is still to be done, to catch faults that both typed texts share.
