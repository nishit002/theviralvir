#!/usr/bin/env python3
"""Static site generator for The Viral Vir. Run: python3 build.py"""
import os, json, shutil, html, datetime
from content import *

BASE = os.environ.get("TVV_BASE", "/theviralvir")
ORIGIN = os.environ.get("TVV_ORIGIN", "https://nishit002.github.io")
ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "docs")
TODAY = datetime.date.today().isoformat()
esc = html.escape
UNSPLASH = json.load(open(os.path.join(ROOT, "unsplash.json"))) if os.path.exists(os.path.join(ROOT, "unsplash.json")) else {}

def u(path=""):
    path = path.strip("/")
    return f"{BASE}/{path}/" if path else f"{BASE}/"
def abs_u(path=""): return ORIGIN + u(path)
def img(name): return f"{BASE}/assets/img/{name}"
PAGES = []

CSS = r"""
:root{--bg:#ffffff;--bg2:#f5f7fb;--card:#ffffff;--ink:#121a2f;--ink2:#4b5566;--ink3:#8691a3;--line:#e5e8ef;--brand:#e63946;--brand-2:#c92a37;--brand-ink:#ffffff;--navy:#121a2f;--navy-ink:#ffffff;--pill:#eef1f7;--shadow:0 1px 3px rgba(18,26,47,.08);--shadow-2:0 12px 32px rgba(18,26,47,.10);
--c-relationships:#e11d74;--c-career:#2563eb;--c-life:#7c3aed;--c-technology:#0d9488;--c-travel-and-living:#16a34a;--c-series:#f59e0b}
:root:not([data-theme="light"]){color-scheme:light dark}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#0f1424;--bg2:#161c30;--card:#1a2138;--ink:#eef1f7;--ink2:#aab3c5;--ink3:#6f7a91;--line:#273050;--brand:#ff5a66;--brand-2:#ff7883;--navy:#eef1f7;--navy-ink:#0f1424;--pill:#232b45;--shadow:0 1px 3px rgba(0,0,0,.4);--shadow-2:0 12px 32px rgba(0,0,0,.45);--c-relationships:#ff5fa2;--c-career:#6b9bff;--c-life:#b08cff;--c-technology:#3fcbbd;--c-travel-and-living:#4ade80}}
:root[data-theme="dark"]{--bg:#0f1424;--bg2:#161c30;--card:#1a2138;--ink:#eef1f7;--ink2:#aab3c5;--ink3:#6f7a91;--line:#273050;--brand:#ff5a66;--brand-2:#ff7883;--navy:#eef1f7;--navy-ink:#0f1424;--pill:#232b45;--shadow:0 1px 3px rgba(0,0,0,.4);--shadow-2:0 12px 32px rgba(0,0,0,.45);--c-relationships:#ff5fa2;--c-career:#6b9bff;--c-life:#b08cff;--c-technology:#3fcbbd;--c-travel-and-living:#4ade80}
.p-relationships{--c:var(--c-relationships)}.p-career{--c:var(--c-career)}.p-life{--c:var(--c-life)}.p-technology{--c:var(--c-technology)}.p-travel-and-living{--c:var(--c-travel-and-living)}.p-series{--c:var(--c-series)}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%;scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--ink);font:15px/1.6 Inter,system-ui,-apple-system,"Segoe UI",sans-serif;-webkit-font-smoothing:antialiased}
a{color:inherit;text-decoration:none}img{max-width:100%;display:block}
.wrap{max-width:1080px;margin:0 auto;padding:0 16px}@media(min-width:768px){.wrap{padding:0 24px}}
h1,h2,h3,h4{font-family:"Plus Jakarta Sans",Inter,system-ui,sans-serif;letter-spacing:-.02em;margin:0 0 .4em}
h1{font-size:34px;font-weight:800;line-height:1.1}@media(min-width:768px){h1{font-size:46px}}
h2{font-size:24px;font-weight:700;line-height:1.2}h3{font-size:18px;font-weight:700;line-height:1.3}
p{margin:0 0 1em}.lede{font-size:17px;color:var(--ink2);max-width:62ch}
.label{font-size:12px;font-weight:600;letter-spacing:.06em;text-transform:uppercase;color:var(--ink3)}
.label.c{color:var(--c)}
.brandc{color:var(--brand)}
/* header */
.top{position:sticky;top:0;z-index:20;background:color-mix(in srgb,var(--bg) 90%,transparent);backdrop-filter:saturate(1.4) blur(12px);border-bottom:1px solid var(--line)}
.top .wrap{display:flex;align-items:center;justify-content:space-between;height:62px;gap:12px}
.brand{display:flex;align-items:center;gap:10px;font-family:"Plus Jakarta Sans",sans-serif;font-weight:800;font-size:18px;letter-spacing:-.02em;white-space:nowrap}
.brand img{width:34px;height:34px;border-radius:50%;border:2px solid var(--brand)}
.brand span{color:var(--brand)}
.nav{display:none;gap:2px}.nav a{padding:10px 12px;border-radius:100px;font-weight:600;color:var(--ink2);font-size:14px;min-height:44px;display:inline-flex;align-items:center}
.nav a:hover,.nav a[aria-current]{background:var(--pill);color:var(--ink)}
@media(min-width:960px){.nav{display:flex}}
.ask-btn{background:var(--brand);color:var(--brand-ink);padding:0 16px;height:40px;border-radius:100px;font-weight:700;font-size:14px;display:inline-flex;align-items:center;gap:6px;white-space:nowrap;box-shadow:0 4px 14px color-mix(in srgb,var(--brand) 35%,transparent)}
.ask-btn:hover{background:var(--brand-2)}.ask-btn:active{transform:scale(.97);opacity:.85}
.menu-btn{display:inline-flex;align-items:center;justify-content:center;width:44px;height:44px;border:1px solid var(--line);border-radius:12px;background:var(--card);cursor:pointer;color:var(--ink);font-size:18px}
@media(min-width:960px){.menu-btn{display:none}}
.drawer{display:none;border-top:1px solid var(--line);background:var(--bg);max-height:75vh;overflow:auto}
.drawer.open{display:block}
.drawer a{display:flex;align-items:center;min-height:48px;padding:0 16px;border-bottom:1px solid var(--line);font-weight:600}
.drawer .sub{padding-left:36px;color:var(--ink2);font-weight:400;font-size:14px;min-height:42px}
/* hero */
.hero{padding:40px 0 32px}@media(min-width:768px){.hero{padding:72px 0 56px}}
.hero-grid{display:grid;gap:28px;align-items:center}.hero-grid>*{min-width:0}@media(min-width:860px){.hero-grid{grid-template-columns:1.1fr .9fr;gap:48px}}
.kicker{display:inline-flex;align-items:center;gap:8px;margin-bottom:18px;padding:7px 14px;border-radius:100px;background:var(--pill);font-size:12px;font-weight:700;letter-spacing:.05em;text-transform:uppercase;color:var(--ink2)}
.kicker i{display:inline-block;width:8px;height:8px;border-radius:50%;background:var(--brand)}
.hero h1{font-size:40px}@media(min-width:768px){.hero h1{font-size:62px}}
.hero h1 span{color:var(--brand)}
.hero p.sub{font-size:18px;color:var(--ink2);max-width:52ch;margin-top:16px}
.quote{font-family:"Plus Jakarta Sans",sans-serif;font-weight:700;font-size:19px;color:var(--ink);max-width:52ch;margin-top:20px;border-left:4px solid var(--brand);padding-left:14px;border-radius:2px}
.portrait{position:relative;max-width:460px;margin:0 auto}
.portrait img{width:100%;height:auto;border-radius:28px;box-shadow:var(--shadow-2);aspect-ratio:1;object-fit:cover}
.chip{position:absolute;background:var(--card);border:1px solid var(--line);border-radius:16px;padding:10px 14px;box-shadow:var(--shadow-2);display:flex;align-items:center;gap:10px;font-weight:700;font-size:14px}
.chip b{font-family:"Plus Jakarta Sans",sans-serif;font-size:20px;font-weight:800;color:var(--brand);line-height:1}
.chip small{display:block;font-weight:500;color:var(--ink3);font-size:11px}
.chip.a{left:-8px;bottom:56px}.chip.b{right:-8px;top:36px}@media(max-width:480px){.chip.a{left:4px;bottom:16px}.chip.b{right:4px;top:12px}}
/* grids + cards */
.grid{display:grid;gap:14px}@media(min-width:600px){.grid.c2{grid-template-columns:1fr 1fr}.grid.c3{grid-template-columns:repeat(3,1fr)}.grid.c6{grid-template-columns:repeat(3,1fr)}}
@media(min-width:900px){.grid.c4{grid-template-columns:repeat(4,1fr)}.grid.c5{grid-template-columns:repeat(5,1fr)}.grid.c6{grid-template-columns:repeat(6,1fr)}}
.card{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:20px;box-shadow:var(--shadow);transition:transform .15s,box-shadow .15s,border-color .15s;position:relative;overflow:hidden}
a.card:hover{box-shadow:var(--shadow-2);border-color:color-mix(in srgb,var(--c,var(--brand)) 45%,var(--line))}
a.card:active{transform:scale(.97);opacity:.85}
.card h3{margin:.5em 0 .3em}.card p{color:var(--ink2);margin:0;font-size:14px}
.card.tint{background:color-mix(in srgb,var(--c) 7%,var(--card))}
.card .ico{width:44px;height:44px;border-radius:12px;display:inline-flex;align-items:center;justify-content:center;font-size:22px;background:color-mix(in srgb,var(--c) 14%,var(--card))}
.card .bar{position:absolute;left:0;top:0;right:0;height:4px;background:var(--c,var(--brand))}
.card.img{padding:0}.card.img .ph{aspect-ratio:16/10;overflow:hidden;background:var(--pill)}.card.img .ph img{width:100%;height:100%;object-fit:cover;transition:transform .3s}.card.img:hover .ph img{transform:scale(1.04)}.card.img .tx{padding:16px 18px 18px}
.section{padding:40px 0}@media(min-width:768px){.section{padding:64px 0}}
.section-head{display:flex;align-items:flex-end;justify-content:space-between;gap:12px;margin-bottom:20px}
.section-head p{color:var(--ink2);margin:0}
.section-head a.more{color:var(--brand);font-weight:700;font-size:14px;white-space:nowrap}
.band{background:var(--bg2)}
.navyband{background:var(--navy);color:var(--navy-ink)}
/* instagram strip */
.ig{display:grid;grid-template-columns:repeat(3,1fr);gap:8px}@media(min-width:760px){.ig{grid-template-columns:repeat(6,1fr);gap:12px}}
.ig a{position:relative;display:block;border-radius:14px;overflow:hidden;aspect-ratio:1;background:var(--pill)}
.ig img{width:100%;height:100%;object-fit:cover;transition:transform .3s}.ig a:hover img{transform:scale(1.05)}
.ig a::after{content:"▶";position:absolute;right:8px;top:8px;width:26px;height:26px;border-radius:50%;background:rgba(0,0,0,.55);color:#fff;font-size:11px;display:flex;align-items:center;justify-content:center}
.follow{display:flex;flex-wrap:wrap;align-items:center;gap:16px}
.follow .who{display:flex;align-items:center;gap:12px}
.follow .who img{width:56px;height:56px;border-radius:50%;border:3px solid var(--brand)}
.follow .who b{display:block;font-family:"Plus Jakarta Sans",sans-serif;font-size:17px}
.follow .who small{color:var(--ink3)}
.igbtn{display:inline-flex;align-items:center;gap:8px;min-height:46px;padding:0 20px;border-radius:100px;font-weight:700;font-size:15px;color:#fff;background:linear-gradient(45deg,#f09433,#e6683c 25%,#dc2743 50%,#cc2366 75%,#bc1888);box-shadow:0 6px 18px rgba(220,39,67,.3)}
.igbtn:active{transform:scale(.97);opacity:.85}
.ytbtn{display:inline-flex;align-items:center;gap:8px;min-height:46px;padding:0 20px;border-radius:100px;font-weight:700;font-size:15px;color:#fff;background:#ff0033}
.stats{display:grid;grid-template-columns:1fr 1fr;gap:14px}@media(min-width:760px){.stats{grid-template-columns:repeat(4,1fr)}}
.stat{text-align:center;padding:22px 12px;border-radius:16px;background:color-mix(in srgb,var(--navy-ink) 8%,transparent)}
.stat b{display:block;font-family:"Plus Jakarta Sans",sans-serif;font-size:36px;font-weight:800;line-height:1;color:var(--brand)}
.stat span{display:block;margin-top:6px;font-size:13px;opacity:.85}
/* lists */
.qlist{list-style:none;margin:0;padding:0;border-top:1px solid var(--line)}
.qlist li{border-bottom:1px solid var(--line)}
.qlist a,.qlist span.row{display:flex;align-items:center;justify-content:space-between;gap:12px;padding:14px 0;min-height:48px;font-weight:600}
.qlist a:hover{color:var(--c,var(--brand))}.qlist .soon{color:var(--ink3);font-weight:400}
.qlist .tag{font-size:12px;color:var(--ink3);font-weight:600;white-space:nowrap}.qlist a .tag{color:var(--c,var(--brand))}
.crumbs{font-size:13px;color:var(--ink3);padding:18px 0 0}.crumbs a:hover{color:var(--brand)}.crumbs span{margin:0 6px}
/* article */
.article{max-width:740px}.article-head{padding:24px 0 8px}@media(min-width:768px){.article-head{padding:44px 0 12px}}
.meta{display:flex;flex-wrap:wrap;gap:8px 16px;align-items:center;color:var(--ink3);font-size:13px;margin-top:14px}
.meta .who{display:flex;align-items:center;gap:8px;color:var(--ink2);font-weight:600}
.avatar{width:30px;height:30px;border-radius:50%;object-fit:cover;border:2px solid var(--brand)}
.heroimg{margin:20px 0 4px}.heroimg img{border-radius:18px;aspect-ratio:16/8;object-fit:cover;width:100%}
.credit{font-size:12px;color:var(--ink3);margin:8px 0 0}.credit a{text-decoration:underline}
.short{background:color-mix(in srgb,var(--c,var(--brand)) 8%,var(--card));border:1px solid color-mix(in srgb,var(--c,var(--brand)) 30%,var(--line));border-left:5px solid var(--c,var(--brand));border-radius:14px;padding:18px 20px;margin:24px 0}
.short .label{margin-bottom:6px;display:block;color:var(--c,var(--brand))}.short p{margin:0;font-size:17px;line-height:1.55;font-weight:500}
.body h2{margin-top:40px}.body p{font-size:16px}
.steps{list-style:none;counter-reset:s;margin:0;padding:0}
.steps li{counter-increment:s;display:grid;grid-template-columns:44px 1fr;gap:12px;padding:14px 0;border-bottom:1px solid var(--line)}
.steps li::before{content:counter(s);width:34px;height:34px;border-radius:10px;background:color-mix(in srgb,var(--c,var(--brand)) 14%,var(--card));color:var(--c,var(--brand));font-family:"Plus Jakarta Sans",sans-serif;font-weight:800;display:flex;align-items:center;justify-content:center}
.steps b{display:block;font-weight:700}.steps span{color:var(--ink2);font-size:15px}
.take{background:var(--bg2);border-radius:18px;padding:22px 22px 8px;margin-top:36px;border:1px solid var(--line)}
.take h2{margin-top:0;display:flex;align-items:center;gap:10px}
.mist{padding-left:0;list-style:none}.mist li{padding:10px 0 10px 30px;position:relative;border-bottom:1px solid var(--line);color:var(--ink2)}
.mist li::before{content:"✕";position:absolute;left:2px;top:11px;width:20px;height:20px;border-radius:6px;background:color-mix(in srgb,var(--brand) 14%,var(--card));color:var(--brand);font-size:11px;font-weight:700;display:flex;align-items:center;justify-content:center}
details{border-bottom:1px solid var(--line)}details summary{cursor:pointer;padding:14px 0;font-weight:700;list-style:none;display:flex;justify-content:space-between;gap:12px;min-height:48px;align-items:center}
details summary::-webkit-details-marker{display:none}
details summary::after{content:"+";color:var(--c,var(--brand));font-size:22px;font-weight:400}details[open] summary::after{content:"–"}
details p{color:var(--ink2);padding-bottom:14px;margin:0}
.related{margin-top:48px}
.followbox{margin-top:40px;border-radius:20px;padding:22px;background:var(--navy);color:var(--navy-ink);display:grid;gap:18px}@media(min-width:700px){.followbox{grid-template-columns:1fr auto;align-items:center}}
.followbox h3{margin:0 0 4px}.followbox p{margin:0;opacity:.8;font-size:14px}
.followbox .mini{display:flex;gap:6px}.followbox .mini img{width:56px;height:56px;border-radius:10px;object-fit:cover}
/* misc */
.pill{display:inline-flex;align-items:center;gap:6px;padding:8px 14px;border-radius:100px;background:var(--pill);font-size:13px;font-weight:600;min-height:36px}
.pills{display:flex;flex-wrap:wrap;gap:8px}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:8px;min-height:48px;padding:0 22px;border-radius:100px;font-weight:700;background:var(--navy);color:var(--navy-ink);font-size:15px;border:0;cursor:pointer}
.btn.brand{background:var(--brand);color:var(--brand-ink);box-shadow:0 6px 18px color-mix(in srgb,var(--brand) 35%,transparent)}.btn.ghost{background:transparent;border:1px solid var(--line);color:var(--ink)}
.btn:active{transform:scale(.97);opacity:.85}
.cta{display:flex;flex-direction:column;gap:12px}@media(min-width:600px){.cta{flex-direction:row;align-items:center;flex-wrap:wrap}}
.def dt{font-family:"Plus Jakarta Sans",sans-serif;font-size:21px;font-weight:800;margin-top:28px}.def dd{margin:6px 0 0;color:var(--ink2)}.def dd b{color:var(--ink);font-weight:700}
form .f{display:flex;flex-direction:column;gap:6px;margin-bottom:16px}
input,select,textarea{font:inherit;padding:12px 14px;border:1px solid var(--line);border-radius:10px;background:var(--card);color:var(--ink);min-height:48px;width:100%}
textarea{min-height:140px;resize:vertical}
.notice{font-size:13px;color:var(--ink3)}
.vs{display:grid;grid-template-columns:1fr auto 1fr;gap:12px;align-items:center;font-family:"Plus Jakarta Sans",sans-serif;font-size:22px;font-weight:800;text-align:center}
.vs i{font-style:normal;color:#fff;background:var(--brand);border-radius:100px;padding:4px 12px;font-size:14px}
.yt{display:grid;gap:14px}@media(min-width:600px){.yt{grid-template-columns:repeat(2,1fr)}}@media(min-width:900px){.yt{grid-template-columns:repeat(3,1fr)}}
.yt a{display:block;border-radius:14px;overflow:hidden;background:var(--card);border:1px solid var(--line)}
.yt .th{position:relative;aspect-ratio:16/9;background:var(--pill)}.yt .th img{width:100%;height:100%;object-fit:cover}
.yt .th::after{content:"▶";position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);width:52px;height:52px;border-radius:50%;background:#ff0033;color:#fff;display:flex;align-items:center;justify-content:center;font-size:18px;padding-left:4px}
.yt b{display:block;padding:12px 14px;font-size:14px;line-height:1.4}
footer{border-top:1px solid var(--line);margin-top:64px;padding:40px 0 48px;color:var(--ink2);font-size:14px;background:var(--bg2)}
footer .cols{display:grid;gap:24px}@media(min-width:768px){footer .cols{grid-template-columns:2fr 1fr 1fr 1fr}}
footer h4{margin:0 0 10px;font-size:12px;letter-spacing:.06em;text-transform:uppercase;color:var(--ink3);font-weight:600}
footer a{display:block;padding:5px 0}footer a:hover{color:var(--brand)}
.foot-note{margin-top:28px;padding-top:20px;border-top:1px solid var(--line);display:flex;flex-wrap:wrap;gap:12px;justify-content:space-between;font-size:13px;color:var(--ink3)}
.theme{background:none;border:1px solid var(--line);border-radius:100px;padding:6px 12px;color:var(--ink2);cursor:pointer;font:inherit;font-size:13px}
"""

