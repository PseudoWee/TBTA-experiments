#!/usr/bin/env python3
"""Build docs/psalms/index.html from data/psalms/psalmN.txt, reusing the Song of Songs page's CSS, key and tab script.
Run from the repo root:  python3 tools/build_psalms_page.py
Input format: '[vN] sentences', untagged lines are shared; '(literal)' / '(dynamic)' lines are one reading each."""
import glob, html, os, re

PRON = {"i","me","my","you","your","we","us","our","they","them","their","he","him","his","she","her","it","its"}
ART = {"the","a","an"}
e = html.escape

def word(w):
    m = re.fullmatch(r"(.*?)-([A-Z])", w)
    body, sup = (m.group(1), m.group(2)) if m else (w, None)
    s = e(body, quote=True) + (f"<sup>{sup}</sup>" if sup else "")
    return f'<span class="fw">{s}</span>' if w.lower() in ART else f'<span class="w">{s}</span>'

def alts(w):
    parts = re.split(r"([/|])", w)
    return "".join(f'<span class="sep">{x}</span>' if x in "/|" else word(x) for x in parts)

TOK = re.compile(r"""(?P<ref>\((?P<rv>[^)]*)\))|(?P<note>\([a-z-]+\))|(?P<tag>_\w+)|(?P<br>[\[\]])|(?P<q>")|(?P<pu>[.,;:?!])|(?P<w>[A-Za-z][A-Za-z'’/|-]*)""")

def encode(text):
    out = []; q_open = False; i = 0; prev = None
    for m in TOK.finditer(text):
        k = m.lastgroup if m.lastgroup not in ("rv",) else "ref"
        s = m.group(0)
        if m.group("ref") is not None:
            k = "ref"
        elif m.group("note"): k = "note"
        if k == "ref" and not (prev == "pron"):
            # standalone parenthesised notation such as (imp)
            h = f'<span class="st nt">{e(s)}</span>'; kind = "note"
        elif k == "ref":
            h = f'<span class="st">(</span><span class="w rf">{e(m.group("rv"))}</span><span class="st">)</span>'; kind = "ref"
        elif k == "tag": h = f'<span class="st tg">{e(s)}</span>'; kind = "tag"
        elif k == "br": h = f'<span class="br">{s}</span>'; kind = "open" if s == "[" else "close"
        elif k == "q":
            h = '<span class="st qt">&quot;</span>'; kind = "qclose" if q_open else "qopen"; q_open = not q_open
        elif k == "pu": h = f'<span class="st pu">{s}</span>'; kind = "pu"
        else:
            if "/" in s or "|" in s:
                h = alts(s)
            elif s.lower() in PRON and text[m.end():m.end()+1] == "(":
                h = f'<span class="pn">{e(s)}</span>'
            else:
                h = word(s)
            kind = "pron" if (s.lower() in PRON and text[m.end():m.end()+1] == "(") else "word"
        no_space = prev is None or prev in ("open", "qopen", "pron") or kind in ("close", "pu", "ref", "qclose")
        out.append(("" if no_space else " ") + h)
        prev = kind
    return "".join(out)

def parse(path):
    verses = []; pre = []; post = []
    for raw in open(path, encoding="utf-8").read().splitlines():
        line = raw.strip()
        if not line: continue
        if line == "(begin-poetry)": pre.append(line); continue
        if line == "(end-poetry)": post.append(line); continue
        m = re.match(r"\[v(\d+)\]\s*(.*)", line)
        if m:
            verses.append({"n": int(m.group(1)), "lines": []}); line = m.group(2)
        verses[-1]["lines"].append(line)
    verses[0]["lines"][:0] = pre
    verses[-1]["lines"].extend(post)
    return verses

def readings(v):
    lit, dyn, paired = [], [], False
    for l in v["lines"]:
        m = re.match(r"\((literal|dynamic)\)\s*(.*)", l)
        if m:
            paired = True
            (lit if m.group(1) == "literal" else dyn).append(m.group(2))
        else:
            lit.append(l); dyn.append(l)
    return lit, dyn, paired

def cell(lines):
    return f'<td class="ec"><div class="blk"><div class="enc">{encode(" ".join(lines))}</div></div></td>'

def build():
    tpl = open("docs/song-of-songs/index.html", encoding="utf-8").read()
    head = tpl[:tpl.index("<header>")].replace("Song of Songs Phase 1 Encoding", "Psalms Phase 1 Encoding")
    key = tpl[tpl.index('<div class="key"'):tpl.index("</header>")]
    script = tpl[tpl.index("<script>"):tpl.index("</script>") + 9]  # chapter-tab router
    files = sorted(glob.glob("data/psalms/psalm[0-9]*.txt"), key=lambda p: int(re.search(r"(\d+)\.txt", p).group(1)))
    nav, secs, nums = [], [], []
    for p in files:
        n = int(re.search(r"(\d+)\.txt", p).group(1)); nums.append(n)
        vs = parse(p); rows = []
        for v in vs:
            lit, dyn, paired = readings(v)
            raw = lambda ver: f'<td class="raw" data-book="PSA" data-bible="{ver}" data-ch="{n}" data-v="{v["n"]}"><span class="scr">Loading scripture from API.Bible…</span></td>'
            second = cell(dyn) if paired else '<td class="ec"><div class="same">Same encoding as the literal column.</div></td>'
            rows.append(f'<tr id="v{n}-{v["n"]}"><th scope="row" class="vn">{n}:{v["n"]}</th>{raw("NIV")}{raw("NASB")}{cell(lit)}{second}</tr>')
        nav.append(f'<a href="#ch{n}" role="tab" data-ch="ch{n}">Psalm {n}</a>')
        secs.append(f'<section id="ch{n}"><h2>Psalm {n}</h2><p class="sub">{len(vs)} verses</p><div class="scroll"><table><thead><tr><th class="vn">Verse</th><th>Raw NIV</th><th>Raw NASB</th><th>Literal</th><th>Dynamic</th></tr></thead><tbody>{"".join(rows)}</tbody></table></div></section>')
    names = ", ".join(f"Psalm {n}" for n in nums)
    header = (f'<header><h1>Psalms Phase 1 Encoding</h1><p class="lead">For each finished psalm: the raw NIV and raw NASB, then the literal and dynamic encodings. Done so far: {names}.</p>'
              f'<nav aria-label="Psalms" role="tablist">{"".join(nav)}</nav>{key}</header>')
    foot = ('<footer id="scripture-credits"><div id="credits-body">Scripture text is loaded live from <a href="https://api.bible">API.Bible</a> and is not stored on this site. Copyright notices appear here once the text has loaded.</div></footer>'
            '<script src="https://pkg.api.bible/fumsV3.min.js"></script>'
            '<script>window.fums=window.fums||function(){(window.fums.q=window.fums.q||[]).push(arguments)};</script>'
            '<script src="../assets/config.js"></script><script src="../assets/scripture.js"></script>')
    os.makedirs("docs/psalms", exist_ok=True)
    open("docs/psalms/index.html", "w", encoding="utf-8").write(head + header + "\n" + "".join(secs) + "\n" + foot + "\n" + script + "\n</body>\n</html>\n")
    print("built", names)

if __name__ == "__main__":
    build()
