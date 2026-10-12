#!/usr/bin/env python3
"""Static site generator for The Viral Veer. Run: python3 build.py"""
import os, json, shutil, html, datetime, sys
from content import *

BASE = os.environ.get("TVV_BASE", "/theviralveer")  # path prefix on GitHub Pages
ORIGIN = os.environ.get("TVV_ORIGIN", "https://nishit002.github.io")
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "docs")
TODAY = datetime.date.today().isoformat()
esc = html.escape

def u(path=""):
    path = path.strip("/")
    return f"{BASE}/{path}/" if path else f"{BASE}/"

def abs_u(path=""):
    return ORIGIN + u(path)

PAGES = []  # (url, priority) for sitemap

CSS = r"""
:root{--paper:#f7f3ec;--paper-2:#efe9df;--card:#fffdf9;--ink:#1c1a17;--ink-2:#5c574f;--ink-3:#8c867c;--line:#e4ddd1;--accent:#b4461c;--accent-ink:#fff6f1;--pill:#f1e9dc;--shadow:0 1px 3px rgba(40,30,10,.08)}
:root:not([data-theme="light"]){color-scheme:light dark}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--paper:#15130f;--paper-2:#1d1a15;--card:#211e18;--ink:#f1ece3;--ink-2:#b8b0a3;--ink-3:#7f786d;--line:#2f2a22;--accent:#e4703f;--accent-ink:#1a0e07;--pill:#2a251d;--shadow:0 1px 3px rgba(0,0,0,.4)}}
:root[data-theme="dark"]{--paper:#15130f;--paper-2:#1d1a15;--card:#211e18;--ink:#f1ece3;--ink-2:#b8b0a3;--ink-3:#7f786d;--line:#2f2a22;--accent:#e4703f;--accent-ink:#1a0e07;--pill:#2a251d;--shadow:0 1px 3px rgba(0,0,0,.4)}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--paper);color:var(--ink);font:15px/1.6 Inter,system-ui,-apple-system,"Segoe UI",sans-serif;-webkit-font-smoothing:antialiased}
a{color:inherit;text-decoration:none}img{max-width:100%;display:block}
.wrap{max-width:1080px;margin:0 auto;padding:0 16px}@media(min-width:768px){.wrap{padding:0 24px}}
.serif{font-family:Fraunces,"Iowan Old Style",Georgia,serif;font-variation-settings:"opsz" 144,"SOFT" 50}
h1,h2,h3{font-family:Fraunces,"Iowan Old Style",Georgia,serif;letter-spacing:-.01em;margin:0 0 .4em}
h1{font-size:36px;font-weight:600;line-height:1.1}@media(min-width:768px){h1{font-size:48px}}
h2{font-size:24px;font-weight:600;line-height:1.2}h3{font-size:19px;font-weight:600;line-height:1.3}
p{margin:0 0 1em}.lede{font-size:17px;color:var(--ink-2);max-width:62ch}
.label{font-size:12px;font-weight:500;letter-spacing:.06em;text-transform:uppercase;color:var(--ink-3)}
.accent{color:var(--accent)}
/* header */
.top{position:sticky;top:0;z-index:20;background:color-mix(in srgb,var(--paper) 88%,transparent);backdrop-filter:saturate(1.4) blur(10px);border-bottom:1px solid var(--line)}
.top .wrap{display:flex;align-items:center;justify-content:space-between;height:60px;gap:12px}
.brand{font-family:Fraunces,Georgia,serif;font-weight:700;font-size:19px;letter-spacing:-.01em;white-space:nowrap}
.brand span{color:var(--accent)}
.nav{display:none;gap:4px}.nav a{padding:10px 12px;border-radius:100px;font-weight:500;color:var(--ink-2);font-size:14px;min-height:44px;display:inline-flex;align-items:center}
.nav a:hover,.nav a[aria-current]{background:var(--pill);color:var(--ink)}
@media(min-width:900px){.nav{display:flex}}
.ask-btn{background:var(--accent);color:var(--accent-ink);padding:0 16px;height:40px;border-radius:100px;font-weight:600;font-size:14px;display:inline-flex;align-items:center;gap:6px;white-space:nowrap}
.ask-btn:active{transform:scale(.97);opacity:.85}
.menu-btn{display:inline-flex;align-items:center;justify-content:center;width:44px;height:44px;border:1px solid var(--line);border-radius:10px;background:var(--card);cursor:pointer;color:var(--ink)}
@media(min-width:900px){.menu-btn{display:none}}
.drawer{display:none;border-top:1px solid var(--line);background:var(--paper)}
.drawer.open{display:block}
.drawer a{display:flex;align-items:center;min-height:48px;padding:0 16px;border-bottom:1px solid var(--line);font-weight:500}
.drawer .sub{padding-left:32px;color:var(--ink-2);font-weight:400;font-size:14px;min-height:40px}
/* hero */
.hero{padding:56px 0 40px}@media(min-width:768px){.hero{padding:96px 0 64px}}
.hero .kicker{display:inline-block;margin-bottom:18px;padding:6px 12px;border-radius:100px;background:var(--pill);font-size:12px;font-weight:500;letter-spacing:.06em;text-transform:uppercase;color:var(--ink-2)}
.hero h1{max-width:14ch}.hero .big{font-size:44px}@media(min-width:768px){.hero .big{font-size:72px}}
.hero p.sub{font-size:18px;color:var(--ink-2);max-width:56ch;margin-top:18px}
.hero .quote{font-family:Fraunces,Georgia,serif;font-style:italic;font-size:19px;color:var(--ink);max-width:52ch;margin-top:22px;border-left:3px solid var(--accent);padding-left:16px}
/* grids */
.grid{display:grid;gap:14px}@media(min-width:600px){.grid.c2{grid-template-columns:1fr 1fr}.grid.c3{grid-template-columns:repeat(3,1fr)}}
@media(min-width:900px){.grid.c4{grid-template-columns:repeat(4,1fr)}.grid.c5{grid-template-columns:repeat(5,1fr)}}
.card{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:20px;box-shadow:var(--shadow);transition:background .15s}
a.card:hover{background:var(--paper-2)}a.card:active{transform:scale(.97);opacity:.85}
.card h3{margin:.4em 0 .3em}.card p{color:var(--ink-2);margin:0;font-size:14px}
.card .emoji{font-size:26px;line-height:1}
.section{padding:40px 0}@media(min-width:768px){.section{padding:64px 0}}
.section-head{display:flex;align-items:baseline;justify-content:space-between;gap:12px;margin-bottom:20px}
.section-head a{color:var(--accent);font-weight:500;font-size:14px;white-space:nowrap}
.band{background:var(--paper-2);border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
/* lists */
.qlist{list-style:none;margin:0;padding:0;border-top:1px solid var(--line)}
.qlist li{border-bottom:1px solid var(--line)}
.qlist a,.qlist span{display:flex;align-items:center;justify-content:space-between;gap:12px;padding:14px 0;min-height:48px;font-weight:500}
.qlist a:hover{color:var(--accent)}.qlist .soon{color:var(--ink-3);font-weight:400}
.qlist .tag{font-size:12px;color:var(--ink-3);font-weight:500;white-space:nowrap}
.crumbs{font-size:13px;color:var(--ink-3);padding:18px 0 0}.crumbs a:hover{color:var(--accent)}.crumbs span{margin:0 6px}
/* article */
.article{max-width:720px}.article-head{padding:28px 0 8px}@media(min-width:768px){.article-head{padding:48px 0 16px}}
.meta{display:flex;flex-wrap:wrap;gap:8px 16px;align-items:center;color:var(--ink-3);font-size:13px;margin-top:14px}
.meta .who{display:flex;align-items:center;gap:8px;color:var(--ink-2);font-weight:500}
.avatar{width:28px;height:28px;border-radius:50%;background:var(--accent);color:var(--accent-ink);display:inline-flex;align-items:center;justify-content:center;font-family:Fraunces,serif;font-weight:700;font-size:13px}
.short{background:var(--card);border:1px solid var(--line);border-left:4px solid var(--accent);border-radius:12px;padding:18px 20px;margin:24px 0;box-shadow:var(--shadow)}
.short .label{margin-bottom:6px;display:block}.short p{margin:0;font-size:17px;line-height:1.55}
.body h2{margin-top:40px}.body p{font-size:16px}
.steps{list-style:none;counter-reset:s;margin:0;padding:0}
.steps li{counter-increment:s;display:grid;grid-template-columns:40px 1fr;gap:12px;padding:14px 0;border-bottom:1px solid var(--line)}
.steps li::before{content:counter(s);font-family:Fraunces,serif;font-size:22px;font-weight:600;color:var(--accent);line-height:1.2}
.steps b{display:block;font-weight:600}.steps span{color:var(--ink-2);font-size:15px}
.take{background:var(--paper-2);border-radius:12px;padding:22px 22px 8px;margin-top:36px;border:1px solid var(--line)}
.take h2{margin-top:0;display:flex;align-items:center;gap:10px}
.mist{padding-left:0;list-style:none}.mist li{padding:10px 0 10px 26px;position:relative;border-bottom:1px solid var(--line);color:var(--ink-2)}
.mist li::before{content:"×";position:absolute;left:4px;top:8px;color:var(--accent);font-weight:700;font-size:18px}
details{border-bottom:1px solid var(--line)}details summary{cursor:pointer;padding:14px 0;font-weight:600;list-style:none;display:flex;justify-content:space-between;gap:12px;min-height:48px;align-items:center}
details summary::after{content:"+";color:var(--accent);font-size:20px;font-weight:300}details[open] summary::after{content:"–"}
details p{color:var(--ink-2);padding-bottom:14px;margin:0}
.related{margin-top:48px}
/* misc */
.pill{display:inline-flex;align-items:center;gap:6px;padding:8px 14px;border-radius:100px;background:var(--pill);font-size:13px;font-weight:500;min-height:36px}
.pills{display:flex;flex-wrap:wrap;gap:8px}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:8px;min-height:48px;padding:0 22px;border-radius:100px;font-weight:600;background:var(--ink);color:var(--paper);font-size:15px;border:0;cursor:pointer}
.btn.accent{background:var(--accent);color:var(--accent-ink)}.btn.ghost{background:transparent;border:1px solid var(--line);color:var(--ink)}
.btn:active{transform:scale(.97);opacity:.85}
.cta{display:flex;flex-direction:column;gap:12px}@media(min-width:600px){.cta{flex-direction:row;align-items:center}}
.stat{font-family:Fraunces,serif;font-size:40px;font-weight:600;line-height:1}
.def dt{font-family:Fraunces,serif;font-size:22px;font-weight:600;margin-top:28px}.def dd{margin:6px 0 0;color:var(--ink-2)}.def dd b{color:var(--ink);font-weight:600}
form .f{display:flex;flex-direction:column;gap:6px;margin-bottom:16px}
input,select,textarea{font:inherit;padding:12px 14px;border:1px solid var(--line);border-radius:8px;background:var(--card);color:var(--ink);min-height:48px;width:100%}
textarea{min-height:140px;resize:vertical}
.notice{font-size:13px;color:var(--ink-3)}
.vs{display:grid;grid-template-columns:1fr auto 1fr;gap:12px;align-items:center;font-family:Fraunces,serif;font-size:22px;font-weight:600;text-align:center}
.vs i{font-style:italic;color:var(--accent);font-size:16px}
footer{border-top:1px solid var(--line);margin-top:64px;padding:40px 0 48px;color:var(--ink-2);font-size:14px}
footer .cols{display:grid;gap:24px}@media(min-width:768px){footer .cols{grid-template-columns:2fr 1fr 1fr 1fr}}
footer h4{margin:0 0 10px;font-size:12px;letter-spacing:.06em;text-transform:uppercase;color:var(--ink-3);font-weight:500}
footer a{display:block;padding:5px 0}footer a:hover{color:var(--accent)}
.foot-note{margin-top:28px;padding-top:20px;border-top:1px solid var(--line);display:flex;flex-wrap:wrap;gap:12px;justify-content:space-between;font-size:13px;color:var(--ink-3)}
.theme{background:none;border:1px solid var(--line);border-radius:100px;padding:6px 12px;color:var(--ink-2);cursor:pointer;font:inherit;font-size:13px}
"""