NAV = [("relationships","Relationships"),("career","Career"),("life","Life"),("technology","Technology"),("travel-and-living","Travel"),("explains","Explains"),("vs","Vs"),("dictionary","Dictionary")]
IG_SVG = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor"/></svg>'
YT_SVG = '<svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M23 7.2a3 3 0 0 0-2.1-2.1C19 4.6 12 4.6 12 4.6s-7 0-8.9.5A3 3 0 0 0 1 7.2 31 31 0 0 0 .5 12 31 31 0 0 0 1 16.8a3 3 0 0 0 2.1 2.1c1.9.5 8.9.5 8.9.5s7 0 8.9-.5a3 3 0 0 0 2.1-2.1A31 31 0 0 0 23.5 12 31 31 0 0 0 23 7.2zM9.8 15.1V8.9l6 3.1-6 3.1z"/></svg>'

def follow_row(dark=False):
    return f'''<div class="follow"><div class="who"><img src="{img('viralvir-240.jpg')}" alt="Viral Vir" width="56" height="56"><div><b>Viral Vir</b><small>{SITE['handle']} · {SITE['stats'][0][0]} followers</small></div></div>
<a class="igbtn" href="{SITE['instagram']}" target="_blank" rel="noopener me">{IG_SVG} Follow on Instagram</a><a class="ytbtn" href="{SITE['youtube']}" target="_blank" rel="noopener me">{YT_SVG} Subscribe on YouTube</a></div>'''

