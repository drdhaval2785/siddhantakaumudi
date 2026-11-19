# Structured Siddhānta Kaumudī

This folder holds the text of this repository arranged by Kaumudī serial (SK number) and Aṣṭādhyāyī sūtra.

- `sk.json`: one record per serial, in text order. 3,980 records are Aṣṭādhyāyī sūtras, 748 are Uṇādi sūtras (SK उ1 …) and 87 are Phiṭ sūtras (फि1 …). Each record has:
  - `sk`: the serial.
  - `sutra` (a.b.c): the sūtra number.
  - `ad_key`: the key used by ashtadhyayi.com data, such as 14108.
  - `prakarana`, `sutra_text`, and `vritti`, the commentary as plain text.
  - `segments`, the same commentary split into typed parts:
    - `text`
    - `varttika`
    - `paribhasha`
    - `dhatu`, with the dhātu number, name and meaning
    - `skref`, a cross-reference to another serial
  - `preamble` and `preamble_segments`, used where a prakaraṇa opens with text before its first sūtra, such as the first root of a gaṇa.
  - `trailer`, the closing line of a prakaraṇa.
- `unattached` in `sk.json`: three passages that stand after the last sūtra of a prakaraṇa.
- `index-by-sutra.json`: maps each sūtra to its SK serial or serials.
- `build.py`: regenerates both files from `sk.xml`. Run `bash redo.sh` first, then `python3 edition/build.py`.

How the text was established is described in `PROVENANCE.md`. The editorial decisions are listed in `DECISIONS.md`.