NAV = [("relationships","Relationships"),("career","Career"),("life","Life"),("technology","Technology"),("travel-and-living","Travel"),("explains","Explains"),("vs","Vs"),("dictionary","Dictionary")]

def layout(title, desc, body, path="", schema=None, current=None, og_type="website"):
    full = title if title == SITE["name"] else f"{title} | {SITE['name']}"
    url = abs_u(path)
    sch = ""
    if schema:
        sch = "".join(f'<script type="application/ld+json">{json.dumps(s, ensure_ascii=False)}</script>' for s in schema)
    cur = ' aria-current="page"'
    nav = "".join(f'<a href="{u(s)}"{cur if current==s else ""}>{n}</a>' for s,n in NAV)
    drawer = ""
    for p in PILLARS:
        drawer += f'<a href="{u(p["slug"])}">{p["emoji"]} {p["name"]}</a>'
        for s in p["subs"]:
            drawer += f'<a class="sub" href="{u(p["slug"]+"/"+s["slug"])}">{s["name"]}</a>'
    for s,n in [("explains","Viral Veer Explains"),("vs","Viral Veer vs"),("dictionary","Viral Veer Dictionary"),("podcast","Podcast / Videos"),("media","Media"),("about","About Viral Veer"),("contact","Contact")]:
        drawer += f'<a href="{u(s)}">{n}</a>'
    pillar_links = "".join(f'<a href="{u(p["slug"])}">{p["name"]}</a>' for p in PILLARS)
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(full)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="{og_type}"><meta property="og:site_name" content="{SITE['name']}">
<meta property="og:title" content="{esc(full)}"><meta property="og:description" content="{esc(desc)}"><meta property="og:url" content="{url}">
<meta name="twitter:card" content="summary">
<meta name="robots" content="index,follow,max-snippet:-1,max-image-preview:large">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='14' fill='%23b4461c'/%3E%3Ctext x='32' y='44' font-family='Georgia,serif' font-size='34' font-weight='700' fill='%23fff6f1' text-anchor='middle'%3EVV%3C/text%3E%3C/svg%3E">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,500;0,9..144,600;0,9..144,700;1,9..144,500&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{BASE}/assets/site.css">
<script>try{{var t=localStorage.getItem('tvv-theme');if(t)document.documentElement.setAttribute('data-theme',t)}}catch(e){{}}</script>
{sch}
</head>
<body>
<header class="top"><div class="wrap">
<a class="brand" href="{u()}">The Viral <span>Veer</span></a>
<nav class="nav" aria-label="Primary">{nav}</nav>
<div style="display:flex;gap:8px;align-items:center">
<a class="ask-btn" href="{u('ask')}">Ask Viral Veer →</a>
<button class="menu-btn" aria-label="Menu" aria-expanded="false" onclick="var d=document.getElementById('drawer');d.classList.toggle('open');this.setAttribute('aria-expanded',d.classList.contains('open'))">☰</button>
</div></div>
<div class="drawer" id="drawer">{drawer}</div>
</header>
<main>{body}</main>
<footer><div class="wrap">
<div class="cols">
<div><div class="brand">The Viral <span>Veer</span></div><p style="margin-top:8px;max-width:38ch">{SITE['tagline']} The guy you ask when life gets complicated.</p>
<div class="pills"><a class="pill" href="{SITE['instagram']}" rel="me">Instagram</a><a class="pill" href="{SITE['youtube']}" rel="me">YouTube</a><a class="pill" href="{SITE['linkedin']}" rel="me">LinkedIn</a><a class="pill" href="{SITE['x']}" rel="me">X</a></div></div>
<div><h4>Topics</h4>{pillar_links}</div>
<div><h4>Series</h4><a href="{u('ask')}">Ask Viral Veer</a><a href="{u('explains')}">Viral Veer Explains</a><a href="{u('vs')}">Viral Veer vs</a><a href="{u('dictionary')}">Dictionary</a><a href="{u('podcast')}">Podcast / Videos</a></div>
<div><h4>Viral Veer</h4><a href="{u('about')}">About</a><a href="{u('media')}">Media</a><a href="{u('contact')}">Contact</a><a href="{BASE}/sitemap.xml">Sitemap</a></div>
</div>
<div class="foot-note"><span>© {datetime.date.today().year} The Viral Veer. Opinions are personal experience, labelled as such.</span>
<button class="theme" onclick="var r=document.documentElement;var d=r.getAttribute('data-theme')==='dark'||(!r.getAttribute('data-theme')&&matchMedia('(prefers-color-scheme: dark)').matches);var n=d?'light':'dark';r.setAttribute('data-theme',n);try{{localStorage.setItem('tvv-theme',n)}}catch(e){{}}">Toggle theme</button></div>
</div></footer>
</body></html>"""

def write(path, html_str, prio="0.6"):
    d = os.path.join(OUT, path.strip("/")) if path else OUT
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "index.html"), "w") as f:
        f.write(html_str)
    PAGES.append((abs_u(path), prio))

def crumbs(items):
    out = f'<div class="wrap crumbs"><a href="{u()}">Home</a>'
    for name, path in items:
        out += f'<span>/</span>' + (f'<a href="{u(path)}">{esc(name)}</a>' if path is not None else esc(name))
    return out + "</div>"

def breadcrumb_schema(items):
    lst = [{"@type":"ListItem","position":1,"name":"Home","item":abs_u()}]
    for i,(name,path) in enumerate(items, start=2):
        lst.append({"@type":"ListItem","position":i,"name":name,"item":abs_u(path or "")})
    return {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":lst}

PERSON = {"@context":"https://schema.org","@type":"Person","@id":abs_u("about")+"#person","name":"Viral Veer","alternateName":"The Viral Veer","url":abs_u(),
    "description":SITE["description"],"jobTitle":"Content creator, technology and corporate professional","nationality":"Indian",
    "knowsAbout":["Relationships","Dating","Marriage","Career advice","Leadership","Salary negotiation","Office politics","Artificial intelligence","Technology","Modern life","Travel"],
    "sameAs":[SITE["instagram"],SITE["youtube"],SITE["linkedin"],SITE["x"]]}
WEBSITE = {"@context":"https://schema.org","@type":"WebSite","name":SITE["name"],"url":abs_u(),"description":SITE["description"],"publisher":{"@id":PERSON["@id"]},"inLanguage":"en"}

def pillar_by(slug): return next(p for p in PILLARS if p["slug"]==slug)
def sub_by(p, slug): return next(s for s in p["subs"] if s["slug"]==slug)
ART_BY_TITLE = {a["title"]: a for a in ARTICLES}

def article_card(a):
    p = pillar_by(a["pillar"])
    return f'<a class="card" href="{u(a["pillar"]+"/"+a["slug"])}"><span class="label">{p["emoji"]} {p["name"]} · {sub_by(p,a["sub"])["name"]}</span><h3>{esc(a["title"])}</h3><p>{esc(a["short"][:140])}…</p></a>'

def qlist(questions, pillar_slug):
    items = ""
    for q in questions:
        a = ART_BY_TITLE.get(q)
        if a:
            items += f'<li><a href="{u(a["pillar"]+"/"+a["slug"])}">{esc(q)}<span class="tag">Read →</span></a></li>'
        else:
            items += f'<li><span class="soon">{esc(q)}<span class="tag">Coming soon</span></span></li>'
    return f'<ul class="qlist">{items}</ul>'

# ---------- pages ----------
def home():
    pillars = "".join(f'<a class="card" href="{u(p["slug"])}"><div class="emoji">{p["emoji"]}</div><h3>{p["name"]}</h3><p>{esc(p["lede"].split(".")[0])}.</p></a>' for p in PILLARS)
    arts = "".join(article_card(a) for a in ARTICLES[:6])
    series = [
        ("explains","Viral Veer Explains","Why people ghost, cheat, procrastinate and hate their jobs. One honest explanation each."),
        ("vs","Viral Veer vs","Love vs attraction. Confidence vs arrogance. Career vs job. The difference, in two lines."),
        ("dictionary","Viral Veer Dictionary","The 3C Rule, the Attention Test, the Exit Test. Concepts I use to think clearly about people."),
        ("ask","Ask Viral Veer","Got a question about life, love or work? Ask. Selected questions get a full answer here."),
    ]
    series_html = "".join(f'<a class="card" href="{u(s)}"><h3>{n}</h3><p>{d}</p></a>' for s,n,d in series)
    asks = "".join(f'<a class="card" href="{u("ask")}"><span class="label">Ask Viral Veer · {c}</span><h3 class="serif" style="font-size:18px">{esc(q)}</h3><p>{esc(a[:150])}…</p></a>' for q,c,a in ASK_SAMPLES)
    body = f"""