def ig_strip():
    tiles = "".join(f'<a href="{SITE["instagram"]}" target="_blank" rel="noopener" aria-label="{esc(cap)}"><img src="{img(f)}" alt="{esc(cap)}" loading="lazy" width="400" height="400"></a>' for f,cap in IG_POSTS)
    return f'<div class="ig">{tiles}</div>'

def layout(title, desc, body, path="", schema=None, current=None, og_type="website", og_image=None, pclass=""):
    full = title if title == SITE["name"] else f"{title} | {SITE['name']}"
    url = abs_u(path)
    og_image = og_image or (ORIGIN + img("viralvir.jpg"))
    sch = "".join(f'<script type="application/ld+json">{json.dumps(s, ensure_ascii=False)}</script>' for s in (schema or []))
    cur = ' aria-current="page"'
    nav = "".join(f'<a href="{u(s)}"{cur if current==s else ""}>{n}</a>' for s,n in NAV)
    drawer = ""
    for p in PILLARS:
        drawer += f'<a href="{u(p["slug"])}">{p["emoji"]} {p["name"]}</a>'
        for s in p["subs"]:
            drawer += f'<a class="sub" href="{u(p["slug"]+"/"+s["slug"])}">{s["name"]}</a>'
    for s,n in [("explains","Viral Vir Explains"),("vs","Viral Vir vs"),("dictionary","Viral Vir Dictionary"),("podcast","Podcast / Videos"),("media","Media"),("about","About Viral Vir"),("contact","Contact")]:
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
<meta property="og:title" content="{esc(full)}"><meta property="og:description" content="{esc(desc)}"><meta property="og:url" content="{url}"><meta property="og:image" content="{og_image}">
<meta name="twitter:card" content="summary_large_image">
<meta name="robots" content="index,follow,max-snippet:-1,max-image-preview:large">
<link rel="icon" href="{img('viralvir-240.jpg')}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@700;800&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{BASE}/assets/site.css">
<script>try{{var t=localStorage.getItem('tvv-theme');if(t)document.documentElement.setAttribute('data-theme',t)}}catch(e){{}}</script>
{sch}
</head>
<body class="{pclass}">
<header class="top"><div class="wrap">
<a class="brand" href="{u()}"><img src="{img('viralvir-240.jpg')}" alt="" width="34" height="34">The Viral <span>Vir</span></a>
<nav class="nav" aria-label="Primary">{nav}</nav>
<div style="display:flex;gap:8px;align-items:center">
<a class="ask-btn" href="{u('ask')}">Ask Viral Vir →</a>
<button class="menu-btn" aria-label="Menu" aria-expanded="false" onclick="var d=document.getElementById('drawer');d.classList.toggle('open');this.setAttribute('aria-expanded',d.classList.contains('open'))">☰</button>
</div></div>
<div class="drawer" id="drawer">{drawer}</div>
</header>
<main>{body}</main>
<footer><div class="wrap">
{follow_row()}
<div class="cols" style="margin-top:32px">
<div><div class="brand"><img src="{img('viralvir-240.jpg')}" alt="" width="34" height="34">The Viral <span>Vir</span></div><p style="margin-top:10px;max-width:40ch">{SITE['tagline']} The guy you ask when life gets complicated. Home of {SITE['show']} and Zindagi ke Smart Tips.</p></div>
<div><h4>Topics</h4>{pillar_links}</div>
<div><h4>Series</h4><a href="{u('ask')}">Ask Viral Vir</a><a href="{u('explains')}">Viral Vir Explains</a><a href="{u('vs')}">Viral Vir vs</a><a href="{u('dictionary')}">Dictionary</a><a href="{u('podcast')}">Podcast / Videos</a></div>
<div><h4>Viral Vir</h4><a href="{u('about')}">About</a><a href="{u('media')}">Media</a><a href="{u('contact')}">Contact</a><a href="{SITE['instagram']}" rel="me">Instagram {SITE['handle']}</a><a href="{SITE['youtube']}" rel="me">YouTube</a><a href="{SITE['facebook']}" rel="me">Facebook</a></div>
</div>
<div class="foot-note"><span>© {datetime.date.today().year} The Viral Vir. Opinions are personal experience, labelled as such.</span>
<button class="theme" onclick="var r=document.documentElement;var d=r.getAttribute('data-theme')==='dark'||(!r.getAttribute('data-theme')&&matchMedia('(prefers-color-scheme: dark)').matches);var n=d?'light':'dark';r.setAttribute('data-theme',n);try{{localStorage.setItem('tvv-theme',n)}}catch(e){{}}">Toggle theme</button></div>
</div></footer>
</body></html>"""

def write(path, html_str, prio="0.6"):
    d = os.path.join(OUT, path.strip("/")) if path else OUT
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "index.html"), "w") as f: f.write(html_str)
    PAGES.append((abs_u(path), prio))

def crumbs(items):
    out = f'<div class="wrap crumbs"><a href="{u()}">Home</a>'
    for name, path in items:
        out += '<span>/</span>' + (f'<a href="{u(path)}">{esc(name)}</a>' if path is not None else esc(name))
    return out + "</div>"

def breadcrumb_schema(items):
    lst = [{"@type":"ListItem","position":1,"name":"Home","item":abs_u()}]
    for i,(name,path) in enumerate(items, start=2):
        lst.append({"@type":"ListItem","position":i,"name":name,"item":abs_u(path or "")})
    return {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":lst}

def photo(key, cls="heroimg"):
    p = UNSPLASH.get(key)
    if not p: return ""
    return f'<figure class="{cls}" style="margin-left:0;margin-right:0"><img src="{p["url"]}" alt="{esc(p["alt"])}" width="1400" height="700" loading="lazy"><figcaption class="credit">Photo by <a href="{p["link"]}?utm_source=theviralvir&utm_medium=referral" rel="noopener">{esc(p["name"])}</a> on <a href="https://unsplash.com/?utm_source=theviralvir&utm_medium=referral" rel="noopener">Unsplash</a></figcaption></figure>'

PERSON = {"@context":"https://schema.org","@type":"Person","@id":abs_u("about")+"#person","name":"Viral Vir","alternateName":["The Viral Vir","The Viral Vir","V Jain"],"url":abs_u(),
    "image":ORIGIN+img("viralvir.jpg"),"description":SITE["description"],"jobTitle":"Content creator, podcast host, technology and corporate professional","nationality":"Indian",
    "knowsAbout":["Relationships","Dating","Marriage","Career advice","Leadership","Salary negotiation","Office politics","Artificial intelligence","Technology","Everyday psychology","Life hacks","Modern life","Travel"],
    "sameAs":[SITE["instagram"],SITE["youtube"],SITE["facebook"]]}
WEBSITE = {"@context":"https://schema.org","@type":"WebSite","name":SITE["name"],"url":abs_u(),"description":SITE["description"],"publisher":{"@id":PERSON["@id"]},"inLanguage":"en"}

def pillar_by(slug): return next(p for p in PILLARS if p["slug"]==slug)
def sub_by(p, slug): return next(s for s in p["subs"] if s["slug"]==slug)
ART_BY_TITLE = {a["title"]: a for a in ARTICLES}

def article_card(a, with_img=True):
    p = pillar_by(a["pillar"]); ph = UNSPLASH.get(a["slug"])
    im = f'<div class="ph"><img src="{ph["thumb"]}" alt="" loading="lazy"></div>' if (with_img and ph) else ""
    return f'<a class="card img p-{p["slug"]}" href="{u(a["pillar"]+"/"+a["slug"])}">{im}<div class="tx"><span class="label c">{p["emoji"]} {p["name"]} · {sub_by(p,a["sub"])["name"]}</span><h3>{esc(a["title"])}</h3><p>{esc(a["short"][:130])}…</p></div></a>'

def qlist(questions):
    items = ""
    for q in questions:
        a = ART_BY_TITLE.get(q)
        if a: items += f'<li><a href="{u(a["pillar"]+"/"+a["slug"])}">{esc(q)}<span class="tag">Read →</span></a></li>'
        else: items += f'<li><span class="row soon">{esc(q)}<span class="tag">Coming soon</span></span></li>'
    return f'<ul class="qlist">{items}</ul>'

def yt_grid(n=6):
    return '<div class="yt">' + "".join(f'<a href="https://www.youtube.com/watch?v={vid}" target="_blank" rel="noopener"><div class="th"><img src="{img(f"yt_{vid}.jpg")}" alt="" loading="lazy"></div><b>{esc(t)}</b></a>' for vid,t in YT_VIDEOS[:n]) + '</div>'

def follow_box():
    mini = "".join(f'<img src="{img(f)}" alt="">' for f,_ in IG_POSTS[:3])
    return f'<div class="followbox"><div><h3>Enjoyed this? Follow me at {SITE["handle"]}</h3><p>New Zindagi ke Smart Tips and {SITE["show"]} clips every week. {SITE["stats"][0][0]} people already do.</p><div class="mini" style="margin-top:12px">{mini}</div></div><a class="igbtn" href="{SITE["instagram"]}" target="_blank" rel="noopener">{IG_SVG} Follow on Instagram</a></div>'

# ---------- pages ----------
def home():
    pillars = "".join(f'<a class="card tint p-{p["slug"]}" href="{u(p["slug"])}"><div class="ico">{p["emoji"]}</div><h3>{p["name"]}</h3><p>{esc(p["lede"].split(".")[0])}.</p></a>' for p in PILLARS)
    arts = "".join(article_card(a) for a in ARTICLES[:6])
    series = [("explains","Viral Vir Explains","Why people ghost, cheat, procrastinate and hate their jobs. One honest explanation each."),
              ("vs","Viral Vir vs","Love vs attraction. Confidence vs arrogance. Career vs job. The difference, in two lines."),
              ("dictionary","Viral Vir Dictionary","The 3C Rule, the Attention Test, the Exit Test. Concepts I use to think clearly about people."),
              ("ask","Ask Viral Vir","Got a question about life, love or work? Ask. Selected questions get a full answer here.")]
    series_html = "".join(f'<a class="card p-series" href="{u(s)}"><span class="bar"></span><h3>{n}</h3><p>{d}</p></a>' for s,n,d in series)
    asks = "".join(f'<a class="card" href="{u("ask")}"><span class="label brandc">Ask Viral Vir · {c}</span><h3 style="font-size:17px">{esc(q)}</h3><p>{esc(a[:150])}…</p></a>' for q,c,a in ASK_SAMPLES)
    stats = "".join(f'<div class="stat"><b>{n}</b><span>{l}</span></div>' for n,l in SITE["stats"])
    body = f"""
