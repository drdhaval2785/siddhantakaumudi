#!/usr/bin/env python3
"""Build the structured Siddhanta Kaumudi (edition/sk.json) from sk.xml.

Usage: python3 edition/build.py      (run from the repository root, after redo.sh)

One record per Kaumudi serial (SK number), in text order, with the Ashtadhyayi
sutra number, the prakarana, the sutra text, the commentary as plain text, and
the commentary as typed segments (text, varttika, paribhasha, dhatu, SK
cross-reference, citation of the Liṅgānuśāsana or Māheśvarasūtras;
vārttikas in verse carry sloka=true). Text that opens a prakarana before its first sutra (e.g. the
first dhatu of a gana) is kept as the next record's preamble. Also writes edition/index-by-sutra.json (sutra -> SK serials).
"""
import json, re, sys
import lxml.etree as ET

NS = '{http://www.tei-c.org/ns/1.0}'
KIND = {'vārtika': 'varttika', 'paribhāṣā': 'paribhasha', 'SKsandarbhaḥ': 'skref'}


def norm(s):
    s = re.sub(r'[ \t\r\f\v]+', ' ', s)
    s = re.sub(r' *\n *', '\n', s)
    s = re.sub(r'\n{2,}', '\n', s)
    return s


def segments(el, out):
    """Flatten el's content into typed segments."""
    def text(s):
        if s:
            if out and out[-1]['t'] == 'text':
                out[-1]['v'] += s
            else:
                out.append({'t': 'text', 'v': s})
    text(el.text)
    for ch in el:
        tag = ch.tag.replace(NS, '')
        typ = ch.get('type')
        if tag == 'div' and typ == 'dhātvarthaḥ':
            roots = []
            artha = ch.text or ''
            for d in ch:
                if d.get('type') == 'dhātuḥ':
                    m = re.match(r'\s*(\d+)\s+(.+?)\s*$', d.text or '')
                    roots.append({'n': int(m.group(1)), 'name': m.group(2)})
                artha += d.tail or ''
            out.append({'t': 'dhatu', 'roots': roots, 'artha': artha.strip()})
        elif tag == 'div' and typ == 'dhātuḥ':
            m = re.match(r'\s*(\d+)\s+(.+?)\s*$', ch.text or '')
            out.append({'t': 'dhatu', 'roots': [{'n': int(m.group(1)), 'name': m.group(2)}], 'artha': ''})
        elif tag == 'div' and typ == 'SKsandarbhaḥ':
            out.append({'t': 'skref', 'sk': (ch.text or '').strip()})
        elif tag == 'div' and typ in KIND:
            out.append({'t': KIND[typ], 'v': norm(''.join(ch.itertext())).strip()})
        else:
            segments(ch, out)
        text(ch.tail)
    return out


def plain(segs):
    parts = []
    for s in segs:
        if s['t'] == 'text':
            parts.append(s['v'])
        elif s['t'] == 'dhatu':
            parts.append(' '.join(f"{r['n']} {r['name']}" for r in s['roots']) + (' ' + s['artha'] if s['artha'] else ''))
        elif s['t'] == 'skref':
            parts.append(s['sk'])
        else:
            parts.append(s['v'])
    out = ''
    for p in parts:
        if out and p and not out[-1].isspace() and not p[0].isspace():
            out += ' '
        out += p
    return norm(out).strip()


def clean(segs):
    out = []
    for s in segs:
        if s['t'] == 'text':
            s['v'] = norm(s['v'])
            if not s['v'].strip():
                continue
        if s['t'] == 'text' and out and out[-1]['t'] == 'text':
            out[-1]['v'] += s['v']
            continue
        out.append(s)
    return out


DEV = str.maketrans('०१२३४५६७८९', '0123456789')
CITE = re.compile(r'\((लि|मा\.सू\.-) ?([०-९]+)\)')
CITE_KIND = {'लि': 'linganushasana', 'मा.सू.-': 'maheshvarasutra'}