<section class="hero"><div class="wrap">
<span class="kicker">Relationships · Career · Technology · Life</span>
<h1 class="big">Smart advice for modern life.</h1>
<p class="sub">I've spent decades navigating people, technology, corporate life, relationships and the world. I've learned a few things along the way. Some the hard way.</p>
<p class="quote">The guy you ask when life gets complicated.</p>
<div class="cta" style="margin-top:28px"><a class="btn accent" href="{u('ask')}">Ask Viral Veer →</a><a class="btn ghost" href="{u('about')}">Who is Viral Veer?</a></div>
</div></section>
<section class="section"><div class="wrap">
<div class="section-head"><h2>What do you want to know?</h2></div>
<div class="grid c5">{pillars}</div>
</div></section>
<section class="section band"><div class="wrap">
<div class="section-head"><h2>Start here</h2><a href="{u('relationships')}">All answers →</a></div>
<div class="grid c3">{arts}</div>
</div></section>
<section class="section"><div class="wrap">
<div class="section-head"><h2>The series</h2></div>
<div class="grid c4">{series_html}</div>
</div></section>
<section class="section band"><div class="wrap">
<div class="section-head"><h2>Recently asked</h2><a href="{u('ask')}">Ask your own →</a></div>
<div class="grid c3">{asks}</div>
</div></section>
<section class="section"><div class="wrap" style="max-width:720px">
<h2>Why this site exists</h2>
<p class="lede">Instagram is where people discover Viral Veer. This site is where the thinking lives in full: one question per page, a short answer first, then the signs, the mistakes and my take. Written from experience, labelled as experience, and sourced when a claim needs a source.</p>
<p><a href="{u('about')}" class="accent" style="font-weight:600">Read about Viral Veer →</a></p>
</div></section>"""
    write("", layout(SITE["name"], SITE["description"], body, "", [WEBSITE, PERSON]), "1.0")

def about():
    body = f"""{crumbs([("About Viral Veer", None)])}