<section class="hero"><div class="wrap hero-grid">
<div>
<span class="kicker"><i></i>Relationships · Career · Technology · Life</span>
<h1>Smart advice for <span>modern life.</span></h1>
<p class="sub">I've spent decades navigating people, technology, corporate life, relationships and the world. I've learned a few things along the way. Some the hard way.</p>
<p class="quote">The guy you ask when life gets complicated.</p>
<div class="cta" style="margin-top:26px"><a class="btn brand" href="{u('ask')}">Ask Viral Vir →</a><a class="igbtn" href="{SITE['instagram']}" target="_blank" rel="noopener">{IG_SVG} Follow {SITE['handle']}</a></div>
</div>
<div class="portrait"><img src="{img('viralvir.jpg')}" alt="Viral Vir, host of {SITE['show']}" width="720" height="720" fetchpriority="high">
<div class="chip a"><b>{SITE['stats'][0][0]}</b><div>followers<small>on Instagram</small></div></div>
<div class="chip b"><b>{SITE['stats'][1][0]}</b><div>views<small>across platforms</small></div></div></div>
</div></section>
<section class="section" style="padding-top:8px"><div class="wrap">
<div class="section-head"><div><h2>What do you want to know?</h2><p>Pick a topic. Every question gets its own page.</p></div></div>
<div class="grid c5">{pillars}</div>
</div></section>
<section class="section band"><div class="wrap">
<div class="section-head"><div><h2>Follow me on Instagram</h2><p>{SITE['handle']} · Zindagi ke Smart Tips, {SITE['show']} and everyday psychology</p></div><a class="more" href="{SITE['instagram']}" target="_blank" rel="noopener">Open Instagram →</a></div>
{ig_strip()}
<div style="margin-top:22px">{follow_row()}</div>
</div></section>
<section class="section"><div class="wrap">
<div class="section-head"><div><h2>Start here</h2><p>Full answers in the Viral Vir format: short answer first, then the signs, the mistakes and my take.</p></div><a class="more" href="{u('relationships')}">All answers →</a></div>
<div class="grid c3">{arts}</div>
</div></section>
<section class="section navyband"><div class="wrap">
<div class="section-head"><div><h2 style="color:inherit">Why people listen</h2><p style="opacity:.8">Featured in {", ".join(SITE['featured'][:2])}. Alumnus of {SITE['featured'][2]}.</p></div></div>
<div class="stats">{stats}</div>
</div></section>
<section class="section"><div class="wrap">
<div class="section-head"><div><h2>Watch {SITE['show']}</h2><p>Original podcast and talk show on love, life, relationships and mental health.</p></div><a class="more" href="{SITE['youtube']}" target="_blank" rel="noopener">YouTube channel →</a></div>
{yt_grid(3)}
</div></section>
<section class="section band"><div class="wrap">
<div class="section-head"><div><h2>The series</h2></div></div>
<div class="grid c4">{series_html}</div>
</div></section>
<section class="section"><div class="wrap">
<div class="section-head"><div><h2>Recently asked</h2></div><a class="more" href="{u('ask')}">Ask your own →</a></div>
<div class="grid c3">{asks}</div>
</div></section>"""
    write("", layout(SITE["name"], SITE["description"], body, "", [WEBSITE, PERSON]), "1.0")

def about():
    stats = "".join(f'<div class="stat" style="background:var(--bg2)"><b>{n}</b><span>{l}</span></div>' for n,l in SITE["stats"])
    body = f"""{crumbs([("About Viral Vir", None)])}