def mark(segs):
    """Type the citations of other texts, and mark śloka-vārttikas (upstream issue #64)."""
    out = []
    for s in segs:
        if s['t'] != 'text':
            out.append(s)
            continue
        v, i = s['v'], 0
        for m in CITE.finditer(v):
            if m.start() > i:
                out.append({'t': 'text', 'v': v[i:m.start()]})
            out.append({'t': 'cite', 'text': CITE_KIND[m.group(1)], 'n': int(m.group(2).translate(DEV)), 'v': m.group(0)})
            i = m.end()
        if i < len(v):
            out.append({'t': 'text', 'v': v[i:]})
    for k, s in enumerate(out):
        if s['t'] == 'varttika' and k + 1 < len(out) and out[k + 1]['t'] == 'text' \
                and re.match(r'\s*\(वा\)\s*[।॥]*\s*\(श्लो\.वा\.\)', out[k + 1]['v']):
            s['sloka'] = True
    return out


def main():
    root = ET.parse('sk.xml').getroot()
    body = root.find(f'.//{NS}body')
    records, intros = [], []
    for prak in body.iter(f'{NS}div'):
        if prak.get('type') != 'prakaraṇa':
            continue
        head = norm(''.join(prak.find(f'{NS}head').itertext())).strip()
        name = re.sub(r'^॥\s*अथ\s*|\s*॥$', '', head)
        trailer = prak.find(f'{NS}trailer')
        loose = []

        def take(seg_list):
            loose.extend(seg_list)

        if prak.find(f'{NS}head') is not None and prak.find(f'{NS}head').tail:
            take([{'t': 'text', 'v': prak.find(f'{NS}head').tail}])
        for ch in prak:
            tag, typ = ch.tag.replace(NS, ''), ch.get('type')
            if tag == 'div' and typ == 'sūtra_with_explanation':
                ab = ch.find(f'{NS}ab')
                labels = {l.get('type'): (l.text or '').strip() for l in ab.findall(f'{NS}label')}
                stext = norm((ab.findall(f'{NS}label')[-1].tail or '')).strip()
                segs = []
                for p in ch.findall(f'{NS}p'):
                    segments(p, segs)
                segs = mark(clean(segs))
                a = labels.get('AS', '')
                sk = labels.get('SK')
                rec = {
                    'sk': sk,
                    'sutra': a.replace('-', '.'),
                    'ad_key': ''.join([a.split('-')[0], a.split('-')[1], a.split('-')[2].zfill(3)]) if sk.isdigit() and a.count('-') == 2 else '',
                    'prakarana': name,
                    'sutra_text': stext,
                }
                pre = clean(loose)
                if pre:
                    rec['preamble'] = plain(pre)
                    rec['preamble_segments'] = pre
                loose = []
                rec['vritti'] = plain(segs)
                rec['segments'] = segs
                records.append(rec)
            elif tag in ('head', 'trailer'):
                pass
            elif tag == 'p':
                take(segments(ch, []))
            else:
                wrap = ET.Element('x')
                wrap.append(ET.fromstring(ET.tostring(ch, with_tail=False)))
                take(segments(wrap, []))
            if tag != 'head' and ch.tail:
                take([{'t': 'text', 'v': ch.tail}])
        rest = clean(loose)
        if rest:
            intros.append({'prakarana': name, 'after_sk': records[-1]['sk'] if records else None, 'text': plain(rest), 'segments': rest})
        if trailer is not None and records:
            records[-1]['trailer'] = norm(''.join(trailer.itertext())).strip()
    index = {}
    for r in records:
        index.setdefault(r['sutra'], []).append(r['sk'])
    with open('edition/sk.json', 'w', encoding='utf-8') as f:
        json.dump({'records': records, 'unattached': intros}, f, ensure_ascii=False, indent=1)
        f.write('\n')
    with open('edition/index-by-sutra.json', 'w', encoding='utf-8') as f:
        json.dump(index, f, ensure_ascii=False, indent=1)
        f.write('\n')
    nd = sum(len(s['roots']) for r in records + intros for s in r.get('preamble_segments', []) + r['segments'] if s['t'] == 'dhatu')
    print(f'{len(records)} records, {len(index)} sutras, {nd} dhatus, {len(intros)} unattached passages', file=sys.stderr)


if __name__ == '__main__':
    main()