<div class="wrap article"><div class="article-head"><span class="label">Who is Viral Veer?</span><h1>Viral Veer</h1>
<p class="lede">Viral Veer is an Indian content creator, technology and corporate professional, and commentator on relationships, careers and modern life. Drawing on decades of professional experience, international exposure and personal observation, he creates practical advice about navigating work, relationships, technology and everyday life.</p></div>
<div class="body">
<h2>In short</h2>
<p>A worldly, experienced, technology-savvy Indian man who has spent decades navigating careers, relationships, people and life, and shares the practical lessons learned along the way. Not a professor, not a guru, not a therapist. The smart older friend who has seen enough of life to tell you what actually happens.</p>
<h2>Career</h2>
<p>Viral Veer has worked in technology and corporate leadership for several decades, including senior technology roles, building and running teams and products across industries. That experience, on both sides of the hiring table and both sides of the management line, informs the <a href="{u('career')}">Career</a> section of this site.</p>
<h2>Technology</h2>
<p>A technology professional by training and trade, he has lived through outsourcing, cloud, mobile and now AI, and writes about <a href="{u('technology')}">technology for real life</a>: what matters for ordinary people and professionals, without the jargon.</p>
<h2>International experience</h2>
<p>Having lived and worked in several countries, he writes about what different cultures teach you about people, and what living abroad teaches you about India. See <a href="{u('travel-and-living')}">Travel &amp; Living</a>.</p>
<h2>Content creation</h2>
<p>Viral Veer is known on Instagram for short, direct advice on relationships, careers and life, including the <em>Zindagi Ke Smart Tips</em> series and <em>The Viral Veer Show</em>. This website is the long-form home for that work: every question gets its own page, written in the <a href="{u('relationships/how-to-know-if-someone-likes-you')}">Viral Veer Answer format</a>.</p>
<h2>Series</h2>
<ul class="qlist">
<li><a href="{u('ask')}">Ask Viral Veer<span class="tag">Questions from readers</span></a></li>
<li><a href="{u('explains')}">Viral Veer Explains<span class="tag">Why people do what they do</span></a></li>
<li><a href="{u('vs')}">Viral Veer vs<span class="tag">Comparisons</span></a></li>
<li><a href="{u('dictionary')}">Viral Veer Dictionary<span class="tag">Concepts and rules</span></a></li>
<li><a href="{u('podcast')}">Podcast / Videos<span class="tag">The Viral Veer Show</span></a></li>
</ul>
<h2>Media and interviews</h2>
<p>Appearances, interviews and quotes are listed on the <a href="{u('media')}">Media page</a>. For interview and collaboration requests, see <a href="{u('contact')}">Contact</a>.</p>
<h2>How the advice is written</h2>
<p>Personal observations are labelled as experience. Factual claims are sourced. On contested topics, both sides are shown: <em>Viral Veer's view</em> and <em>what research suggests</em>, kept separate so you can tell which is which.</p>
<h2>Profiles</h2>
<div class="pills"><a class="pill" href="{SITE['instagram']}" rel="me">Instagram</a><a class="pill" href="{SITE['youtube']}" rel="me">YouTube</a><a class="pill" href="{SITE['linkedin']}" rel="me">LinkedIn</a><a class="pill" href="{SITE['x']}" rel="me">X</a></div>
</div></div>"""
    write("about", layout("About Viral Veer", "Who is Viral Veer? Indian content creator, technology and corporate professional, and commentator on relationships, careers, technology and modern life.", body, "about", [PERSON, breadcrumb_schema([("About Viral Veer","about")])], og_type="profile"), "0.9")

def pillar_pages():
    for p in PILLARS:
        subs = "".join(f'<a class="card" href="{u(p["slug"]+"/"+s["slug"])}"><h3>{s["name"]}</h3><p>{esc(s["lede"])}</p><p style="margin-top:10px;color:var(--ink-3);font-size:12px">{len(s["questions"])} questions</p></a>' for s in p["subs"])
        arts = [a for a in ARTICLES if a["pillar"]==p["slug"]]
        arts_html = ("<div class='section-head'><h2>Answers</h2></div><div class='grid c2'>" + "".join(article_card(a) for a in arts) + "</div>") if arts else ""
        allq = []
        for s in p["subs"]: allq += s["questions"]
        body = f"""{crumbs([(p["name"], None)])}