<div class="wrap"><div class="hero-grid" style="padding:28px 0 8px">
<div><span class="label brandc">Who is Viral Vir?</span><h1>Viral Vir</h1>
<p class="lede">Viral Vir is an Indian content creator, podcast host, technology and corporate professional, and commentator on relationships, careers and modern life. Drawing on decades of professional experience, international exposure and personal observation, he creates practical advice about navigating work, relationships, technology and everyday life.</p>
<div class="cta" style="margin-top:8px"><a class="igbtn" href="{SITE['instagram']}" target="_blank" rel="noopener">{IG_SVG} Follow {SITE['handle']}</a><a class="ytbtn" href="{SITE['youtube']}" target="_blank" rel="noopener">{YT_SVG} {SITE['show']}</a></div></div>
<div class="portrait" style="max-width:380px"><img src="{img('viralvir-about.jpg')}" alt="Viral Vir" width="720" height="720"></div>
</div>
<div class="stats" style="margin:28px 0 8px">{stats}</div>
<div class="article"><div class="body">
<h2>In short</h2>
<p>A worldly, experienced, technology-savvy Indian man who has spent decades navigating careers, relationships, people and life, and shares the practical lessons learned along the way. Not a professor, not a guru, not a therapist. The smart older friend who has seen enough of life to tell you what actually happens.</p>
<h2>Career</h2>
<p>Viral Vir has worked in technology and corporate leadership for several decades, building and running teams and products across industries. That experience, on both sides of the hiring table and both sides of the management line, informs the <a class="brandc" href="{u('career')}">Career</a> section of this site.</p>
<h2>Technology</h2>
<p>A technology professional by training and trade, and an alumnus of IIT Bombay, he has lived through outsourcing, cloud, mobile and now AI, and writes about <a class="brandc" href="{u('technology')}">technology for real life</a>: what matters for ordinary people and professionals, without the jargon.</p>
<h2>International experience</h2>
<p>Having lived and worked in several countries, he writes about what different cultures teach you about people, and what living abroad teaches you about India. See <a class="brandc" href="{u('travel-and-living')}">Travel &amp; Living</a>.</p>
<h2>Content creation</h2>
<p>On Instagram ({SITE['handle']}, {SITE['stats'][0][0]} followers, over a billion views) he is known for <em>Zindagi ke Smart Tips</em>, short direct advice on everyday psychology, relationships and life hacks, and for <em>{SITE['show']}</em>, an original podcast and talk show on love, life, relationships and mental health. His work has been featured in {", ".join(SITE['featured'][:2])}. This website is the long-form home for that work: every question gets its own page, written in the <a class="brandc" href="{u('relationships/how-to-know-if-someone-likes-you')}">Viral Vir Answer format</a>.</p>
<h2>Series</h2>
<ul class="qlist">
<li><a href="{u('ask')}">Ask Viral Vir<span class="tag">Questions from readers</span></a></li>
<li><a href="{u('explains')}">Viral Vir Explains<span class="tag">Why people do what they do</span></a></li>
<li><a href="{u('vs')}">Viral Vir vs<span class="tag">Comparisons</span></a></li>
<li><a href="{u('dictionary')}">Viral Vir Dictionary<span class="tag">Concepts and rules</span></a></li>
<li><a href="{u('podcast')}">Podcast / Videos<span class="tag">{SITE['show']}</span></a></li>
</ul>
<h2>Media and interviews</h2>
<p>Appearances, interviews and quotes are listed on the <a class="brandc" href="{u('media')}">Media page</a>. For interview, guest and collaboration requests, see <a class="brandc" href="{u('contact')}">Contact</a>.</p>
<h2>How the advice is written</h2>
<p>Personal observations are labelled as experience. Factual claims are sourced. On contested topics, both sides are shown: <em>Viral Vir's view</em> and <em>what research suggests</em>, kept separate so you can tell which is which.</p>
{follow_box()}
</div></div></div>"""
    write("about", layout("About Viral Vir", "Who is Viral Vir? Indian content creator, host of The Viral Vir Show, technology and corporate professional, and commentator on relationships, careers and modern life.", body, "about", [PERSON, breadcrumb_schema([("About Viral Vir","about")])], og_type="profile"), "0.9")

def pillar_pages():
    for p in PILLARS:
        subs = "".join(f'<a class="card tint p-{p["slug"]}" href="{u(p["slug"]+"/"+s["slug"])}"><h3>{s["name"]}</h3><p>{esc(s["lede"])}</p><p style="margin-top:10px;color:var(--c);font-size:12px;font-weight:700">{len(s["questions"])} questions →</p></a>' for s in p["subs"])
        arts = [a for a in ARTICLES if a["pillar"]==p["slug"]]
        arts_html = ("<div class='section-head'><h2>Answers</h2></div><div class='grid c2'>" + "".join(article_card(a) for a in arts) + "</div>") if arts else ""
        allq = []
        for s in p["subs"]: allq += s["questions"]
        body = f"""{crumbs([(p["name"], None)])}
