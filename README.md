# The Viral Veer

Static site for theviralveer: smart advice for modern life (relationships, career, life, technology, travel).

- `content.py` — all content: pillars, sub-topics, question bank, flagship articles, Explains, Vs, Dictionary, media, episodes.
- `build.py` — generator. Run `python3 build.py` to regenerate `docs/` (served by GitHub Pages from `main` / `docs`).
- Base path is `/theviralveer`. For a custom domain, build with `TVV_BASE="" TVV_ORIGIN="https://theviralveer.com" python3 build.py` and rename `docs/CNAME.example` to `docs/CNAME`.

Each answer page follows the Viral Veer Answer format: short answer, signs/steps, "the important part", common mistakes, FAQs, Viral Veer's take. Schema: WebSite, Person, Article, FAQPage, BreadcrumbList, DefinedTermSet.