<div class="wrap"><div class="article-head"><span class="label">{p["emoji"]} Pillar</span><h1>{p["name"]}</h1><p class="lede">{esc(p["lede"])}</p></div>
<div class="grid c3" style="margin:12px 0 48px">{subs}</div>
{arts_html}
<div class="section-head" style="margin-top:48px"><h2>Every question in {p["name"]}</h2></div>
<div class="article">{qlist(allq, p["slug"])}</div>
</div>"""
        write(p["slug"], layout(p["name"], p["lede"], body, p["slug"], [breadcrumb_schema([(p["name"],p["slug"])])], current=p["slug"]), "0.9")
        for s in p["subs"]:
            path = f'{p["slug"]}/{s["slug"]}'
            body = f"""{crumbs([(p["name"], p["slug"]),(s["name"], None)])}
<div class="wrap article"><div class="article-head"><span class="label">{p["emoji"]} {p["name"]}</span><h1>{s["name"]}</h1><p class="lede">{esc(s["lede"])}</p></div>
<h2 style="margin-top:24px">Questions</h2>{qlist(s["questions"], p["slug"])}
<div class="take" style="margin-top:40px"><h2>Have a question not listed?</h2><p>Ask it. Selected questions get a full answer page.</p><p><a class="btn accent" href="{u('ask')}">Ask Viral Veer →</a></p></div>
</div>"""
            write(path, layout(f'{s["name"]} · {p["name"]}', s["lede"], body, path, [breadcrumb_schema([(p["name"],p["slug"]),(s["name"],path)])], current=p["slug"]), "0.8")

def article_pages():
    for a in ARTICLES:
        p = pillar_by(a["pillar"]); s = sub_by(p, a["sub"])
        path = f'{a["pillar"]}/{a["slug"]}'
        steps = "".join(f'<li><div><b>{esc(h)}</b><span>{esc(d)}</span></div></li>' for h,d in a["signs"])
        take = "".join(f'<p>{esc(t)}</p>' for t in a["take"])
        mist = "".join(f'<li>{esc(m)}</li>' for m in a["mistakes"])
        faqs = "".join(f'<details><summary>{esc(q)}</summary><p>{esc(ans)}</p></details>' for q,ans in a["faqs"])
        related = [x for x in ARTICLES if x["slug"]!=a["slug"]][:3]
        rel = "".join(article_card(x) for x in related)
        body = f"""{crumbs([(p["name"],p["slug"]),(s["name"],f'{p["slug"]}/{s["slug"]}'),(a["title"],None)])}
