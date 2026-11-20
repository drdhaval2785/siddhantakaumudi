# Provenance and rights

## Base text
- **Typed text:** `sk0.txt` in this repository, a fork of github.com/drdhaval2785/siddhantakaumudi. The fork's code and markup are under the MIT licence (Dr. Dhaval Patel, 2017; see `LICENCE.txt`).
- **Origin of the typed file:** a .docx posted by Dr. H. N. Bhat to the bvparishat Google group on 2016-12-26. That file names neither its source edition nor its typist, and it carries no licence statement.
- **The work itself:** Bhaṭṭoji Dīkṣita's Siddhānta Kaumudī (17th century) is in the public domain. Corrections and structure added in this fork are released under the same MIT licence.

## Witnesses used to correct it
The witnesses are listed in order of authority, as decided for this edition.
1. **1910 print of the Siddhānta Kaumudī with the Bālamanoramā.** Page scans and text on sa.wikisource (`पुटम्:सिद्धान्तकौमुदी (बालमनोरमा …).djvu/N`). This is the first appeal for any reading.
2. **1908 Nirṇaya Sāgara print with the Tattvabodhinī.** OCR held by the project; used for readings only.
3. **The Kaumudī text in github.com/shastravid/ashtadhyayi-data** (from ashtadhyayi.com). This is a converted copy of the same typed lineage as the base, so it is not an independent witness: where both texts agree, a fault can still be shared. It was collated word by word with the base. Its vārttika, gaṇasūtra and paribhāṣā markup was compared with the base markup.
4. **The Kāśikā, and the Bālamanoramā as typed in ashtadhyayi-data.** Used for the wording of sūtras and of examples.
5. **premabase.com/siddhanta-kaumudi.** Derived from ashtadhyayi.com and states no licence. It was consulted for reference only and nothing was copied from it.
6. **The Dhātupāṭha data in ashtadhyayi-data (`dhatu/data.txt`, field `sk`).** Used for the dhātu numbers.

Readings that differ between prints are not changed. Only clear faults are corrected.

## What was changed, and where it is recorded
Every correction is a separate commit with a message that gives the SK serial, the old and new reading, and the ground. Pull requests #1–#10 group them:
- #1–#3: about 390 typing faults, ऌ/ॢ, and three Vedic passages.
- #4: uniformity.
- #5 and #7: single readings.
- #6: twelve sūtra numbers, and the order of 3187/3189.
- #8: the pratīka dash.
- #9: dhātu numbers.
- #10: the Python 3 build.

Corrections that also apply to ashtadhyayi-data were made there as separate pull requests.
