#!/usr/bin/env python3
"""Build the single docs/index.html (Song of Songs + Psalms + Isaiah, vertical book tabs) from tools/templates/song-of-songs.html and data/psalms/psalmN.txt and data/isaiah/isaiahN.txt.
Run from the repo root:  python3 tools/build_site.py   (add --offline to skip the editor lookups and use data/levels.json only)
Colours: each word is coloured by the ontology level the live TaBiThA /check returns (cached in data/levels.json), exactly as editor.tabitha.bible does it.
Input format: '[vN] sentences', untagged lines are shared; '(literal)' / '(dynamic)' lines are one reading each."""
import glob, html, json, os, re, sys, time, urllib.parse, urllib.request
from concurrent.futures import ThreadPoolExecutor

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

TOK = re.compile(r"""(?P<ref>\((?P<rv>[^)]*)\))|(?P<note>\([a-z-]+\))|(?P<tag>_\w+)|(?P<br>[\[\]])|(?P<q>")|(?P<pu>[.,;:?!])|(?P<w>[A-Za-z0-9][A-Za-z0-9'’/|-]*)""")

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

def isaiah_fragment(tpl_key):
    files = sorted(glob.glob("data/isaiah/isaiah[0-9]*.txt"), key=lambda p: int(re.search(r"(\d+)\.txt", p).group(1)))
    nav, secs, names = [], [], []
    ee_path = lambda n: f"data/isaiah/ee{n}.txt"
    for p in files:
        n = int(re.search(r"(\d+)\.txt", p).group(1))
        vs = parse(p); rows = []
        ee = {v["n"]: " ".join(v["lines"]) for v in parse(ee_path(n))}
        for v in vs:
            lit, dyn, paired = readings(v)
            raw = lambda ver: f'<td class="raw" data-book="ISA" data-bible="{ver}" data-ch="{n}" data-v="{v["n"]}"><span class="scr">Loading scripture from API.Bible…</span></td>'
            second = cell(dyn) if paired else '<td class="ec"><div class="same">Same encoding as the literal column.</div></td>'
            rows.append(f'<tr id="v{n}-{v["n"]}"><th scope="row" class="vn">{n}:{v["n"]}</th>{raw("NASB")}<td class="raw ee">{e(ee[v["n"]])}</td>{cell(lit)}{second}</tr>')
        first, last = vs[0]["n"], vs[-1]["n"]
        label = f"Isaiah {n}:{first}\u2013{last}"; names.append(label)
        nav.append(f'<a href="#ch{n}" role="tab" data-ch="ch{n}">{label}</a>')
        secs.append(f'<section id="ch{n}"><h2>{label}</h2><p class="sub">{len(vs)} verses</p><div class="scroll"><table><thead><tr><th class="vn">Verse</th><th>Raw NASB</th><th>Easy English text</th><th>Literal (NASB)</th><th>Dynamic (Easy English)</th></tr></thead><tbody>{"".join(rows)}</tbody></table></div></section>')
    header = (f'<header><h1>Isaiah Phase 1 Encoding</h1><p class="lead">For each finished passage: the raw NASB (loaded from API.Bible), then the Easy English text, then the literal encoding (from the NASB) and the dynamic encoding (from the Easy English text). NIV was not used. The Easy English text is shown as supplied by the project team; its copyright remains with its owner, so confirm permission before sharing this page more widely. Done so far: {", ".join(names)}.</p>'
              f'<nav aria-label="Isaiah" role="tablist">{"".join(nav)}</nav>{tpl_key}</header>')
    return header + "".join(secs)

def namespace(frag, pre):
    frag = re.sub(r'\bid="ch(\d+)"', rf'id="{pre}-ch\1"', frag)
    frag = re.sub(r'\bid="v(\d+-\d+)"', rf'id="{pre}-v\1"', frag)
    frag = re.sub(r'href="#ch(\d+)"', rf'href="#{pre}-ch\1"', frag)
    frag = re.sub(r'href="#v(\d+-\d+)"', rf'href="#{pre}-v\1"', frag)
    frag = re.sub(r'data-ch="ch(\d+)"', rf'data-ch="{pre}-ch\1"', frag)
    return frag


# ---------------------------------------------------------------------------
# Editor-accurate colouring.  The TaBiThA editor (editor.tabitha.bible) colours each Word token by
# the ontology level of its first lookup result (CSS classes L0..L4); FunctionWord, Note and Punctuation
# tokens are plain text; a pronoun is an outlined box followed by its referent in parentheses; a token
# with checker messages gets a joined icon box (warning/error/suggest/info).  Levels are read from the
# live /check response and cached in data/levels.json so the build works offline afterwards.
# ---------------------------------------------------------------------------
LEVELS_PATH = "data/levels.json"
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"
SKIP_MSG = ("cannot determine which part", "errors and warnings within the same clause may not")
ENC_RE = re.compile(r'(<div class="enc">)(.*?)(</div>)', re.S)
SPAN_RE = re.compile(r'<span class="([^"]*)">(.*?)</span>', re.S)

