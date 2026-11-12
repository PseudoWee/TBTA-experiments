#!/usr/bin/env python3
"""Build the single docs/index.html (Song of Songs + Psalms, vertical book tabs) from tools/templates/song-of-songs.html and data/psalms/psalmN.txt.
Run from the repo root:  python3 tools/build_site.py
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

def psalms_fragment(tpl_key):
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
              f'<nav aria-label="Psalms" role="tablist">{"".join(nav)}</nav>{tpl_key}</header>')
    return header + "".join(secs)

def namespace(frag, pre):
    frag = re.sub(r'\bid="ch(\d+)"', rf'id="{pre}-ch\1"', frag)
    frag = re.sub(r'\bid="v(\d+-\d+)"', rf'id="{pre}-v\1"', frag)
    frag = re.sub(r'href="#ch(\d+)"', rf'href="#{pre}-ch\1"', frag)
    frag = re.sub(r'href="#v(\d+-\d+)"', rf'href="#{pre}-v\1"', frag)
    frag = re.sub(r'data-ch="ch(\d+)"', rf'data-ch="{pre}-ch\1"', frag)
    return frag

EXTRA_CSS = """
.app{display:flex;align-items:flex-start;min-height:100vh}
.side{position:sticky;top:0;flex:0 0 190px;padding:28px 12px;display:flex;flex-direction:column;gap:8px;border-right:1px solid var(--line);min-height:100vh;background:var(--panel)}
.side .t{font-size:.7rem;text-transform:uppercase;letter-spacing:.06em;color:var(--mute);margin:0 8px 4px}
.side a{padding:9px 12px;border-radius:8px;color:var(--ink);text-decoration:none;font-weight:600;font-size:.95rem;border:1px solid transparent}
.side a:hover{border-color:var(--line)}
.side a[aria-current="true"]{background:var(--accent);color:#fff}
.main{flex:1;min-width:0}
.book.off{display:none}
@media (max-width:760px){.app{flex-direction:column}.side{position:static;flex:none;flex-direction:row;flex-wrap:wrap;min-height:0;width:100%;border-right:0;border-bottom:1px solid var(--line);padding:12px 16px}.side .t{display:none}}
"""

ROUTER = r"""<script>
(function(){
var books={sos:document.getElementById('book-sos'),ps:document.getElementById('book-ps')},
    sides=[].slice.call(document.querySelectorAll('.side a[data-book]'));
function show(book,id,scrollTo){
  if(!books[book])book='sos';
  var b=books[book],secs=[].slice.call(b.querySelectorAll('section[id*="-ch"]'));
  if(!document.getElementById(id)||!b.contains(document.getElementById(id)))id=secs[0].id;
  Object.keys(books).forEach(function(k){books[k].classList.toggle('off',k!==book)});
  sides.forEach(function(a){a.setAttribute('aria-current',a.dataset.book===book?'true':'false')});
  secs.forEach(function(s){s.classList.toggle('off',s.id!==id)});
  [].slice.call(b.querySelectorAll('nav a[data-ch]')).forEach(function(a){a.setAttribute('aria-selected',a.dataset.ch===id?'true':'false')});
  if(scrollTo){var e=document.getElementById(scrollTo);if(e)e.scrollIntoView({block:'start'});}
  else window.scrollTo(0,0);
}
function route(){
  var h=location.hash.slice(1),m=/^(sos|ps)-(?:(ch\d+)|v(\d+)-\d+)$/.exec(h);
  if(!m){show('sos','sos-ch1');return;}
  if(m[2])show(m[1],m[1]+'-'+m[2]);else show(m[1],m[1]+'-ch'+m[3],h);
}
window.addEventListener('hashchange',route);route();
})();
</script>"""

def build():
    tpl = open("tools/templates/song-of-songs.html", encoding="utf-8").read()
    css = tpl[tpl.index("<style>") + 7:tpl.index("</style>")]
    head_open = tpl[:tpl.index("<style>")].replace("Song of Songs Phase 1 Encoding", "Phase 1 Encodings — new verses")
    key = tpl[tpl.index('<div class="key"'):tpl.index("</header>")]
    sos = tpl[tpl.index("<header>"):tpl.index("<footer>")]  # header + all chapter sections; drops the old private-use footer
    ps = psalms_fragment(key)
    side = ('<aside class="side" aria-label="Books"><div class="t">Book</div>'
            '<a href="#sos-ch1" data-book="sos">Song of Songs</a><a href="#ps-ch1" data-book="ps">Psalms</a></aside>')
    foot = ('<footer id="scripture-credits"><div id="credits-body">Scripture text is loaded live from <a href="https://api.bible">API.Bible</a> and is not stored on this site. Copyright notices appear here once the text has loaded.</div></footer>')
    scripts = ('<script src="https://pkg.api.bible/fumsV3.min.js"></script>'
               '<script>window.fums=window.fums||function(){(window.fums.q=window.fums.q||[]).push(arguments)};</script>'
               '<script src="assets/config.js"></script><script src="assets/scripture.js"></script>')
    page = (head_open + "<style>" + css + EXTRA_CSS + "</style>\n</head>\n<body>\n"
            + '<div class="app">' + side + '<div class="main">'
            + '<div class="book" id="book-sos">' + namespace(sos, "sos") + '</div>'
            + '<div class="book off" id="book-ps">' + namespace(ps, "ps") + '</div>'
            + foot + '</div></div>\n' + scripts + "\n" + ROUTER + "\n</body>\n</html>\n")
    open("docs/index.html", "w", encoding="utf-8").write(page)
    print("built docs/index.html")

if __name__ == "__main__":
    build()