<div class="wrap article">
<div class="article-head"><span class="label">{p["emoji"]} {p["name"]} · {s["name"]}</span><h1>{esc(a["title"])}</h1>
<div class="meta"><span class="who"><span class="avatar">VV</span>Viral Veer</span><span>Updated {TODAY}</span><span>From experience, labelled as such</span></div></div>
<div class="short"><span class="label">Short answer</span><p>{esc(a["short"])}</p></div>
<div class="body">
<h2>{esc(a["signs_heading"])}</h2><ol class="steps">{steps}</ol>
<div class="take"><h2><span class="avatar">VV</span>But here's the important part</h2>{take}</div>
<h2>Common mistakes people make</h2><ul class="mist">{mist}</ul>
<h2>Frequently asked questions</h2>{faqs}
<div class="take"><h2>Viral Veer's take</h2><p>{esc(a["take"][-1])}</p><p class="notice">This is personal experience and observation, not clinical or legal advice. Where research is cited, it is linked.</p></div>
</div>
<div class="related"><div class="section-head"><h2>Keep reading</h2></div><div class="grid c3">{rel}</div></div>
</div>"""
        schema = [
            {"@context":"https://schema.org","@type":"Article","headline":a["title"],"description":a["description"],"url":abs_u(path),"datePublished":TODAY,"dateModified":TODAY,
             "author":{"@id":PERSON["@id"]},"publisher":{"@id":PERSON["@id"]},"mainEntityOfPage":abs_u(path),"articleSection":p["name"],"inLanguage":"en"},
            {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":ans}} for q,ans in a["faqs"]]},
            breadcrumb_schema([(p["name"],p["slug"]),(s["name"],f'{p["slug"]}/{s["slug"]}'),(a["title"],path)]),
        ]
        write(path, layout(a["title"], a["description"], body, path, schema, current=p["slug"], og_type="article"), "0.8")

def ask():
    cats = "".join(f'<span class="pill">{e} {n}</span>' for e,n in ASK_CATEGORIES)
    opts = "".join(f'<option>{n}</option>' for e,n in ASK_CATEGORIES)
    samples = "".join(f'<div class="card"><span class="label">{c}</span><h3 class="serif">Ask Viral Veer: {esc(q)}</h3><p style="font-size:15px;color:var(--ink)">{esc(a)}</p></div>' for q,c,a in ASK_SAMPLES)
    body = f"""{crumbs([("Ask Viral Veer", None)])}
<div class="wrap"><div class="article-head"><span class="label">The heart of the site</span><h1>Ask Viral Veer</h1><p class="lede">Got a question about life, love or work? Ask it here. Selected questions are answered in full on this site, anonymised. The rest get a short reply by email when time allows.</p>
<div class="pills" style="margin-top:16px">{cats}</div></div>
<div class="grid c2" style="margin-top:32px;align-items:start">
<form class="card" action="mailto:{SITE['email']}" method="post" enctype="text/plain" onsubmit="return tvvSend(this)">
<div class="f"><label class="label" for="q">Your question</label><textarea id="q" name="question" required placeholder="I'm 35 and afraid I'll never find the right partner. What should I do?"></textarea></div>
<div class="f"><label class="label" for="c">Category</label><select id="c" name="category">{opts}</select></div>
<div class="f"><label class="label" for="n">Name or initials (optional)</label><input id="n" name="name" placeholder="A., Pune"></div>
<div class="f"><label class="label" for="e">Email (optional, for a reply)</label><input id="e" name="email" type="email" placeholder="you@example.com"></div>
<button class="btn accent" type="submit">Send to Viral Veer</button>
<p class="notice" style="margin-top:12px">Questions may be published in edited, anonymised form. No names, employers or identifying details are ever published.</p>
</form>
<div><div class="grid">{samples}</div></div>
</div></div>
<script>function tvvSend(f){{var s="Question: "+f.question.value+"\\nCategory: "+f.category.value+"\\nName: "+f.name.value+"\\nEmail: "+f.email.value;location.href="mailto:{SITE['email']}?subject="+encodeURIComponent("Ask Viral Veer: "+f.category.value)+"&body="+encodeURIComponent(s);return false}}</script>"""
    write("ask", layout("Ask Viral Veer", "Ask Viral Veer a question about relationships, career, life, technology, money, travel or family. Selected questions are answered in full.", body, "ask", [breadcrumb_schema([("Ask Viral Veer","ask")])]), "0.9")

def explains():
    cards = "".join(f'<a class="card" href="{u("explains/"+s)}"><span class="label">Viral Veer Explains</span><h3>{esc(t)}</h3><p>{esc(d)}</p></a>' for s,t,d in EXPLAINS)
    body = f"""{crumbs([("Viral Veer Explains", None)])}
<div class="wrap"><div class="article-head"><span class="label">Series</span><h1>Viral Veer Explains</h1><p class="lede">Why people do what they do. One honest explanation per page, from someone who has watched the same patterns repeat for decades.</p></div>
<div class="grid c2" style="margin-top:24px">{cards}</div></div>"""
    write("explains", layout("Viral Veer Explains", "Why people ghost, cheat, fall out of love, procrastinate and hate their jobs. Short, honest explanations from Viral Veer.", body, "explains", [breadcrumb_schema([("Viral Veer Explains","explains")])], current="explains"), "0.8")
    for s,t,d in EXPLAINS:
        path = "explains/"+s
        others = "".join(f'<li><a href="{u("explains/"+s2)}">{esc(t2)}<span class="tag">Read →</span></a></li>' for s2,t2,_ in EXPLAINS if s2!=s)
        body = f"""{crumbs([("Viral Veer Explains","explains"),(t,None)])}
<div class="wrap article"><div class="article-head"><span class="label">Viral Veer Explains</span><h1>{esc(t)}</h1>
<div class="meta"><span class="who"><span class="avatar">VV</span>Viral Veer</span><span>Updated {TODAY}</span></div></div>
<div class="short"><span class="label">In one breath</span><p>{esc(d)}</p></div>
<div class="body"><p>{esc(d)} That is the short version. The full explanation, with the patterns I have seen and what to do about it, is being written. Until then, the short version is the part that matters.</p>
<div class="take"><h2>Viral Veer's take</h2><p>Most human behaviour that looks mysterious is just a habit plus an incentive. Find the incentive and the mystery disappears.</p></div>
<h2>More explanations</h2><ul class="qlist">{others}</ul></div></div>"""
        write(path, layout(t, d, body, path, [breadcrumb_schema([("Viral Veer Explains","explains"),(t,path)]), {"@context":"https://schema.org","@type":"Article","headline":t,"description":d,"url":abs_u(path),"author":{"@id":PERSON["@id"]},"datePublished":TODAY}], current="explains", og_type="article"), "0.7")

def versus():
    cards = "".join(f'<a class="card" href="{u("vs/"+s)}"><span class="label">Viral Veer vs</span><h3>{esc(t)}</h3><p>{esc(l)}</p></a>' for s,t,l,_ in VERSUS)
    body = f"""{crumbs([("Viral Veer vs", None)])}