def enc_text(inner):
    t = re.sub(r"<sup>([A-Z])</sup>", r"-\1", inner)
    return html.unescape(re.sub(r"<[^>]+>", "", t)).strip()

def flatten(tok, out):
    ty = tok.get("type")
    if ty in ("Word", "FunctionWord"):
        lr = tok.get("lookup_results") or []
        lv = lr[0].get("level") if lr else None
        ms = [m for m in (tok.get("messages") or []) if not any(x in m["message"] for x in SKIP_MSG)]
        label = tok["messages"][0]["label"] if tok.get("messages") else None
        out.append([tok.get("token", ""), "W" if ty == "Word" else "F", lv, label, (ms[0]["message"][:160] if ms else "")])
    if tok.get("pairing"):          # X|Y or X/Y: the editor nests the second word under the first
        flatten(tok["pairing"], out)
    for sub in tok.get("sub_tokens") or []:
        flatten(sub, out)

def fetch_tokens(text):
    err = ""
    for a in range(3):
        try:
            req = urllib.request.Request("https://editor.tabitha.bible/check?" + urllib.parse.urlencode({"text": text}),
                                         headers={"User-Agent": UA, "Accept": "application/json"})
            r = json.loads(urllib.request.urlopen(req, timeout=90).read())
            out = []
            for t in r.get("tokens", []): flatten(t, out)
            return out
        except Exception as ex:
            err = str(ex); time.sleep(2 * (a + 1))
    print("  /check failed:", err[:120], "for", text[:60], file=sys.stderr)
    return None

def load_levels():
    return json.load(open(LEVELS_PATH, encoding="utf-8")) if os.path.exists(LEVELS_PATH) else {}