<div class="wrap p-{p["slug"]}"><div class="article-head"><span class="label c">{p["emoji"]} Pillar</span><h1>{p["name"]}</h1><p class="lede">{esc(p["lede"])}</p></div>
{photo(p["slug"])}
<div class="grid c3" style="margin:24px 0 48px">{subs}</div>
{arts_html}
<div class="section-head" style="margin-top:48px"><h2>Every question in {p["name"]}</h2></div>
<div class="article">{qlist(allq)}{follow_box()}</div>
</div>"""
        ph = UNSPLASH.get(p["slug"])
        write(p["slug"], layout(p["name"], p["lede"], body, p["slug"], [breadcrumb_schema([(p["name"],p["slug"])])], current=p["slug"], og_image=ph["url"] if ph else None), "0.9")
        for s in p["subs"]:
            path = f'{p["slug"]}/{s["slug"]}'
            body = f"""{crumbs([(p["name"], p["slug"]),(s["name"], None)])}
<div class="wrap article p-{p["slug"]}"><div class="article-head"><span class="label c">{p["emoji"]} {p["name"]}</span><h1>{s["name"]}</h1><p class="lede">{esc(s["lede"])}</p></div>
<h2 style="margin-top:24px">Questions</h2>{qlist(s["questions"])}
<div class="take" style="margin-top:40px"><h2>Have a question not listed?</h2><p>Ask it. Selected questions get a full answer page.</p><p><a class="btn brand" href="{u('ask')}">Ask Viral Vir →</a></p></div>
{follow_box()}
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
        ph = UNSPLASH.get(a["slug"])
        body = f"""{crumbs([(p["name"],p["slug"]),(s["name"],f'{p["slug"]}/{s["slug"]}'),(a["title"],None)])}
<div class="wrap article p-{p["slug"]}">
<div class="article-head"><span class="label c">{p["emoji"]} {p["name"]} · {s["name"]}</span><h1>{esc(a["title"])}</h1>
<div class="meta"><span class="who"><img class="avatar" src="{img('viralvir-240.jpg')}" alt="">Viral Vir</span><span>Updated {TODAY}</span><span>From experience, labelled as such</span></div></div>
{photo(a["slug"])}
<div class="short"><span class="label">Short answer</span><p>{esc(a["short"])}</p></div>
<div class="body">
<h2>{esc(a["signs_heading"])}</h2><ol class="steps">{steps}</ol>
<div class="take"><h2><img class="avatar" src="{img('viralvir-240.jpg')}" alt="">But here's the important part</h2>{take}</div>
<h2>Common mistakes people make</h2><ul class="mist">{mist}</ul>
<h2>Frequently asked questions</h2>{faqs}
<div class="take"><h2>Viral Vir's take</h2><p>{esc(a["take"][-1])}</p><p class="notice">This is personal experience and observation, not clinical or legal advice. Where research is cited, it is linked.</p></div>
</div>
{follow_box()}
<div class="related"><div class="section-head"><h2>Keep reading</h2></div><div class="grid c3">{rel}</div></div>
</div>"""
        schema = [
            {"@context":"https://schema.org","@type":"Article","headline":a["title"],"description":a["description"],"url":abs_u(path),"datePublished":TODAY,"dateModified":TODAY,"image":ph["url"] if ph else ORIGIN+img("viralvir.jpg"),
             "author":{"@id":PERSON["@id"]},"publisher":{"@id":PERSON["@id"]},"mainEntityOfPage":abs_u(path),"articleSection":p["name"],"inLanguage":"en"},
            {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":ans}} for q,ans in a["faqs"]]},
            breadcrumb_schema([(p["name"],p["slug"]),(s["name"],f'{p["slug"]}/{s["slug"]}'),(a["title"],path)]),
        ]
        write(path, layout(a["title"], a["description"], body, path, schema, current=p["slug"], og_type="article", og_image=ph["url"] if ph else None), "0.8")

def ask():
    cats = "".join(f'<span class="pill">{e} {n}</span>' for e,n in ASK_CATEGORIES)
    opts = "".join(f'<option>{n}</option>' for e,n in ASK_CATEGORIES)
    samples = "".join(f'<div class="card"><span class="label brandc">{c}</span><h3>Ask Viral Vir: {esc(q)}</h3><p style="font-size:15px;color:var(--ink)">{esc(a)}</p></div>' for q,c,a in ASK_SAMPLES)
    body = f"""{crumbs([("Ask Viral Vir", None)])}
<div class="wrap"><div class="article-head"><span class="label brandc">The heart of the site</span><h1>Ask Viral Vir</h1><p class="lede">Got a question about life, love or work? Ask it here. Selected questions are answered in full on this site, anonymised. You can also DM {SITE['handle']} on Instagram.</p>
<div class="pills" style="margin-top:16px">{cats}</div></div>
<div class="grid c2" style="margin-top:32px;align-items:start">
<form class="card" onsubmit="return tvvSend(this)">
<div class="f"><label class="label" for="q">Your question</label><textarea id="q" name="question" required placeholder="I'm 35 and afraid I'll never find the right partner. What should I do?"></textarea></div>
<div class="f"><label class="label" for="c">Category</label><select id="c" name="category">{opts}</select></div>
<div class="f"><label class="label" for="n">Name or initials (optional)</label><input id="n" name="name" placeholder="A., Pune"></div>
<div class="f"><label class="label" for="e">Email (optional, for a reply)</label><input id="e" name="email" type="email" placeholder="you@example.com"></div>
<button class="btn brand" type="submit">Send to Viral Vir</button>
<p class="notice" style="margin-top:12px">Questions may be published in edited, anonymised form. No names, employers or identifying details are ever published.</p>
</form>
<div><div class="grid">{samples}</div><div style="margin-top:14px">{follow_box()}</div></div>
</div></div>
<script>function tvvSend(f){{var s="Question: "+f.question.value+"\\nCategory: "+f.category.value+"\\nName: "+f.name.value+"\\nEmail: "+f.email.value;location.href="mailto:{SITE['email']}?subject="+encodeURIComponent("Ask Viral Vir: "+f.category.value)+"&body="+encodeURIComponent(s);return false}}</script>"""
    write("ask", layout("Ask Viral Vir", "Ask Viral Vir a question about relationships, career, life, technology, money, travel or family. Selected questions are answered in full.", body, "ask", [breadcrumb_schema([("Ask Viral Vir","ask")])]), "0.9")

def explains():
    cards = "".join(f'<a class="card p-series" href="{u("explains/"+s)}"><span class="bar"></span><span class="label c">Viral Vir Explains</span><h3>{esc(t)}</h3><p>{esc(d)}</p></a>' for s,t,d in EXPLAINS)
    body = f"""{crumbs([("Viral Vir Explains", None)])}
<div class="wrap"><div class="article-head"><span class="label brandc">Series</span><h1>Viral Vir Explains</h1><p class="lede">Why people do what they do. One honest explanation per page, from someone who has watched the same patterns repeat for decades.</p></div>
<div class="grid c2" style="margin-top:24px">{cards}</div></div>"""
    write("explains", layout("Viral Vir Explains", "Why people ghost, cheat, fall out of love, procrastinate and hate their jobs. Short, honest explanations from Viral Vir.", body, "explains", [breadcrumb_schema([("Viral Vir Explains","explains")])], current="explains"), "0.8")
    for s,t,d in EXPLAINS:
        path = "explains/"+s
        others = "".join(f'<li><a href="{u("explains/"+s2)}">{esc(t2)}<span class="tag">Read →</span></a></li>' for s2,t2,_ in EXPLAINS if s2!=s)
        body = f"""{crumbs([("Viral Vir Explains","explains"),(t,None)])}
<div class="wrap article p-series"><div class="article-head"><span class="label c">Viral Vir Explains</span><h1>{esc(t)}</h1>
<div class="meta"><span class="who"><img class="avatar" src="{img('viralvir-240.jpg')}" alt="">Viral Vir</span><span>Updated {TODAY}</span></div></div>
<div class="short"><span class="label">In one breath</span><p>{esc(d)}</p></div>
<div class="body"><p>{esc(d)} That is the short version. The full explanation, with the patterns I have seen and what to do about it, is being written. Until then, the short version is the part that matters.</p>
<div class="take"><h2>Viral Vir's take</h2><p>Most human behaviour that looks mysterious is just a habit plus an incentive. Find the incentive and the mystery disappears.</p></div>
<h2>More explanations</h2><ul class="qlist">{others}</ul></div>{follow_box()}</div>"""
        write(path, layout(t, d, body, path, [breadcrumb_schema([("Viral Vir Explains","explains"),(t,path)]), {"@context":"https://schema.org","@type":"Article","headline":t,"description":d,"url":abs_u(path),"author":{"@id":PERSON["@id"]},"datePublished":TODAY}], current="explains", og_type="article"), "0.7")

def versus():
    cards = "".join(f'<a class="card p-series" href="{u("vs/"+s)}"><span class="bar"></span><span class="label c">Viral Vir vs</span><h3>{esc(t)}</h3><p>{esc(l)}</p></a>' for s,t,l,_ in VERSUS)
    body = f"""{crumbs([("Viral Vir vs", None)])}
<div class="wrap"><div class="article-head"><span class="label brandc">Series</span><h1>Viral Vir vs</h1><p class="lede">Two things people confuse, and the difference that matters. Love vs attraction. Confidence vs arrogance. Career vs job.</p></div>
<div class="grid c2" style="margin-top:24px">{cards}</div></div>"""
    write("vs", layout("Viral Vir vs", "Love vs attraction, confidence vs arrogance, chemistry vs compatibility, career vs job. Viral Vir explains the difference.", body, "vs", [breadcrumb_schema([("Viral Vir vs","vs")])], current="vs"), "0.8")
    for s,t,l,d in VERSUS:
        path = "vs/"+s; a,b = t.split(" vs ")
        others = "".join(f'<li><a href="{u("vs/"+s2)}">{esc(t2)}<span class="tag">Read →</span></a></li>' for s2,t2,_,_ in VERSUS if s2!=s)
        body = f"""{crumbs([("Viral Vir vs","vs"),(t,None)])}
<div class="wrap article p-series"><div class="article-head"><span class="label c">Viral Vir vs</span><h1>{esc(t)}</h1>
<div class="meta"><span class="who"><img class="avatar" src="{img('viralvir-240.jpg')}" alt="">Viral Vir</span><span>Updated {TODAY}</span></div></div>
<div class="card" style="margin:20px 0"><div class="vs"><span>{esc(a)}</span><i>vs</i><span>{esc(b)}</span></div></div>
<div class="short"><span class="label">The difference</span><p>{esc(l)}</p></div>
<div class="body"><p>{esc(d)}</p>
<div class="take"><h2>Viral Vir's take</h2><p>{esc(l)}</p></div>
<h2>More comparisons</h2><ul class="qlist">{others}</ul></div>{follow_box()}</div>"""
        write(path, layout(t, l+" "+d, body, path, [breadcrumb_schema([("Viral Vir vs","vs"),(t,path)]), {"@context":"https://schema.org","@type":"Article","headline":t,"description":l,"url":abs_u(path),"author":{"@id":PERSON["@id"]},"datePublished":TODAY}], current="vs", og_type="article"), "0.7")

def dictionary():
    dl = "".join(f'<dt id="{s}"><a href="{u("dictionary/"+s)}">{esc(t)}</a></dt><dd><b>{esc(o)}</b> {esc(d)}</dd>' for s,t,o,d in DICTIONARY)
    body = f"""{crumbs([("Viral Vir Dictionary", None)])}
<div class="wrap article"><div class="article-head"><span class="label brandc">Series</span><h1>Viral Vir Dictionary</h1><p class="lede">The concepts and rules I use to think clearly about people, work and life. Each one is a shortcut earned the slow way.</p></div>
<dl class="def">{dl}</dl>{follow_box()}</div>"""
    defined = [{"@type":"DefinedTerm","name":t,"description":o+" "+d,"url":abs_u("dictionary/"+s)} for s,t,o,d in DICTIONARY]
    write("dictionary", layout("Viral Vir Dictionary", "The 3C Rule, the 3R Rule, the Career Ceiling, the Attention Test, the Exit Test and other Viral Vir concepts, defined.", body, "dictionary", [breadcrumb_schema([("Viral Vir Dictionary","dictionary")]), {"@context":"https://schema.org","@type":"DefinedTermSet","name":"Viral Vir Dictionary","hasDefinedTerm":defined}], current="dictionary"), "0.8")
    for s,t,o,d in DICTIONARY:
        path = "dictionary/"+s
        others = "".join(f'<li><a href="{u("dictionary/"+s2)}">{esc(t2)}<span class="tag">{esc(o2)}</span></a></li>' for s2,t2,o2,_ in DICTIONARY if s2!=s)
        body = f"""{crumbs([("Viral Vir Dictionary","dictionary"),(t,None)])}
<div class="wrap article p-series"><div class="article-head"><span class="label c">Viral Vir Dictionary</span><h1>What is {esc(t)}?</h1></div>
<div class="short"><span class="label">Definition</span><p>{esc(o)}</p></div>
<div class="body"><p>{esc(d)}</p>
<div class="take"><h2>Where it came from</h2><p>{esc(t)} is a Viral Vir concept: a rule of thumb built from years of watching the same situations play out in offices, families and relationships. It is a lens, not a law.</p></div>
<h2>More concepts</h2><ul class="qlist">{others}</ul></div>{follow_box()}</div>"""
        write(path, layout(f"What is {t}?", f"{t}: {o} {d}", body, path, [breadcrumb_schema([("Viral Vir Dictionary","dictionary"),(t,path)]), {"@context":"https://schema.org","@type":"DefinedTerm","name":t,"description":o+" "+d,"url":abs_u(path),"inDefinedTermSet":abs_u("dictionary")}], current="dictionary"), "0.7")

def podcast():
    body = f"""{crumbs([("Podcast / Videos", None)])}
<div class="wrap"><div class="article-head"><span class="label brandc">{SITE['show']} · Zindagi ke Smart Tips</span><h1>Podcast / Videos</h1><p class="lede">Original podcast and talk show on love, life, relationships and mental health in modern times. Every Reel and episode maps to a question on this site. Watch the short version there, read the full version here.</p>
<div class="cta" style="margin-top:8px"><a class="ytbtn" href="{SITE['youtube']}" target="_blank" rel="noopener">{YT_SVG} Subscribe on YouTube</a><a class="igbtn" href="{SITE['instagram']}" target="_blank" rel="noopener">{IG_SVG} Reels on Instagram</a></div></div>
<h2 style="margin-top:32px">Latest on YouTube</h2>{yt_grid(6)}
<h2 style="margin-top:40px">Latest on Instagram</h2>{ig_strip()}
<div class="take" style="margin-top:40px;max-width:740px"><h2>How the show works</h2><p>One idea becomes one article, ten FAQs, a 60-second Reel, a longer video and a podcast conversation. Same thinking, different lengths. Pick the one that fits your day.</p></div></div>"""
    write("podcast", layout("Podcast / Videos", "The Viral Vir Show and Zindagi ke Smart Tips: videos, Reels and podcast episodes on relationships, career, technology and life.", body, "podcast", [breadcrumb_schema([("Podcast / Videos","podcast")])]), "0.7")

def media():
    cards = "".join(f'<a class="card p-series" href="{u("media/"+m["slug"])}"><span class="bar"></span><span class="label c">{m["outlet"]} · {m["topic"]} · {m["date"]}</span><h3>{esc(m["title"])}</h3><p>{esc(m["summary"])}</p></a>' for m in MEDIA)
    body = f"""{crumbs([("Media", None)])}
<div class="wrap"><div class="article-head"><span class="label brandc">Viral Vir in the media</span><h1>Media</h1><p class="lede">Interviews, podcast appearances, quotes and features. Featured in {", ".join(SITE['featured'][:2])}. Viral Vir speaks on three things: modern relationships, technology and careers, and modern life.</p></div>
<div class="grid c3" style="margin-top:24px">{cards}</div>
<div class="take" style="margin-top:40px;max-width:740px"><h2>For journalists and podcasters</h2><p>Available for comment on modern dating, relationships in India, AI and careers, executive careers, office politics, everyday psychology and living abroad. <a class="brandc" style="font-weight:700" href="{u('contact')}">Contact →</a></p></div></div>"""
    write("media", layout("Viral Vir in the Media", "Interviews, podcast appearances and features with Viral Vir on relationships, technology, careers and modern life.", body, "media", [breadcrumb_schema([("Media","media")])]), "0.7")
    for m in MEDIA:
        path = "media/"+m["slug"]
        body = f"""{crumbs([("Media","media"),(m["title"],None)])}
<div class="wrap article"><div class="article-head"><span class="label brandc">{m["outlet"]} · {m["topic"]} · {m["date"]}</span><h1>{esc(m["title"])}</h1><p class="lede">{esc(m["summary"])}</p></div>
<p><a class="btn ghost" href="{m["url"]}" rel="noopener">View the original coverage →</a></p>
<p class="notice">Link to be added when coverage is published.</p>
<div class="take"><h2>Related reading on this site</h2><ul class="qlist">{"".join(f'<li><a href="{u(a["pillar"]+"/"+a["slug"])}">{esc(a["title"])}<span class="tag">Read →</span></a></li>' for a in ARTICLES[:3])}</ul></div></div>"""
        write(path, layout(m["title"], m["summary"], body, path, [breadcrumb_schema([("Media","media"),(m["title"],path)])]), "0.5")

def contact():
    body = f"""{crumbs([("Contact", None)])}
<div class="wrap article"><div class="article-head"><span class="label brandc">Get in touch</span><h1>Contact</h1><p class="lede">For interviews, podcast invitations, guest appearances on {SITE['show']}, speaking, collaborations and press. For personal questions, use <a class="brandc" href="{u('ask')}">Ask Viral Vir</a> instead.</p></div>
<div class="grid c2">
<div class="card"><span class="label brandc">Email</span><h3><a href="mailto:{SITE['email']}">{SITE['email']}</a></h3><p>Business enquiries and guest requests for the show.</p></div>
<div class="card"><span class="label brandc">Social</span><div class="pills" style="margin-top:10px"><a class="pill" href="{SITE['instagram']}">Instagram {SITE['handle']}</a><a class="pill" href="{SITE['youtube']}">YouTube</a><a class="pill" href="{SITE['facebook']}">Facebook</a></div></div>
</div>
<div class="take" style="margin-top:32px"><h2>What Viral Vir speaks on</h2><p>Modern dating and relationships · everyday psychology · AI and careers · executive careers and office politics · technology for real life · living abroad and what it teaches you about India.</p></div>
{follow_box()}</div>"""
    write("contact", layout("Contact Viral Vir", "Contact Viral Vir for interviews, podcasts, speaking, collaborations and press.", body, "contact", [breadcrumb_schema([("Contact","contact")])]), "0.5")

def not_found():
    body = f"""<div class="wrap hero"><span class="kicker"><i></i>404</span><h1>That page has moved on.</h1><p class="sub">Which, as it happens, is a topic I cover. Try one of the pillars or ask a question.</p>
<div class="cta" style="margin-top:24px"><a class="btn" href="{u()}">Home</a><a class="btn brand" href="{u('ask')}">Ask Viral Vir →</a></div></div>"""
    with open(os.path.join(OUT, "404.html"), "w") as f: f.write(layout("Page not found", "Page not found", body, "404"))

def extras():
    os.makedirs(os.path.join(OUT, "assets"), exist_ok=True)
    with open(os.path.join(OUT, "assets", "site.css"), "w") as f: f.write(CSS)
    open(os.path.join(OUT, ".nojekyll"), "w").close()
    with open(os.path.join(OUT, "robots.txt"), "w") as f:
        f.write(f"User-agent: *\nAllow: /\n\n# AI search crawlers explicitly welcome\nUser-agent: OAI-SearchBot\nAllow: /\nUser-agent: ChatGPT-User\nAllow: /\nUser-agent: PerplexityBot\nAllow: /\nUser-agent: Google-Extended\nAllow: /\nUser-agent: Bingbot\nAllow: /\n\nSitemap: {ORIGIN}{BASE}/sitemap.xml\n")
    with open(os.path.join(OUT, "sitemap.xml"), "w") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
        for url, prio in PAGES: f.write(f"  <url><loc>{url}</loc><lastmod>{TODAY}</lastmod><priority>{prio}</priority></url>\n")
        f.write("</urlset>\n")
    with open(os.path.join(OUT, "CNAME.example"), "w") as f: f.write("theviralvir.com\n")

if __name__ == "__main__":
    keep = os.path.join(OUT, "assets", "img")
    tmp = os.path.join(ROOT, "_img_keep")
    if os.path.isdir(keep): shutil.copytree(keep, tmp, dirs_exist_ok=True)
    if os.path.isdir(OUT): shutil.rmtree(OUT)
    os.makedirs(os.path.join(OUT, "assets"))
    if os.path.isdir(tmp): shutil.move(tmp, keep)
    home(); about(); pillar_pages(); article_pages(); ask(); explains(); versus(); dictionary(); podcast(); media(); contact(); not_found(); extras()
    print(f"built {len(PAGES)} pages -> {OUT}")