<div class="wrap"><div class="article-head"><span class="label">Series</span><h1>Viral Veer vs</h1><p class="lede">Two things people confuse, and the difference that matters. Love vs attraction. Confidence vs arrogance. Career vs job.</p></div>
<div class="grid c2" style="margin-top:24px">{cards}</div></div>"""
    write("vs", layout("Viral Veer vs", "Love vs attraction, confidence vs arrogance, chemistry vs compatibility, career vs job. Viral Veer explains the difference.", body, "vs", [breadcrumb_schema([("Viral Veer vs","vs")])], current="vs"), "0.8")
    for s,t,l,d in VERSUS:
        path = "vs/"+s
        a,b = t.split(" vs ")
        others = "".join(f'<li><a href="{u("vs/"+s2)}">{esc(t2)}<span class="tag">Read →</span></a></li>' for s2,t2,_,_ in VERSUS if s2!=s)
        body = f"""{crumbs([("Viral Veer vs","vs"),(t,None)])}
<div class="wrap article"><div class="article-head"><span class="label">Viral Veer vs</span><h1>{esc(t)}</h1>
<div class="meta"><span class="who"><span class="avatar">VV</span>Viral Veer</span><span>Updated {TODAY}</span></div></div>
<div class="card" style="margin:20px 0"><div class="vs"><span>{esc(a)}</span><i>vs</i><span>{esc(b)}</span></div></div>
<div class="short"><span class="label">The difference</span><p>{esc(l)}</p></div>
<div class="body"><p>{esc(d)}</p>
<div class="take"><h2>Viral Veer's take</h2><p>{esc(l)}</p></div>
<h2>More comparisons</h2><ul class="qlist">{others}</ul></div></div>"""
        write(path, layout(t, l+" "+d, body, path, [breadcrumb_schema([("Viral Veer vs","vs"),(t,path)]), {"@context":"https://schema.org","@type":"Article","headline":t,"description":l,"url":abs_u(path),"author":{"@id":PERSON["@id"]},"datePublished":TODAY}], current="vs", og_type="article"), "0.7")

def dictionary():
    dl = "".join(f'<dt id="{s}"><a href="{u("dictionary/"+s)}">{esc(t)}</a></dt><dd><b>{esc(o)}</b> {esc(d)}</dd>' for s,t,o,d in DICTIONARY)
    body = f"""{crumbs([("Viral Veer Dictionary", None)])}
<div class="wrap article"><div class="article-head"><span class="label">Series</span><h1>Viral Veer Dictionary</h1><p class="lede">The concepts and rules I use to think clearly about people, work and life. Each one is a shortcut earned the slow way.</p></div>
<dl class="def">{dl}</dl></div>"""
    defined = [{"@type":"DefinedTerm","name":t,"description":o+" "+d,"url":abs_u("dictionary/"+s)} for s,t,o,d in DICTIONARY]
    write("dictionary", layout("Viral Veer Dictionary", "The 3C Rule, the 3R Rule, the Career Ceiling, the Attention Test, the Exit Test and other Viral Veer concepts, defined.", body, "dictionary", [breadcrumb_schema([("Viral Veer Dictionary","dictionary")]), {"@context":"https://schema.org","@type":"DefinedTermSet","name":"Viral Veer Dictionary","hasDefinedTerm":defined}], current="dictionary"), "0.8")
    for s,t,o,d in DICTIONARY:
        path = "dictionary/"+s
        others = "".join(f'<li><a href="{u("dictionary/"+s2)}">{esc(t2)}<span class="tag">{esc(o2)}</span></a></li>' for s2,t2,o2,_ in DICTIONARY if s2!=s)
        body = f"""{crumbs([("Viral Veer Dictionary","dictionary"),(t,None)])}
<div class="wrap article"><div class="article-head"><span class="label">Viral Veer Dictionary</span><h1>What is {esc(t)}?</h1></div>
<div class="short"><span class="label">Definition</span><p>{esc(o)}</p></div>
<div class="body"><p>{esc(d)}</p>
<div class="take"><h2>Where it came from</h2><p>{esc(t)} is a Viral Veer concept: a rule of thumb built from years of watching the same situations play out in offices, families and relationships. It is a lens, not a law.</p></div>
<h2>More concepts</h2><ul class="qlist">{others}</ul></div></div>"""
        write(path, layout(f"What is {t}?", f"{t}: {o} {d}", body, path, [breadcrumb_schema([("Viral Veer Dictionary","dictionary"),(t,path)]), {"@context":"https://schema.org","@type":"DefinedTerm","name":t,"description":o+" "+d,"url":abs_u(path),"inDefinedTermSet":abs_u("dictionary")}], current="dictionary"), "0.7")

def podcast():
    eps = "".join(f'<li><a href="{e["url"]}" target="_blank" rel="noopener">{esc(e["title"])}<span class="tag">{e["kind"]} · {e["dur"]}</span></a></li>' for e in EPISODES)
    body = f"""{crumbs([("Podcast / Videos", None)])}