def ensure_levels(page, cache, fetch=True):
    texts = sorted({enc_text(m.group(2)) for m in ENC_RE.finditer(page)} - set(cache))
    if texts and fetch:
        print(f"fetching editor levels for {len(texts)} encodings...", flush=True)
        with ThreadPoolExecutor(max_workers=4) as ex:
            for t, toks in zip(texts, ex.map(fetch_tokens, texts)):
                if toks is not None: cache[t] = toks
        json.dump(cache, open(LEVELS_PATH, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
    return cache

GLYPH = {"error": "✕", "warning": "⚠", "suggest": "✦", "info": "i"}

def norm(w):
    return re.sub(r"['\u2019]s?$", "", w.strip().lower())

def colorize_enc(inner, toks, stats):
    if not toks: return inner
    toks = [[w] + t[1:] for t in toks for w in (t[0].split() or [t[0]])]   # multi-word tokens ("in order to") -> one entry per word
    j = 0
    def sub(m):
        nonlocal j
        cls, body = m.group(1), m.group(2)
        if cls not in ("w", "w rf", "fw"): return m.group(0)
        txt = norm(enc_text(body))
        for k in range(j, min(j + 8, len(toks))):
            if norm(toks[k][0]) == txt:
                t = toks[k]; j = k + 1; break
        else:
            stats["unmatched"] += 1
            return m.group(0)
        stats["matched"] += 1
        _, ty, lv, label, msg = t
        if ty == "W":
            lc = f"L{lv}" if isinstance(lv, int) and 0 <= lv <= 4 else "Lu"
            core = f'<span class="w {lc}{" rf" if cls == "w rf" else ""}">{body}</span>'
        else:
            core = f'<span class="fw">{body}</span>'
        if label:
            inner_core = core.replace('class="fw"', 'class="fw bx"')
            core = (f'<span class="mj {label}" title="{html.escape(msg or label, quote=True)}">'
                    f'<span class="ic">{GLYPH.get(label, "i")}</span>{inner_core}</span>')
        return core
    return SPAN_RE.sub(sub, inner)

def colorize_page(page, fetch=True):
    cache = ensure_levels(page, load_levels(), fetch)
    stats = {"matched": 0, "unmatched": 0, "missing": 0}
    def enc(m):
        toks = cache.get(enc_text(m.group(2)))
        if toks is None: stats["missing"] += 1; return m.group(0)
        return m.group(1) + colorize_enc(m.group(2), toks, stats) + m.group(3)
    out = ENC_RE.sub(enc, page)
    print("colour:", stats)
    return out

LEVEL_CSS = """
/* colours copied from the editor's own stylesheet (.L0-.L4); outline-only = word not in the ontology */
.w.L0{color:#f5f5f5;background:#0b66ff;border-color:#f5f5f5}
.w.L1{color:#00008b;filter:saturate(200%);background:#fcffc5;border-color:#00008b}
.w.L2{color:#ff0;background:#fb00ff;border-color:#ff0}
.w.L3{color:#f5f5f5;background:#0f7000;border-color:#f5f5f5}
.w.L4{color:#f5f5f5;background:#6b2f30;border-color:#f5f5f5}
.w.Lu{color:var(--enc-ink);background:transparent;border-color:currentColor}
.w sup{color:inherit}
.mj{display:inline-flex;align-items:stretch;margin:0 1px;vertical-align:baseline;border-radius:6px}
.mj .ic{display:inline-flex;align-items:center;padding:0 .35em;border:1px solid currentColor;border-right:0;border-radius:6px 0 0 6px;font-size:.85em;line-height:1.6}
.mj>.w{border-radius:0 6px 6px 0;margin:0}
.mj>.fw.bx{display:inline-block;padding:0 .4em;border:1px solid currentColor;border-radius:0 6px 6px 0;line-height:1.6;color:var(--enc-ink)}
.mj.warning .ic,.mj.suggest .ic{color:oklch(82% .189 84.429)}
.mj.error .ic{color:oklch(71% .194 13.428)}
.mj.info .ic{color:oklch(74% .16 232.661)}
.mj.warning>.fw.bx,.mj.suggest>.fw.bx{border-color:oklch(82% .189 84.429)}
.mj.error>.fw.bx{border-color:oklch(71% .194 13.428)}
.key .w{margin-right:4px}
"""

KEY = """<div class="key" role="note" aria-label="How to read the encodings">
<span class="l">Reading the encodings (same colours as editor.tabitha.bible)</span>
<span><span class="w L0">said</span> level 0, primitive</span>
<span><span class="w L1">leader</span> level 1, simple</span>
<span><span class="w L2">prophet</span> level 2, complex</span>
<span><span class="w L3">apostle</span> level 3, very complex</span>
<span><span class="w L4">Judah</span> level 4, names and key terms</span>
<span><span class="w Lu">Shebna</span> not in the ontology</span>
<span><span class="fw">the</span> function word (plain text)</span>
<span><span class="pn">you</span><span class="st">(</span><span class="w L1 rf">leader</span><span class="st">)</span> pronoun and its referent</span>
<span><span class="mj warning"><span class="ic">&#9888;</span><span class="w L1">Please</span></span> checker message (hover for text)</span>
<span class="st tg">_implicitNecessary</span><span class="st nt">(imp)</span><span class="br">[</span><span class="br">]</span><span class="st">structure: tags, notation, clause brackets</span>
</div>
"""

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
var books={sos:document.getElementById('book-sos'),ps:document.getElementById('book-ps'),is:document.getElementById('book-is')},
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
  var h=location.hash.slice(1),m=/^(sos|ps|is)-(?:(ch\d+)|v(\d+)-\d+)$/.exec(h);
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
    key = KEY
    sos = tpl[tpl.index("<header>"):tpl.index("<footer>")]  # header + all chapter sections; drops the old private-use footer
    sos = re.sub(r'<div class="key".*?</div>\n', lambda m: KEY, sos, count=1, flags=re.S)
    ps = psalms_fragment(key)
    isa = isaiah_fragment(key)
    side = ('<aside class="side" aria-label="Books"><div class="t">Book</div>'
            '<a href="#sos-ch1" data-book="sos">Song of Songs</a><a href="#ps-ch1" data-book="ps">Psalms</a><a href="#is-ch36" data-book="is">Isaiah</a></aside>')
    foot = ('<footer id="scripture-credits"><div id="credits-body">Scripture text is loaded live from <a href="https://api.bible">API.Bible</a> and is not stored on this site. Copyright notices appear here once the text has loaded.</div></footer>')
    scripts = ('<script src="https://pkg.api.bible/fumsV3.min.js"></script>'
               '<script>window.fums=window.fums||function(){(window.fums.q=window.fums.q||[]).push(arguments)};</script>'
               '<script src="assets/config.js"></script><script src="assets/scripture.js"></script>')
    page = (head_open + "<style>" + css + LEVEL_CSS + EXTRA_CSS + "</style>\n</head>\n<body>\n"
            + '<div class="app">' + side + '<div class="main">'
            + '<div class="book" id="book-sos">' + namespace(sos, "sos") + '</div>'
            + '<div class="book off" id="book-ps">' + namespace(ps, "ps") + '</div>'
            + '<div class="book off" id="book-is">' + namespace(isa, "is") + '</div>'
            + foot + '</div></div>\n' + scripts + "\n" + ROUTER + "\n</body>\n</html>\n")
    page = colorize_page(page, fetch="--offline" not in sys.argv)
    open("docs/index.html", "w", encoding="utf-8").write(page)
    print("built docs/index.html")

if __name__ == "__main__":
    build()