<div class="wrap article"><div class="article-head"><span class="label">The Viral Veer Show · Zindagi Ke Smart Tips</span><h1>Podcast / Videos</h1><p class="lede">Every Reel and episode maps to a question on this site. Watch the short version there, read the full version here.</p></div>
<div class="pills" style="margin:8px 0 28px"><a class="pill" href="{SITE['youtube']}">YouTube</a><a class="pill" href="{SITE['instagram']}">Instagram Reels</a></div>
<h2>Latest</h2><ul class="qlist">{eps}</ul>
<div class="take" style="margin-top:40px"><h2>How the show works</h2><p>One idea becomes one article, ten FAQs, a 60-second Reel, a longer video and a podcast conversation. Same thinking, different lengths. Pick the one that fits your day.</p></div></div>"""
    write("podcast", layout("Podcast / Videos", "The Viral Veer Show and Zindagi Ke Smart Tips: videos, Reels and podcast episodes on relationships, career, technology and life.", body, "podcast", [breadcrumb_schema([("Podcast / Videos","podcast")])]), "0.7")

def media():
    cards = "".join(f'<a class="card" href="{u("media/"+m["slug"])}"><span class="label">{m["outlet"]} · {m["topic"]} · {m["date"]}</span><h3>{esc(m["title"])}</h3><p>{esc(m["summary"])}</p></a>' for m in MEDIA)
    body = f"""{crumbs([("Media", None)])}
<div class="wrap"><div class="article-head"><span class="label">Viral Veer in the media</span><h1>Media</h1><p class="lede">Interviews, podcast appearances, quotes and features. Viral Veer speaks on three things: modern relationships, technology and careers, and modern life.</p></div>
<div class="grid c3" style="margin-top:24px">{cards}</div>
<div class="take" style="margin-top:40px;max-width:720px"><h2>For journalists and podcasters</h2><p>Available for comment on modern dating, relationships in India, AI and careers, executive careers, office politics and living abroad. <a class="accent" style="font-weight:600" href="{u('contact')}">Contact →</a></p></div></div>"""
    write("media", layout("Viral Veer in the Media", "Interviews, podcast appearances and features with Viral Veer on relationships, technology, careers and modern life.", body, "media", [breadcrumb_schema([("Media","media")])]), "0.7")
    for m in MEDIA:
        path = "media/"+m["slug"]
        body = f"""{crumbs([("Media","media"),(m["title"],None)])}
<div class="wrap article"><div class="article-head"><span class="label">{m["outlet"]} · {m["topic"]} · {m["date"]}</span><h1>{esc(m["title"])}</h1><p class="lede">{esc(m["summary"])}</p></div>
<p><a class="btn ghost" href="{m["url"]}" rel="noopener">View the original coverage →</a></p>
<p class="notice">Link to be added when coverage is published.</p>
<div class="take"><h2>Related reading on this site</h2><ul class="qlist">{"".join(f'<li><a href="{u(a["pillar"]+"/"+a["slug"])}">{esc(a["title"])}<span class="tag">Read →</span></a></li>' for a in ARTICLES[:3])}</ul></div></div>"""
        write(path, layout(m["title"], m["summary"], body, path, [breadcrumb_schema([("Media","media"),(m["title"],path)])]), "0.5")

def contact():
    body = f"""{crumbs([("Contact", None)])}
<div class="wrap article"><div class="article-head"><span class="label">Get in touch</span><h1>Contact</h1><p class="lede">For interviews, podcast invitations, speaking, collaborations and press. For personal questions, use <a class="accent" href="{u('ask')}">Ask Viral Veer</a> instead.</p></div>
<div class="grid c2">
<div class="card"><span class="label">Email</span><h3><a href="mailto:{SITE['email']}">{SITE['email']}</a></h3><p>Replies within a few days for media and business requests.</p></div>
<div class="card"><span class="label">Social</span><div class="pills" style="margin-top:10px"><a class="pill" href="{SITE['instagram']}">Instagram</a><a class="pill" href="{SITE['youtube']}">YouTube</a><a class="pill" href="{SITE['linkedin']}">LinkedIn</a><a class="pill" href="{SITE['x']}">X</a></div></div>
</div>
<div class="take" style="margin-top:32px"><h2>What Viral Veer speaks on</h2><p>Modern dating and relationships · AI and careers · executive careers and office politics · technology for real life · living abroad and what it teaches you about India.</p></div></div>"""
    write("contact", layout("Contact Viral Veer", "Contact Viral Veer for interviews, podcasts, speaking, collaborations and press.", body, "contact", [breadcrumb_schema([("Contact","contact")])]), "0.5")

def not_found():
    body = f"""<div class="wrap hero"><span class="kicker">404</span><h1>That page has moved on.</h1><p class="sub">Which, as it happens, is a topic I cover. Try one of the pillars or ask a question.</p>
<div class="cta" style="margin-top:24px"><a class="btn" href="{u()}">Home</a><a class="btn accent" href="{u('ask')}">Ask Viral Veer →</a></div></div>"""
    html_str = layout("Page not found", "Page not found", body, "404")
    with open(os.path.join(OUT, "404.html"), "w") as f: f.write(html_str)

def extras():
    os.makedirs(os.path.join(OUT, "assets"), exist_ok=True)
    with open(os.path.join(OUT, "assets", "site.css"), "w") as f: f.write(CSS)
    open(os.path.join(OUT, ".nojekyll"), "w").close()
    with open(os.path.join(OUT, "robots.txt"), "w") as f:
        f.write(f"User-agent: *\nAllow: /\n\n# AI search crawlers explicitly welcome\nUser-agent: OAI-SearchBot\nAllow: /\nUser-agent: ChatGPT-User\nAllow: /\nUser-agent: PerplexityBot\nAllow: /\nUser-agent: Google-Extended\nAllow: /\nUser-agent: Bingbot\nAllow: /\n\nSitemap: {ORIGIN}{BASE}/sitemap.xml\n")
    with open(os.path.join(OUT, "sitemap.xml"), "w") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
        for url, prio in PAGES:
            f.write(f"  <url><loc>{url}</loc><lastmod>{TODAY}</lastmod><priority>{prio}</priority></url>\n")
        f.write("</urlset>\n")
    with open(os.path.join(OUT, "CNAME.example"), "w") as f: f.write("theviralveer.com\n")

if __name__ == "__main__":
    if os.path.isdir(OUT): shutil.rmtree(OUT)
    os.makedirs(OUT)
    home(); about(); pillar_pages(); article_pages(); ask(); explains(); versus(); dictionary(); podcast(); media(); contact(); not_found(); extras()
    print(f"built {len(PAGES)} pages -> {OUT}")
